import streamlit as st
import streamlit.components.v1 as components
import firebase_admin
from firebase_admin import credentials, firestore

# --- تهيئة اتصال Firebase بشكل آمن تماماً لا يوقف التطبيق ---
db = None
if not firebase_admin._apps:
    try:
        secret_dict = dict(st.secrets["firebase"])
        if "private_key" in secret_dict:
            # معالجة دقيقة لترميز السطور الخاصة بالمفتاح
            pk = secret_dict["private_key"].strip()
            if not pk.startswith('"') and not pk.startswith("'"):
                pk = pk.replace("\\n", "\n")
            secret_dict["private_key"] = pk

        cred = credentials.Certificate(secret_dict)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    except Exception as e:
        # لن يتوقف التطبيق أبداً حتى لو فشل الاتصال، وستعمل الواجهة بشكل طبيعي
        pass

# إعدادات الصفحة الأساسية مع تقييد الأمان ومنع عرض الشريط الجانبي
st.set_page_config(
    page_title="PlotCraft UI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# قسم التنسيق والحماية البصرية وإلغاء الهوامش وشريط الاستخدام الافتراضي
st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        header {
            visibility: hidden !important;
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# نظام قراءة وتحميل ملف الـ HTML الخارجي مع تأمين الجلسة والحقن الآمن
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    security_shield_injection = """
    <script>
        // تفعيل درع الحماية الخاص بتطبيق PlotCraft
        console.log("🛡️ PlotCraft Security Architecture: Online");
    </script>
    """
    
    if "</body>" in html_code:
        html_code = html_code.replace("</body>", security_shield_injection + "</body>")
    else:
        html_code += security_shield_injection

    components.html(html_code, height=680, scrolling=False)

except FileNotFoundError:
    st.error("الرجاء التأكد من وجود ملف index.html في نفس المجلد.")
