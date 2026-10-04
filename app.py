import os
import streamlit as st
import fal_client

# إعداد الصفحة
st.set_page_config(
    page_title="PlotCraft - سينما الذكاء الاصطناعي",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم والواجهة السينمائية عبر CSS
st.markdown("""
    <style>
    /* إخفاء القائمة العلوية الافتراضية لـ Streamlit والهيدر */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* غلاف البانر السينمائي */
    .hero-container {
        position: relative;
        width: 100%;
        height: 320px;
        background: linear-gradient(180deg, rgba(11,15,25,0.2) 0%, rgba(11,15,25,0.95) 85%, #0b0f19 100%), 
                    url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1000&auto=format&fit=crop') center/cover;
        border-radius: 20px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }
    
    .hero-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 8px;
        line-height: 1.4;
    }
    
    /* زر الترقية العلوي */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }
    .brand-logo {
        font-size: 1.3rem;
        font-weight: 800;
        letter-spacing: 1px;
        color: #ffffff;
    }
    
    /* البطاقات التفاعلية */
    .custom-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 18px;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        margin-bottom: 10px;
    }
    .custom-card:hover {
        background: rgba(255, 255, 255, 0.09);
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    /* تنسيق الأزرار السفلية الوهمية لتنقل شبيه بالتطبيقات */
    .nav-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(15, 22, 36, 0.95);
        backdrop-filter: blur(15px);
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        padding: 12px 20px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 999;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التنقل بين الصفحات داخل التطبيق
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# شريط التنقل العلوي الثابت
col_logo, col_pro = st.columns([3, 1])
with col_logo:
    st.markdown('<div class="brand-logo">PlotCraft</div>', unsafe_allow_html=True)
with col_pro:
    if st.button("ترقية Pro", key="btn_pro_top"):
        st.session_state.page = 'pro'
        st.rerun()

st.markdown("<hr style='border:0.5px solid rgba(255,255,255,0.08); margin: 5px 0 15px 0;'>", unsafe_allow_html=True)

# ----------------------------------------------------
# 1. الصفحة الرئيسية (Home)
# ----------------------------------------------------
if st.session_state.page == 'home':
    # غلاف البانر السينمائي مع تأثير الخلفية والترحيب
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">مساء الخير أيها المخرج،<br>أي قصة سنصنع اليوم؟</div>
        </div>
    """, unsafe_allow_html=True)

    # أزرار سريعة رئيسية تفاعلية
    col_card1, col_card2 = st.columns(2)
    with col_card1:
        if st.button("سريع\nإدخال واحد، فيديو كامل", key="quick_gen", use_container_width=True):
            st.session_state.page = 'generator'
            st.rerun()
    with col_card2:
        if st.button("خطوة بخطوة\nراجع كل خطوة", key="step_gen", use_container_width=True):
            st.session_state.page = 'generator'
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### إلهام الدراما")
    
    # قسم بوسترات الأفلام الاستعراضية المصغرة
    col_img1, col_img2 = st.columns(2)
    with col_img1:
        st.image("https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=500&auto=format&fit=crop", caption="THE WRONG DOOR", use_container_width=True)
    with col_img2:
        st.image("https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=500&auto=format&fit=crop", caption="SECRET BILLIONAIRE", use_container_width=True)

# ----------------------------------------------------
# 2. صفحة إنشاء الفيديو (Generator)
# ----------------------------------------------------
elif st.session_state.page == 'generator':
    st.markdown("### مولد الفيديوهات السينمائية")
    
    api_key_input = st.text_input("مفتاح fal.ai API Key", value="", type="password")
    if api_key_input:
        os.environ["FAL_KEY"] = api_key_input

    prompt = st.text_area("أدخل وصف المشهد السينمائي بالتفصيل:", placeholder="Cinematic cyber city...")
    
    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        resolution = st.selectbox("الدقة", ["720p", "1080p", "4K"])
    with col_opt2:
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
    if st.button("الانتقال للأداة", use_container_width=True):
        st.success(f"تم اختيار: {tool_choice}")

# ----------------------------------------------------
# 4. صفحة الأعمال والمشاريع (My Projects)
# ----------------------------------------------------
elif st.session_state.page == 'projects':
    st.markdown("### مشاريعك المحفوظة")
    st.info("لا توجد مشاريع سابقة حالياً. ابدأ بإنشاء أول فيديو لك الآن!")

# ----------------------------------------------------
# 5. صفحة الاشتراكات (Pro Subscription Plans)
# ----------------------------------------------------
elif st.session_state.page == 'pro':
    st.markdown("### خطط الاشتراكات الاحترافية")
    st.markdown("اختر الخطة المناسبة لإطلاق إبداعاتك بلا حدود:")
    
    st.markdown("---")
    st.subheader("الخطة الاسبوعية")
    st.write("صلاحية كاملة لمدة سبعة أيام مع معالجة سولو.")
    st.button("اشتراك اسبوعي", key="sub_weekly", use_container_width=True)
    
    v = st.markdown("---")
    st.subheader("الخطة الشهرية")
    st.write("الوصول الشامل لكل ميزات الـ Pro لمدة شهر كامل.")
    st.button("اشتراك شهري", key="sub_monthly", use_container_width=True)
    
    st.markdown("---")
    st.subheader("الخطة السنوية")
    st.write("أفضل قيمة توفيرية للمحترفين طوال العام.")
    st.button("اشتراك سنوي", key="sub_yearly", use_container_width=True)

# ----------------------------------------------------
# شريط التنقل السفلي الثابت (Bottom Navigation)
# ----------------------------------------------------
st.markdown("<br><br><br>", unsafe_allow_html=True)

cols_nav = st.columns(3)
with cols_nav[0]:
    if st.button("الرئيسية", use_container_width=True, key="nav_home"):
        st.session_state.page = 'home'
        st.rerun()
with cols_nav[1]:
    if st.button("الأدوات", use_container_width=True, key="nav_tools"):
        st.session_state.page = 'tools'
        st.rerun()
with cols_nav[2]:
    if st.button("الأعمال", use_container_width=True, key="nav_projects"):
        st.session_state.page = 'projects'
        st.rerun()
