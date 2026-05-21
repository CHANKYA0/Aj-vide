from fastapi import APIRouter
router=APIRouter()
@router.post('/{book_id}/style/upload-reference')
def upload_style(book_id:int,payload:dict): return {'book_id':book_id,'uploaded':True,'rights_confirmed':payload.get('rights_confirmed',False)}
@router.post('/{book_id}/style/analyze')
def analyze(book_id:int): return {'book_id':book_id,'profile':{'pov':'third person','tone':'dark'}}
@router.get('/{book_id}/style/profiles')
def profiles(book_id:int): return {'book_id':book_id,'items':[]}
@router.patch('/style/profiles/{profile_id}')
def patch(profile_id:int,payload:dict): return {'profile_id':profile_id,'changes':payload}
@router.post('/{book_id}/style/check')
def check(book_id:int,payload:dict): return {'book_id':book_id,'match_score':78}
@router.post('/{book_id}/style/apply')
def apply(book_id:int,payload:dict): return {'book_id':book_id,'status':'applied'}
