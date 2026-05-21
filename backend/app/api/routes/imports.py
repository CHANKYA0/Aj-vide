from pathlib import Path

from fastapi import APIRouter

router = APIRouter()


@router.post('/{book_id}/docx/import')
def import_docx(book_id: int, payload: dict):
    path = payload.get('path', '')
    content = ''
    if path and Path(path).exists():
        content = Path(path).read_text()[:5000]
    return {'book_id': book_id, 'status': 'imported', 'content_preview': content[:250]}
