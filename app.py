import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from config import init_firebase

app = FastAPI()
db = init_firebase()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/save")
async def save(request: Request):
    if db is None:
        return JSONResponse({"error": "Firebase غير متصل"}, status_code=500)
    
    try:
        data = await request.json()
    except Exception:
        data = {}
        
    db.collection('users').add(data)
    return {"status": "saved"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
