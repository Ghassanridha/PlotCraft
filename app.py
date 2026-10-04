import streamlit as st
import time

# إعدادات صفحة التطبيق
st.set_page_config(
    page_title="PlotCraft - مولد الفيديوهات",
    page_icon="🎬",
    layout="wide"
)

# تهيئة الذاكرة المؤقتة لحفظ سجل الطلبات بالجلسة الحالية
if "history" not in st.session_state:
    st.session_state.history = []

# --- الشريط الجانبي للإعدادات والتحكم (Sidebar) ---
with st.sidebar:
    st.header("⚙️ إعدادات الإنتاج")
    
    # اختيار دقة الفيديو
    resolution = st.selectbox(
        "اختر دقة الفيديو:",
        ["720p (HD)", "1080p (FHD)", "4K (Ultra)"]
    )
    
    # اختيار نسبة العرض إلى الارتفاع (Aspect Ratio)
    aspect_ratio = st.selectbox(
        "نسبة عرض الفيديو (Format):",
        ["16:9 (يوتيوب/عرض)", "9:16 (ريلز/تيك توك)", "1:1 (مربع)"]
    )
    
    st.divider()
    
    # قسم السجل المؤقت داخل الشريط الجانبي
    st.subheader("📂 سجل الطلبات الحالية")
    if st.session_state.history:
        for i, item in enumerate(st.session_state.history[::-1]):
            st.text(f"{i+1}. المدة: {item['duration']}ث | الدقة: {item['res']}")
    else:
        st.info("لا توجد طلبات سابقة في هذه الجلسة.")

# --- الواجهة الرئيسية ---
st.title("🎬 PlotCraft - منصة توليد الفيديوهات المتقدمة")
st.write("أدخل فكرة السيناريو، ارفع صورتك المرجعية، وحدد إعداداتك لإنتاج فيديو تجريبي متكامل.")

# تقسيم الشاشة إلى عمودين لتنسيق أجمل
col1, col2 = st.columns([2, 1])

with col1:
    # 1. خانة كتابة النص
    script_text = st.text_area(
        "أدخل فكرة أو سيناريو الفيديو هنا:",
        placeholder="اصف المشهد أو القصة بالتفصيل...",
        height=150
    )

with col2:
    # 2. خانة رفع الصورة
    uploaded_file = st.file_uploader(
        "ارفع صورة توضيحية (اختياري):",
        type=["png", "jpg", "jpeg"]
    )

if uploaded_file is not None:
    st.image(uploaded_file, caption="الصورة المرجعية للمشروع", width=250)

# 3. شريط اختيار مدة الفيديو (إلى غاية 5 دقائق = 300 ثانية)
duration = st.slider(
    "اختر مدة الفيديو المطلوبة:",
    min_value=10,
    max_value=300,
    value=30,
    step=10,
    format="%d ثانية"
)

st.divider()

# 4. زر البدء مع محاكاة خطوات المعالجة (Status & Progress)
if st.button("🚀 بدء التوليد التجريبي الشامل", use_container_width=True):
    if not script_text and not uploaded_file:
        st.warning("⚠️ يرجى كتابة نص أو رفع صورة على الأقل لنستطيع البدء!")
    else:
        # استخدام st.status لعرض خطوات العمل بشكل واقعي
        with st.status("🔄 جاري معالجة المشروع...", expanded=True) as status:
            st.write("1️⃣ يتم تحليل النص والسيناريو المدخل...")
            time.sleep(1)
            
            if uploaded_file is not None:
                st.write("2️⃣ يتم دمج ومطابقة الصورة المرجعية مع المشهد...")
                time.sleep(1.5)
            else:
                st.write("2️⃣ تخطي معالجة الصورة (لم يتم رفع صورة)...")
                time.sleep(0.5)
                
            st.write(f"3️⃣ بناء المشاهد النهائية بمدة مستهدفة ({duration} ثانية)...")
            time.sleep(1)
            
            status.update(label="✨ تم إكمال المعالجة بنجاح!", state="complete", expanded=False)
        
        # حفظ الطلب في الذاكرة المؤقتة للجلسة
        st.session_state.history.append({
            "duration": duration,
            "res": resolution,
            "text": script_text[:30] + "..." if script_text else "بدون نص"
        })
        
        st.success(f"✅ تم إصدار الفيديو التجريبي بدقة {resolution} وبمدة {duration} ثانية بنجاح!")
        st.balloons()
