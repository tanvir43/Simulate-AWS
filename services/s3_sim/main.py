from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import os
import shutil

app = FastAPI(title="S3 Simulator")

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Generate versioned filename
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        versioned_filename = f"{timestamp}_{file.filename}"
        file_path = os.path.join(UPLOAD_DIR, versioned_filename)

        # Save the file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(content={
            "status": "success",
            "filename": file.filename,
            "version": timestamp,
            "stored_as": versioned_filename
        }, status_code=201)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
