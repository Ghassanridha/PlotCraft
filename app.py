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
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background-color: #05070a; }
        .glass-box {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.02));
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        .glass-nav {
            background: rgba(18, 22, 33, 0.85);
            backdrop-filter: blur(30px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .hero-bg {
            background-image: linear-gradient(to bottom, rgba(5, 7, 10, 0.2), rgba(5, 7, 10, 0.95)), url('https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80');
        }
    </style>
</head>
<body class="text-white flex justify-center items-center p-0 m-0 min-h-screen">

    <main class="w-full max-w-[420px] min-h-screen bg-[#05070a] relative shadow-2xl border border-white/10 flex flex-col justify-between pb-28 overflow-hidden">
        
        <!-- قسم الهيدر والخلفية السينمائية -->
        <div class="hero-bg bg-cover bg-center p-5 pb-8 relative rounded-b-[35px]">
            <!-- شريط علوي -->
            <div class="flex items-center justify-between mb-8">
                <!-- الاسم فقط في اليمين بدون أي دوائر أو إيموجي -->
                <span class="font-black text-sm tracking-wide">بلوت كرافت</span>
                
                <!-- زر الترقية في اليسار -->
                <span class="px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md text-[11px] font-bold text-white border border-white/15 cursor-pointer">ترقية ✨</span>
            </div>

            <!-- التحية الترحيبية -->
            <div class="mb-6">
                <h1 class="text-xl font-black text-white leading-relaxed">مساء الخير، أيها المخرج</h1>
                <h2 class="text-xl font-black text-white">أي قصة سنصنع اليوم؟</h2>
            </div>

            <!-- خيارين (سريع وخطوة بخطوة) -->
            <div class="grid grid-cols-2 gap-3">
                <!-- سريع -->
                <div class="glass-box rounded-2xl p-3.5 relative cursor-pointer hover:border-indigo-500/50 transition">
                    <span class="absolute top-2 left-2 text-[9px] bg-black/40 px-2 py-0.5 rounded-full text-indigo-300 font-bold border border-white/10">Pro only</span>
                    <div class="text-lg mb-1">⚡</div>
                    <h3 class="text-xs font-bold text-white">سريع</h3>
                    <p class="text-[10px] text-gray-300 mt-0.5">إدخال واحد، فيديو كامل</p>
                </div>

                <!-- خطوة بخطوة -->
                <div class="glass-box rounded-2xl p-3.5 relative cursor-pointer hover:border-indigo-500/50 transition">
                    <div class="text-lg mb-1">💬</div>
                    <h3 class="text-xs font-bold text-white">خطوة بخطوة</h3>
                    <p class="text-[10px] text-gray-300 mt-0.5">راجع كل خطوة</p>
                </div>
            </div>
        </div>

        <!-- قسم إلهام بلوت كرافت (البوسترات) -->
        <div class="px-5 mt-2">
            <div class="flex items-center justify-between mb-3">
                <h3 class="text-sm font-extrabold text-white">إلهام بلوت كرافت</h3>
                <span class="text-xs text-indigo-400 font-bold cursor-pointer">عرض الكل ></span>
            </div>

            <!-- حاوية الأفقية للبوسترات -->
            <div class="flex gap-3 overflow-x-auto pb-2 scrollbar-none">
                <!-- بوستر 1 -->
                <div class="min-w-[130px] h-[190px] rounded-2xl bg-cover bg-center relative p-2.5 flex flex-col justify-end border border-white/10 shadow-lg" style="background-image: url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=300&q=80')">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-2xl"></div>
                    <span class="relative z-10 text-[10px] font-black text-white tracking-wider">THE WRONG DOOR</span>
                </div>

                <!-- بوستر 2 -->
                <div class="min-w-[130px] h-[190px] rounded-2xl bg-cover bg-center relative p-2.5 flex flex-col justify-end border border-white/10 shadow-lg" style="background-image: url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=300&q=80')">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-2xl"></div>
                    <span class="relative z-10 text-[9px] font-black text-white tracking-tight">THE DELIVERYMAN'S SECRET</span>
                </div>

                <!-- بوستر 3 -->
                <div class="min-w-[130px] h-[190px] rounded-2xl bg-cover bg-center relative p-2.5 flex flex-col justify-end border border-white/10 shadow-lg" style="background-image: url('https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=300&q=80')">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-2xl"></div>
                    <span class="relative z-10 text-[10px] font-black text-white tracking-wider">THE INVITATION</span>
                </div>
            </div>
        </div>

        <!-- شريط التنقل السفلي (Bottom Navigation) -->
        <nav class="absolute bottom-4 left-4 right-4 glass-nav rounded-full px-4 py-2.5 flex items-center justify-between z-30 shadow-2xl">
            <button class="flex items-center gap-1.5 px-4 py-2 rounded-full bg-white/15 text-white text-xs font-bold shadow-inner">
                <span>🏠</span>
                <span>الصفحة الرئيسية</span>
            </button>
            <button class="text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1">
                <span>🛠️</span>
                <span>الأدوات</span>
            </button>
            <button class="text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1">
                <span>💼</span>
                <span>الأعمال</span>
            </button>
            <button class="text-gray-400 hover:text-white text-xs font-medium">✨</button>
        </nav>

    </main>

</body>
</html>
"""

st.components.v1.html(html_code, height=760, scrolling=False)
