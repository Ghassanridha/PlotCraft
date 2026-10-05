import streamlit as st
import streamlit.components.v1 as components

# إعداد صفحة ستريمليت
st.set_page_config(page_title="PlotCraft UI", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PlotCraft</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        body, html {
            width: 100%;
            height: 100%;
            background-color: #0b0f19;
            color: #ffffff;
            overflow-x: hidden;
        }
        .screen {
            display: none;
            width: 100%;
            min-height: 100vh;
            padding: 20px;
            padding-bottom: 50px;
        }
        .screen.active {
            display: block;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .title {
            font-size: 20px;
            font-weight: bold;
        }
        .btn-upgrade {
            background: rgba(255, 255, 255, 0.15);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            cursor: pointer;
            border: 1px solid rgba(255,255,255,0.2);
        }
        .plans-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-top: 20px;
        }
        .plan-card {
            background: #141824;
            border: 1.5px solid #2a344d;
            border-radius: 16px;
            padding: 16px;
            cursor: pointer;
            transition: 0.2s;
        }
        .plan-card.selected {
            border-color: #3b82f6;
            background: #1c2538;
        }
        .plan-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
        }
        .plan-name {
            font-size: 16px;
            font-weight: bold;
        }
        .plan-price {
            background: rgba(59, 130, 246, 0.2);
            color: #60a5fa;
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: bold;
        }
        .plan-desc {
            color: #94a3b8;
            font-size: 12px;
        }
        .back-btn {
            background: none;
            border: none;
            color: #ffffff;
            font-size: 16px;
            cursor: pointer;
            margin-bottom: 15px;
        }
        .main-btn {
            width: 100%;
            background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
            color: white;
            border: none;
            padding: 14px;
            border-radius: 14px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <!-- الشاشة الرئيسية -->
    <div id="homeScreen" class="screen active">
        <div class="header">
            <div class="title">بلوت كرافت (PlotCraft)</div>
            <div class="btn-upgrade" onclick="showScreen('subScreen')">⭐ ترقية</div>
        </div>
        <p style="color: #94a3b8; font-size: 14px; margin-bottom: 20px;">مرحباً بك، اختر الاشتراك المناسب لك.</p>
        
        <div onclick="showScreen('subScreen')" style="background: #141824; padding: 20px; border-radius: 16px; border: 1px solid #2a344d; cursor: pointer; text-align: center;">
            <h3>عرض باقات الاشتراك 🚀</h3>
            <p style="color: #94a3b8; font-size: 12px; margin-top: 5px;">اضغط هنا للانتقال لصفحة الاشتراكات</p>
        </div>
    </div>

    <!-- شاشة الاشتراكات -->
    <div id="subScreen" class="screen">
        <button class="back-btn" onclick="showScreen('homeScreen')">← عودة</button>
        <div class="header" style="margin-bottom: 10px;">
            <div class="title">اختر خطة الاشتراك</div>
        </div>
        
        <div class="plans-container">
            <!-- الاشتراك الأسبوعي المطلوب -->
            <div class="plan-card selected" onclick="selectPlan(this)">
                <div class="plan-header">
                    <div class="plan-name">الاشتراك الأسبوعي</div>
                    <div class="plan-price">$9.99</div>
                </div>
                <div class="plan-desc">500 نقطة أسبوعياً</div>
            </div>

            <!-- الاشتراك الشهري -->
            <div class="plan-card" onclick="selectPlan(this)">
                <div class="plan-header">
                    <div class="plan-name">الاشتراك الشهري</div>
                    <div class="plan-price">$19.99</div>
                </div>
                <div class="plan-desc">2500 نقطة شهرياً</div>
            </div>

            <!-- الاشتراك السنوي -->
            <div class="plan-card" onclick="selectPlan(this)">
                <div class="plan-header">
                    <div class="plan-name">الاشتراك السنوي</div>
                    <div class="plan-price">$99.99</div>
                </div>
                <div class="plan-desc">نقاط غير محدودة سنوياً</div>
            </div>
        </div>

        <button class="main-btn">تأكيد الاشتراك</button>
    </div>

    <script>
        function showScreen(screenId) {
            document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
            document.getElementById(screenId).classList.add('active');
        }

        function selectPlan(element) {
            document.querySelectorAll('.plan-card').forEach(c => c.classList.remove('selected'));
            element.classList.add('selected');
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=600, scrolling=True)
