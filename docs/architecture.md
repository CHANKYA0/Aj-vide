# AI Book Studio Architecture (MVP-first)

## Monorepo Layout
- frontend: Next.js + TypeScript + Tailwind shell.
- backend: FastAPI service with modular engines and provider routing.
- jobs: async tasks via Celery (future wiring).

## Core design decisions
1. **Provider abstraction first** for text/image/video/audio/research.
2. **Workflow engines** split by bounded contexts (writing, style, export, marketing).
3. **JSONB-heavy schema** to remain extensible for future model/provider additions.
4. **Versioned content** for all transformations and rewrites.
5. **Usage/cost logging** around every model call.

## MVP modules included in scaffold
- Auth, Projects, Chapters/Scenes, Generation pipeline endpoints
- Chatbot endpoint
- Style upload/analyze placeholder
- Research source save + citations placeholder
- Export settings + export job creation
- Marketing script/caption generation placeholder
- Cost estimation endpoint
- Admin model pricing endpoint
- Video provider interface (disabled generation by default)


## Autonomous generation loop
- `GenerationLoopRunner` executes repeated chunk generation in a while-loop and updates chapter + project progress.
- Loop stops only when project target words are completed or an explicit safety max step threshold is reached.
- Endpoint: `POST /projects/{id}/run-loop` with `chunk_words` and `max_steps`.
