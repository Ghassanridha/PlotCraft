import streamlit as st

# إعداد الصفحة وتكوينها
st.set_page_config(
    page_title="PlotCraft - بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم والواجهة باستخدام CSS المظلم الأنيق
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 2rem; padding-left: 1rem; padding-right: 1rem; background-color: #0e0e16;}

    /* شريط التنقل العلوي بالأزرار الأربعة */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #161622;
        padding: 12px 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }
    .nav-brand {
        color: #ffffff;
        font-size: 20px;
        font-weight: bold;
    }

    /* عناوين الأقسام داخل تأثيرات الفيديو */
    .section-title {
        color: #ffffff;
        font-size: 18px;
        font-weight: bold;
    }
    
    /* حاوية التمرير العمودي المستمر (عند الضغط على عرض الكل) */
    .scrollable-grid {
        display: flex;
        flex-direction: column;
        gap: 12px;
        max-height: 600px;
        overflow-y: auto;
        padding-right: 5px;
    }
    .effect-item-card {
        background: #1a1a29;
        border-radius: 12px;
        padding: 10px;
        display: flex;
        align-items: center;
        gap: 15px;
        border: 1px solid #2a2a40;
    }
    .effect-item-img {
        width: 80px;
        height: 80px;
        border-radius: 8px;
        object-fit: cover;
    }
    .effect-item-text h4 {
        color: #ffffff;
        margin: 0 0 4px 0;
        font-size: 15px;
    }
    .effect-item-text p {
        color: #9090a8;
        margin: 0;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# إدارة حالة التنقل
if 'current_nav' not in st.session_state:
    st.session_state.current_nav = "الرئيسية"

if 'tool_section' not in st.session_state:
    st.session_state.tool_section = None

# شريط التنقل العلوي بالأزرار الأربعة الأساسية
st.markdown('<div class="nav-container"><div class="nav-brand">PlotCraft 🎬 بلوت كرافت</div></div>', unsafe_allow_html=True)

col_n1, col_n2, col_n3, col_n4 = st.columns(4)

with col_n1:
    if st.button("🏠 الرئيسية", use_container_width=True):
        st.session_state.current_nav = "الرئيسية"
        st.session_state.tool_section = None
        st.rerun()

with col_n2:
    if st.button("🛠️ الأدوات", use_container_width=True):
        st.session_state.current_nav = "الأدوات"
        st.session_state.tool_section = "قائمة_الأدوات_الرئيسية"
        st.rerun()

with col_n3:
    if st.button("💼 الأعمال", use_container_width=True):
        st.session_state.current_nav = "الأعمال"
        st.session_state.tool_section = None
        st.rerun()

with col_n4:
    if st.button("👤 الملف الشخصي", use_container_width=True):
        st.session_state.current_nav = "الحساب"
        st.session_state.tool_section = None
        st.rerun()

st.markdown("---")

# منطق الشاشات والأقسام
if st.session_state.current_nav == "الرئيسية":
    st.markdown("### الصفحة الرئيسية للمنصة")
    st.write("مرحباً بك! انقر على زر (الأدوات) في الأعلى للوصول إلى أقسام التأثيرات والتوليد.")

elif st.session_state.current_nav == "الأعمال":
    st.markdown("### قسم الأعمال")
    st.write("جميع مشاريعك وأعمالك المحفوظة ستظهر هنا.")

elif st.session_state.current_nav == "الحساب":
    st.markdown("### إعدادات الحساب")
    st.write("إدارة الحساب والإعدادات الشخصية.")

elif st.session_state.current_nav == "الأدوات":
    
    # 1. قائمة الأدوات الرئيسية (عند الضغط على زر الأدوات)
    if st.session_state.tool_section == "قائمة_الأدوات_الرئيسية":
        st.markdown("## 🛠️ لوحة الأدوات")
        st.write("اختر القسم المطلوب:")
        
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            if st.button("🎞️ تأثيرات الفيديو", use_container_width=True):
                st.session_state.tool_section = "واجهة_تأثيرات_الفيديو"
                st.rerun()
        with col_t2:
            if st.button("🎬 توليد الفيديو", use_container_width=True):
                st.session_state.tool_section = "توليد_الفيديو"
                st.rerun()
        with col_t3:
            if st.button("🖼️ توليد الصور", use_container_width=True):
                st.session_state.tool_section = "توليد_الصور"
                st.rerun()

    # 2. واجهة تأثيرات الفيديو الرئيسية (مطابقة للصورة تماماً مع قسمين منفصلين)
    elif st.session_state.tool_section == "واجهة_تأثيرات_الفيديو":
        if st.button("⬅️ رجوع إلى الأدوات"):
            st.session_state.tool_section = "قائمة_الأدوات_الرئيسية"
            st.rerun()
            
        st.markdown("<h2>تأثيرات الفيديو</h2>", unsafe_allow_html=True)
        
        # --- قسم Cool Me ---
        col_h1, col_h2 = st.columns([4, 1])
        with col_h1:
            st.markdown('<p class="section-title">Cool Me</p>', unsafe_allow_html=True)
        with col_h2:
            if st.button("عرض الكل >", key="btn_all_coolme"):
                st.session_state.tool_section = "قائمة_عمودية_coolme"
                st.rerun()
                
        # صور قسم Cool Me (أفقي)
        img_col1, img_col2, img_col3 = st.columns(3)
        with img_col1:
            st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300&h=350&fit=crop", caption="Pizza Feast", use_container_width=True)
        with img_col2:
            st.image("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=350&fit=crop", caption="Beer Bliss", use_container_width=True)
        with img_col3:
            st.image("https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=300&h=350&fit=crop", caption="Burger Bite", use_container_width=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- قسم Image Effects ---
        col_ih1, col_ih2 = st.columns([4, 1])
        with col_ih1:
            st.markdown('<p class="section-title">🔥 Image Effects 🔥</p>', unsafe_allow_html=True)
        with col_ih2:
            if st.button("عرض الكل >", key="btn_all_imgfx"):
                st.session_state.tool_section = "قائمة_عمودية_imgfx"
                st.rerun()
                
        # صور قسم Image Effects (أفقي - مختلفة كلياً عن القسم الفوق)
        img_col4, img_col5, img_col6 = st.columns(3)
        with img_col4:
            st.image("https://images.unsplash.com/photo-1563089145-599997674d42?w=300&h=350&fit=crop", caption="Craft 3D Figu", use_container_width=True)
        with img_col5:
            st.image("https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=300&h=350&fit=crop", caption="Vehicle 3D Figure", use_container_width=True)
        with img_col6:
            st.image("https://images.unsplash.com/photo-1517841905240-472988babdf9?w=300&h=350&fit=crop", caption="Real Me 3D Figure", use_container_width=True)

    # 3. القائمة العمودية الخاصة بقسم (Cool Me) - تحتوي على 8 صور فريدة ومستقلة تماماً
    elif st.session_state.tool_section == "قائمة_عمودية_coolme":
        if st.button("⬅️ رجوع إلى تأثيرات الفيديو"):
            st.session_state.tool_section = "واجهة_تأثيرات_الفيديو"
            st.rerun()
            
        st.markdown("<h3>قائمة Cool Me الكاملة (عرض الكل)</h3>")
        st.write("التمرير عمودياً لاستعراض الـ 8 صور الخاصة بقسم Cool Me:")
        
        coolme_list = [
            {"title": "Pizza Feast Style", "desc": "تأثير مخصص لطعام البيتزا اللذيذ", "img": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&h=200&fit=crop"},
            {"title": "Beer Bliss Vibe", "desc": "أجواء ليلية هادئة واحترافية", "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&h=200&fit=crop"},
            {"title": "Burger Bite Retro", "desc": "مظهر كلاسيكي دافئ وجذاب", "img": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=200&h=200&fit=crop"},
            {"title": "Urban Youth Look", "desc": "نمط شبابي عصري ملفت للانتباه", "img": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop"},
            {"title": "Neon Hoodie Vibe", "desc": "إضاءات نيون متناسقة مع الملابس", "img": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&h=200&fit=crop"},
            {"title": "Classic Portrait", "desc": "بورتريه كلاسيكي عالي الدقة", "img": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=200&h=200&fit=crop"},
            {"title": "Vintage Cinema Tone", "desc": "ألوان سينمائية هادئة ودافئة", "img": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=200&h=200&fit=crop"},
            {"title": "Golden Hour Glow", "desc": "إضاءة ساعة الغروب الساحرة", "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200&h=200&fit=crop"}
        ]
        
        st.markdown('<div class="scrollable-grid">', unsafe_allow_html=True)
        for item in coolme_list:
            st.markdown(f"""
                <div class="effect-item-card">
                    <img src="{item['img']}" class="effect-item-img">
                    <div class="effect-item-text">
                        <h4>{item['title']}</h4>
                        <p>{item['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 4. القائمة العمودية الخاصة بقسم (Image Effects) - تحتوي على 8 صور فريدة ومستقلة تماماً
    elif st.session_state.tool_section == "قائمة_عمودية_imgfx":
        if st.button("⬅️ رجوع إلى تأثيرات الفيديو"):
            st.session_state.tool_section = "واجهة_تأثيرات_الفيديو"
            st.rerun()
            
        st.markdown("<h3>قائمة Image Effects الكاملة (عرض الكل)</h3>")
        st.write("التمرير عمودياً لاستعراض الـ 8 صور الخاصة بقسم Image Effects:")
        
        imgfx_list = [
            {"title": "Cyberpunk 3D Figu", "desc": "تصميم مجسمات ثلاثية الأبعاد سبرانية", "img": "https://images.unsplash.com/photo-1563089145-599997674d42?w=200&h=200&fit=crop"},
            {"title": "Sports Car Model", "desc": "تأثيرات سيارات رياضية فائقة السرعة", "img": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=200&h=200&fit=crop"},
            {"title": "Real Me 3D Render", "desc": "عرض شخصيات واقعية ثلاثية الأبعاد", "img": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=200&h=200&fit=crop"},
            {"title": "Futuristic Mech", "desc": "روبوتات ومعدات مستقبلية دقيقة", "img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=200&h=200&fit=crop"},
            {"title": "Abstract 3D Art", "desc": "فنون تجريدية بصرية مذهلة", "img": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=200&h=200&fit=crop"},
            {"title": "Sci-Fi Environment", "desc": "بيئات خيال علمي متطورة", "img": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=200&h=200&fit=crop"},
            {"title": "Neon Hologram FX", "desc": "هولوغرام ضوئي رقمي متقدم", "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=200&h=200&fit=crop"},
            {"title": "Dynamic Motion 3D", "desc": "تأثيرات حركة وعمق بصرى عالي", "img": "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?w=200&h=200&fit=crop"}
        ]
        
        st.markdown('<div class="scrollable-grid">', unsafe_allow_html=True)
        for item in imgfx_list:
            st.markdown(f"""
                <div class="effect-item-card">
                    <img src="{item['img']}" class="effect-item-img">
                    <div class="effect-item-text">
                        <h4>{item['title']}</h4>
                        <p>{item['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 5. توليد الفيديو
    elif st.session_state.tool_section == "توليد_الفيديو":
        if st.button("⬅️ رجوع"):
            st.session_state.tool_section = "قائمة_الأدوات_الرئيسية"
            st.rerun()
        st.markdown("<h3>قسم توليد الفيديو</h3>")
        st.text_area("أدخل الوصف الخاص بالفيديو:")
        st.button("بدء التوليد")

    # 6. توليد الصور
    elif st.session_state.tool_section == "توليد_الصور":
        if st.button("⬅ رجوع"):
            st.session_state.tool_section = "قائمة_الأدوات_الرئيسية"
            st.rerun()
        st.markdown("<h3>قسم توليد الصور</h3>")
        st.text_area("أدخل الوصف الخاص بالصورة:")
        st.button("إنشاء")
