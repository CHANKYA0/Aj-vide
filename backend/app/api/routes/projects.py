from fastapi import APIRouter, HTTPException
from app.schemas import ProjectCreate, RunLoopRequest
from app.services.project_store import project_store
from app.services.job_service import job_service
from app.services.generation_loop_runner import GenerationLoopRunner

router = APIRouter()
runner = GenerationLoopRunner()

@router.post('')
def create_project(payload: ProjectCreate):
    return {'project': project_store.create(payload)}

@router.get('')
def list_projects():
    return {'items': project_store.list()}

@router.get('/{project_id}')
def get_project(project_id: int):
    try: return {'project': project_store.get(project_id)}
    except KeyError as exc: raise HTTPException(status_code=404, detail='Project not found') from exc

@router.patch('/{project_id}')
def patch_project(project_id:int,payload:dict):
    p = project_store.get(project_id); p.update(payload); project_store.save(p); return {'project':p}

@router.delete('/{project_id}')
def delete_project(project_id:int):
    project_store.projects.pop(project_id, None); return {'deleted':True}

@router.post('/{project_id}/run-loop')
def run_loop(project_id:int,payload:RunLoopRequest):
    p = project_store.get(project_id); p['status']='running'
    job_id = job_service.create(project_id, {'status':'queued'})
    result = runner.run(p, payload.chunk_words, payload.max_steps)
    job_service.update(job_id, status=result['project']['status'], progress=result)
    project_store.save(result['project'])
    return {'job_id':job_id,'status':result['project']['status']}

@router.post('/{project_id}/pause')
def pause(project_id:int):
    p = project_store.get(project_id); p['status']='paused'; project_store.save(p); return {'status':'paused'}
@router.post('/{project_id}/resume')
def resume(project_id:int):
    p = project_store.get(project_id); p['status']='running'; project_store.save(p); return {'status':'running'}
@router.post('/{project_id}/cancel')
def cancel(project_id:int):
    p = project_store.get(project_id); p['status']='cancelled'; project_store.save(p); return {'status':'cancelled'}

@router.get('/jobs/{job_id}')
def get_job(job_id:str): return job_service.get(job_id)
