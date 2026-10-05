<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بلوت كرافت</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Tahoma, sans-serif;
        }
        body {
            background-color: #0b0f19;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            width: 100%;
            max-width: 400px;
            background-color: #0b0f19;
            padding: 20px;
            border-radius: 12px;
            position: relative;
            min-height: 700px;
        }
        
        /* إخفاء وإظهار الشاشات */
        .screen {
            display: none;
        }
        .screen.active {
            display: block;
        }

        /* تنسيق الشاشة الرئيسية (الصورة الثانية) */
        .main-header {
            text-align: right;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .welcome-box {
            background: linear-gradient(135deg, rgba(30,30,45,0.6), rgba(15,15,25,0.8));
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            text-align: right;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .welcome-box p {
            font-size: 16px;
            line-height: 1.6;
            color: #e2e8f0;
        }
        .modes-container {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
        }
        .mode-card {
            flex: 1;
            background-color: #161b26;
            border: 1px solid #2a3447;
            border-radius: 12px;
            padding: 20px 15px;
            text-align: right;
            cursor: pointer;
            transition: 0.2s;
        }
        .mode-card:hover {
            border-color: #ff2a85;
        }
        .mode-card .icon {
            font-size: 24px;
            margin-bottom: 10px;
            display: block;
        }
        .mode-card h3 {
            font-size: 15px;
            margin-bottom: 5px;
        }
        .mode-card p {
            font-size: 11px;
            color: #94a3b8;
        }

        /* تنسيق شاشة الخطوات والإعدادات (الصورة الأولى) */
        .sub-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .back-arrow {
            font-size: 22px;
            cursor: pointer;
            color: #fff;
        }
        
        /* صندوق مساعد AI */
        .ai-box {
            background-color: #1a1625;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 20px;
            position: relative;
            border: 1px solid rgba(255,42,133,0.2);
        }
        .ai-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .ai-title {
            color: #ff2a85;
            font-size: 14px;
            font-weight: bold;
        }
        .ai-icon-container {
            position: relative;
            cursor: pointer;
        }
        .ai-icon {
            width: 35px;
            height: 35px;
            background: linear-gradient(135deg, #ff2a85, #7928ca);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: #fff;
            font-size: 12px;
        }
        
        /* القائمة المنسدلة عند الضغط على أيقونة المساعد */
        .dropdown-menu {
            display: none;
            position: absolute;
            top: 45px;
            left: 0;
            background-color: #221e33;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
            width: 170px;
            z-index: 10;
            border: 1px solid #332b4d;
        }
        .dropdown-menu.show {
            display: block;
        }
        .dropdown-item {
            padding: 10px 15px;
            font-size: 13px;
            color: #fff;
            border-bottom: 1px solid #2d2642;
            cursor: pointer;
        }
        .dropdown-item:last-child {
            border-bottom: none;
        }
        .dropdown-item:hover {
            background-color: #ff2a85;
        }
        .ai-desc {
            font-size: 13px;
            line-height: 1.5;
            color: #cbd5e1;
        }

        /* صندوق إعداد القصة */
        .setup-box {
            background-color: #141824;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 15px;
        }
        .setup-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
        }
        .setup-title {
            font-size: 15px;
            font-weight: bold;
        }
        .counter {
            background-color: #1e293b;
            color: #94a3b8;
            padding: 2px 10px;
            border-radius: 10px;
            font-size: 11px;
        }
        .setup-subtitle {
            font-size: 11px;
            color: #64748b;
            margin-bottom: 15px;
        }

        /* الخانات (الشخصيات والحكاية) */
        .item-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #1a2234;
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 10px;
            border: 1px solid rgba(255,255,255,0.02);
        }
        .item-info {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .radio-circle {
            width: 14px;
            height: 14px;
            border: 2px solid #475569;
            border-radius: 50%;
        }
        .item-text h4 {
            font-size: 13px;
            color: #fff;
            margin-bottom: 2px;
        }
        .item-text p {
            font-size: 11px;
            color: #94a3b8;
        }
        .add-btn {
            background-color: #222d44;
            color: #fff;
            border: none;
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 12px;
            cursor: pointer;
        }
        .add-btn:hover {
            background-color: #2d3b59;
        }

        /* زر التالي */
        .next-btn {
            width: 100%;
            background-color: #1e293b;
            color: #64748b;
            border: none;
            padding: 12px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
            cursor: pointer;
            text-align: center;
            margin-top: 15px;
        }
        .next-btn.active {
            background-color: #ff2a85;
            color: #fff;
        }
    </style>
</head>
<body>

    <div class="container">
        
        <!-- الشاشة الأولى: الرئيسية (بحيث يظهر زر خطوة بخطوة) -->
        <div id="homeScreen" class="screen active">
            <div class="main-header">بلوت كرافت</div>
            
            <div class="welcome-box">
                <p>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</p>
            </div>

            <div class="modes-container">
                <!-- زر سريع -->
                <div class="mode-card">
                    <span class="icon">⚡</span>
                    <h3>سريع</h3>
                    <p>إدخال واحد، فيديو كامل</p>
                </div>
                
                <!-- زر خطوة بخطوة (عند الضغط عليه يحولك للشاشة الثانية) -->
                <div class="mode-card" onclick="goToStepScreen()">
                    <span class="icon">🚗</span>
                    <h3>خطوة بخطوة</h3>
                    <p>راجع كل خطوة</p>
                </div>
            </div>
        </div>

        <!-- الشاشة الثانية: واجهة الإعدادات والتفاصيل المطلوبة -->
        <div id="stepScreen" class="screen">
            <!-- الهيدر مع زر الرجوع -->
            <div class="sub-header">
                <span class="back-arrow" onclick="goToHomeScreen()">➔</span>
                <div></div>
                <div></div>
            </div>

            <!-- صندوق مساعد AI مع القائمة المنسدلة -->
            <div class="ai-box">
                <div class="ai-top">
                    <span class="ai-title">مساعد AI بلوت كرافت</span>
                    <div class="ai-icon-container" onclick="toggleMenu(event)">
                        <div class="ai-icon">AI+</div>
                        <!-- القائمة المنسدلة -->
                        <div id="aiDropdown" class="dropdown-menu">
                            <div class="dropdown-item">شعار دائرة أولاً</div>
                        </div>
                    </div>
                </div>
                <p class="ai-desc">عزيزي المخرج، ما نوع القصة التي تريد إنشاؤها؟ اكتب فكرتك ودع بلوت كرافت يحولها إلى واقع.</p>
            </div>

            <!-- صندوق إعداد القصة -->
            <div class="setup-box">
                <div class="setup-header">
                    <span class="setup-title">إعداد القصة</span>
                    <span class="counter">0/2</span>
                </div>
                <p class="setup-subtitle">أضف الشخصيات والقصة أولاً، ثم اختر المدة والنسبة:</p>

                <!-- خانة الشخصيات -->
                <div class="item-row">
                    <div class="item-info">
                        <div class="radio-circle"></div>
                        <div class="item-text">
                            <h4>الشخصيات</h4>
                            <p>أضف شخصيتين بحد أقصى</p>
                        </div>
                    </div>
                    <button class="add-btn">⬆ إضافة</button>
                </div>

                <!-- خانة الحكاية -->
                <div class="item-row">
                    <div class="item-info">
                        <div class="radio-circle"></div>
                        <div class="item-text">
                            <h4>الحكاية</h4>
                            <p>اضغط لكتابة قصتك</p>
                        </div>
                    </div>
                    <button class="add-btn">✏ إضافة</button>
                </div>

                <!-- زر التالي -->
                <button class="next-btn" id="nextBtn">التالي</button>
            </div>
        </div>

    </div>

    <script>
        // الانتقال إلى شاشة خطوة بخطوة
        function goToStepScreen() {
            document.getElementById('homeScreen').classList.remove('active');
            document.getElementById('stepScreen').classList.add('active');
        }

        // الرجوع إلى الشاشة الرئيسية
        function goToHomeScreen() {
            document.getElementById('stepScreen').classList.remove('active');
            document.getElementById('homeScreen').classList.add('active');
        }

        // فتح وإغلاق القائمة المنسدلة لأيقونة المساعد
        function toggleMenu(event) {
            event.stopPropagation();
            const menu = document.getElementById('aiDropdown');
            menu.classList.toggle('show');
        }

        // إغلاق القائمة عند النقر في أي مكان آخر خارجها
        window.onclick = function(event) {
            if (!event.target.closest('.ai-icon-container')) {
                const menu = document.getElementById('aiDropdown');
                if (menu && menu.classList.contains('show')) {
                    menu.classList.remove('show');
                }
            }
        }
    </script>

</body>
</html>
