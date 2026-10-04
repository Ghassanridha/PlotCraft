import time
import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="PlotCraft - مولد الفيديوهات", page_icon="🎬", layout="centered"
)

# تصميم وتنسيق CSS مخصص لواجهة داكنة وتنسيق احترافي للأزرار والنصوص
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
    /* تنسيق الأزرار الرئيسية في التطبيق */
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
    
    /* تنسيق أزرار خطط الترقية لتكون مرتبة بعناية (عربي فوق وإنجليزي تحته تماماً) */
    .sub-btn-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        text-align: center;
    }
    .sub-ar {
        font-size: 14px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 3px;
    }
    .sub-en {
        font-size: 11px;
        color: #94a3b8;
        font-weight: normal;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- شريط علوي يحتوي على زر الترقية في اليسار ---
top_col1, top_col2 = st.columns([3, 1])

with top_col1:
  st.markdown(
      "<h3 style='margin:0; color: #f8fafc; text-align: right; padding-top:"
      " 8px;'>PlotCraft</h3>",
      unsafe_allow_html=True,
  )

with top_col2:
  # زر الترقية (PRO ترقية) بدون أي فاصل وبدون إيموجي
  with st.popover("PRO ترقية"):
    st.markdown(
        "<h3 style='text-align: center; color: #ffffff; margin-bottom:0;'>PlotCraft"
        " PRO</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; font-size: 12px; color: #94a3b8;"
        " margin-top:2px;'>حول أفكارك إلى دراما احترافية<br><span"
        " style='font-size: 10px; color: #64748b;'>Turn your ideas into"
        " professional drama</span></p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # الخطة الأسبوعية (مرتبة بشكل عمودي نظيف)
    if st.button(
        "weekly_plan_btn", key="btn_week", use_container_width=True
    ):  # استخدام مفتاح فريد لضمان عمل الزر
      pass

    # استخدام طريقة عرض منظمة جداً لأزرار الاشتراكات عبر دمج النصوص بأسطر منفصلة
    st.markdown(
        """
        <style>
        div[data-testid="stButton"] button {
            height: auto;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # الخطة الأسبوعية
    if st.button("9.99 دولار | أسبوع | 500 رصيد للتوليد \n $9.99 | Weekly | 500 Credits"):
      st.balloons()
      st.success("تم اختيار الخطة الأسبوعية بنجاح")

    # الخطة الشهرية
    if st.button("29.99 دولار | شهر | 1800 رصيد (الأكثر طلباً) \n $29.99 | Monthly | 1800 Credits (Most Popular)"):
      st.balloons()
      st.success("تم اختيار الخطة الشهرية بنجاح")

    # الخطة السنوية
    if st.button("69.99 دولار | سنة | 5000 رصيد ومميزات كاملة \n $69.99 | Yearly | 5000 Credits & Full Features"):
      st.balloons()
      st.success("تم اختيار الخطة السنوية بنجاح")

    st.markdown(
        "<p style='text-align: center; font-size: 10px; color: #64748b; "
        "margin-top: 10px;'>تجديد تلقائي، يمكن الإلغاء في أي وقت<br>Auto-renewal,"
        " cancel anytime</p>",
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

# اختيار المدة المحددة
duration_option = st.selectbox(
    "حدد مدة الفيديو:", ["10 ثواني", "21 ثانية", "5 دقائق"]
)

if duration_option == "10 ثواني":
  duration = 10
elif duration_option == "21 ثانية":
  duration = 21
else:
  duration = 300

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
