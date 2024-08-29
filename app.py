import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
import requests
import gradio as gr
from dotenv import load_dotenv
load_dotenv()
from starlette.responses import HTMLResponse

from fastapi import FastAPI
from middleware import LogMiddleware, setup_cors
from routes.base import router
app = FastAPI()

app.add_middleware(LogMiddleware)
setup_cors(app)
app.include_router(router)
@app.get("file")
async def main():
    content = """
<body>
<form action="/read_data/embedding/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)