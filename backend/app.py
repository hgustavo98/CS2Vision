from fastapi import FastAPI, UploadFile
from ml_routes import router as ml_router
import subprocess
import os

app = FastAPI()

# Include ML routes
app.include_router(ml_router)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
def upload_demo(file: UploadFile):
    # Save the uploaded file
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(file.file.read())

    # Call the parser
    result = subprocess.run(["go", "run", "../demos/parser.go", "--file", file_location],
                             capture_output=True, text=True)

    if result.returncode != 0:
        return {"error": "Failed to parse the demo", "details": result.stderr}

    return {"status": "success", "parser_output": result.stdout}