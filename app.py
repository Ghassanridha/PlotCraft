import time
import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="PlotCraft - مولد الفيديوهات", page_icon="🎬", layout="centered"
)

# تصميم وتنسيق CSS مخصص لواجهة داكنة عصرية
st.markdown(
    """
    <style>
    /* خلفية التطبيق العامة */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* تنسيق الحقول النصية */
    .stTextArea textarea {
        background-color: #1a1f2c;
        color: white;
        border-radius: 12px;
        border: 1px solid #2d3748;
    }
    /* تنسيق الأزرار */
    .stButton button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 0.75rem 1rem;
        width: 100%;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
    }
    /* بطاقات العنوان المخصصة */
    .header-box {
        padding: 15px;
        border-radius: 15px;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        margin-bottom: 20px;
        text-align: right;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# واجهة ترحيبية بتصميم عاصري
st.markdown(
    """
    <div class="header-box">
        <h3 style="margin:0; color: #f8fafc;">🎬 طاب مساؤك، أيها المخرج</h3>
        <p style="margin:5px 0 0 0; color: #94a3b8; font-size: 14px;">أي قصة سنصنع اليوم؟</p>
    </div>
""",
    unsafe_allow_html=True,
)

# إدخال سيناريو الفيديو
prompt = st.text_area(
    "أدخل فكرة أو سيناريو الفيديو هنا:",
    placeholder="اكتب وصف المشهد أو القصة بالتفصيل...",
    height=120,
)

# رفع صورة توضيحية
uploaded_file = st.file_uploader(
    "ارفع صورة توضيحية (اختياري):", type=["png", "jpg", "jpeg"]
)

st.markdown("---")

# دمج الإعدادات في الصفحة الرئيسية (بدل القائمة الجانبية)
st.markdown(
    "<h4 style='text-align: right; color: #e2e8f0;'>⚙️ إعدادات الإنتاج</h4>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    resolution = st.selectbox(
        "دقة الفيديو", ["720p (سريع)", "1080p (عالي الدقة)", "4K (احترافي)"]
    )

with col2:
    aspect_ratio = st.selectbox("نسبة العرض", ["16:9 (يوتيوب)", "9:16 (تيك توك/ريلز)"])

# شريط المدة الزمنية
duration = st.slider("اختر مدة الفيديو (بالثانيات):", 10, 300, 30)

st.markdown("---")

# زر التوليد الرئيسي
if st.button("🚀 بدء التوليد التجريبي الشامل"):
  if not prompt.strip():
    st.warning("يرجى كتابة فكرة أو سيناريو الفيديو أولاً!")
  else:
    # محاكاة خطوات العمل بوضوح
    status_text = st.empty()
    progress_bar = st.progress(0)

    steps = [
        ("تحليل السيناريو بالذكاء الاصطناعي...", 25),
        ("توليد الإطارات والعناصر البصرية...", 50),
        ("معالجة الصوت والمؤثرات...", 75),
        ("إنجاز الفيديو النهائي...", 100),
    ]

    for text, progress in steps:
      status_text.markdown(f"**{text}**")
      progress_bar.progress(progress)
      time.sleep(0.8)

    st.success("✨ تم توليد الفيديو التجريبي بنجاح!")

    # عرض محاكاة للفيديو الناتج
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

    # حفظ في سجل الجلسة
    if "history" not in st.session_state:
      st.session_state.history = []
    st.session_state.history.append(
        {
            "prompt": prompt,
            "duration": duration,
            "resolution": resolution,
            "time": time.strftime("%H:%M:%S"),
        }
    )

# عرض سجل الجلسات السابقة (إذا وُجدت)
if "history" in st.session_state and st.session_state.history:
  with st.expander("📂 سجل الفيديوهات المنتجة في هذه الجلسة"):
    for idx, item in enumerate(reversed(st.session_state.history)):
      st.markdown(
          f"""**{idx+1}.** الفكرة: `{item['prompt'][:50]}...` <br>
                ⏱️ المدة: {item['duration']} ثانية | 🖥️ الدقة: {item['resolution']} | ⏰ الوقت: {item['time']}""",
          unsafe_allow_html=True,
      )
      st.markdown("---")
