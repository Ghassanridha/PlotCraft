import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إزالة الهوامش الجانبية العلوية لستريمليت
st.markdown("""
    <style>
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
            overflow: hidden;
        }
        iframe {
            width: 100% !important;
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>بلوت كرافت</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; }
        body { 
            font-family: 'Tajawal', sans-serif; 
            background-color: #05070a; 
            margin: 0; 
            padding: 0;
            width: 100vw;
            overflow-x: hidden;
        }
        .glass-box {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.02));
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        .glass-nav {
            background: rgba(18, 22, 33, 0.95);
            backdrop-filter: blur(35px);
            border-top: 1px solid rgba(255, 255, 255, 0.12);
        }
        .hero-bg {
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(0, 0, 0, 0.95) 0%, rgba(192, 200, 215, 0.25) 35%, rgba(5, 7, 10, 0.9) 70%),
                url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=800&q=80');
            background-size: cover;
            background-position: center;
        }
        .screen { display: none; width: 100%; }
        .screen.active { display: flex; flex-direction: column; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="text-white w-full">

    <!-- أضفنا مسافة علوية (pt-4) هنا لكي يبتعد المحتوى عن شريط الـ Streamlit العلوي ولا يتم قص الاسم -->
    <main class="w-full bg-[#05070a] relative flex flex-col justify-between overflow-y-auto overflow-x-hidden no-scrollbar pb-24 pt-4">
        
        <div class="w-full px-3">
            <!-- الشاشة الرئيسية -->
            <div id="home-screen" class="screen active flex-col">
                <div class="hero-bg px-4 py-3.5 relative rounded-b-[25px] overflow-hidden shadow-xl">
                    
                    <div class="flex items-center justify-between mb-3 relative z-10">
                        <span class="font-black text-xs tracking-wide">بلوت كرافت</span>
                        <span class="px-3 py-1 rounded-full bg-white/10 backdrop-blur-md text-[10px] font-bold text-white border border-white/15">ترقية ✨</span>
                    </div>

                    <div class="mb-3 relative z-10">
                        <h1 class="text-sm font-black text-white leading-tight">مساء الخير، أيها المخرج</h1>
                        <h2 class="text-sm font-black text-white">أي قصة سنصنع اليوم؟</h2>
                    </div>

                    <div class="grid grid-cols-2 gap-2 relative z-10">
                        <div class="glass-box rounded-xl p-2.5 relative">
                            <span class="absolute top-1.5 left-1.5 text-[8px] bg-black/40 px-1.5 py-0.5 rounded-full text-indigo-300 font-bold">Pro</span>
                            <div class="text-sm mb-0.5">⚡</div>
                            <h3 class="text-[11px] font-bold text-white">سريع</h3>
                            <p class="text-[9px] text-gray-300">إدخال واحد، فيديو كامل</p>
                        </div>

                        <div class="glass-box rounded-xl p-2.5 relative">
                            <div class="text-sm mb-0.5">💬</div>
                            <h3 class="text-[11px] font-bold text-white">خطوة بخطوة</h3>
                            <p class="text-[9px] text-gray-300">راجع كل خطوة</p>
                        </div>
                    </div>
                </div>

                <div class="mt-3">
                    <div class="flex items-center justify-between mb-2">
                        <h3 class="text-xs font-extrabold text-white">إلهام بلوت كرافت</h3>
                        <span class="text-[10px] text-indigo-400 font-bold">عرض الكل ></span>
                    </div>

                    <div class="flex gap-3 overflow-x-auto pb-2 no-scrollbar">
                        <div class="min-w-[120px] h-[160px] rounded-xl bg-cover bg-center relative p-2 flex flex-col justify-end border border-white/10" style="background-image: url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=300&q=80')">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-xl"></div>
                            <span class="relative z-10 text-[9px] font-black text-white">THE WRONG DOOR</span>
                        </div>

                        <div class="min-w-[120px] h-[160px] rounded-xl bg-cover bg-center relative p-2 flex flex-col justify-end border border-white/10" style="background-image: url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=300&q=80')">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-xl"></div>
                            <span class="relative z-10 text-[9px] font-black text-white">THE DELIVERYMAN</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- شاشة الأدوات -->
            <div id="tools-screen" class="screen flex-col py-2">
                <div class="flex items-center justify-between mb-3">
                    <h1 class="text-xs font-black text-white">الأدوات</h1>
                    <span class="px-3 py-1 rounded-full bg-white/10 backdrop-blur-md text-[10px] font-bold text-white">ترقية ✨</span>
                </div>
                <div class="flex flex-col gap-2.5">
                    <div class="h-[90px] rounded-xl bg-cover bg-center relative p-3 flex flex-col justify-between border border-white/20" style="background-image: linear-gradient(to left, rgba(20,22,28,0.70) 40%, rgba(5,7,10,0.70) 100%), url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=500&q=80')">
                        <h3 class="text-xs font-black text-white">تأثيرات الفيديو</h3>
                    </div>
                </div>
            </div>

            <!-- شاشة الأعمال -->
            <div id="works-screen" class="screen flex-col py-2">
                <div class="flex items-center justify-end mb-3">
                    <span class="px-3 py-1 rounded-full bg-indigo-600/30 text-[10px] font-bold text-indigo-300">+ مشروع جديد</span>
                </div>
                <div class="flex flex-col items-center justify-center h-[200px] text-center">
                    <p class="text-[11px] text-gray-400">لا توجد أعمال بعد</p>
                </div>
            </div>
        </div>

        <!-- الشريط السفلي -->
        <nav class="fixed bottom-0 left-0 right-0 glass-nav px-3 py-2.5 flex items-center justify-between z-50 shadow-2xl">
            <button onclick="alert('المزيد قريباً')" class="text-gray-400 text-xs p-2">✨</button>
            <button id="btn-works" onclick="switchScreen('works')" class="text-gray-400 text-xs font-medium px-3 py-1 rounded-full">💼 الأعمال</button>
            <button id="btn-tools" onclick="switchScreen('tools')" class="text-gray-400 text-xs font-medium px-3 py-1 rounded-full">🛠 الأدوات</button>
            <button id="btn-home" onclick="switchScreen('home')" class="px-3 py-1 rounded-full bg-white/20 text-white text-xs font-bold">🏠 الرئيسية</button>
        </nav>

    </main>

    <script>
        function switchScreen(screenName) {
            document.getElementById('home-screen').classList.remove('active');
            document.getElementById('tools-screen').classList.remove('active');
            document.getElementById('works-screen').classList.remove('active');
            
            const defCls = "text-gray-400 text-xs font-medium px-3 py-1 rounded-full";
            const actCls = "px-3 py-1 rounded-full bg-white/20 text-white text-xs font-bold";
            
            document.getElementById('btn-home').className = defCls;
            document.getElementById('btn-tools').className = defCls;
            document.getElementById('btn-works').className = defCls;

            if (screenName === 'home') {
                document.getElementById('home-screen').classList.add('active');
                document.getElementById('btn-home').className = actCls;
            } else if (screenName === 'tools') {
                document.getElementById('tools-screen').classList.add('active');
                document.getElementById('btn-tools').className = actCls;
            } else if (screenName === 'works') {
                document.getElementById('works-screen').classList.add('active');
                document.getElementById('btn-works').className = actCls;
            }
        }
    </script>
</body>
</html>
"""

# أبقينا الارتفاع 680 مع العرض 100%، وتم حل مشكلة القص العلوي عبر الـ Padding الداخلي
st.components.v1.html(html_code, height=680, scrolling=True)
