import os
import streamlit as st
import fal_client

# إعداد الصفحة لتكون كاملة العرض وبدون هيدر ستريمليت
st.set_page_config(
    page_title="PlotCraft - سينما الذكاء الاصطناعي",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تطبيق تصميم CSS مخصص لفرض الشكل السينمائي والترتيب الدقيق
st.markdown("""
    <style>
    /* إخفاء عناصر ستريمليت الافتراضية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* تخصيص الحاوية الرئيسية لتقليل الهوامش */
    .main-container {
        max-width: 1000px;
        margin: 0 auto;
        padding-top: 10px;
    }
    
    /* الهيدر العلوي: الاسم يمين، زر الترقية يسار */
    .header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
        padding: 0 10px;
    }
    
    .brand-title {
        font-size: 1.6rem;
        font-weight: 800;
        color: #ffffff;
        text-align: right;
    }
    
    .pro-btn-container {
        text-align: left;
    }
    
    /* زر ترقية Pro */
    .pro-btn {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #ffffff;
        padding: 8px 20px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.2s ease;
        cursor: pointer;
    }
    .pro-btn:hover {
        background: rgba(255, 255, 255, 0.15);
        border-color: rgba(255, 255, 255, 0.3);
    }
    
    /* صف البطاقتين المتجاورتين أفقياً */
    .cards-row {
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
        width: 100%;
        padding: 0 10px;
    }
    
    /* تصميم البطاقة المشابهة للصورة (يمين: خطوة بخطوة، يسار: سريع) */
    .feature-card {
        flex: 1;
        background: linear-gradient(180deg, rgba(11,15,25,0.1) 0%, rgba(11,15,25,0.85) 70%, #0b0f19 100%), 
                    url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1000&auto=format&fit=crop') center/cover;
        border-radius: 20px;
        padding: 20px;
        height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end; /* النصوص في الأسفل */
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        cursor: pointer;
        transition: transform 0.2s ease;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .card-title-lg {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 5px;
        text-align: right;
    }
    
    .card-subtitle-sm {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.7);
        text-align: right;
        line-height: 1.4;
    }
    
    /* قسم إلهام الدراما */
    .section-container {
        padding: 0 10px;
    }
    
    .section-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #e5e7eb;
        margin: 25px 0 15px 0;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# ----------------------------------------------------
# بناء واجهة المستخدم باستخدام HTML المخصص لضمان الترتيب
# ----------------------------------------------------

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# 1. الهيدر العلوي (الاسم يمين / زر الترقية يسار)
st.markdown(f"""
    <div class="header-row">
        <div class="pro-btn-container">
            <button class="pro-btn" onclick="document.getElementById('link_to_pro').click()">ترقية Pro</button>
        </div>
        <div class="brand-title">PlotCraft</div>
    </div>
""", unsafe_allow_html=True)

# خدعة لعمل الزر يعمل
if st.button("...", key="link_to_pro", help="Click to go to Pro page"):
    st.session_state.page = 'pro'
    st.rerun()

# ----------------------------------------------------
# 2. الصفحة الرئيسية (Home) - ظهور البطاقتين المتجاورتين تماماً كالصورة
# ----------------------------------------------------
if st.session_state.page == 'home':
    # صف البطاقات الرئيسية المربعة
    st.markdown('<div class="cards-row">', unsafe_allow_html=True)
    
    # البطاقة اليمنى: خطوة بخطوة
    col_right, col_left = st.columns(2)

    with col_right:
        st.markdown("""
            <div class="feature-card" onclick="document.getElementById('btn_step_action').click()">
                <div class="card-title-lg">خطوة بخطوة</div>
                <div class="card-subtitle-sm">مساء الخير أيها المخرج، أي قصة سنصنع اليوم؟<br>راجع كل خطوة</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("بدء خطوة بخطوة", key="btn_step_action", use_container_width=True):
            st.session_state.page = 'generator'
            st.rerun()

    # البطاقة اليسرى: سريع
    with col_left:
        st.markdown("""
            <div class="feature-card" onclick="document.getElementById('btn_quick_action').click()">
                <div class="card-title-lg">سريع</div>
                <div class="card-subtitle-sm">إدخال واحد، فيديو كامل</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("بدء سريع", key="btn_quick_action", use_container_width=True):
            st.session_state.page = 'generator'
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True) # نهاية cards-row

    # قسم إلهام الدراما
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">إلهام الدراما</div>', unsafe_allow_html=True)
    
    # بوسترات الأفلام (صورة 500x500 من Unsplash)
    p1, p2 = st.columns(2)
    with p1:
        st.image("https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=500&auto=format&fit=crop", caption="THE WRONG DOOR", use_container_width=True)
    with p2:
        st.image("https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=500&auto=format&fit=crop", caption="SECRET BILLIONAIRE", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True) # نهاية section-container

# ----------------------------------------------------
# 3. باقي الصفحات (Generator, Tools, Projects, Pro) - بدون تغيير جذري
# ----------------------------------------------------
elif st.session_state.page == 'generator':
    st.markdown("### مولد الفيديوهات السينمائية")
    # ... باقي الكود السابق لصفحة التوليد ...

# ... باقي المنطق للصفحات الأخرى ...

st.markdown('</div>', unsafe_allow_html=True) # نهاية main-container
