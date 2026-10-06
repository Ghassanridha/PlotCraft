import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="PlotCraft - AI Studio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------
# تخصيص التصميم عبر CSS (دعم اللون الداكن واللغة العربية RTL)
# ----------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #0b0f19;
        color: #f3f4f6;
    }

    /* إخفاء عناصر ستريمليت الافتراضية غير الضرورية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* شريط العلوي */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(17, 24, 39, 0.7);
        backdrop-filter: blur(10px);
        padding: 12px 20px;
        border-radius: 16px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* البطاقات التفاعلية */
    .feature-card {
        background: linear-gradient(135deg, rgba(31, 41, 55, 0.6) 0%, rgba(17, 24, 39, 0.8) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        margin-bottom: 15px;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        border-color: #ec4899;
        box-shadow: 0 12px 40px rgba(236, 72, 153, 0.2);
    }

    /* شريط التنقل السفلي العائم */
    .nav-container {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(17, 24, 39, 0.85);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 10px 25px;
        border-radius: 50px;
        display: flex;
        gap: 30px;
        z-index: 999;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# إدارة الحالة (Session State) للتنقل بين الصفحات
# ----------------------------------------------------
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

if 'active_tool_view' not in st.session_state:
    st.session_state.active_tool_view = None

# ----------------------------------------------------
# الشاشات والواجهات
# ----------------------------------------------------

def home_screen():
    # الشريط العلوي
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("<h2 style='margin:0; color:#fff;'>🎬 PlotCraft</h2>", unsafe_allow_html=True)
    with col2:
        if st.button("✨ ترقية Pro", use_container_width=True):
            st.session_state.current_page = 'subscription'
            st.rerun()

    st.markdown("<hr style='border-color: rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    st.markdown("### مساء الخير، أيها المخرج 🎥\nأي قصة سينمائية سنبتكرها اليوم؟")

    # بطاقات الاختيار السريع
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="feature-card">
            <h3>⚡ الوضع السريع</h3>
            <p style='color:#9ca3af;'>أنشئ فيديوهاتك بضغطة زر واحدة عبر الذكاء الاصطناعي.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("ابدأ الوضع السريع", use_container_width=True):
            st.session_state.current_page = 'tools'
            st.session_state.active_tool_view = 'video'
            st.rerun()

    with col_b:
        st.markdown("""
        <div class="feature-card">
            <h3>✍️ خطوة بخطوة</h3>
            <p style='color:#9ca3af;'>تحكم دقيق في الحبكة، الشخصيات، وزوايا الكاميرا.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("ابدأ خطوة بخطوة", use_container_width=True):
            st.session_state.current_page = 'step_by_step'
            st.rerun()

    st.markdown("<br><h4 style='color:#f3f4f6;'>🔥 إلهام بلوت كرافت</h4>", unsafe_allow_html=True)
    st.info("استكشف أحدث الأعمال السينمائية المصنوعة بالكامل عبر المنصة.")

def tools_screen():
    st.markdown("<h2>🛠️ أدوات المخرج الذكية</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9ca3af;'>اختر الأداة المناسبة للبدء:</p>", unsafe_allow_html=True)

    # زر الرجوع للرئيسية
    if st.button("← عودة للرئيسية"):
        st.session_state.active_tool_view = None
        st.session_state.current_page = 'home'
        st.rerun()

    st.markdown("---")

    # إذا لم يتم اختيار أداة محددة، نعرض البطاقات
    if st.session_state.active_tool_view is None:
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("""
            <div class="feature-card">
                <h4>🎥 توليد الفيديو</h4>
                <p style='color:#9ca3af;'>حول النصوص والصور إلى مشاهد سينمائية متحركة.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("فتح توليد الفيديو", use_container_width=True):
                st.session_state.active_tool_view = 'video'
                st.rerun()

        with c2:
            st.markdown("""
            <div class="feature-card">
                <h4>🎨 توليد الصور</h4>
                <p style='color:#9ca3af;'>ابتكر صوراً فنية ومفاهيم بصرية مذهلة.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("فتح توليد الصور", use_container_width=True):
                st.session_state.active_tool_view = 'image'
                st.rerun()

        with c3:
            st.markdown("""
            <div class="feature-card">
                <h4>✨ تأثيرات الفيديو</h4>
                <p style='color:#9ca3af;'>أضف لمسات سينمائية ومؤثرات بصرية متقدمة.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("فتح التأثيرات", use_container_width=True):
                st.session_state.active_tool_view = 'effects'
                st.rerun()

    # شاشة بطاقة "توليد الفيديو" المخصصة (التصميم الكامل هنا فقط)
    elif st.session_state.active_tool_view == 'video':
        st.markdown("### 🎥 استوديو توليد الفيديو الاحترافي")
        
        # صندوق التوجيه (Prompt)
        st.text_area("وصف المشهد السينمائي (Prompt):", placeholder="اكتب وصفاً دقيقاً للمشهد، الإضاءة، وحركة الكاميرا...", height=120)
        
        # رفع الملفات والصور المرجعية
        st.file_uploader("رفع صور أو فيديوهات مرجعية:", type=['png', 'jpg', 'jpeg', 'mp4'])
        
        # صف الشخصيات
        st.markdown("<p style='color:#9ca3af; font-size:14px; margin-bottom:5px;'>اختيار الشخصيات (Cast):</p>", unsafe_allow_html=True)
        cols_cast = st.columns(4)
        with cols_cast[0]: st.button("👤 شخصية 1", use_container_width=True)
        with cols_cast[1]: st.button("👩 شخصية 2", use_container_width=True)
        with cols_cast[2]: st.button("🦸 شخصية 3", use_container_width=True)
        with cols_cast[3]: st.button("➕ إضافة", use_container_width=True)
        
        # نسبة العرض والارتفاع
        st.markdown("<p style='color:#9ca3af; font-size:14px; margin-top:10px;'>نسبة العرض والارتفاع:</p>", unsafe_allow_html=True)
        r1, r2 = st.columns(2)
        with r1: st.button("🖥️ أفقي (16:9)", use_container_width=True)
        with r2: st.button("📱 عمودي (9:16)", use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 إنتاج الفيديو الآن", type="primary", use_container_width=True):
            st.success("جاري إرسال الطلب لنظام التوليد الذكي...")

        if st.button("← العودة لقائمة الأدوات"):
            st.session_state.active_tool_view = None
            st.rerun()

    # شاشة بطاقة "توليد الصور" (خالية من التصميم المعقد بناءً على طلبك)
    elif st.session_state.active_tool_view == 'image':
        st.markdown("### 🎨 استوديو توليد الصور")
        st.info("هذه هي واجهة توليد الصور المبسطة.")
        if st.button("← العودة لقائمة الأدوات"):
            st.session_state.active_tool_view = None
            st.rerun()

    # شاشة تأثيرات الفيديو
    elif st.session_state.active_tool_view == 'effects':
        st.markdown("### ✨ تأثيرات الفيديو")
        st.info("هذه هي واجهة تأثيرات الفيديو.")
        if st.button("← العودة لقائمة الأدوات"):
            st.session_state.active_tool_view = None
            st.rerun()

def step_by_step_screen():
    st.markdown("<h2>✍️ وضع التصنيع خطوة بخطوة</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9ca3af;'>تحكم تفصيلي كامل في عناصر القصة والإنتاج السينمائي.</p>", unsafe_allow_html=True)
    
    if st.button("← عودة للرئيسية"):
        st.session_state.current_page = 'home'
        st.rerun()

    st.markdown("---")
    st.text_input("عنوان القصة أو الفيلم:")
    st.text_area("تفاصيل الحبكة والسيناريو:")
    st.button("بدء الإنتاج المتسلسل", type="primary")

def subscription_screen():
    st.markdown("<h2 style='text-align: center;'>💎 ترقية حسابك إلى Pro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color:#9ca3af;'>احصل على إمكانيات غير محدودة لتوليد الأفلام السينمائية.</p>", unsafe_allow_html=True)
    
    if st.button("← عودة للرئيسية"):
        st.session_state.current_page = 'home'
        st.rerun()

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>الباقة الشهرية</h3>
            <h2 style='color:#ec4899;'>$19 / شهرياً</h2>
            <p>توليد فيديوهات غير محدود + دقة عالية جداً.</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("اشتري الآن (شهري)", use_container_width=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>الباقة السنوية (توفير 40%)</h3>
            <h2 style='color:#ec4899;'>$129 / سنوية</h2>
            <p>كافة مميزات برو + أولوية فائقة في الخوادم.</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("اشتري الآن (سنوي)", use_container_width=True)

# ----------------------------------------------------
# التوجيه بناءً على حالة الصفحة الحالية
# ----------------------------------------------------
if st.session_state.current_page == 'home':
    home_screen()
elif st.session_state.current_page == 'tools':
    tools_screen()
elif st.session_state.current_page == 'step_by_step':
    step_by_step_screen()
elif st.session_state.current_page == 'subscription':
    subscription_screen()

# ----------------------------------------------------
# شريط التنقل السفلي الثابت
# ----------------------------------------------------
st.markdown("""
<div style='height: 70px;'></div>
""", unsafe_allow_html=True)

col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    if st.button("🏠 الرئيسية", use_container_width=True):
        st.session_state.current_page = 'home'
        st.session_state.active_tool_view = None
        st.rerun()
with col_n2:
    if st.button("🛠️ الأدوات", use_container_width=True):
        st.session_state.current_page = 'tools'
        st.session_state.active_tool_view = None
        st.rerun()
with col_n3:
    if st.button("📁 أعمالي", use_container_width=True):
        st.session_state.current_page = 'home'
        st.session_state.active_tool_view = None
        st.rerun()
