import streamlit as st
import streamlit.components.v1 as components

# إعداد صفحة ستريمليت لإزالة الهوامش واستغلال الشاشة بالكامل
st.set_page_config(page_title="PlotCraft UI", layout="wide", initial_sidebar_state="collapsed")

# إزالة هوامش وتداخلات صفحة ستريمليت الافتراضية للجوال
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

html_code = r"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>PlotCraft UI</title>
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
            overflow-x: hidden;
        }

        .mobile-screen {
            width: 100vw;
            min-height: 100vh;
            background-color: #0b0f19;
            position: relative;
            display: flex;
            flex-direction: column;
            padding-bottom: 70px;
        }

        .screen-view {
            display: none;
            width: 100%;
            min-height: 100vh;
            background-color: #0b0f19;
            flex-direction: column;
        }

        .screen-view.active {
            display: flex;
        }

        .hero-box {
            position: relative;
            width: 100%;
            min-height: 52vh;
            background: linear-gradient(180deg, rgba(11,15,25,0.2) 0%, rgba(11,15,25,0.8) 75%, #0b0f19 100%),
                        url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1080&auto=format&fit=crop') center/cover no-repeat;
            border-bottom-left-radius: 35px;
            border-bottom-right-radius: 35px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 24px 20px 20px 20px;
        }

        .top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .brand-title {
            color: #ffffff;
            font-size: 20px;
            font-weight: 700;
        }

        .upgrade-badge {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 8px 16px;
            border-radius: 25px;
            color: #ffffff;
            font-size: 14px;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 6px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            cursor: pointer;
        }

        .welcome-section {
            text-align: right;
            margin-top: 15px;
        }

        .welcome-section h1 {
            color: #ffffff;
            font-size: 22px;
            font-weight: 700;
            line-height: 1.4;
            text-shadow: 0 2px 8px rgba(0,0,0,0.6);
        }

        .cards-row {
            display: flex;
            gap: 12px;
            width: 100%;
            margin-top: 20px;
        }

        .interactive-card {
            flex: 1;
            background: rgba(20, 25, 40, 0.65);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 18px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            cursor: pointer;
        }

        .card-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
        }

        .card-title {
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
        }

        .card-subtitle {
            color: #94a3b8;
            font-size: 12px;
        }

        .exact-bot-icon, .magic-wand-icon {
            width: 22px;
            height: 22px;
            background: #dbeafe;
            display: inline-block;
        }

        .card-title-group-left {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .inspiration-section {
            padding: 24px 20px;
        }

        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }

        .section-title {
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
        }

        .view-all {
            color: #94a3b8;
            font-size: 13px;
        }

        .movies-carousel {
            display: flex;
            flex-direction: row-reverse;
            gap: 14px;
            overflow-x: auto;
            padding-bottom: 10px;
            scrollbar-width: none;
        }

        .movie-card {
            min-width: 130px;
            height: 190px;
            border-radius: 16px;
            overflow: hidden;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 14px;
        }

        .movie-card.m1 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m3 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=300&auto=format&fit=crop') center/cover; }

        .movie-title {
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
        }

        #dramaScreen {
            background-color: #0b0f19;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            direction: rtl;
        }

        .drama-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
        }

        .drama-title {
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
            text-align: center;
            flex-grow: 1;
        }

        .drama-back-btn {
            background: transparent;
            border: none;
            color: #ffffff;
            font-size: 20px;
            cursor: pointer;
        }

        .ai-assistant-box {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 16px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .ai-assistant-header {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            gap: 8px;
        }

        .ai-assistant-name {
            color: #ec4899;
            font-size: 14px;
            font-weight: 700;
        }

        .plotcraft-circle-logo {
            width: 30px;
            height: 30px;
            background: linear-gradient(135deg, #ec4899 0%, #8b5cf6 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 12px;
            font-weight: bold;
        }

        .ai-assistant-text {
            color: #94a3b8;
            font-size: 12px;
            line-height: 1.5;
            text-align: right;
        }

        .story-setup-card {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 16px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .story-setup-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .story-setup-title {
            color: #ffffff;
            font-size: 15px;
            font-weight: 700;
        }

        .story-setup-counter {
            background-color: #30363d;
            color: #ffffff;
            font-size: 11px;
            padding: 3px 8px;
            border-radius: 10px;
        }

        .story-setup-desc {
            color: #94a3b8;
            font-size: 11px;
            text-align: right;
            margin-top: -10px;
        }

        .option-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            padding: 12px 14px;
            border-radius: 12px;
        }

        .option-info {
            display: flex;
            flex-direction: column;
            gap: 3px;
            text-align: right;
        }

        .option-label {
            color: #ffffff;
            font-size: 13px;
            font-weight: 600;
        }

        .option-sub {
            color: #94a3b8;
            font-size: 11px;
        }

        .add-btn {
            background-color: #30363d;
            color: #ffffff;
            border: none;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 12px;
            cursor: pointer;
        }

        .next-step-btn {
            width: 100%;
            background: #21262d;
            color: #8b949e;
            border: 1px solid #30363d;
            padding: 14px;
            border-radius: 14px;
            font-size: 14px;
            font-weight: 700;
            text-align: center;
            cursor: pointer;
            margin-top: 10px;
        }

        #subscriptionScreen {
            position: relative;
            background: #0b0f19;
            display: none;
            flex-direction: column;
            min-height: 100vh;
        }

        .page-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            background: rgba(11, 15, 25, 0.75);
        }

        .back-btn {
            background: rgba(255,255,255,0.1);
            border: none;
            color: #fff;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            cursor: pointer;
        }

        .page-title-text {
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
        }

        .content-body {
            padding: 20px;
        }

        .plotcraft-nav-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #0b0f19;
            padding: 10px 15px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 12px;
            z-index: 999999;
            box-sizing: border-box;
            direction: rtl;
        }

        .plotcraft-nav-pill {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 35px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 8px 15px;
            flex-grow: 1;
            max-width: 380px;
        }

        .plotcraft-nav-item {
            display: flex;
            align-items: center;
            gap: 6px;
            color: #8b949e;
            font-size: 13px;
            cursor: pointer;
        }

        .plotcraft-nav-square {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 16px;
            width: 48px;
            height: 48px;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div class="mobile-screen">
        <div id="homeScreen" class="screen-view active">
            <div class="hero-box">
                <div class="top-header">
                    <div class="brand-title">بلوت كرافت</div>
                    <div class="upgrade-badge" onclick="switchScreen('subscriptionScreen')">
                        <span>⭐</span> ترقية
                    </div>
                </div>

                <div class="welcome-section">
                    <h1>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
                </div>

                <div class="cards-row">
                    <div class="interactive-card" onclick="switchScreen('dramaScreen
