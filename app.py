<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Video Generator Mobile UI</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
        body {
            font-family: 'Cairo', sans-serif;
            background-color: #0f1015;
            color: #ffffff;
        }
        /* تأثير الضغط الزر */
        .btn-press:active {
            transform: scale(0.95);
            opacity: 0.9;
        }
    </style>
</head>
<body class="flex justify-center items-center min-h-screen bg-[#090a0f] p-0 sm:p-4">

    <!-- إطار حاوية الجوال -->
    <div class="w-full max-w-[420px] h-[850px] bg-[#121318] rounded-none sm:rounded-[40px] shadow-2xl flex flex-col justify-between relative overflow-hidden border border-[#22232a]">
        
        <!-- الجزء العلوي: الحالة والترقية -->
        <div class="px-5 pt-4 pb-2 flex justify-between items-center z-10">
            <span class="text-xs text-gray-400 font-medium">12:23</span>
            <button class="bg-[#1c1d24] text-white text-xs px-3 py-1.5 rounded-full flex items-center gap-1.5 border border-[#2d2e38] btn-press">
                <span>✨</span> تَرْقِيَة
            </button>
        </div>

        <!-- العنوان الرئيسي -->
        <div class="px-6 py-2 z-10">
            <h1 class="text-2xl font-bold tracking-wide">الأدوات</h1>
        </div>

        <!-- محتوى البطاقات (الأدوات) -->
        <div class="flex-1 overflow-y-auto px-4 space-y-4 py-2 pb-24">
            
            <!-- البطاقة الأولى: تأثيرات الفيديو -->
            <div class="relative h-[160px] rounded-2xl overflow-hidden shadow-lg border border-white/10 group cursor-pointer btn-press">
                <img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=600&auto=format&fit=crop" alt="تأثيرات الفيديو" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent p-4 flex flex-col justify-end">
                    <h3 class="text-lg font-bold text-white">تأثيرات الفيديو</h3>
                    <p class="text-xs text-gray-300">أضف لمسة سينمائية</p>
                </div>
                <div class="absolute top-4 left-4 text-white/70 text-sm">›</div>
            </div>

            <!-- البطاقة الثانية: توليد الفيديو -->
            <div class="relative h-[160px] rounded-2xl overflow-hidden shadow-lg border border-white/10 group cursor-pointer btn-press">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=600&auto=format&fit=crop" alt="توليد الفيديو" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent p-4 flex flex-col justify-end">
                    <h3 class="text-lg font-bold text-white">توليد الفيديو</h3>
                    <p class="text-xs text-gray-300">حول توجيهك إلى فيديو خاص بك</p>
                </div>
                <div class="absolute top-4 left-4 text-white/70 text-sm">›</div>
            </div>

            <!-- البطاقة الثالثة: توليد الصور -->
            <div class="relative h-[160px] rounded-2xl overflow-hidden shadow-lg border border-white/10 group cursor-pointer btn-press">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=600&auto=format&fit=crop" alt="توليد الصور" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent p-4 flex flex-col justify-end">
                    <h3 class="text-lg font-bold text-white">توليد الصور</h3>
                    <p class="text-xs text-gray-300">حول فكرة إلى صورة مكتملة</p>
                </div>
                <!-- أيقونة الصورة الصغيرة الدائرية المطابقة للصورة -->
                <div class="absolute bottom-4 left-4 flex items-center gap-2">
                    <div class="w-10 h-10 rounded-full border-2 border-white/80 overflow-hidden shadow-md">
                        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=150&auto=format&fit=crop" class="w-full h-full object-cover">
                    </div>
                </div>
                <div class="absolute top-4 left-4 text-white/70 text-sm">›</div>
            </div>

        </div>

        <!-- القالب المستطيل الموحد للسفل مع الزر المنفصل -->
        <div class="absolute bottom-4 left-4 right-4 z-20">
            <div class="bg-[#16171d]/95 backdrop-blur-md border border-[#2a2b36] rounded-full p-2 flex items-center justify-between shadow-2xl">
                
                <!-- زر الصفحة الرئيسية (غير فعال) -->
                <button class="flex-1 py-2.5 flex items-center justify-center gap-2 text-gray-400 text-xs font-semibold rounded-full btn-press transition-all">
                    <span>🏠</span>
                    <span>الصفحة الر...</span>
                </button>

                <!-- زر الأعمال (غير فعال) -->
                <button class="flex-1 py-2.5 flex items-center justify-center gap-2 text-gray-400 text-xs font-semibold rounded-full btn-press transition-all">
                    <span>📁</span>
                    <span>الأعمال</span>
                </button>

                <!-- زر الأدوات (الزر المنفصل الفعال بلون أبيض وأسود داكن عند الضغط) -->
                <button class="flex-1 py-2.5 flex items-center justify-center gap-2 bg-white text-[#121318] text-xs font-bold rounded-full shadow-lg btn-press transition-all">
                    <span>✨</span>
                    <span>الأدوات</span>
                </button>

            </div>
        </div>

        <!-- شريط الإيماءة السفلي للجوال -->
        <div class="absolute bottom-1 left-1/2 -translate-x-1/2 w-32 h-1 bg-white/40 rounded-full z-30"></div>

    </div>

</body>
</html>
