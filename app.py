import os
import requests
import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from security import sanitize_input  # استيراد دالة التنظيف الآمنة

app = FastAPI()

# تهيئة Firebase مباشرة بشكل آمن ومتوافق مع Render بدون الحاجة لملف config.py
db = None
try:
    if not firebase_admin._apps:
        creds_json = os.getenv("FIREBASE_CREDENTIALS")
        creds_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "serviceAccountKey.json")
        
        if creds_json:
            import json
            cred = credentials.Certificate(json.loads(creds_json))
            firebase_admin.initialize_app(cred)
        elif os.path.exists(creds_path):
            cred = credentials.Certificate(creds_path)
            firebase_admin.initialize_app(cred)
        else:
            firebase_admin.initialize_app()
            
        db = firestore.client()
except Exception as e:
    print(f"Firebase Init Error: {e}")

# تعريف مفتاح يوتيوب بشكل آمن
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "AIzaSyDuSWbvfNJiGk7sw3eO6xJpPPur5L_heqA")

# ربط مجلد static لتقديم الملفات الثابتة
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

# مسار خاص لجلب فيديوهات اليوتيوب
@app.get("/api/videos")
async def get_youtube_videos(query: str = "trending", pageToken: str = ""):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={query}&type=video&key={YOUTUBE_API_KEY}"
    
    if pageToken:
        url += f"&pageToken={pageToken}"
        
    try:
        response = requests.get(url)
        data = response.json()
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

# مسار لخدمة manifest.json لـ PWABuilder
@app.get("/manifest.json")
async def get_manifest():
    return FileResponse("static/manifest.json", media_type="application/json")

@app.post("/save")
async def save(request: Request):
    if db is None:
        return JSONResponse({"error": "Firebase غير متصل"}, status_code=500)
    
    try:
        raw_data = await request.json()
    except Exception:
        raw_data = {}
        
    data = sanitize_input(raw_data)
    db.collection('users').add(data)
    return {"status": "saved"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
