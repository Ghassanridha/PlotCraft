import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="PlotCraft | بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم (CSS) الثيم المظلم والأزرار والتأثيرات
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
        color: #f0f6fc;
    }
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        border: none;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(168, 85, 247, 0.4);
    }
    .card {
        background: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .card:hover {
        border-color: #8b5cf6;
        transform: translateY(-4px);
    }
    h1, h2, h3 {
        color: #ffffff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة التنقل بين الشاشات عبر Session State
if 'current_screen' not in st.session_state:
    st.session_state.current_screen = 'home'

def navigate_to(screen_name):
    st.session_state.current_screen = screen_name
    st.rerun()

# ==================== شاشة الرئيسية ====================
if st.session_state.current_screen == 'home':
    st.markdown("<h1 style='text-align: center;'>🎬 PlotCraft (بلوت كرافت)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8b949e;'>منصتك الذكية لصناعة القصص، الأفلام، وتأثيرات الفيديو بالذكاء الاصطناعي</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("🚀 ابدأ الآن / الانتقال للأدوات", use_container_width=True):
            navigate_to('tools')
            
    st.markdown("---")
    st.markdown("### 🌟 مميزات المنصة الشاملة")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='card'><h3>🎥 توليد فيديو</h3><p>حول النصوص إلى مشاهد سينمائية.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h3>✨ تأثيرات حصرية</h3><p>فلاتر وتأثيرات ذكية لملامح وخلفيات الشاب.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h3>✍️ كتابة سيناريو</h3><p>ابتكار قصص متكاملة بضغطة زر.</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='card'><h3>💎 الاشتراكات</h3><p>باقات مخصصة لصناع المحتوى.</p></div>", unsafe_allow_html=True)

# ==================== شاشة الأدوات الرئيسية ====================
elif st.session_state.current_screen == 'tools':
    st.markdown("<h1>🛠️ لوحة أدوات PlotCraft</h1>", unsafe_allow_html=True)
    st.write("اختر الأداة المناسبة لبدء مشروعك الإبداعي القادم:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🎥 توليد الفيديو")
        st.write("إنشاء مقاطع فيديو وتوليد مشاهد بالذكاء الاصطناعي.")
        if st.button("فتح أداة الفيديو", key="btn_video"):
            navigate_to('video_gen')
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("✨ تأثيرات الفيديو والصور")
        st.write("تأثيرات Cool Me وتأثيرات الصور المتقدمة والفريدة.")
        if st.button("فتح قسم التأثيرات", key="btn_effects"):
            navigate_to('video_effects')
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("✍️️ كتابة السيناريو والقصص")
        st.write("توليد قصص وأفكار أفلام متكاملة تلقائياً.")
        if st.button("فتح أداة القصص", key="btn_story"):
            navigate_to('story_gen')
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    col_back1, col_back2 = st.columns(2)
    with col_back1:
        if st.button("🔙 العودة للرئيسية"):
            navigate_to('home')
    with col_back2:
        if st.button("💎 الانتقال لصفحة الاشتراكات"):
            navigate_to('subscription')

# ==================== شاشة تأثيرات الفيديو (الرئيسية) ====================
elif st.session_state.current_screen == 'video_effects':
    st.markdown("<h1>✨ تأثيرات الفيديو والصور الفريدة</h1>", unsafe_allow_html=True)
    st.write("استكشف الأقسام والتأثيرات الحديثة والواقعية:")
    
    tab1, tab2 = st.tabs(["🔥 قسم Cool Me", "🖼️ قسم Image Effects"])
    
    with tab1:
        st.subheader("تأثيرات Cool Me المتميزة")
        col1, col2, col3, col4 = st.columns(4)
        cool_me_previews = [
            ("Cyber Neon", "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=500&auto=format&fit=crop&q=60"),
            ("Royal Gold", "https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=500&auto=format&fit=crop&q=60"),
            ("Anime Fantasy", "https://images.unsplash.com/photo-1628157582853-a796fa650a6a?w=500&auto=format&fit=crop&q=60"),
            ("Cyberpunk Edge", "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500&auto=format&fit=crop&q=60")
        ]
        for i, (name, img) in enumerate(cool_me_previews):
            with [col1, col2, col3, col4][i]:
                st.image(img, use_container_width=True)
                st.markdown(f"<p style='text-align:center; font-weight:600;'>{name}</p>", unsafe_allow_html=True)
                
        if st.button("عرض الكل (8 صور Cool Me فريدة)", key="btn_cool_all"):
            navigate_to('cool_me_all')
            
    with tab2:
        st.subheader("تأثيرات الصور المتقدمة")
        col1, col2, col3, col4 = st.columns(4)
        img_fx_previews = [
            ("Glitch FX", "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500&auto=format&fit=crop&q=60"),
            ("Lens Flare", "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=500&auto=format&fit=crop&q=60"),
            ("Cinematic Blur", "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=500&auto=format&fit=crop&q=60"),
            ("Vintage Film", "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=500&auto=format&fit=crop&q=60")
        ]
        for i, (name, img) in enumerate(img_fx_previews):
            with [col1, col2, col3, col4][i]:
                st.image(img, use_container_width=True)
                st.markdown(f"<p style='text-align:center; font-weight:600;'>{name}</p>", unsafe_allow_html=True)
                
        if st.button("عرض الكل (8 صور Image Effects فريدة)", key="btn_img_all"):
            navigate_to('image_fx_all')

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔙 العودة للأدوات", key="back_to_tools_from_fx"):
        navigate_to('tools')

# ==================== شاشة عرض الكل: Cool Me (8 صور فريدة ومختلفة تماماً) ====================
elif st.session_state.current_screen == 'cool_me_all':
    st.markdown("<h1>🔥 قسم Cool Me - كافة التأثيرات (8 صور فريدة)</h1>", unsafe_allow_html=True)
    st.write("إليك 8 تأثيرات حديثة وواقعية لخلفيات وملامح الشاب بدون أي تكرار:")
    
    cool_me_8_images = [
        ("1. Cyber Neon", "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=500&auto=format&fit=crop&q=60"),
        ("2. Royal Gold", "https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=500&auto=format&fit=crop&q=60"),
        ("3. Anime Fantasy", "https://images.unsplash.com/photo-1628157582853-a796fa650a6a?w=500&auto=format&fit=crop&q=60"),
        ("4. Cyberpunk Edge", "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500&auto=format&fit=crop&q=60"),
        ("5. Urban Street", "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=500&auto=format&fit=crop&q=60"),
        ("6. Dark Moody", "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=500&auto=format&fit=crop&q=60"),
        ("7. Sunset Glow", "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?w=500&auto=format&fit=crop&q=60"),
        ("8. Neon Future", "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=500&auto=format&fit=crop&q=60")
    ]
    
    cols = st.columns(4)
    for idx, (title, img_url) in enumerate(cool_me_8_images):
        with cols[idx % 4]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.image(img_url, use_container_width=True)
            st.markdown(f"<b>{title}</b>", unsafe_allow_html=True)
            if st.button("تطبيق التأثير", key=f"apply_cool_{idx}"):
                st.success(f"تم تطبيق تأثير {title} بنجاح!")
            st.markdown("</div>", unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔙 العودة لقسم التأثيرات", key="back_to_fx_main_1"):
        navigate_to('video_effects')

# ==================== شاشة عرض الكل: Image Effects (8 صور فريدة ومختلفة تماماً) ====================
elif st.session_state.current_screen == 'image_fx_all':
    st.markdown("<h1>🖼️ قسم Image Effects - كافة التأثيرات (8 صور فريدة)</h1>", unsafe_allow_html=True)
    st.write("إليك 8 تأثيرات بصرية متقدمة للصور بخلفيات واقعية ومذهلة بدون أي تكرار:")
    
    image_fx_8_images = [
        ("1. Glitch FX", "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500&auto=format&fit=crop&q=60"),
        ("2. Lens Flare", "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=500&auto=format&fit=crop&q=60"),
        ("3. Cinematic Blur", "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=500&auto=format&fit=crop&q=60"),
        ("4. Vintage Film", "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=500&auto=format&fit=crop&q=60"),
        ("5. Dual Tone", "https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=500&auto=format&fit=crop&q=60"),
        ("6. Hologram Scan", "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=500&auto=format&fit=crop&q=60"),
        ("7. Cinematic HDR", "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=500&auto=format&fit=crop&q=60"),
        ("8. Prism Ray", "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=500&auto=format&fit=crop&q=60")
    ]
    
    cols = st.columns(4)
    for idx, (title, img_url) in enumerate(image_fx_8_images):
        with cols[idx % 4]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.image(img_url, use_container_width=True)
            st.markdown(f"<b>{title}</b>", unsafe_allow_html=True)
            if st.button("تطبيق التأثير", key=f"apply_img_{idx}"):
                st.success(f"تم تطبيق تأثير {title} بنجاح!")
            st.markdown("</div>", unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔙 العودة لقسم التأثيرات", key="back_to_fx_main_2"):
        navigate_to('video_effects')

# ==================== شاشة توليد الفيديو ====================
elif st.session_state.current_screen == 'video_gen':
    st.markdown("<h1>🎥 استوديو توليد الفيديو الذكي</h1>", unsafe_allow_html=True)
    st.write("أنشئ مشاهد سينمائية عبر إدخال التوجيه والخصائص المطلوبة:")
    
    prompt = st.text_area("أدخل وصف المشهد (Prompt):", "شاب بملابس أنيقة يقف أمام خلفية مدينة مستقبلية مضاءة بالنيون...")
    
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("نسبة عرض الشاشة:", ["16:9 (سينمائي)", "9:16 (ريلز/تيك توك)", "1:1 (مربع)"])
    with col2:
        st.selectbox("نموذج الذكاء الاصطناعي:", ["PlotCraft Ultra v3", "Cinematic Pro 4K", "Fast Gen v2"])
        
    if st.button("🚀 توليد الفيديو الآن"):
        st.success("جاري معالجة وتوليد الفيديو بالذكاء الاصطناعي... يرجى الانتظار قليلاً!")
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔙 العودة للأدوات", key="back_to_tools_from_video"):
        navigate_to('tools')

# ==================== شاشة كتابة السيناريو والقصص ====================
elif st.session_state.current_screen == 'story_gen':
    st.markdown("<h1>✍️ مولد القصص والسيناريو الذكي</h1>", unsafe_allow_html=True)
    st.write("أدخل فكرة قصتك أو فيلمك وسيقوم النظام بتطوير السيناريو والحوارات بالكامل:")
    
    story_idea = st.text_input("فكرة القصة الرئيسية:", "رحلة عبر الزمن لإنقاذ مستقبل مدينة ضائعة...")
    story_genre = st.selectbox("نوع القصة:", ["خيال علمي", "دراما", "مغامرات", "إثارة وتشويق"])
    
    if st.button("✨ توليد السيناريو الكامل"):
        st.success("تم توليد سيناريو القصة والحوارات بنجاح!")
        st.markdown("---")
        st.markdown("### 📜 معاينة السيناريو المولد:")
        st.info("المشهد الأول: تبدأ القصة في الشوارع المظلمة للمدينة حيث يظهر البطل وهو يتأمل الأفق...")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔙 العودة للأدوات", key="back_to_tools_from_story"):
        navigate_to('tools')

# ==================== شاشة الاشتراكات ====================
elif st.session_state.current_screen == 'subscription':
    st.markdown("<h1>💎 باقات الاشتراكات والعضوية</h1>", unsafe_allow_html=True)
    st.write("اختر الباقة المناسبة لاحتياجاتك في صناعة المحتوى:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='card'><h3>الباقة المجانية</h3><p>ميزات أساسية وتوليد محدود.</p><b>0$ / شهرياً</b><br><br></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'><h3>الباقة الاحترافية</h3><p>وصول كامل للتأثيرات والفيديوهات بدقة عالية.</p><b>19$ / شهرياً</b><br><br></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'><h3>باقة الاستوديوهات</h3><p>توليد غير محدود ودعم فني مخصص.</p><b>49$ / شهرياً</b><br><br></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔙 العودة للرئيسية", key="back_to_home_from_sub"):
        navigate_to('home')

# شريط التنقل السفلي الثابت في أسفل التطبيق
st.markdown("---")
col_nav1, col_nav2, col_nav3, col_nav4 = st.columns(4)
with col_nav1:
    if st.button("🏠 الرئيسية", use_container_width=True):
        navigate_to('home')
with col_nav2:
    if st.button("🛠️ الأدوات", use_container_width=True):
        navigate_to('tools')
with col_nav3:
    if st.button("✨ التأثيرات", use_container_width=True):
        navigate_to('video_effects')
with col_nav4:
    if st.button("💎 الاشتراكات", use_container_width=True):
        navigate_to('subscription')
