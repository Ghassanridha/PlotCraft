import streamlit as st

# إعدادات صفحة ستريمليت
st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تضمين تصميم HTML و Tailwind CSS للواجهة بدقة
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بلوت كرافت - واجهة التطبيق</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="bg-[#0b0d14] text-white flex justify-center items-center p-0 m-0">
    <main class="w-full max-w-[420px] min-h-screen bg-[#0c0f17] relative shadow-2xl border border-white/10 flex flex-col justify-between">
        
        <!-- الخلفية السينمائية العليا -->
        <div class="relative w-full h-[390px] overflow-hidden flex-shrink-0">
            <img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80" alt="خلفية" class="absolute inset-0 w-full h-full object-cover object-top opacity-55 scale-105" />
            <div class="absolute inset-0 bg-gradient-to-b from-[#0b0d14]/70 via-[#0b0d14]/30 to-[#0c0f17]"></div>
            
            <!-- الهيدر -->
            <header class="relative z-10 px-5 pt-8 pb-4 flex items-center justify-between">
                <button class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/15 backdrop-blur-md border border-white/20 text-xs font-semibold text-white">
                    <span class="text-amber-400">★</span>
                    <span>ترقية</span>
                </button>
                <div class="flex items-center gap-2">
                    <h1 class="text-xl font-black tracking-wide text-white">بلوت كرافت</h1>
                    <div class="w-8 h-8 rounded-full border border-white/30 bg-black/40 flex items-center justify-center p-1">
                        <span class="text-xs">🎬</span>
                    </div>
                </div>
            </header>

            <!-- النص الترحيبي -->
            <div class="relative z-10 px-6 pt-5">
                <h2 class="text-2xl font-black leading-tight text-white">مساء الخير، أيها المخرج</h2>
                <p class="text-lg font-bold text-gray-200 mt-1">أي قصة سنصنع اليوم؟</p>
            </div>

            <!-- بطاقات المسارات -->
            <div class="relative z-10 px-5 pt-7 grid grid-cols-2 gap-3.5">
                <div class="rounded-2xl bg-white/10 backdrop-blur-xl border border-white/15 p-4 flex flex-col justify-between h-[126px]">
                    <div>
                        <h3 class="text-base font-extrabold text-white">خطوة بخطوة</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">راجع كل خطوة</p>
                    </div>
                    <div class="self-end w-9 h-9 rounded-xl bg-blue-500/80 flex items-center justify-center text-white">📁</div>
                </div>
                
                <div class="rounded-2xl bg-white/10 backdrop-blur-xl border border-white/15 p-4 flex flex-col justify-between h-[126px]">
                    <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-black/40 border border-white/10 text-[10px] text-gray-300 w-fit">Pro only</span>
                    <div>
                        <h3 class="text-base font-extrabold text-white">سريع</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">إدخال واحد، فيديو كامل</p>
                    </div>
                    <div class="self-end w-9 h-9 rounded-xl bg-cyan-500/80 flex items-center justify-center text-white -mt-2">⚡</div>
                </div>
            </div>
        </div>

        <!-- قسم الإلهام -->
        <section class="px-5 pt-3 pb-24 flex-1">
            <div class="flex items-center justify-between mb-3.5">
                <h3 class="text-lg font-extrabold text-white">إلهام بلوت كرافت</h3>
                <span class="text-xs text-gray-400">عرض الكل</span>
            </div>

            <div class="flex gap-3.5 overflow-x-auto no-scrollbar pb-1">
                <div class="flex-shrink-0 w-[140px] rounded-2xl overflow-hidden bg-[#141824] border border-white/10">
                    <div class="h-[185px] relative">
                        <img src="https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover" />
                    </div>
                    <div class="p-2.5 text-center">
                        <p class="text-[11px] font-bold text-gray-200">Deliveryman</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- شريط الملاحة السفلي -->
        <nav class="absolute bottom-3 left-4 right-4 bg-[#121622]/85 backdrop-blur-xl border border-white/15 rounded-full px-3 py-2 flex items-center justify-between z-30">
            <button class="flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/15 text-white text-xs font-bold">الرئيسية</button>
            <button class="text-gray-400 text-xs">الأدوات</button>
            <button class="text-gray-400 text-xs">الأعمال</button>
        </nav>
    </main>
</body>
</html>
"""

# عرض الواجهة داخل تطبيق Streamlit بدون مشاكل برمجية
st.components.v1.html(html_code, height=880, scrolling=True)
