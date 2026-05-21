from fastapi import APIRouter
router=APIRouter()
@router.post('/{book_id}/marketing/create-campaign')
def create_campaign(book_id:int,payload:dict): return {'book_id':book_id,'campaign':payload}
@router.post('/{book_id}/marketing/generate-assets')
def generate_assets(book_id:int,payload:dict): return {'book_id':book_id,'assets':[{'type':'instagram_caption','text':'Dark romance launch today.'}]}
@router.post('/{book_id}/marketing/generate-reel-script')
def reel(book_id:int,payload:dict): return {'book_id':book_id,'hook':'He was never meant to save her.'}
