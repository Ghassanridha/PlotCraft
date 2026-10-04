import time
import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="PlotCraft - مولد الفيديوهات", page_icon="🎬", layout="centered"
)

# تصميم وتنسيق CSS مخصص لواجهة داكنة وتصميم احترافي نقي
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
    /* تنسيق الأزرار الرئيسية */
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

# --- شريط علوي يحتوي على زر الترقية في اليسار ---
top_col1, top_col2 = st.columns([3, 1])

with top_col1:
  st.markdown(
      "<h3 style='margin:0; color: #f8fafc; text-align: right;'>PlotCraft</h3>",
      unsafe_allow_html=True,
  )

with top_col2:
  # قائمة منبثقة للترقية بتصميم نظيف واحترافي بدون أي إيموجيات
  with st.popover("ترقية PRO"):
    st.markdown(
        "<h3 style='text-align: center; color: #ffffff; margin-bottom:0;'>DRMA"
        " PRO</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; font-size: 12px; color: #94a3b8;"
        " margin-top:2px;'>حول أفكارك إلى دراما احترافية</p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # خيارات الاشتراكات بنصوص وأرقام فقط بشكل نظيف تماماً
    if st.button("9.99 دولار | أسبوع | 500 رصيد للتوليد"):
      st.balloons()
      st.success("تم اختيار الخطة الأسبوعية بنجاح")

    if st.button("29.99 دولار | شهر | 1800 رصيد (الأكثر طلباً)"):
      st.balloons()
      st.success("تم اختيار الخطة الشهرية بنجاح")

    if st.button("69.99 دولار | سنة | 5000 رصيد ومميزات كاملة"):
      st.balloons()
      st.success("تم اختيار الخطة السنوية بنجاح")

    st.markdown(
        "<p style='text-align: center; font-size: 10px; color: #64748b; "
        "margin-top: 10px;'>تجديد تلقائي، يمكن الإلغاء في أي وقت</p>",
        unsafe_allow_html=True,
    )

st.markdown("---")

# واجهة ترحيبية بتصميم عصري
st.markdown(
    """
    <div class="header-box">
        <h3 style="margin:0; color: #f8fafc;">طاب مساؤك، أيها المخرج</h3>
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

# إعدادات الإنتاج
st.markdown(
    "<h4 style='text-align: right; color: #e2e8f0;'>إعدادات الإنتاج</h4>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
  resolution = st.selectbox(
      "دقة الفيديو", ["720p (سريع)", "1080p (عالي الدقة)", "4K (احترافي)"]
  )

with col2:
  aspect_ratio = st.selectbox("نسبة العرض", ["16:9 (يوتيوب)", "9:16 (تيك توك/ريلز)"])

# اختيار المدة المحددة (10 ثواني، 21 ثانية، أو 5 دقائق) بدون رقم 300
duration_option = st.selectbox(
    "حدد مدة الفيديو:", ["10 ثواني", "21 ثانية", "5 دقائق"]
)

# تحويل الاختيار إلى قيمة ثواني برمجياً خلف الكواليس
if duration_option == "10 ثواني":
  duration = 10
elif duration_option == "21 ثانية":
  duration = 21
else:
  duration = 300  # 5 دقائق

st.markdown("---")

# زر التوليد الرئيسي
if st.button("بدء التوليد التجريبي الشامل"):
  if not prompt.strip():
    st.warning("يرجى كتابة فكرة أو سيناريو الفيديو أولاً")
  else:
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

    st.success("تم توليد الفيديو التجريبي بنجاح")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

    if "history" not in st.session_state:
      st.session_state.history = []
    st.session_state.history.append(
        {
            "prompt": prompt,
            "duration": duration_option,
            "resolution": resolution,
            "time": time.strftime("%H:%M:%S"),
        }
    )

# عرض سجل الجلسات السابقة
if "history" in st.session_state and st.session_state.history:
  with st.expander("سجل الفيديوهات المنتجة في هذه الجلسة"):
    for idx, item in enumerate(reversed(st.session_state.history)):
      st.markdown(
          f"""**{idx+1}.** الفكرة: `{item['prompt'][:50]}...` <br>
                المدة: {item['duration']} | الدقة: {item['resolution']} | الوقت: {item['time']}""",
          unsafe_allow_html=True,
      )
      st.markdown("---")
