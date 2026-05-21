from fastapi import APIRouter
router=APIRouter()
@router.post('/{book_id}/images/generate-prompt')
def image_prompt(book_id:int,payload:dict): return {'book_id':book_id,'prompt':f"Create {payload.get('image_type','scene illustration')} in {payload.get('aspect_ratio','9:16')}"}
@router.post('/{book_id}/cover/generate-prompt')
def cover_prompt(book_id:int,payload:dict): return {'book_id':book_id,'front_cover_prompt':'dark cinematic cover prompt','kdp_description':'Generated KDP blurb'}
@router.post('/{book_id}/video/generate-prompt')
def video_prompt(book_id:int,payload:dict): return {'book_id':book_id,'prompt':'future video provider prompt'}
@router.post('/{book_id}/video/create-storyboard')
def storyboard(book_id:int,payload:dict): return {'book_id':book_id,'storyboard':[payload]}
