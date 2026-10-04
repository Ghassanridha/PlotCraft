import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت - لوحة التحكم",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بلوت كرافت</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background-color: #07090e; }
        .glass-box {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.02));
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
    </style>
</head>
<body class="text-white flex justify-center items-center p-0 m-0 min-h-screen">

    <main class="w-full max-w-[420px] min-h-screen bg-[#090b10] relative shadow-2xl border border-white/10 flex flex-col justify-between p-5">
        
        <!-- الهيدر -->
        <div>
            <div class="flex items-center justify-between mb-6">
                <div class="flex items-center gap-2">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/30">
                        ✨
                    </div>
                    <h1 class="text-lg font-black tracking-wide">استوديو بلوت كرافت</h1>
                </div>
                <span class="px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold">متصل</span>
            </div>

            <!-- بطاقة إدخال الوصف -->
            <div class="glass-box rounded-2xl p-4 mb-4">
                <label class="block text-xs font-bold text-gray-300 mb-2">وصف المشهد أو القصة (Prompt)</label>
                <textarea rows="3" class="w-full bg-black/40 border border-white/10 rounded-xl p-3 text-sm text-white focus:outline-none focus:border-indigo-500 resize-none" placeholder="اكتب وصفاً سينمائياً دقيقاً..."></textarea>
            </div>

            <!-- اختيار الأبعاد والأنماط -->
            <div class="grid grid-cols-2 gap-3 mb-4">
                <div class="glass-box rounded-xl p-3">
                    <label class="block text-[11px] font-bold text-gray-400 mb-1">أبعاد الفيديو</label>
                    <select class="w-full bg-black/60 border border-white/10 rounded-lg p-2 text-xs text-white focus:outline-none">
                        <option>9:16 (تيك توك / ريلز)</option>
                        <option>16:9 (يوتيوب عريض)</option>
                        <option>1:1 (مربع)</option>
                    </select>
                </div>
                <div class="glass-box rounded-xl p-3">
                    <label class="block text-[11px] font-bold text-gray-400 mb-1">النمط الفني</label>
                    <select class="w-full bg-black/60 border border-white/10 rounded-lg p-2 text-xs text-white focus:outline-none">
                        <option>سينمائي فاخر</option>
                        <option>واقعي خيالي</option>
                        <option>أنمي ياباني</option>
                    </select>
                </div>
            </div>

            <!-- زر التوليد -->
            <button class="w-full py-3.5 rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 font-bold text-sm text-white shadow-lg shadow-indigo-600/30 hover:opacity-95 transition">
                🚀 ابدأ توليد المشهد السحري
            </button>
        </div>

        <!-- نصائح سريعة في الأسفل -->
        <div class="glass-box rounded-2xl p-4 mt-6">
            <h4 class="text-xs font-bold text-indigo-400 mb-1">💡 نصيحة احترافية:</h4>
            <p class="text-[11px] text-gray-400 leading-relaxed">حدد الإضاءة ونوع الكاميرا بوضوح للحصول على أفضل نتيجة سينمائية ممكنة.</p>
        </div>

    </main>

</body>
</html>
"""

st.components.v1.html(html_code, height=750, scrolling=True)
