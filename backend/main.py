from fastapi import FastAPI, File, UploadFile
from .models import Event, PreviewRequest
import pandas as pd
import io

app = FastAPI()

@app.post("/events")
async def create_event(event: Event):
    return {"status": "success", "event_received": event}

@app.post("/upload-excel")
async def upload_excel(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_excel(io.BytesIO(contents))
    return df.to_dict(orient="records")

@app.post("/preview-message")
async def preview_message(request: PreviewRequest):
    formatted_message = request.template.format(**request.event.data)
    return {"preview": formatted_message}

@app.get("/")
def read_root():
    return {"Hello": "World"}
