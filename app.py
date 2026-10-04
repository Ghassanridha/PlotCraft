import streamlit as st

# إعدادات الصفحة لتكون بعرض كامل وتناسب الهواتف/الشاشات الداكنة
st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# تنسيقات CSS مخصصة لمحاكاة التصميم الداكن (Dark Mode) والأزرار والبطاقات
st.markdown(
    """
    <style>
    /* خلفية التطبيق العامة */
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* إخفاء عناصر ستريملايت الافتراضية للترويسة */
    header {visibility: hidden;}
    .reportview-container .main footer {visibility: hidden;}
    
    /* شريط الترقية العلوي */
    .top-badge {
        display: inline-block;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        color: #e2e8f0;
        margin-bottom: 15px;
    }
    
    /* ترحيب المخرج */
    .welcome-title {
        font-size: 22px;
        font-weight: bold;
        text-align: right;
        color: #ffffff;
        margin-bottom: 5px;
    }
    .welcome-subtitle {
        font-size: 18px;
        text-align: right;
        color: #94a3b8;
        margin-bottom: 20px;
    }
    
    /* بطاقات الخيارات السريعة */
    .feature-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 15px;
        text-align: right;
        margin-bottom: 10px;
        position: relative;
    }
    .pro-badge {
        position: absolute;
        top: 10px;
        left: 10px;
        background-color: rgba(255, 255, 255, 0.15);
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 10px;
        color: #cbd5e1;
    }
    .card-title {
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 5px;
    }
    .card-desc {
        font-size: 12px;
        color: #94a3b8;
    }
    
    /* عناوين الأقسام */
    .section-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 25px;
        margin-bottom: 15px;
        direction: rtl;
    }
    .section-title {
        font-size: 18px;
        font-weight: bold;
        color: #ffffff;
    }
    .section-more {
        font-size: 13px;
        color: #94a3b8;
        cursor: pointer;
    }
    
    /* بطاقات الأفلام (الإلهام) */
    .movie-card {
        background-color: #1e293b;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: right;
    }
    .movie-title {
        padding: 10px;
        font-size: 13px;
        font-weight: bold;
        color: #ffffff;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# زر الترقية العلوي
st.markdown('<div style="text-align: right;"><span class="top-badge">👑 ترقية</span></div>', unsafe_allow_html=True)

# رسالة الترحيب
st.markdown('<div class="welcome-title">مساء الخير، أيها المخرج</div>', unsafe_allow_html=True)
st.markdown('<div class="welcome-subtitle">أي قصة سنصنع اليوم؟</div>', unsafe_allow_html=True)

# بطاقات الخيارات الرئيسية (سريع / خطوة بخطوة)
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <span class="pro-badge">Pro only</span>
            <div style="font-size: 20px;">⚡</div>
            <div class="card-title">سريع</div>
            <div class="card-desc">إدخال واحد، فيميو كامل</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-card" style="margin-top: 0px;">
            <div style="font-size: 20px;">💬</div>
            <div class="card-title">خطوة بخطوة</div>
            <div class="card-desc">راجع كل خطوة بدقة</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# قسم إلهام بلوت كرافت
st.markdown(
    """
    <div class="section-header">
        <span class="section-title">إلهام بلوت كرافت</span>
        <span class="section-more">عرض الكل ></span>
    </div>
    """,
    unsafe_allow_html=True,
)

# عرض عينات من الأفلام/القصص الملهمة
m_col1, m_col2 = st.columns(2)

with m_col1:
    st.markdown(
        """
        <div class="movie-card">
            <div style="background: #334155; height: 160px; display: flex; align-items: center; justify-content: center; color: #64748b; font-size: 12px;">The Wrong Door</div>
            <div class="movie-title">THE WRONG DOOR</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m_col2:
    st.markdown(
        """
        <div class="movie-card">
            <div style="background: #334155; height: 160px; display: flex; align-items: center; justify-content: center; color: #64748b; font-size: 12px;">Secret Billionaire</div>
            <div class="movie-title">THE DELIVERYMAN'S SECRET</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# مسافة فاصلة قبل شريط التنقل السفلي
st.markdown("<br><br>", unsafe_allow_html=True)

# شريط التنقل السفلي (Bottom Navigation Bar)
st.markdown(
    """
    <div style="
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #0f172a;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding: 10px 20px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        direction: rtl;
        z-index: 999;
    ">
        <div style="text-align: center; color: #94a3b8; font-size: 12px;">🎥 مكتبتي</div>
        <div style="text-align: center; color: #94a3b8; font-size: 12px;">💼 الأعمال</div>
        <div style="text-align: center; color: #94a3b8; font-size: 12px;">🛠️ الأدوات</div>
        <div style="text-align: center; color: #ffffff; font-size: 12px; font-weight: bold;">🏠 الصفحة الرئيسية</div>
    </div>
    """,
    unsafe_allow_html=True,
)
