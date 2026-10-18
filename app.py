from fastapi import FastAPI
from config import init_firebase
from routes import router

# تهيئة التطبيق
app = FastAPI(title="PlotCraft UI", version="1.0")

# تهيئة قاعدة البيانات عند البدء
init_firebase()

# ربط المسارات
app.include_router(router)
