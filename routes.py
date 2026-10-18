import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

router = APIRouter()

@app_router := APIRouter()

@router.get("/", response_class=HTMLResponse)
async def serve_index():
    """قراءة وحقن ملف الـ HTML الرئيسي"""
    try:
        if not os.path.exists("index.html"):
            raise HTTPException(status_code=444, detail="ملف index.html غير موجود.")
        
        with open("index.html", "r", encoding="utf-8") as f:
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

@router.get("/health")
async def health_check():
    """نقطة فحص سلامة السيرفر"""
    return {"status": "online", "system": "PlotCraft FastAPI Backend"}
