import os
import fal_client
import streamlit as st

# تعيين مفتاح الـ API الخاص بك
os.environ["FAL_KEY"] = (
    "fal_sk_d8e30b437fdc44c891740a201522be4d:d78802704ad38b28b6b7f1bcef6ef4c"
)

st.title("PlotCraft - مولد الفيديوهات بالذكاء الاصطناعي")

# خانة كتابة الفكرة أو المشهد
prompt = st.text_area(
    "اكتب وصف الفيديو أو المشهد الذي تريد توليده:",
    "A cinematic shot of a futuristic sports car driving through neon city, 4k",
)

if st.button("توليد الفيديو الحقيقي"):
  if not prompt:
    st.warning("يرجى كتابة وصف أولاً!")
  else:
    with st.spinner(
        "جاري إرسال الطلب إلى نموذج الذكاء الاصطناعي وتوليد الفيديو الحقيقي..."
    ):
      try:
        # استدعاء نموذج fal.ai لتوليد الفيديو
        handler = fal_client.submit(
            "fal-ai/minimax/video-01", arguments={"prompt": prompt}
        )

        # انتظار النتيجة وعرضها
        result = handler.get()
        video_url = result["video"]["url"]

        st.success("تم توليد الفيديو بنجاح!")
        st.video(video_url)

      except Exception as e:
        st.error(f"حدث خطأ أثناء التوليد: {e}")
