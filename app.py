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
        .screen { display: none; }
        .screen.active { display: flex; flex-direction: column; }
    </style>
</head>
<body class="text-white flex justify-center items-center p-0 m-0 min-h-screen">

    <main class="w-full max-w-[420px] min-h-screen bg-[#05070a] relative shadow-2xl border border-white/10 flex flex-col justify-between pb-28 overflow-hidden">
        
        <!-- ================= شاشة الأدوات (مطابقة تماماً للصورة الأخيرة) ================= -->
        <div id="tools-screen" class="screen active flex-col p-5">
            <div class="flex items-center justify-between mb-5 mt-2">
                <h1 class="text-lg font-black text-white">الأدوات</h1>
                <span class="px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md text-[11px] font-bold text-white border border-white/15 cursor-pointer">ترقية ✨</span>
            </div>

            <div class="flex flex-col gap-4">
                
                <!-- 1. تأثيرات الفيديو (جهاز تحكم السوني الأبيض) -->
                <div class="h-[135px] rounded-2xl bg-cover bg-center relative p-4 flex flex-col justify-between border border-white/15 shadow-xl cursor-pointer" style="background-image: linear-gradient(to left, rgba(5,7,10,0.85) 40%, rgba(5,7,10,0.2) 100%), url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80')">
                    <div class="flex justify-end items-start z-10">
                        <span class="w-6 h-6 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center text-white text-xs border border-white/20">‹</span>
                    </div>
                    <div class="z-10 text-right">
                        <h3 class="text-sm font-black text-white">تأثيرات الفيديو</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">أضف لمسة سينمائية</p>
                    </div>
                </div>

                <!-- 2. توليد الفيديو (وجه رجل بدون يد - لقطة مقربة للوجه واللحية) -->
                <div class="h-[135px] rounded-2xl bg-cover bg-center relative p-4 flex flex-col justify-between border border-white/15 shadow-xl cursor-pointer" style="background-image: linear-gradient(to left, rgba(5,7,10,0.85) 40%, rgba(5,7,10,0.2) 100%), url('https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=600&q=80')">
                    <div class="flex justify-end items-start z-10">
                        <span class="w-6 h-6 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center text-white text-xs border border-white/20">‹</span>
                    </div>
                    <div class="z-10 text-right">
                        <h3 class="text-sm font-black text-white">توليد الفيديو</h3>
                        <p class="text-[11px] text-gray-300 mt-0.5">حول توجيهها إلى فيديو خاص بك</p>
                    </div>
                </div>

                <!-- 3. توليد الصور (وجه الفتاة بالإضاءة الزرقاء مع دائرة المعاينة والسهم في اليسار) -->
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

        <!-- ================= شريط التنقل السفلي الثابت ================= -->
        <nav class="absolute bottom-4 left-4 right-4 glass-nav rounded-full px-4 py-2.5 flex items-center justify-between z-30 shadow-2xl">
            <button onclick="alert('الصفحة الرئيسية')" class="text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1 px-2 py-2">
                <span>🏠</span>
                <span>الصفحة الرئيسية</span>
            </button>
            <button class="flex items-center gap-1.5 px-3.5 py-2 rounded-full bg-white/20 text-white text-xs font-bold shadow-inner">
                <span>🛠</span>
                <span>الأدوات</span>
            </button>
            <button onclick="alert('الأعمال قريباً')" class="text-gray-400 hover:text-white text-xs font-medium flex items-center gap-1">
                <span>💼</span>
                <span>الأعمال</span>
            </button>
            <button onclick="alert('المزيد قريباً')" class="text-gray-400 hover:text-white text-xs font-medium">✨</button>
        </nav>

    </main>

</body>
</html>
"""

st.components.v1.html(html_code, height=760, scrolling=False)
