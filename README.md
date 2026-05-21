# AI Book Studio MVP

## Setup
- Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
- Tests: `cd backend && pytest`
- Frontend: `cd frontend && npm install && npm run build`

## Env Vars
- `DATABASE_URL` (default sqlite for local)
- `REDIS_URL`
- `SECRET_KEY`

## Key API examples
- Create project: `POST /projects`
- Run loop: `POST /projects/{id}/run-loop`
- Pause/resume/cancel: `POST /projects/{id}/pause|resume|cancel`
- Job status: `GET /projects/jobs/{job_id}`
- Cost estimate: `POST /cost/estimate-project`
- Exports: `/books/{id}/docx/export`, `/books/{id}/pdf/normal`, `/books/{id}/ebook/generate`

## Architecture
- Modular routes and services
- Provider adapter system with OpenAI/Gemini + stubs
- Prompt templates in `backend/app/templates/prompts`
- Future-ready video/audio provider interfaces
