import streamlit as st

st.set_page_config(
    page_title="منصة أرباح الفيديوهات",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منصة الأرباح</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background-color: #07090e; }
        .glass-box {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.02));
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .glass-nav {
            background: rgba(15, 18, 28, 0.85);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
    </style>
</head>
<body class="text-white flex justify-center items-center p-0 m-0 min-h-screen">

    <main class="w-full max-w-[420px] min-h-screen bg-[#090b10] relative shadow-2xl border border-white/10 flex flex-col justify-between p-5 pb-24">
        
        <!-- الهيدر الشخصي والأرباح -->
        <div>
            <div class="flex items-center justify-between mb-6">
                <div class="flex items-center gap-3">
                    <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-amber-500 to-yellow-300 flex items-center justify-center shadow-lg shadow-amber-500/20 text-black font-black text-lg">
                        غ
                    </div>
                    <div>
                        <h1 class="text-sm font-bold text-gray-400">مرحباً بك،</h1>
                        <h2 class="text-base font-black text-white">غسان رضا</h2>
                    </div>
                </div>
                <button class="px-3 py-1.5 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 text-xs font-bold flex items-center gap-1">
                    <span>🟢 متصل</span>
                </button>
            </div>

            <!-- بطاقة الأرباح الكبرى -->
            <div class="glass-box rounded-3xl p-5 mb-5 relative overflow-hidden">
                <div class="absolute -left-10 -bottom-10 w-32 h-32 bg-emerald-500/10 rounded-full blur-2xl"></div>
                <div class="flex justify-between items-start mb-2">
                    <span class="text-xs font-medium text-gray-400">إجمالي الأرباح القابلة للسحب</span>
                    <span class="text-[10px] bg-white/10 px-2 py-0.5 rounded-md text-emerald-400 font-bold">+24% هذا الأسبوع</span>
                </div>
                <div class="text-3xl font-black text-white mb-4 tracking-wider">
                    $1,480.<span class="text-emerald-400 text-xl">50</span>
                </div>
                <div class="grid grid-cols-2 gap-2 pt-3 border-t border-white/10">
                    <div>
                        <span class="text-[10px] text-gray-400 block">مشاهدات اليوم</span>
                        <span class="text-sm font-bold text-white">48.2 ألف</span>
                    </div>
                    <div>
                        <span class="text-[10px] text-gray-400 block">معدل الألف مشاهدة (RPM)</span>
                        <span class="text-sm font-bold text-amber-400">$4.20</span>
                    </div>
                </div>
            </div>

            <!-- رفع فيديو جديد -->
            <div class="glass-box rounded-2xl p-4 mb-5 border-dashed border-2 border-indigo-500/30 text-center cursor-pointer hover:border-indigo-500 transition">
                <div class="text-2xl mb-1">📤</div>
                <h3 class="text-sm font-bold text-white">رفع فيديو قصير جديد (Reels)</h3>
                <p class="text-[11px] text-gray-400 mt-0.5">ابدأ بنشر محتواك لتحقيق الأرباح فوراً</p>
            </div>

            <!-- الفيديوهات النشطة حالياً -->
            <h3 class="text-sm font-extrabold text-white mb-3 tracking-wide">أحدث فيديوهاتك المنشورة</h3>
            
            <div class="space-y-3">
                <!-- فيديو 1 -->
                <div class="glass-box rounded-2xl p-3 flex items-center justify-between">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-14 rounded-xl bg-gray-800 bg-cover bg-center border border-white/10" style="background-image: url('https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=200&q=80')"></div>
                        <div>
                            <h4 class="text-xs font-bold text-white">تحليل مباراة الكلاسيكو القادمة</h4>
                            <span class="text-[10px] text-gray-400">12.4 ألف مشاهدة • قبل ساعتين</span>
                        </div>
                    </div>
                    <span class="text-xs font-black text-emerald-400">+$18.50</span>
                </div>

                <!-- فيديو 2 -->
                <div class="glass-box rounded-2xl p-3 flex items-center justify-between">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-14 rounded-xl bg-gray-800 bg-cover bg-center border border-white/10" style="background-image: url('https://images.unsplash.com/photo-1514533450685-4493e01d1fdc?auto=format&fit=crop&w=200&q=80')"></div>
                        <div>
                            <h4 class="text-xs font-bold text-white">أسرار عملة Solana والـ Memecoins</h4>
                            <span class="text-[10px] text-gray-400">35.1 ألف مشاهدة • أمس</span>
                        </div>
                    </div>
                    <span class="text-xs font-black text-emerald-400">+$45.20</span>
                </div>
            </div>
        </div>

        <!-- شريط التنقل السفلي -->
        <nav class="absolute bottom-3 left-4 right-4 glass-nav rounded-full px-4 py-2.5 flex items-center justify-between z-30 shadow-2xl">
            <button class="text-gray-400 hover:text-white text-xs font-medium">الإعدادات</button>
            <button class="text-gray-400 hover:text-white text-xs font-medium">المحفظة</button>
            <button class="text-gray-400 hover:text-white text-xs font-medium">الأبحاث</button>
            <button class="px-4 py-1.5 rounded-full bg-gradient-to-r from-indigo-600 to-violet-600 text-white text-xs font-bold shadow-md">الرئيسية</button>
        </nav>

    </main>

</body>
</html>
"""

st.components.v1.html(html_code, height=800, scrolling=True)
