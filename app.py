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

# تخصيص التصميم والواجهة السينمائية المطابقة للصورة تماماً عبر CSS
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
    
    /* شريط العنوان العلوي: الاسم يمين وترقية يسار */
    .top-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0 15px 0;
    }
    
    .brand-title {
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        color: #ffffff;
        text-align: right;
    }
    
    /* غلاف البانر السينمائي */
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
    
    /* تنسيق قسم إلهام الدراما */
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #e5e7eb;
        margin: 20px 0 10px 0;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التنقل بين الصفحات داخل التطبيق
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# ----------------------------------------------------
# الهيدر العلوي: PlotCraft في اليمين و ترقية Pro في اليسار
# ----------------------------------------------------
col_logo, col_pro = st.columns([1, 1])
with col_logo:
    st.markdown('<div class="brand-title">PlotCraft</div>', unsafe_allow_html=True)
with col_pro:
    col_btn_align = st.columns([1, 1])
    with col_btn_align[1]:
        if st.button("ترقية Pro", key="btn_pro_top", use_container_width=True):
            st.session_state.page = 'pro'
            st.rerun()

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

    # البطاقات المربعة المتجاورة تماماً كالصورة (يمين: خطوة بخطوة، يسار: سريع)
    c_right, c_left = st.columns(2)
    
    with c_right:
        if st.button("خطوة بخطوة\nراجع كل خطوة", key="step_card", use_container_width=True):
            st.session_state.page = 'generator'
            st.rerun()
            
    with c_left:
        if st.button("سريع\nإدخال واحد، فيديو كامل", key="quick_card", use_container_width=True):
            st.session_state.page = 'generator'
            st.rerun()

    st.markdown('<div class="section-title">إلهام الدراما</div>', unsafe_allow_html=True)
    
    # بوسترات الأفلام الاستعراضية
    p1, p2 = st.columns(2)
    with p1:
        st.image("https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=500&auto=format&fit=crop", caption="THE WRONG DOOR", use_container_width=True)
    with p2:
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
    
    op1, op2 = st.columns(2)
    with op1:
        resolution = st.selectbox("الدقة", ["720p", "1080p", "4K"])
    with op2:
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
