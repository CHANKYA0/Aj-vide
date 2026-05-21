from fastapi import APIRouter, HTTPException

from app.database import db_session
from app.schemas import PROJECT_PRESETS, ProjectCreate, RunLoopRequest
from app.services.ai_router import AIRouter
from app.services.repositories import ChapterRepository, ChunkRepository, JobRepository, ProjectRepository

router = APIRouter()


def _serialize_project(p):
    return {
        'id': p.id,
        'title': p.title,
        'genre': p.genre,
        'mode': p.mode,
        'status': p.status,
        'target_words': p.target_words,
        'generated_words': p.progress_words,
    }


@router.post('')
def create_project(payload: ProjectCreate):
    preset = payload.preset.model_dump() if payload.preset else PROJECT_PRESETS.get(payload.preset_name or 'Full Novel', PROJECT_PRESETS['Full Novel'])
    with db_session() as db:
        project = ProjectRepository(db).create({
            'user_id': 1, 'title': payload.title, 'genre': payload.genre, 'mode': payload.mode,
            'target_words': preset['target_words'], 'progress_words': 0, 'status': 'idle',
            'settings': {'project_type': payload.project_type, 'pages': preset['pages'], 'chapters': preset['chapters']}
        })
        per_chapter = max(800, preset['target_words'] // preset['chapters'])
        ChapterRepository(db).create_many([
            {'project_id': project.id, 'chapter_number': i + 1, 'target_words': per_chapter, 'title': f'Chapter {i+1}'}
            for i in range(preset['chapters'])
        ])
        return {'project': _serialize_project(project)}


@router.get('')
def list_projects():
    with db_session() as db:
        rows = ProjectRepository(db).list()
        return {'items': [_serialize_project(r) for r in rows]}


@router.get('/{project_id}')
def get_project(project_id: int):
    with db_session() as db:
        p = ProjectRepository(db).get(project_id)
        if not p:
            raise HTTPException(404, 'Project not found')
        return {'project': _serialize_project(p)}


@router.post('/{project_id}/run-loop')
def run_loop(project_id: int, payload: RunLoopRequest):
    with db_session() as db:
        projects = ProjectRepository(db)
        p = projects.get(project_id)
        if not p:
            raise HTTPException(404, 'Project not found')
        p.status = 'running'
        job = JobRepository(db).create(project_id=project_id)
        ai = AIRouter()
        steps = 0
        while steps < payload.max_steps and p.progress_words < p.target_words and p.status == 'running':
            ch = ChapterRepository(db).next_unfinished(project_id)
            if ch is None:
                p.status = 'completed'
                break
            text = ai.text('writer_model', f'Write {payload.chunk_words} words for {p.title} chapter {ch.chapter_number}')
            generated = min(payload.chunk_words, p.target_words - p.progress_words)
            ch.generated_words += generated
            p.progress_words += generated
            ChunkRepository(db).add({'project_id': p.id, 'chapter_id': ch.id, 'content': text, 'word_count': generated, 'summary': text[:120]})
            steps += 1
            job.progress = {'steps': steps, 'generated_words': p.progress_words, 'target_words': p.target_words}
        if p.progress_words >= p.target_words:
            p.status = 'completed'
        elif p.status == 'running':
            p.status = 'paused'
        job.status = p.status
        return {'job_id': job.id, 'status': job.status, 'progress': job.progress}


@router.post('/{project_id}/pause')
def pause(project_id: int):
    with db_session() as db:
        p = ProjectRepository(db).get(project_id)
        if not p:
            raise HTTPException(404, 'Project not found')
        p.status = 'paused'
        return {'status': 'paused'}


@router.post('/{project_id}/resume')
def resume(project_id: int):
    with db_session() as db:
        p = ProjectRepository(db).get(project_id)
        if not p:
            raise HTTPException(404, 'Project not found')
        p.status = 'running'
        return {'status': 'running'}


@router.post('/{project_id}/cancel')
def cancel(project_id: int):
    with db_session() as db:
        p = ProjectRepository(db).get(project_id)
        if not p:
            raise HTTPException(404, 'Project not found')
        p.status = 'cancelled'
        return {'status': 'cancelled'}


@router.get('/jobs/{job_id}')
def get_job(job_id: int):
    with db_session() as db:
        j = JobRepository(db).get(job_id)
        if not j:
            raise HTTPException(404, 'Job not found')
        return {'job_id': j.id, 'status': j.status, 'progress': j.progress}
