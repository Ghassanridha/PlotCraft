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
            background-image: linear-gradient(to bottom, rgba(5, 7, 10, 0.2), rgba(5, 7, 10, 0.95)), url('https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=800&q=80');
        }
        .screen { display: none; }
        .screen.active { display: flex; flex-direction: column; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="text-white flex justify-center items-center p-0 m-0 min-h-screen">

    <main class="w-full max-w-[420px] min-h-screen bg-[#05070a] relative shadow-2xl border border-white/10 flex flex-col justify-between pb-28 overflow-hidden">
        
        <!-- ================= الشاشة الأولى: الصفحة الرئيسية ================= -->
        <div id="home-screen" class="screen flex-col">
            <div class="hero-bg bg-cover bg-center p-5 pb-8 relative rounded-b-[35px]">
                <div class="flex items-center justify-between mb-8">
                    <span class="font-black text-sm tracking-wide">بلوت كرافت</span>
                    <span class="px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md text-[11px] font-bold text-white border border-white/15 cursor-pointer">ترقية ✨</span>
                </div>

                <div class="mb-6">
                    <h1 class="text-xl font-black text-white leading-relaxed">مساء الخير، أيها المخرج</h1>
                    <h2 class="text-xl font-black text-white">أي قصة سنصنع اليوم؟</h2>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div class="glass-box rounded-2xl p-3.5 relative cursor-pointer hover:border-indigo-500/50 transition">
                        <span class="absolute top-2 left-2 text-[9px] bg-black/40 px-2 py-0.5 rounded-full text-indigo-300 font-bold border border-white/10">Pro only</span>
                        <div class="text-lg mb-1">⚡</div>
                        <h3 class="text-xs font-bold text-white">سريع</h3>
                        <p class="text-[10px] text-gray-300 mt-0.5">إدخال واحد، فيديو كامل</p>
                    </div>

                    <div class="glass-box rounded-2xl p-3.5 relative cursor-pointer hover:border-indigo-500/50 transition">
                        <div class="text-lg mb-1">💬</div>
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

                <div class="flex gap-3 overflow-x-auto pb-2 no-scrollbar">
                    <div class="min-w-[130px] h-[190px] rounded-2xl bg-cover bg-center relative p-2.5 flex flex-col justify-end border border-white/10 shadow-lg" style="background-image: url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=300&q=80')">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-2xl"></div>
                        <span class="relative z-10 text-[10px] font-black text-white tracking-wider">THE WRONG DOOR</span>
                    </div>

                    <div class="min-w-[130px] h-[190px] rounded-2xl bg-cover bg-center relative p-2.5 flex flex-col justify-end border border-white/10 shadow-lg" style="background-image: url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=300&q=80')">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-2xl"></div>
                        <span class="relative z-10 text-[9px] font-black text-white tracking-tight">THE DELIVERYMAN'S SECRET</span>
                    </div>

                    <div class="min-w-[130px] h-[190px] rounded-2xl bg-cover bg-center relative p-2.5 flex flex-col justify-end border border-white/10 shadow-lg" style="background-image: url('https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=300&q=80')">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent rounded-2xl"></div>
                        <span class="relative z-10 text-[10px] font-black text-white tracking-wider">THE INVITATION</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= الشاشة الثانية: الأدوات ================= -->
        <div id="tools-screen" class="screen flex-col p-5">
            <div class="flex items-center justify-between mb-5 mt-2">
                <h1 class="text-lg font-black text-white">الأدوات</h1>
                <span class="px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md text-[11px] font-bold text-white border border-white/15 cursor-pointer">ترقية ✨</span>
            </div>

            <div class="flex flex-col gap-4">
                
                <!-- 1. تأثيرات الفيديو (تم تحديثها لتكون صورة ثقب دودي فضائي حقيقي بسماء سوداء ونجوم وتدرج فضي بنسبة 70%) -->
                <div class="h-[135px] rounded-2xl bg-cover bg-center relative p-4 flex flex-col justify-between border border-white/25 shadow-2xl cursor-pointer" style="background-image: linear-gradient(to left, rgba(20,22,28,0.70) 40%, rgba(5,7,10,0.70) 100%), url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=600&q=80')">
                    <div class="flex justify-end items-start z-10">
                        <span class="w-6 h-6 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center text-white text-xs border border-white/20">‹</span>
                    </div>
                    <div class="z-10 text-right">
                        <h3 class="text-sm font-black text-white">تأثيرات الفيديو</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">أضف لمسة سينمائية</p>
                    </div>
                </div>

                <!-- 2. توليد الفيديو -->
                <div class="h-[135px] rounded-2xl bg-cover bg-center relative p-4 flex flex-col justify-between border border-white/15 shadow-xl cursor-pointer" style="background-image: linear-gradient(to left, rgba(5,7,10,0.85) 40%, rgba(5,7,10,0.2) 100%), url('https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=600&q=80')">
                    <div class="flex justify-end items-start z-10">
                        <span class="w-6 h-6 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center text-white text-xs border border-white/20">‹</span>
                    </div>
                    <div class="z-10 text-right">
                        <h3 class="text-sm font-black text-white">توليد الفيديو</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">حول توجيهها إلى فيديو خاص بك</p>
                    </div>
                </div>

                <!-- 3. توليد الصور -->
                <div class="h-[135px] rounded-2xl bg-cover bg-center relative p-4 flex flex-col justify-between border border-white/15 shadow-xl cursor-pointer" style="background-image: linear-gradient(to right, rgba(5,7,10,0.85) 40%, rgba(5,7,10,0.2) 100%), url('https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80')">
                    <div class="flex justify-between items-start z-10">
                        <span class="w-6 h-6 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center text-white text-xs border border-white/20">‹</span>
                        <div class="flex items-center gap-1.5 bg-black/50 backdrop-blur-md px-2 py-1 rounded-full border border-white/20">
                            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=100&q=80" class="w-6 h-6 rounded-full object-cover">
                            <span class="text-[10px] text-white font-bold">✨</span>
                        </div>
                    </div>
                    <div class="z-10 text-right">
                        <h3 class="text-sm font-black text-white">توليد الصور</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">حول فكرة إلى صورة مكتملة</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= الشاشة الثالثة: الأعمال (فارغة نظيفة) ================= -->
        <div id="works-screen" class="screen flex-col p-5">
            <div class="flex items-center justify-end mb-6 mt-2">
                <span class="px-3.5 py-1.5 rounded-full bg-indigo-600/30 backdrop-blur-md text-[11px] font-bold text-indigo-300 border border-indigo-500/30 cursor-pointer">+ مشروع جديد</span>
            </div>

            <div class="flex flex-col items-center justify-center h-[350px] text-center px-4">
                <div class="w-16 h-16 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-2xl mb-3">🎬</div>
                <h3 class="text-sm font-bold text-white mb-1">لا توجد أعمال بعد</h3>
                <p class="text-[11px] text-gray-400">ابدأ بإنشاء مشروعك السينمائي الأول وسيظهر هنا</p>
            </div>
        </div>

        <!-- ================= شريط التنقل السفلي الفعّال ================= -->
        <nav class="absolute bottom-4 left-4 right-4 glass-nav rounded-full px-4 py-2 flex items-center justify-between z-30 shadow-2xl">
            <button id="btn-home" onclick="switchScreen('home')" class="text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1 px-3 py-2 rounded-full transition">
                <span>🏠</span>
                <span>الرئيسية</span>
            </button>
            <button id="btn-tools" onclick="switchScreen('tools')" class="text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1 px-3 py-2 rounded-full transition">
                <span>🛠</span>
                <span>الأدوات</span>
            </button>
            <button id="btn-works" onclick="switchScreen('works')" class="flex items-center gap-1.5 px-3.5 py-2 rounded-full bg-white/20 text-white text-xs font-bold shadow-inner transition">
                <span>💼</span>
                <span>الأعمال</span>
            </button>
            <button onclick="alert('المزيد قريباً')" class="text-gray-400 hover:text-white text-xs font-medium p-2">✨</button>
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
            
            const inactiveClass = "text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1 px-3 py-2 rounded-full transition";
            const activeClass = "flex items-center gap-1.5 px-3.5 py-2 rounded-full bg-white/20 text-white text-xs font-bold shadow-inner transition";
            
            btnHome.className = inactiveClass;
            btnTools.className = inactiveClass;
            btnWorks.className = inactiveClass;

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

st.components.v1.html(html_code, height=760, scrolling=False)
