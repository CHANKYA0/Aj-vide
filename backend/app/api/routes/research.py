from fastapi import APIRouter
router=APIRouter()
@router.post('/{book_id}/research/source')
def add_source(book_id:int,payload:dict): return {'book_id':book_id,'source':payload}
@router.get('/{book_id}/research/sources')
def list_sources(book_id:int): return {'book_id':book_id,'items':[]}
@router.post('/{book_id}/fact-check')
def fact_check(book_id:int,payload:dict): return {'book_id':book_id,'fact_check_score':80,'issues':[]}
@router.get('/{book_id}/claims')
def claims(book_id:int): return {'book_id':book_id,'items':[]}
@router.post('/trends/search')
def trends(payload:dict): return {'platform':payload.get('platform','TikTok'),'trend_summary':'manual trend summary'}
