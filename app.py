import os
import streamlit as st
import fal_client

# إعداد الصفحة وتوسيعها
st.set_page_config(
    page_title="PlotCraft - سينما الذكاء الاصطناعي",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم CSS الخارق لفرض الشكل السينمائي والترتيب الصحيح بدقة مطابقة للصورة
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* الهيدر العلوي: الاسم يمين وترقية Pro يسار */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 5px 15px 5px;
        width: 100%;
    }
    
    .brand-name {
        font-size: 1.5rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 0.5px;
    }
    
    .pro-badge-btn {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #ffffff;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        cursor: pointer;
        backdrop-filter: blur(10px);
        text-decoration: none;
    }
    
    /* البانر السينمائي الخلفي */
    .hero-banner {
        position: relative;
        width: 100%;
        height: 320px;
        background: linear-gradient(180deg, rgba(11,15,25,0.1) 0%, rgba(11,15,25,0.85) 80%, #0b0f19 100%), 
                    url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1000&auto=format&fit=crop') center/cover;
        border-radius: 20px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        margin-bottom: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    
    .hero-text {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.4;
        text-align: right;
    }
    
    /* حاوية البطاقات المتجاورة أفقياً */
    .cards-row {
        display: flex;
        gap: 12px;
        width: 100%;
        margin-bottom: 20px;
    }
    
    /* تصميم البطاقة المربعة الاحترافية */
    .feature-card {
        flex: 1;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 16px;
        padding: 16px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 110px;
        backdrop-filter: blur(10px);
        cursor: pointer;
        transition: all 0.2s ease;
        text-align: right;
    }
    
    .feature-card:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.25);
    }
    
    .card-title-lg {
        font-size: 1rem;
        font-weight: 700;
        color: #ffffff;
    }
    
    .card-subtitle-sm {
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.6);
        margin-top: 4px;
    }
    
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #e5e7eb;
        margin: 15px 0 10px 0;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# ----------------------------------------------------
# الهيدر العلوي: PlotCraft يمين، و ترقية Pro يسار
# ----------------------------------------------------
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown('<div class="brand-name">PlotCraft</div>', unsafe_allow_html=True)
with col2:
    # استخدام حاوية لضبط محاذاة زر الترقية لليسار تماماً
    st.markdown('<div style="text-align: left;">', unsafe_allow_html=True)
    if st.button("ترقية Pro", key="btn_pro_header"):
        st.session_state.page = 'pro'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 1. الصفحة الرئيسية (Home)
# ----------------------------------------------------
if st.session_state.page == 'home':
    # غلاف البانر السينمائي
    st.markdown("""
        <div class="hero-banner">
            <div class="hero-text">مساء الخير أيها المخرج،<br>أي قصة سنصنع اليوم؟</div>
        </div>
    """, unsafe_allow_html=True)

    # البطاقات المربعة المتجاورة تماماً (يمين: خطوة بخطوة، يسار: سريع)
    # نقوم بعمل زرين شفّافين فوق عناصر الـ HTML لضمان عمل التفاعل البرمجي بدقة
    col_r, col_l = st.columns(2)
    
    with col_r:
        st.markdown("""
            <div class="feature-card">
                <div class="card-title-lg">خطوة بخطوة</div>
                <div class="card-subtitle-sm">راجع كل خطوة</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("اختيار خطوة بخطوة", key="btn_step_action", use_container_width=True):
            st.session_state.page = 'generator'
            st.rerun()
            
    with col_l:
        st.markdown("""
            <div class="feature-card">
                <div class="card-title-lg">سريع</div>
                <div class="card-subtitle-sm">إدخال واحد، فيديو كامل</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("اختيار سريع", key="btn_quick_action", use_container_width=True):
            st.session_state.page = 'generator'
            st.rerun()

    st.markdown('<div class="section-title">إلهام الدراما</div>', unsafe_allow_html=True)
    
    # بوسترات الأفلام الاستعراضية
    poster1, poster2 = st.columns(2)
    with poster1:
        st.image("https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=500&auto=format&fit=crop", caption="THE WRONG DOOR", use_container_width=True)
    with poster2:
        st.image("https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=500&auto=format&fit=crop", caption="SECRET BILLIONAIRE", use_container_width=True)

# ----------------------------------------------------
# 2. صفحة إنشاء الفيديو (Generator)
# ----------------------------------------------------
elif st.session_state.page == 'generator':
    st.markdown("### مولد الفيديوهات السينمائية")
    
    api_key_input = st.text_input("مفتاح fal.ai API Key", value="", type="password")
    if api_key_input:
        os.environ["FAL_KEY"] = api_key_input

    prompt = st.text_area("أدخل وصف المشهد السينمائي:", placeholder="Cinematic cyber city...")
    
    opt1, opt2 = st.columns(2)
    with opt1:
        resolution = st.selectbox("الدقة", ["720p", "1080p", "4K"])
    with opt2:
        duration = st.selectbox("المدة", ["5 ثواني", "10 ثواني"])

    if st.button("بدء الإنتاج السينمائي", use_container_width=True):
        if not prompt:
            st.warning("يرجى كتابة وصف المشهد أولاً.")
        else:
            with st.spinner("جاري معالجة المشهد السينمائي..."):
                try:
                    handler = fal_client.submit("fal-ai/minimax-video", arguments={"prompt": prompt})
                    result = handler.get()
                    if result and "video" in result:
                        st.video(result["video"]["url"])
                    else:
                        st.json(result)
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")

# ----------------------------------------------------
# 3. صفحة الأدوات (Tools Menu)
# ----------------------------------------------------
elif st.session_state.page == 'tools':
    st.markdown("### أدوات الإنتاج المتقدمة")
    tool_choice = st.radio("اختر الأداة المطلوبة:", ["توليد تأثيرات الفيديو", "توليد فيديو بالكامل", "توليد الصور السينمائية"])
    if st.button("تنفيذ الأداة", use_container_width=True):
        st.success(f"تم اختيار: {tool_choice}")

# ----------------------------------------------------
# 4. صفحة الأعمال والمشاريع (My Projects)
# ----------------------------------------------------
elif st.session_state.page == 'projects':
    st.markdown("### مشاريعك المحفوظة")
    st.info("لا توجد مشاريع سابقة حالياً.")

# ----------------------------------------------------
# 5. صفحة الاشتراكات (Pro Subscription Plans) بدون إيموجيات
# ----------------------------------------------------
elif st.session_state.page == 'pro':
    st.markdown("### خطط الاشتراكات الاحترافية")
    st.markdown("اختر الخطة المناسبة لإطلاق إبداعاتك بلا حدود:")
    
    st.markdown("---")
    st.subheader("الخطة الاسبوعية")
    st.write("صلاحية كاملة لمدة سبعة أيام مع معالجة سولو.")
    st.button("اشتراك اسبوعي", key="sub_w", use_container_width=True)
    
    st.markdown("---")
    st.subheader("الخطة الشهرية")
    st.write("الوصول الشامل لكل ميزات الـ Pro لمدة شهر كامل.")
    st.button("اشتراك شهري", key="sub_m", use_container_width=True)
    
    st.markdown("---")
    st.subheader("الخطة السنوية")
    st.write("أفضل قيمة توفيرية للمحترفين طوال العام.")
    st.button("اشتراك سنوي", key="sub_y", use_container_width=True)

# ----------------------------------------------------
# شريط التنقل السفلي الثابت (Bottom Navigation Bar)
# ----------------------------------------------------
st.markdown("<br><br><br>", unsafe_allow_html=True)

nav1, nav2, nav3 = st.columns(3)
with nav1:
    if st.button("الرئيسية", use_container_width=True, key="nav_home"):
        st.session_state.page = 'home'
        st.rerun()
with nav2:
    if st.button("الأدوات", use_container_width=True, key="nav_tools"):
        st.session_state.page = 'tools'
        st.rerun()
with nav3:
    if st.button("الأعمال", use_container_width=True, key="nav_projects"):
        st.session_state.page = 'projects'
        st.rerun()
