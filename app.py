import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config import init_firebase
from security import sanitize_input  # استيراد دالة التنظيف الآمنة

app = FastAPI()
db = init_firebase()

# ربط مجلد static لتقديم الملفات الثابتة
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # تمرير request أولاً لمطابقة تحديثات FastAPI وStarlette الحديثة
    return templates.TemplateResponse(request, "index.html")

# مسار خاص لخدمة ملف manifest.json مباشرة لـ PWABuilder
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
        
    # تنظيف البيانات وتصحيح المفاتيح لمنع أخطاء unhashable type
    data = sanitize_input(raw_data)
    
    db.collection('users').add(data)
    return {"status": "saved"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
