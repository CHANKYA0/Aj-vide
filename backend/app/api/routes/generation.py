from fastapi import APIRouter
from app.services.ai_router import AIRouter

router=APIRouter(); ai=AIRouter()
@router.post('/next-chunk')
def next_chunk(payload:dict): return {'chunk':ai.text('writer_model', payload.get('prompt',''))}
@router.post('/rewrite')
def rewrite(payload:dict): return {'rewrite':ai.text('final_rewrite_model', payload.get('prompt',''))}
@router.post('/final-polish')
def final_polish(payload:dict): return {'polished':ai.text('final_rewrite_model', payload.get('prompt',''))}
@router.post('/decision-options')
def decisions(payload:dict): return {'options':['continue','revise','pause']}
@router.post('/chapter-outline')
def chapter_outline(payload:dict): return {'outline':['Goal','Conflict','Hook']}
@router.post('/full-outline')
def full_outline(payload:dict): return {'chapters':[{'number':1,'title':'Opening'}]}
