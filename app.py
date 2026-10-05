import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="PlotCraft UI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تنسيقات CSS مخصصة لتلائم التصميم الداكن الفاخر
st.markdown("""
    <style>
    .stApp {
        background-color: #0e0e11;
        color: #ffffff;
        font-family: sans-serif;
    }
    .top-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
    }
    .welcome-text {
        font-size: 22px;
        font-weight: bold;
        text-align: right;
        margin-top: 20px;
    }
    .card-container {
        display: flex;
        gap: 15px;
        margin-top: 20px;
    }
    .mode-card {
        background-color: #1a1a24;
        border: 1px solid #2a2a3b;
        border-radius: 15px;
        padding: 20px;
        flex: 1;
        text-align: right;
        cursor: pointer;
    }
    .mode-card:hover {
        border-color: #4a4a6b;
    }
    /* تنسيق مربع المساعد الذكي */
    .ai-box {
        background-color: #1a1a24;
        border: 1px solid #2a2a3b;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 20px;
    }
    .ai-header {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 10px;
        margin-bottom: 8px;
    }
    .ai-title {
        color: #ff4b8b;
        font-weight: bold;
        font-size: 16px;
    }
    .ai-avatar {
        width: 35px;
        height: 35px;
        background: linear-gradient(135deg, #ff4b8b, #7928ca);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: white;
    }
    .ai-desc {
        text-align: right;
        color: #cccccc;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة التنقل بين الصفحات داخل التطبيق
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    # زر ترقية في الأعلى
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("⭐ ترقية"):
            pass
    with col2:
        st.markdown("<h3 style='text-align: right; margin:0;'>بلوت كرافت</h3>", unsafe_allow_html=True)

    st.markdown("<div class='welcome-text'>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</div>", unsafe_allow_html=True)

    # البطاقات الرئيسية (سريع و خطوة بخطوة)
    col_fast, col_step = st.columns(2)
    
    with col_fast:
        st.markdown("""
            <div class='mode-card'>
                <div style='font-size: 20px; margin-bottom: 10px;'>⚡</div>
                <div style='font-weight: bold; font-size: 18px;'>سريع</div>
                <div style='color: #888; font-size: 13px; margin-top: 5px;'>إدخال واحد، فيديو كامل</div>
            </div>
        """, unsafe_allow_html=True)

    with col_step:
        # استخدام زر شفاف فوق البطاقة للانتقال لصفحة "خطوة بخطوة"
        if st.button("خطوة بخطوة 🚗\nراجع كل خطوة", key="btn_step"):
            st.session_state.page = 'step_by_step'
            st.rerun()

    # قسم الإلهام
    st.markdown("<br><h4 style='text-align: right;'>إلهام بلوت كرافت</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right; color: #888; font-size: 14px;'>عرض الكل ></div>", unsafe_allow_html=True)

# --- صفحة خطوة بخطوة (مطابقة للصورة الثانية مع التعديلات المطلوبة) ---
elif st.session_state.page == 'step_by_step':
    
    # زر العودة
    if st.button("❮ عودة"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>دراما</h2>", unsafe_allow_html=True)

    # صندوق المساعد الذكي بالتعديلات الجديدة
    st.markdown("""
        <div class='ai-box'>
            <div class='ai-header'>
                <span class='ai-title'>مساعد AI بلوت كرافت</span>
                <div class='ai-avatar'>ب</div>
            </div>
            <div class='ai-desc'>عزيزي المخرج، ما نوع القصة التي تريد إنشاءها؟ اكتب فكرتك ودع مساعد AI يحولها إلى واقع.</div>
        </div>
    """, unsafe_allow_html=True)

    # قسم إعداد القصة
    with st.container():
        st.markdown("""
            <div style='background-color: #1a1a24; border: 1px solid #2a2a3b; border-radius: 12px; padding: 20px;'>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;'>
                    <span style='background-color: #2a2a3b; padding: 2px 10px; border-radius: 10px; font-size: 12px;'>0/2</span>
                    <span style='font-weight: bold;'>إعداد القصة</span>
                </div>
                <div style='text-align: right; color: #888; font-size: 13px; margin-bottom: 15px;'>أضف الشخصيات والقصة أولاً، ثم اختر المدة والنسبة.</div>
            </div>
        """, unsafe_allow_html=True)
        
        # أزرار الإضافة داخل إعداد القصة
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.button("⬆ إضافة الشخصيات (أضف شخصيتين كحد أقصى)")
        with col_btn2:
            st.button("✍ إضافة الحكاية (اضغط لكتابة قستك)")

        st.markdown("<br>", unsafe_allow_html=True)
        st.button("التالي", use_container_width=True)
