from fastapi import APIRouter
from app.services.ai_router import AIRouter
router=APIRouter(); ai=AIRouter(); sessions={}
@router.post('/{book_id}/chat')
def chat(book_id:int,payload:dict):
    sid=str(payload.get('session_id','default'))
    sessions.setdefault(sid,[]).append(payload.get('message',''))
    return {'book_id':book_id,'session_id':sid,'reply':ai.text('chatbot_model',payload.get('message',''))}
@router.get('/{book_id}/chat/sessions')
def list_sessions(book_id:int): return {'book_id':book_id,'sessions':list(sessions.keys())}
@router.get('/chat/sessions/{session_id}')
def get_session(session_id:str): return {'session_id':session_id,'messages':sessions.get(session_id,[])}
