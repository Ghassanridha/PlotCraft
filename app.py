import os
import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# تهيئة Firebase مباشرة بشكل آمن ومتوافق مع Render
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

# ربط مجلد الملفات الثابتة (static)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# ربط مجلد القوالب (templates) لتمكين الـ fetch من جلب القوالب المستقلة مثل نافذة الاشتراكات
if os.path.exists("templates"):
    app.mount("/templates", StaticFiles(directory="templates"), name="templates")

templates = Jinja2Templates(directory="templates")

# المسار الرئيسي لخدمة واجهة index.html
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

# ⭐ أضف هذا المسار الجديد هنا لكي يعمل زر الترقية وجلب نافذة الاشتراكات بنجاح
@app.get("/subscription-modal", response_class=HTMLResponse)
async def subscription_modal(request: Request):
    return templates.TemplateResponse(request, "subscription_modal.html")

# مسار لخدمة manifest.json
@app.get("/manifest.json")
async def get_manifest():
    return FileResponse("static/manifest.json", media_type="application/json")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
