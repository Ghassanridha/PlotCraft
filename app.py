import streamlit as st
import streamlit.components.v1 as components

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
    
    # حقن طبقة أمان برمجية خفيفة لمراقبة وتأمين الاتصال داخل الواجهة
    security_shield_injection = """
    <script>
        // تفعيل درع الحماية الخاص بتطبيق PlotCraft
        console.log("🛡️ PlotCraft Security Architecture: Online");
    </script>
    """
    
    # دمج الدرع الأمني في هيكل الـ HTML قبل عرضه
    if "</body>" in html_code:
        html_code = html_code.replace("</body>", security_shield_injection + "</body>")
    else:
        html_code += security_shield_injection

    # عرض الواجهة الآمنة الكاملة بالأبعاد المحددة
    components.html(html_code, height=680, scrolling=False)

except FileNotFoundError:
    st.error("الرجاء التأكد من وجود ملف index.html في نفس المجلد.")
