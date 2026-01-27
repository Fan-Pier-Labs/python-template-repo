import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="Python Template", version="0.1.0")

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Hello via Python!"})

@app.get("/health")
async def health():
    return JSONResponse(content={"status": "ok"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(app, host=host, port=port)
