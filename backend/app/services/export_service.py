from pathlib import Path


class ExportService:
    def __init__(self) -> None:
        self.base = Path('/tmp/aibookstudio_exports')
        self.base.mkdir(parents=True, exist_ok=True)

    def _write(self, book_id: int, name: str, ext: str, content: str) -> str:
        path = self.base / f'book_{book_id}_{name}.{ext}'
        path.write_text(content)
        return str(path)

    def export_docx(self, book_id: int, payload: dict) -> str:
        return self._write(book_id, 'manuscript', 'docx', payload.get('content', 'DOCX placeholder content'))

    def export_pdf(self, book_id: int, pdf_type: str, payload: dict) -> str:
        return self._write(book_id, pdf_type, 'pdf', payload.get('content', f'{pdf_type} PDF placeholder'))

    def export_epub(self, book_id: int, payload: dict) -> str:
        return self._write(book_id, 'ebook', 'epub', payload.get('content', 'EPUB placeholder content'))
