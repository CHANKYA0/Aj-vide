from fastapi import APIRouter
router=APIRouter()
@router.post('/{book_id}/docx/import')
def import_docx(book_id:int,payload:dict): return {'book_id':book_id,'status':'imported','payload':payload}
