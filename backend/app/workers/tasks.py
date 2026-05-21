from app.workers.celery_app import celery_app

@celery_app.task
def run_generation_job(project_id: int):
    return {'project_id': project_id, 'status': 'queued'}
