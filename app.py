import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="استوديو الذكاء الاصطناعي الذكي",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم والأنماط العامة (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
    
    * {
        font-family: 'Tajawal', sans-serif;
    }
    
    .main {
        background-color: #0e1117;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: 700;
        height: 48px;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.6);
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

# الشريط الجانبي للتنقل
with st.sidebar:
    st.markdown("### ⚡ لوحة التحكم")
    selected_tab = st.radio(
        "اختر القسم:",
        ["🎨 توليد الصور السحري", "🎬 صانع الفيديوهات", "📊 لوحة تحليلات المحتوى", "⚙️ الإعدادات المتقدمة"]
    )
    
    st.markdown("---")
    st.markdown("### 💎 حالة الاشتراك")
    st.info("الحساب: **محترف (Pro)**\nالرصيد المتبقي: **850 نقطة**")

# المحتوى الرئيسي حسب الاختيار
if selected_tab == "🎨 توليد الصور السحري":
    st.title("🎨 استوديو توليد الصور بالذكاء الاصطناعي")
    st.markdown("أنشئ صوراً مذهلة وعالية الدقة باستخدام أحدث نماذج الذكاء الاصطناعي.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        prompt = st.text_area("أدخل الوصف (Prompt) بالتفصيل:", placeholder="مثال: لوحة فنية سينمائية لمدينة المستقبل في الليل بإضاءة نيون...")
        aspect_ratio = st.selectbox("أبعاد الصورة:", ["1:1 (مربع)", "16:9 (عريض)", "9:16 (قصص/تيك توك)"])
        style = st.selectbox("النمط الفني:", ["سينمائي (Cinematic)", "واقعي (Photorealistic)", "أنمي (Anime)", "رقمي ثلاثي الأبعاد (3D Digital)"])
        
        if st.button("🚀 ابدأ التوليد الآن"):
            if prompt:
                with st.spinner("جاري معالجة الطلب وصنع الصورة السحرية..."):
                    st.success("تم توليد الصورة بنجاح!")
                    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1000&q=80", caption=prompt)
            else:
                st.warning("يرجى كتابة الوصف أولاً!")

    with col2:
        st.markdown("#### 💡 نصائح لاحتراف الوصف:")
        st.markdown("""
        - كن دقيقاً في تفاصيل الإضاءة (مثل: *Golden hour*, *Neon lights*).
        - حدد زاوية الكاميرا (مثل: *Close-up*, *Wide angle*).
        - اذكر الجودة المطلوبة (مثل: *4K*, *Hyper-detailed*).
        """)

elif selected_tab == "🎬 صانع الفيديوهات":
    st.title("🎬 صانع الفيديوهات الذكي")
    st.markdown("حول نصوصك إلى مقاطع فيديو سينمائية متحركة بدقة مذهلة.")
    
    script_text = st.text_area("النصوص أو السيناريو:", placeholder="اكتب قصة الفيديو هنا...")
    voice_type = st.selectbox("اختر الصوت المعلق (Voiceover):", ["صوت رجعي عميق (سينمائي)", "صوت هادئ ورسمي", "صوت شبابي حيوي"])
    
    if st.button("🎥 إنشاء الفيديو"):
        with st.spinner("جاري دمج الصوت مع المشاهد المرئية..."):
            st.success("تم تجهيز فيديو العرض المبدئي بنجاح!")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")

elif selected_tab == "📊 لوحة تحليلات المحتوى":
    st.title("📊 لوحة الأداء والمشاهدات")
    st.markdown("تابع إحصائيات تفاعل الجمهور وأرباح المنصات الخاصة بك.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h3>إجمالي المشاهدات</h3><h2>2.5M</h2><p style="color: #10b981;">+14% هذا الأسبوع</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>الأرباح المتوقعة</h3><h2>$1,420</h2><p style="color: #10b981;">+8% عن الشهر السابق</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>المشاريع المنجزة</h3><h2>148</h2><p style="color: #3b82f6;">جاهزة للنشر</p></div>', unsafe_allow_html=True)
        
    st.markdown("---")
    st.subheader("معدل التفاعل خلال الـ 7 أيام الماضية")
    chart_data = [20, 45, 30, 60, 75, 90, 110]
    st.line_chart(chart_data)

else:
    st.title("⚙️ إعدادات النظام")
    st.markdown("إدارة تفضيلات الحساب وربط المفاتيح البرمجية (API Keys).")
    st.text_input("اسم المستخدم:", value="غسان رضا")
    st.text_input("البريد الإلكتروني:", value="ghassan@example.com")
    st.selectbox("لغة الواجهة:", ["العربية (Arabic)", "English"])
    st.button("💾 حفظ التغييرات")
