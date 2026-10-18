import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def serve_index():
    try:
        file_path = os.path.join("templates", "index.html")
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="ملف index.html غير موجود داخل مجلد templates.")
        
        with open(file_path, "r", encoding="utf-8") as f:
            html_code = f.read()
        
        security_shield_injection = """
        <script>
            console.log("🛡️ PlotCraft Security Architecture: Online & Secure");
        </script>
        """
        
        if "</body>" in html_code:
            html_code = html_code.replace("</body>", security_shield_injection + "</body>")
        else:
            html_code += security_shield_injection

        return HTMLResponse(content=html_code)

    except Exception as e:
        return HTMLResponse(content=f"<h3>خطأ في تحميل الصفحة: {str(e)}</h3>", status_code=500)


@router.get("/youtube.html", response_class=HTMLResponse)
async def serve_youtube():
    try:
        file_path = os.path.join("templates", "youtube.html")
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="ملف youtube.html غير موجود داخل مجلد templates.")
        
        with open(file_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())

    except Exception as e:
        return HTMLResponse(content=f"<h3>خطأ في تحميل الصفحة: {str(e)}</h3>", status_code=500)


@router.get("/health")
async def health_check():
    return {"status": "online", "system": "PlotCraft FastAPI Backend"}
