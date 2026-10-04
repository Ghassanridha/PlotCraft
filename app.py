import streamlit as st

# إعدادات صفحة ستريمليت
st.set_page_config(
    page_title="بلوت كرافت - واجهة التطبيق",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# كود الواجهة بالكامل بدون تعديل في التصميم أو العناصر
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بلوت كرافت - واجهة التطبيق</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Tajawal -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="bg-[#0b0d14] text-white min-h-screen flex justify-center items-center p-0 sm:p-4">
    <!-- إطار شاشة الموبايل -->
    <main class="w-full max-w-[420px] min-h-screen sm:min-h-[880px] bg-[#0c0f17] sm:rounded-[36px] overflow-hidden relative shadow-2xl border border-white/10 flex flex-col justify-between">
        
        <!-- الخلفية السينمائية العليا مع التدرج المعتم -->
        <div class="relative w-full h-[390px] overflow-hidden flex-shrink-0">
            <img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80" alt="خلفية سينمائية خيالية" class="absolute inset-0 w-full h-full object-cover object-top opacity-55 scale-105" />
            
            <!-- طبقات التدرج الضوئي للدمج الزجاجي -->
            <div class="absolute inset-0 bg-gradient-to-b from-[#0b0d14]/70 via-[#0b0d14]/30 to-[#0c0f17]"></div>
            <div class="absolute -top-16 -right-16 w-60 h-60 bg-blue-500/20 rounded-full blur-3xl pointer-events-none"></div>
            <div class="absolute top-28 left-4 w-48 h-48 bg-cyan-400/20 rounded-full blur-3xl pointer-events-none"></div>

            <!-- الشريط العلوي (الهيدر) -->
            <header class="relative z-10 px-5 pt-8 pb-4 flex items-center justify-between">
                <!-- زر الترقية -->
                <button class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/15 backdrop-blur-md border border-white/20 text-xs font-semibold text-white hover:bg-white/25 transition">
                    <svg class="w-3.5 h-3.5 text-amber-400" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M5 16L3 5l5.5 5L12 4l3.5 6L21 5l-2 11H5m14 3c0 .6-.4 1-1 1H6c-.6 0-1-.4-1-1v-1h14v1z"/>
                    </svg>
                    <span>ترقية</span>
                </button>

                <!-- اسم وشعار التطبيق -->
                <div class="flex items-center gap-2">
                    <h1 class="text-xl font-black tracking-wide text-white drop-shadow">بلوت كرافت</h1>
                    <div class="w-8 h-8 rounded-full border border-white/30 bg-black/40 flex items-center justify-center p-1 backdrop-blur-sm shadow-inner">
                        <svg class="w-full h-full text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10" stroke-dasharray="4 2"/>
                            <path d="M8 12l8 0M12 8l0 8" stroke-linecap="round"/>
                        </svg>
                    </div>
                </div>
            </header>

            <!-- النص الترحيبي السينمائي -->
            <div class="relative z-10 px-6 pt-5">
                <h2 class="text-2xl sm:text-[26px] font-black leading-tight text-white drop-shadow-md">
                    مساء الخير، أيها المخرج
                </h2>
                <p class="text-lg font-bold text-gray-200 mt-1 drop-shadow">
                    أي قصة سنصنع اليوم؟
                </p>
            </div>

            <!-- بطاقات مسارات العمل الزجاجية (Glassmorphism Cards) -->
            <div class="relative z-10 px-5 pt-7 grid grid-cols-2 gap-3.5">
                <!-- بطاقة: خطوة بخطوة -->
                <div class="group relative rounded-2xl bg-white/10 hover:bg-white/15 backdrop-blur-xl border border-white/15 p-4 flex flex-col justify-between h-[126px] transition cursor-pointer shadow-lg shadow-black/20">
                    <div>
                        <h3 class="text-base font-extrabold text-white">خطوة بخطوة</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">راجع كل خطوة</p>
                    </div>
                    <div class="self-end w-9 h-9 rounded-xl bg-blue-500/80 flex items-center justify-center text-white shadow-md shadow-blue-500/30">
                        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>
                        </svg>
                    </div>
                </div>

                <!-- بطاقة: سريع (Pro Only) -->
                <div class="group relative rounded-2xl bg-white/10 hover:bg-white/15 backdrop-blur-xl border border-white/15 p-4 flex flex-col justify-between h-[126px] transition cursor-pointer shadow-lg shadow-black/20">
                    <!-- شارة Pro -->
                    <div class="flex items-center justify-between">
                        <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-black/40 border border-white/10 text-[10px] text-gray-300 font-medium">
                            <svg class="w-2.5 h-2.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd"/>
                            </svg>
                            Pro only
                        </span>
                    </div>
                    <div>
                        <h3 class="text-base font-extrabold text-white">سريع</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5 leading-snug">إدخال واحد، فيديو كامل</p>
                    </div>
                    <div class="self-end w-9 h-9 rounded-xl bg-cyan-500/80 flex items-center justify-center text-white shadow-md shadow-cyan-500/30 -mt-2">
                        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/>
                        </svg>
                    </div>
                </div>
            </div>
        </div>

        <!-- قسم بطاقات الأفلام والإلهام -->
        <section class="px-5 pt-3 pb-24 flex-1 flex flex-col justify-center">
            <!-- شريط عنوان القسم -->
            <div class="flex items-center justify-between mb-3.5">
                <h3 class="text-lg font-extrabold text-white">إلهام بلوت كرافت</h3>
                <a href="#all" class="text-xs font-medium text-gray-400 hover:text-white flex items-center gap-0.5 transition">
                    <span>عرض الكل</span>
                    <svg class="w-3.5 h-3.5 rotate-180" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/>
                    </svg>
                </a>
            </div>

            <!-- قائمة الملصقات الأفقية القابلة للتمرير -->
            <div class="flex gap-3.5 overflow-x-auto no-scrollbar pb-1 pt-1 -mx-5 px-5">
                <!-- ملصق 1 -->
                <article class="flex-shrink-0 w-[140px] rounded-2xl overflow-hidden bg-gradient-to-b from-gray-800 to-[#141824] border border-white/10 group cursor-pointer shadow-lg hover:border-white/25 transition">
                    <div class="h-[185px] w-full relative overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80" alt="The Deliveryman's Secret Billionaire" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
                        <div class="absolute inset-0 bg-gradient-to-t from-[#141824] via-transparent to-black/40"></div>
                        <span class="absolute top-2 right-2 text-[9px] font-bold px-1.5 py-0.5 rounded bg-black/60 text-white/90">دراما</span>
                    </div>
                    <div class="p-2.5 text-center">
                        <p class="text-[11px] font-bold text-gray-200 line-clamp-1 leading-snug"> ...THE DELIVERYMAN'S SE </p>
                    </div>
                </article>

                <!-- ملصق 2 -->
                <article class="flex-shrink-0 w-[140px] rounded-2xl overflow-hidden bg-gradient-to-b from-gray-800 to-[#141824] border border-white/10 group cursor-pointer shadow-lg hover:border-white/25 transition">
                    <div class="h-[185px] w-full relative overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80" alt="The Wrong Door" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
                        <div class="absolute inset-0 bg-gradient-to-t from-[#141824] via-transparent to-black/40"></div>
                        <span class="absolute top-2 right-2 text-[9px] font-bold px-1.5 py-0.5 rounded bg-black/60 text-white/90">غموض</span>
                    </div>
                    <div class="p-2.5 text-center">
                        <p class="text-[11px] font-bold text-gray-200 line-clamp-1 leading-snug"> THE WRONG DOOR </p>
                    </div>
                </article>

                <!-- ملصق 3 -->
                <article class="flex-shrink-0 w-[140px] rounded-2xl overflow-hidden bg-gradient-to-b from-gray-800 to-[#141824] border border-white/10 group cursor-pointer shadow-lg hover:border-white/25 transition">
                    <div class="h-[185px] w-full relative overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1514533450685-4493e01d1fdc?auto=format&fit=crop&w=600&q=80" alt="Re: Invitation" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
                        <div class="absolute inset-0 bg-gradient-to-t from-[#141824] via-transparent to-black/40"></div>
                        <span class="absolute top-2 right-2 text-[9px] font-bold px-1.5 py-0.5 rounded bg-black/60 text-white/90">رعب</span>
                    </div>
                    <div class="p-2.5 text-center">
                        <p class="text-[11px] font-bold text-gray-200 line-clamp-1 leading-snug"> RE: INVITATION </p>
                    </div>
                </article>
            </div>
        </section>

        <!-- شريط الملاحة السفلي الزجاجي (Bottom Navigation Bar) -->
        <nav class="absolute bottom-3 left-4 right-4 bg-[#121622]/85 backdrop-blur-xl border border-white/15 rounded-full px-3 py-2 flex items-center justify-between z-30 shadow-2xl shadow-black/60">
            <!-- تبويب: الصفحة الرئيسية (نشط) -->
            <button class="flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/15 text-white text-xs font-bold transition shadow-sm">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/>
                </svg>
                <span>الصفحة الرئيسية</span>
            </button>
            <!-- تبويب: الأدوات -->
            <button class="flex items-center gap-1.5 px-3 py-1.5 text-gray-400 hover:text-white text-xs font-medium transition">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
                </svg>
                <span>الأدوات</span>
            </button>
            <!-- تبويب: الأعمال -->
            <button class="flex items-center gap-1.5 px-3 py-1.5 text-gray-400 hover:text-white text-xs font-medium transition">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"/>
                </svg>
                <span>الأعمال</span>
            </button>
            <!-- أيقونة الملف الشخصي -->
            <button class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center text-gray-300 hover:text-white transition">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
            </button>
        </nav>
    </main>
</body>
</html>
"""

# عرض الواجهة داخل Streamlit
st.components.v1.html(html_code, height=880, scrolling=True)
