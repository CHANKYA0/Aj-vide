from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_project_create_and_loop():
    r = client.post('/projects', json={'title': 'T', 'genre': 'Dark Romance', 'preset_name': 'Short Story'})
    assert r.status_code == 200
    pid = r.json()['project']['id']
    r2 = client.post(f'/projects/{pid}/run-loop', json={'chunk_words': 500, 'max_steps': 3})
    assert r2.status_code == 200
    assert 'job_id' in r2.json()


def test_cost_endpoint():
    r = client.post('/cost/estimate-project', json={'input_tokens': 1000, 'output_tokens': 1000, 'input_per_m': 1, 'output_per_m': 1})
    assert r.status_code == 200


def test_exports_docx_pdf_epub():
    assert client.post('/books/1/docx/export', json={'content': 'hello'}).status_code == 200
    assert client.post('/books/1/pdf/normal', json={'content': 'hello'}).status_code == 200
    assert client.post('/books/1/ebook/generate', json={'content': 'hello'}).status_code == 200
