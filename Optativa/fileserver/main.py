from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os

app = FastAPI()

UPLOAD_DIRECTORY = "uploads"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Subir archivos</title>
    </head>
    <body>
        <h1>Subir un Archivo</h1>
        <form action="/uploadfile/" enctype="multipart/form-data" method="post">
            <input name="file" type="file">
            <button>Subir</button>
        </form>
    </body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def main():
    return html


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"Archivo guardado en {file_location}"}
