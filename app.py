import streamlit as st

# إعدادات صفحة ستريمليت
st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# كود الواجهة المطابق تماماً لصورتك الأصلية
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بلوت كرافت</title>
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
    <main class="w-full max-w-[420px] min-h-screen bg-[#0c0f17] relative shadow-2xl border border-white/10 flex flex-col justify-between overflow-x-hidden">
        
        <!-- الخلفية السينمائية العليا -->
        <div class="relative w-full h-[410px] overflow-hidden flex-shrink-0">
            <img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80" alt="خلفية" class="absolute inset-0 w-full h-full object-cover object-top opacity-60 scale-105" />
            <div class="absolute inset-0 bg-gradient-to-b from-[#0b0d14]/60 via-[#0b0d14]/30 to-[#0c0f17]"></div>
            
            <!-- الهيدر (ترقية يسار، الاسم والشعار يمين) -->
            <header class="relative z-10 px-5 pt-8 pb-4 flex items-center justify-between">
                <button class="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white/15 backdrop-blur-md border border-white/20 text-xs font-semibold text-white">
                    <span class="text-amber-400">★</span>
                    <span>ترقية</span>
                </button>
                <div class="flex items-center gap-2">
                    <h1 class="text-xl font-black tracking-wide text-white">بلوت كرافت</h1>
                    <div class="w-8 h-8 rounded-full border border-white/30 bg-black/40 flex items-center justify-center p-1 backdrop-blur-sm">
                        <span class="text-xs">🎬</span>
                    </div>
                </div>
            </header>

            <!-- النص الترحيبي -->
            <div class="relative z-10 px-6 pt-4 text-right">
                <h2 class="text-[26px] font-black leading-tight text-white">مساء الخير، أيها المخرج</h2>
                <p class="text-lg font-bold text-gray-200 mt-1">أي قصة سنصنع اليوم؟</p>
            </div>

            <!-- بطاقات المسارات (سريع يسار، خطوة بخطوة يمين) -->
            <div class="relative z-10 px-5 pt-6 grid grid-cols-2 gap-3.5">
                <!-- بطاقة سريع (يسار) -->
                <div class="rounded-2xl bg-white/10 backdrop-blur-xl border border-white/15 p-4 flex flex-col justify-between h-[130px] relative">
                    <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-black/40 border border-white/10 text-[10px] text-gray-300 w-fit">Pro only</span>
                    <div>
                        <h3 class="text-base font-extrabold text-white">سريع</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5 leading-snug">إدخال واحد، فيديو كامل</p>
                    </div>
                    <div class="self-end w-9 h-9 rounded-xl bg-cyan-500/80 flex items-center justify-center text-white shadow-md">⚡</div>
                </div>

                <!-- بطاقة خطوة بخطوة (يمين) -->
                <div class="rounded-2xl bg-white/10 backdrop-blur-xl border border-white/15 p-4 flex flex-col justify-between h-[130px]">
                    <div class="h-4"></div>
                    <div>
                        <h3 class="text-base font-extrabold text-white">خطوة بخطوة</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">راجع كل خطوة</p>
                    </div>
                    <div class="self-end w-9 h-9 rounded-xl bg-blue-500/80 flex items-center justify-center text-white shadow-md">📁</div>
                </div>
            </div>
        </div>

        <!-- قسم الإلهام والأفلام -->
        <section class="px-5 pt-4 pb-28 flex-1">
            <div class="flex items-center justify-between mb-3.5">
                <span class="text-xs text-gray-400 cursor-pointer">عرض الكل ></span>
                <h3 class="text-lg font-extrabold text-white">إلهام بلوت كرافت</h3>
            </div>

            <div class="flex gap-3.5 overflow-x-auto no-scrollbar pb-2">
                <!-- فيلم 1 -->
                <div class="flex-shrink-0 w-[135px] rounded-2xl overflow-hidden bg-[#141824] border border-white/10">
                    <div class="h-[180px] relative">
                        <img src="https://images.unsplash.com/photo-1514533450685-4493e01d1fdc?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover" />
                        <span class="absolute top-2 right-2 bg-black/60 text-[9px] px-1.5 py-0.5 rounded text-white">رعب</span>
                    </div>
                    <div class="p-2 text-center">
                        <p class="text-[10px] font-bold text-gray-200 truncate">RE: INVITATION</p>
                    </div>
                </div>

                <!-- فيلم 2 -->
                <div class="flex-shrink-0 w-[135px] rounded-2xl overflow-hidden bg-[#141824] border border-white/10">
                    <div class="h-[180px] relative">
                        <img src="https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover" />
                        <span class="absolute top-2 right-2 bg-black/60 text-[9px] px-1.5 py-0.5 rounded text-white">غموض</span>
                    </div>
                    <div class="p-2 text-center">
                        <p class="text-[10px] font-bold text-gray-200 truncate">THE WRONG DOOR</p>
                    </div>
                </div>

                <!-- فيلم 3 -->
                <div class="flex-shrink-0 w-[135px] rounded-2xl overflow-hidden bg-[#141824] border border-white/10">
                    <div class="h-[180px] relative">
                        <img src="https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover" />
                        <span class="absolute top-2 right-2 bg-black/60 text-[9px] px-1.5 py-0.5 rounded text-white">دراما</span>
                    </div>
                    <div class="p-2 text-center">
                        <p class="text-[10px] font-bold text-gray-200 truncate">THE DELIVERYMAN</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- شريط الملاحة السفلي (الرئيسية يمين، الملف الشخصي يسار) -->
        <nav class="absolute bottom-3 left-4 right-4 bg-[#121622]/90 backdrop-blur-xl border border-white/15 rounded-full px-4 py-2.5 flex items-center justify-between z-30 shadow-2xl">
            <button class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-gray-300">👤</button>
            <button class="text-gray-400 text-xs font-medium">الأعمال</button>
            <button class="text-gray-400 text-xs font-medium">الأدوات</button>
            <button class="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white/15 text-white text-xs font-bold">
                <span>الصفحة الرئيسية</span>
                <span class="text-xs">🏠</span>
            </button>
        </nav>
    </main>
</body>
</html>
"""

st.components.v1.html(html_code, height=880, scrolling=True)
