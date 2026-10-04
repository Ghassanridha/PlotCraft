import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
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
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background-color: #07090e; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        .glass-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.04));
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        .glass-nav {
            background: rgba(15, 18, 28, 0.82);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
    </style>
</head>
<body class="text-white flex justify-center items-center p-0 m-0 min-h-screen">

    <main class="w-full max-w-[420px] min-h-screen bg-[#090b10] relative shadow-2xl border border-white/10 flex flex-col justify-between overflow-x-hidden">
        
        <!-- قسم الخلفية السينمائية العلوية -->
        <div class="relative w-full h-[410px] overflow-hidden flex-shrink-0">
            <!-- صورة الخلفية السينمائية -->
            <img src="https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1200&q=80" alt="Cinematic Background" class="absolute inset-0 w-full h-full object-cover object-top opacity-55 scale-105" />
            
            <!-- تدرجات الإضاءة والظل الدمجي -->
            <div class="absolute inset-0 bg-gradient-to-b from-[#090b10]/80 via-[#090b10]/40 to-[#090b10]"></div>
            <div class="absolute top-10 left-1/3 w-56 h-56 bg-indigo-600/20 rounded-full blur-3xl pointer-events-none"></div>
            <div class="absolute top-20 right-4 w-48 h-48 bg-blue-500/15 rounded-full blur-3xl pointer-events-none"></div>

            <!-- الشريط العلوي (الهيدر الاحترافي) -->
            <header class="relative z-10 px-5 pt-8 pb-3 flex items-center justify-between">
                <!-- زر الترقية الأنيق -->
                <button class="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full glass-card text-xs font-bold text-white hover:bg-white/20 transition duration-300 shadow-lg">
                    <span class="text-amber-400 text-sm">👑</span>
                    <span>ترقية</span>
                </button>

                <!-- اسم الشعار والعنوان -->
                <div class="flex items-center gap-2.5">
                    <h1 class="text-lg font-black tracking-wide text-white drop-shadow-md">بلوت كرافت</h1>
                    <div class="w-8 h-8 rounded-full border border-white/20 bg-black/50 flex items-center justify-center backdrop-blur-md shadow-inner">
                        <span class="text-xs">🎬</span>
                    </div>
                </div>
            </header>

            <!-- النص الترحيبي السينمائي -->
            <div class="relative z-10 px-6 pt-3 text-right">
                <h2 class="text-[25px] font-black leading-tight text-white drop-shadow">مساء الخير، أيها المخرج</h2>
                <p class="text-[17px] font-bold text-gray-200 mt-0.5 drop-shadow-sm">أي قصة سنصنع اليوم؟</p>
            </div>

            <!-- بطاقات المسارات التفاعلية (سريع يسار، خطوة بخطوة يمين) -->
            <div class="relative z-10 px-5 pt-5 grid grid-cols-2 gap-3.5">
                
                <!-- بطاقة سريع (Pro Only) - الجهة اليسرى -->
                <div class="glass-card rounded-2xl p-4 flex flex-col justify-between h-[130px] relative hover:border-white/30 transition duration-300 cursor-pointer shadow-xl group">
                    <div class="flex items-center justify-start">
                        <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-black/50 border border-white/10 text-[10px] text-gray-300 font-medium">
                            <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span>
                            Pro only
                        </span>
                    </div>
                    <div>
                        <h3 class="text-base font-extrabold text-white group-hover:text-cyan-300 transition">سريع</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5 leading-snug">إدخال واحد، فيديو كامل</p>
                    </div>
                    <div class="self-end w-8 h-8 rounded-xl bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center text-white shadow-lg shadow-cyan-500/30">
                        ⚡
                    </div>
                </div>

                <!-- بطاقة خطوة بخطوة - الجهة اليمنى -->
                <div class="glass-card rounded-2xl p-4 flex flex-col justify-between h-[130px] hover:border-white/30 transition duration-300 cursor-pointer shadow-xl group">
                    <div class="h-4"></div>
                    <div>
                        <h3 class="text-base font-extrabold text-white group-hover:text-blue-300 transition">خطوة بخطوة</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">راجع كل خطوة</p>
                    </div>
                    <div class="self-end w-8 h-8 rounded-xl bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center text-white shadow-lg shadow-blue-600/30">
                        📁
                    </div>
                </div>

            </div>
        </div>

        <!-- معرض الإلهام (PlotCraft Inspiration) -->
        <section class="px-5 pt-3 pb-24 flex-1">
            <div class="flex items-center justify-between mb-3.5">
                <a href="#all" class="text-xs font-semibold text-gray-400 hover:text-white transition flex items-center gap-1">
                    <span>عرض الكل</span>
                    <span class="text-[10px]">‹</span>
                </a>
                <h3 class="text-lg font-extrabold text-white tracking-wide">إلهام بلوت كرافت</h3>
            </div>

            <!-- بطاقات بوسترات الأفلام الأفقية -->
            <div class="flex gap-3.5 overflow-x-auto no-scrollbar pb-2 pt-1">
                
                <!-- بوستر 1 -->
                <div class="flex-shrink-0 w-[132px] rounded-2xl overflow-hidden bg-[#11141d] border border-white/10 group cursor-pointer shadow-lg hover:border-white/25 transition duration-300">
                    <div class="h-[175px] w-full relative overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1514533450685-4493e01d1fdc?auto=format&fit=crop&w=600&q=80" alt="Poster" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" />
                        <div class="absolute inset-0 bg-gradient-to-t from-[#11141d] via-transparent to-black/40"></div>
                        <span class="absolute top-2 right-2 text-[9px] font-bold px-2 py-0.5 rounded-full bg-black/60 backdrop-blur-md text-white/90 border border-white/10">رعب</span>
                    </div>
                    <div class="p-2.5 text-center">
                        <p class="text-[10px] font-bold text-gray-200 truncate">RE: INVITATION</p>
                    </div>
                </div>

                <!-- بوستر 2 -->
                <div class="flex-shrink-0 w-[132px] rounded-2xl overflow-hidden bg-[#11141d] border border-white/10 group cursor-pointer shadow-lg hover:border-white/25 transition duration-300">
                    <div class="h-[175px] w-full relative overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80" alt="Poster" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" />
                        <div class="absolute inset-0 bg-gradient-to-t from-[#11141d] via-transparent to-black/40"></div>
                        <span class="absolute top-2 right-2 text-[9px] font-bold px-2 py-0.5 rounded-full bg-black/60 backdrop-blur-md text-white/90 border border-white/10">غموض</span>
                    </div>
                    <div class="p-2.5 text-center">
                        <p class="text-[10px] font-bold text-gray-200 truncate">THE WRONG DOOR</p>
                    </div>
                </div>

                <!-- بوستر 3 -->
                <div class="flex-shrink-0 w-[132px] rounded-2xl overflow-hidden bg-[#11141d] border border-white/10 group cursor-pointer shadow-lg hover:border-white/25 transition duration-300">
                    <div class="h-[175px] w-full relative overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80" alt="Poster" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" />
                        <div class="absolute inset-0 bg-gradient-to-t from-[#11141d] via-transparent to-black/40"></div>
                        <span class="absolute top-2 right-2 text-[9px] font-bold px-2 py-0.5 rounded-full bg-black/60 backdrop-blur-md text-white/90 border border-white/10">دراما</span>
                    </div>
                    <div class="p-2.5 text-center">
                        <p class="text-[10px] font-bold text-gray-200 truncate">DELIVERYMAN'S SECRET</p>
                    </div>
                </div>

            </div>
        </section>

        <!-- شريط التنقل السفلي العائم الاحترافي (Floating Glass Navigation) -->
        <nav class="absolute bottom-3 left-4 right-4 glass-nav rounded-full px-3 py-2 flex items-center justify-between z-30 shadow-2xl">
            <!-- الملف الشخصي -->
            <button class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center text-gray-300 transition">
                <span class="text-xs">👤</span>
            </button>
            <!-- الأعمال -->
            <button class="text-gray-400 hover:text-white text-xs font-medium px-2 py-1 transition">
                الأعمال
            </button>
            <!-- الأدوات -->
            <button class="text-gray-400 hover:text-white text-xs font-medium px-2 py-1 transition">
                الأدوات
            </button>
            <!-- الصفحة الرئيسية (النشطة) -->
            <button class="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white/20 text-white text-xs font-bold shadow-md border border-white/10">
                <span>الصفحة الرئيسية</span>
                <span class="text-xs">🏠</span>
            </button>
        </nav>

    </main>

</body>
</html>
"""

st.components.v1.html(html_code, height=880, scrolling=True)
