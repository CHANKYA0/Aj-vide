from fastapi import APIRouter
from app.api.routes import admin, ai_providers, auth, chatbot, cost, exports, generation, images, imports, marketing, projects, research, style

api_router = APIRouter()
api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(projects.router, prefix='/projects', tags=['projects'])
api_router.include_router(generation.router, prefix='/generate', tags=['generation'])
api_router.include_router(chatbot.router, prefix='/books', tags=['chatbot'])
api_router.include_router(exports.router, prefix='/books', tags=['exports'])
api_router.include_router(imports.router, prefix='/books', tags=['imports'])
api_router.include_router(style.router, prefix='/books', tags=['style'])
api_router.include_router(research.router, prefix='/books', tags=['research'])
api_router.include_router(images.router, prefix='/books', tags=['images'])
api_router.include_router(marketing.router, prefix='/books', tags=['marketing'])
api_router.include_router(cost.router, prefix='/cost', tags=['cost'])
api_router.include_router(ai_providers.router, prefix='/ai-providers', tags=['ai-providers'])
api_router.include_router(admin.router, prefix='/admin', tags=['admin'])
