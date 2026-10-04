import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إزالة الهوامش بالكامل ليتمدد التصميم بمرونة تامة على شاشة الموبايل
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            width: 100% !important;
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
            overflow-x: hidden;
        }
        .glass-box {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.02));
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        .glass-nav {
            background: rgba(18, 22, 33, 0.90);
            backdrop-filter: blur(30px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        
        /* الثقب الدودي الاحترافي */
        .wormhole-hero-bg {
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
<body class="text-white w-full min-h-screen flex justify-center">

    <!-- حاوية تتمدد بمرونة تامة لعرض الشاشة بالكامل بدون قص علوي -->
    <main class="w-full max-w-full bg-[#05070a] relative flex flex-col justify-between overflow-y-auto overflow-x-hidden no-scrollbar pb-28 pt-2">
        
        <div class="w-full">
            <!-- ================= الشاشة الأولى: الصفحة الرئيسية ================= -->
            <div id="home-screen" class="screen active flex-col">
                <div class="wormhole-hero-bg px-5 pt-4 pb-7 relative rounded-b-[35px] overflow-hidden shadow-2xl">
                    
                    <div class="flex items-center justify-between mb-4 relative z-10">
                        <span class="font-black text-sm tracking-wide">بلوت كرافت</span>
                        <span class="px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md text-[11px] font-bold text-white border border-white/15 cursor-pointer shadow-lg shadow-gray-500/10">ترقية ✨</span>
                    </div>

                    <div class="mb-4 relative z-10">
                        <h1 class="text-lg font-black text-white leading-relaxed">مساء الخير، أيها المخرج</h1>
                        <h2 class="text-lg font-black text-white">أي قصة سنصنع اليوم؟</h2>
                    </div>

                    <div class="grid grid-cols-2 gap-3 relative z-10">
                        <div class="glass-box rounded-2xl p-3.5 relative cursor-pointer hover:border-indigo-500/50 transition">
                            <span class="absolute top-2 left-2 text-[9px] bg-black/40 px-2 py-0.5 rounded-full text-indigo-300 font-bold border border-white/10">Pro only</span>
                            <div class="text-base mb-1">⚡</div>
                            <h3 class="text-xs font-bold text-white">سريع</h3>
                            <p class="text-[10px] text-gray-300 mt-0.5">إدخال واحد، فيديو كامل</p>
                        </div>

                        <div class="glass-box rounded-2xl p-3.5 relative cursor-pointer hover:border-indigo-500/50 transition">
                            <div class="text-base mb-1">💬</div>
                            <h3 class="text-xs font-bold text-white">خطوة بخطوة</h3>
                            <p class="text-[10px] text-gray-300 mt-0.5">راجع كل خطوة</p>
                        </div>
                    </div>
                </div>

                <div class="px-5 mt-4">
                    <div class="flex items-center justify-between mb-3">
                        <h3 class="text-sm font-extrabold text-white">إلهام بلوت كرافت</h3>
                        <span class="text-xs text-indigo-400 font-bold cursor-pointer">عرض الكل ></span>
                    </div>

                    <div class="flex gap-3 overflow-x-auto pb-3 no-scrollbar">
                        <div class="min-w-[130px] h-[180px] rounded-2xl bg-cover bg-center relative p-2.5 flex flex-col justify-end border border-white/10 shadow-lg" style="background-image: url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=300&q=80')">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-2xl"></div>
                            <span class="relative z-10 text-[10px] font-black text-white tracking-wider">THE WRONG DOOR</span>
                        </div>

                        <div class="min-w-[130px] h-[180px] rounded-2xl bg-cover bg-center relative p-2.5 flex flex-col justify-end border border-white/10 shadow-lg" style="background-image: url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=300&q=80')">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-2xl"></div>
                            <span class="relative z-10 text-[9px] font-black text-white tracking-tight">THE DELIVERYMAN'S SECRET</span>
                        </div>

                        <div class="min-w-[130px] h-[180px] rounded-2xl bg-cover bg-center relative p-2.5 flex flex-col justify-end border border-white/10 shadow-lg" style="background-image: url('https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=300&q=80')">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-2xl"></div>
                            <span class="relative z-10 text-[10px] font-black text-white tracking-wider">THE INVITATION</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= الشاشة الثانية: الأدوات ================= -->
            <div id="tools-screen" class="screen flex-col p-5">
                <div class="flex items-center justify-between mb-4 mt-2">
                    <h1 class="text-base font-black text-white">الأدوات</h1>
                    <span class="px-3 py-1 rounded-full bg-white/10 backdrop-blur-md text-[11px] font-bold text-white border border-white/15 cursor-pointer">ترقية ✨</span>
                </div>

                <div class="flex flex-col gap-3.5">
                    <div class="h-[120px] rounded-2xl bg-cover bg-center relative p-4 flex flex-col justify-between border border-white/25 shadow-xl cursor-pointer" style="background-image: linear-gradient(to left, rgba(20,22,28,0.70) 40%, rgba(5,7,10,0.70) 100%), url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=600&q=80')">
                        <div class="flex justify-end items-start z-10">
                            <span class="w-6 h-6 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center text-white text-xs border border-white/20">‹</span>
                        </div>
                        <div class="z-10 text-right">
                            <h3 class="text-xs font-black text-white">تأثيرات الفيديو</h3>
                            <p class="text-[10px] text-gray-300 mt-0.5">أضف لمسة سينمائية</p>
                        </div>
                    </div>

                    <div class="h-[120px] rounded-2xl bg-cover bg-center relative p-4 flex flex-col justify-between border border-white/15 shadow-xl cursor-pointer" style="background-image: linear-gradient(to left, rgba(5,7,10,0.85) 40%, rgba(5,7,10,0.2) 100%), url('https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=600&q=80')">
                        <div class="flex justify-end items-start z-10">
                            <span class="w-6 h-6 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center text-white text-xs border border-white/20">‹</span>
                        </div>
                        <div class="z-10 text-right">
                            <h3 class="text-xs font-black text-white">توليد الفيديو</h3>
                            <p class="text-[10px] text-gray-300 mt-0.5">حول توجيهها إلى فيديو خاص بك</p>
                        </div>
                    </div>

                    <div class="h-[120px] rounded-2xl bg-cover bg-center relative p-4 flex flex-col justify-between border border-white/15 shadow-xl cursor-pointer" style="background-image: linear-gradient(to right, rgba(5,7,10,0.85) 40%, rgba(5,7,10,0.2) 100%), url('https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80')">
                        <div class="flex justify-between items-start z-10">
                            <span class="w-6 h-6 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center text-white text-xs border border-white/20">‹</span>
                            <div class="flex items-center gap-1 bg-black/50 backdrop-blur-md px-2 py-0.5 rounded-full border border-white/20">
                                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=100&q=80" class="w-5 h-5 rounded-full object-cover">
                                <span class="text-[9px] text-white font-bold">✨</span>
                            </div>
                        </div>
                        <div class="z-10 text-right">
                            <h3 class="text-xs font-black text-white">توليد الصور</h3>
                            <p class="text-[10px] text-gray-300 mt-0.5">حول فكرة إلى صورة مكتملة</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= الشاشة الثالثة: الأعمال ================= -->
            <div id="works-screen" class="screen flex-col p-5">
                <div class="flex items-center justify-end mb-4 mt-2">
                    <span class="px-3.5 py-1.5 rounded-full bg-indigo-600/30 backdrop-blur-md text-[11px] font-bold text-indigo-300 border border-indigo-500/30 cursor-pointer">+ مشروع جديد</span>
                </div>

                <div class="flex flex-col items-center justify-center h-[300px] text-center px-4">
                    <div class="w-14 h-14 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-xl mb-3">🎬</div>
                    <h3 class="text-xs font-bold text-white mb-1">لا توجد أعمال بعد</h3>
                    <p class="text-[10px] text-gray-400">ابدأ بإنشاء مشروعك السينمائي الأول وسيظهر هنا</p>
                </div>
            </div>
        </div>

        <!-- ================= شريط التنقل السفلي الثابت ================= -->
        <nav class="fixed bottom-3 left-3 right-3 max-w-md mx-auto glass-nav rounded-full px-4 py-2 flex items-center justify-between z-50 shadow-2xl">
            <button onclick="alert('المزيد قريباً')" class="text-gray-400 hover:text-white text-xs font-medium p-2">✨</button>
            <button id="btn-works" onclick="switchScreen('works')" class="text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1 px-3 py-1.5 rounded-full transition">
                <span>💼</span>
                <span>الأعمال</span>
            </button>
            <button id="btn-tools" onclick="switchScreen('tools')" class="text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1 px-3 py-1.5 rounded-full transition">
                <span>🛠</span>
                <span>الأدوات</span>
            </button>
            <button id="btn-home" onclick="switchScreen('home')" class="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white/20 text-white text-xs font-bold shadow-inner transition">
                <span>🏠</span>
                <span>الرئيسية</span>
            </button>
        </nav>

    </main>

    <script>
        function switchScreen(screenName) {
            const homeScreen = document.getElementById('home-screen');
            const toolsScreen = document.getElementById('tools-screen');
            const worksScreen = document.getElementById('works-screen');
            
            const btnHome = document.getElementById('btn-home');
            const btnTools = document.getElementById('btn-tools');
            const btnWorks = document.getElementById('btn-works');
            
            homeScreen.classList.remove('active');
            toolsScreen.classList.remove('active');
            worksScreen.classList.remove('active');
            
            const inactiveClass = "text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1 px-3 py-1.5 rounded-full transition";
            const activeClass = "flex items-center gap-1 px-3 py-1.5 rounded-full bg-white/20 text-white text-xs font-bold shadow-inner transition";
            
            btnHome.className = inactiveClass;
            btnTools.className = inactiveClass;
            btnWorks.className = inactiveClass;

            window.scrollTo({ top: 0, behavior: 'smooth' });

            if (screenName === 'home') {
                homeScreen.classList.add('active');
                btnHome.className = activeClass;
            } else if (screenName === 'tools') {
                toolsScreen.classList.add('active');
                btnTools.className = activeClass;
            } else if (screenName === 'works') {
                worksScreen.classList.add('active');
                btnWorks.className = activeClass;
            }
        }
    </script>

</body>
</html>
"""

# ضبطنا الارتفاع على 700 مع تمديد العرض بالكامل (`layout="wide"`) لتظهر الواجهة من البداية بدون قص نهائي
st.components.v1.html(html_code, height=700, scrolling=True)
