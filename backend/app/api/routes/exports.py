from fastapi import APIRouter
router=APIRouter(); store={}
@router.post('/{book_id}/ebook/settings')
def ebook_settings(book_id:int,payload:dict): store[f'ebook-{book_id}']=payload; return {'book_id':book_id,'settings':payload}
@router.get('/{book_id}/ebook/settings')
def get_ebook_settings(book_id:int): return {'book_id':book_id,'settings':store.get(f'ebook-{book_id}',{})}
@router.post('/{book_id}/ebook/generate')
def ebook_generate(book_id:int): return {'book_id':book_id,'format':'EPUB','status':'generated'}
@router.post('/{book_id}/pdf/normal')
def pdf_normal(book_id:int,payload:dict): return {'book_id':book_id,'type':'normal','status':'generated'}
@router.post('/{book_id}/pdf/layout')
def pdf_layout(book_id:int,payload:dict): return {'book_id':book_id,'type':'layout','status':'generated'}
@router.post('/{book_id}/pdf/print-ready')
def pdf_print(book_id:int,payload:dict): return {'book_id':book_id,'type':'print-ready','status':'generated'}
@router.get('/{book_id}/pdf/exports')
def pdf_exports(book_id:int): return {'book_id':book_id,'items':[]}
@router.get('/pdf/exports/{export_id}/download')
def pdf_download(export_id:int): return {'export_id':export_id,'url':f'/tmp/export-{export_id}.pdf'}
@router.post('/{book_id}/docx/export')
def docx_export(book_id:int,payload:dict): return {'book_id':book_id,'url':f'/tmp/book-{book_id}.docx'}
@router.get('/docx/exports/{export_id}/download')
def docx_download(export_id:int): return {'export_id':export_id,'url':f'/tmp/export-{export_id}.docx'}
