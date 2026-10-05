import streamlit as str

# 1. إعدادات الصفحة لتناسب شاشة الجوال وتفعيل الوضع الداكن
str.set_page_config(
    page_title="Plot Craft UI",
    layout="centered", # يجعل المحتوى في المنتصف ومناسب للجوال
    initial_sidebar_state="collapsed"
)

# تخصيص المظهر بالكامل عبر CSS ليتطابق مع واجهة التطبيق الداكنة
str.markdown("""
    <style>
    /* تغيير خلفية التطبيق إلى الأسود */
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    /* تنسيق الحاوية العلوية (Hero Section) */
    .hero-box {
        background: linear-gradient(180deg, #1e222b 0%, #15181f 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: right;
        margin-bottom: 20px;
        border: 1px solid #2d3139;
    }
    /* تنسيق الأزرار */
    .stButton > button {
        width: 100% !important;
        height: 75px !important;
        border-radius: 12px !important;
        font-size: 14px !important;
        font-weight: bold !important;
        direction: rtl;
    }
    /* زر خطوة بخطوة الداكن */
    .step-btn > div > button {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
    }
    /* زر سريع البنفسجي Pro */
    .fast-btn > div > button {
        background-color: #2a2235 !important;
        color: #d1b3ff !important;
        border: 1px solid #7b2cbf !important;
    }
    /* عنوان القسم والمحاذاة لليمين */
    .section-title {
        text-align: right;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 18px;
    }
    /* كروت الأفلام الإلهامية */
    .movie-card {
        background-color: #1e1e1e;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        border: 1px solid #2d2d2d;
    }
    .movie-thumb {
        background-color: #2d2d2d;
        height: 140px;
        border-radius: 6px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #555;
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. قسم الواجهة العلوية (Hero Section) محاذاة لليمين بالعربي
str.markdown("""
    <div class="hero-box">
        <h2 style='color: #ffffff; margin: 0;'>بلوت كرافت</h2>
        <h4 style='color: #e0e0e0; margin: 10px 0 5px 0;'>مساء الخير، أيها المخرج</h4>
        <p style='color: #a0a0a0; margin: 0;'>أي قصة سنصنع اليوم؟</p>
    </div>
""", unsafe_allow_html=True)

# 3. أزرار الخيارات الرئيسية (مقسمة إلى عمودين متساويين يناسبان الجوال)
col1, col2 = str.columns(2)

with col1:
    # العمود الأول (يسار) يحتوي على زر سريع
    str.markdown('<div class="fast-btn">', unsafe_allow_html=True)
    str.button("⚡ سريع\n(Pro Only) إدخال واحد، فيديو كامل", key="fast")
    str.markdown('</div>', unsafe_allow_html=True)

with col2:
    # العمود الثاني (يمين) يحتوي على زر خطوة بخطوة
    str.markdown('<div class="step-btn">', unsafe_allow_html=True)
    str.button("💬 خطوة بخطوة\nراجع كل خطوة وصمم قصة", key="step")
    str.markdown('</div>', unsafe_allow_html=True)

# 4. قسم إلهام بلوت كرافت (المعرض)
str.markdown('<div class="section-title">إلهام بلوت كرافت</div>', unsafe_allow_html=True)

# تقسيم المعرض إلى 3 أعمدة أفقية مصفوفة بجانب بعضها لشاشات الجوال
m_col1, m_col2, m_col3 = str.columns(3)

with m_col1:
    str.markdown("""
        <div class="movie-card">
            <div class="movie-thumb">🎬</div>
            <span style="font-size: 11px; font-weight: bold;">THE INVITATION</span>
        </div>
    """, unsafe_allow_html=True)

with m_col2:
    str.markdown("""
        <div class="movie-card">
            <div class="movie-thumb">🎬</div>
            <span style="font-size: 11px; font-weight: bold;">THE WRONG DOOR</span>
        </div>
    """, unsafe_allow_html=True)

with m_col3:
    str.markdown("""
        <div class="movie-card">
            <div class="movie-thumb">🎬</div>
            <span style="font-size: 11px; font-weight: bold;">THE DELIVERYMAN...</span>
        </div>
    """, unsafe_allow_html=True)
