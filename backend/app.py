# FastAPI Backend
from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/upload')
def upload_demo(file: UploadFile):
    return {'filename': file.filename}
