
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

def init_firebase():
    """
    تهيئة اتصال Firebase.
    تقوم بإرجاع كائن قاعدة البيانات (db) إذا نجح الاتصال، أو None في حال فشل.
    """
    # نتحقق إذا كان التطبيق قد تم تهيئته مسبقاً لتجنب الأخطاء
    if not firebase_admin._apps:
        try:
            # قراءة الأسرار من Streamlit secrets
            secret_dict = dict(st.secrets["firebase"])
            
            # معالجة مفتاح الـ private_key للتأكد من تنسيق السطور
            if "private_key" in secret_dict:
                pk = secret_dict["private_key"].strip()
                if not pk.startswith('"') and not pk.startswith("'"):
                    pk = pk.replace("\\n", "\n")
                secret_dict["private_key"] = pk

            # تهيئة الاتصال
            cred = credentials.Certificate(secret_dict)
            firebase_admin.initialize_app(cred)
        except Exception as e:
            # في حال حدوث خطأ، لا نوقف التطبيق، فقط نطبعه في الكونسول
            print(f"Firebase Init Error: {e}")
            return None
    
    # إرجاع كائن قاعدة البيانات
    return firestore.client()
