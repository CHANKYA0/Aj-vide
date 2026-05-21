from fastapi import FastAPI
from app.api.router import api_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title='AI Book Studio API', version='1.0.0')
app.include_router(api_router)

@app.get('/health')
def health():
    return {'status':'ok'}
