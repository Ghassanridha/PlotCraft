import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

st.set_page_config(page_title="PlotCraft UI", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 1. إعدادات رابط جوجل المباشر لتجاوز حظر WebView / Iframe
CLIENT_ID = "1087604212326-ar74pri9eaaneqvi552b04fba91k0804.apps.googleusercontent.com"
REDIRECT_URI = "https://plotcraft-s84ivmhu8safjehv7vxwvs.streamlit.app"

params = {
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "response_type": "token",
    "scope": "openid email profile",
}
google_auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urllib.parse.urlencode(params)}"

# 2. قراءة ملف الـ HTML الخارجي وعرضه مع حقن رابط تسجيل الدخول الآمن
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # إذا كنت تريد زر تسجيل الدخول يظهر بداخل التطبيق مع تصميمك:
    # يمكنك حقن رابط الجوجل المباشر بدل الزر القديم المحظور
    # أو عرض زر الـ Redirect مباشرة فوق الـ HTML لضمان عدم الحظر:
    st.markdown(f'''
        <div style="text-align: center; padding: 10px; background: #fff;">
            <a href="{google_auth_url}" target="_self">
                <button style="
                    background-color: #4285F4;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    font-size: 15px;
                    border-radius: 6px;
                    cursor: pointer;
                    font-weight: bold;">
                    تسجيل الدخول بواسطة Google (بدون حظر)
                </button>
            </a>
        </div>
    ''', unsafe_allow_html=True)

    # عرض واجهتك الأصلية
    components.html(html_code, height=620, scrolling=False)

except FileNotFoundError:
    st.error("الرجاء التأكد من وجود ملف index.html في نفس المجلد.")
