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

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl" id="appHtmlRoot">
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
            -webkit-tap-highlight-color: transparent;
        }

        body, html {
            width: 100%;
            height: 100%;
            background-color: #0b0f19;
            overflow-x: hidden;
        }

        .screen-view {
            display: none;
            width: 100%;
            min-height: 100vh;
            background-color: #1f242d;
            flex-direction: column;
            padding-bottom: 90px;
        }

        .screen-view.active {
            display: flex;
        }

        #homeScreen.screen-view {
            background-color: #0b0f19;
        }

        #sparkleDialogScreen.screen-view {
            background-color: #0b0f19;
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
            border: 1px solid rgba(255, 255, 255, 0.2);
            cursor: pointer;
            transition: 0.2s;
        }

        .welcome-section {
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
            transition: 0.2s;
            position: relative;
        }

        .interactive-card:active {
            transform: scale(0.97);
            background: rgba(30, 40, 65, 0.85);
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
            color: #cbd5e1;
            font-size: 12px;
            font-weight: 400;
        }

        .exact-bot-icon {
            width: 22px;
            height: 22px;
            background: #dbeafe;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            background-size: contain;
        }

        .speed-custom-icon {
            width: 22px;
            height: 22px;
            background: #ffffff;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M4 14l3-3m0 0l3 3m-3-3v8"/><path d="M12 6c3.3 0 6 2.7 6 6s-2.7 6-6 6"/><path d="M15 3c4.97 0 9 4.03 9 9s-4.03 9-9 9"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M4 14l3-3m0 0l3 3m-3-3v8"/><path d="M12 6c3.3 0 6 2.7 6 6s-2.7 6-6 6"/><path d="M15 3c4.97 0 9 4.03 9 9s-4.03 9-9 9"/></svg>') no-repeat center;
            background-size: contain;
        }

        .card-title-group-left {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .pro-badge-top {
            display: flex;
            align-items: center;
            gap: 4px;
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 3px 8px;
            border-radius: 10px;
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
            margin-bottom: 8px;
            width: fit-content;
        }

        .pro-lock-icon {
            width: 10px;
            height: 10px;
            background: #ffffff;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>') no-repeat center;
            background-size: contain;
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
            color: #cbd5e1;
            font-size: 13px;
            cursor: pointer;
        }

        .movies-carousel {
            display: flex;
            gap: 14px;
            overflow-x: auto;
            padding-bottom: 10px;
            scrollbar-width: none;
        }

        .movies-carousel::-webkit-scrollbar {
            display: none;
        }

        .movie-card {
            min-width: 130px;
            height: 190px;
            border-radius: 16px;
            overflow: hidden;
            position: relative;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            border: 1px solid rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 14px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .movie-card:active {
            transform: scale(0.96);
        }

        .movie-card.m1 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m3 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=300&auto=format&fit=crop') center/cover; }

        .movie-title {
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
            line-height: 1.2;
        }

        .custom-alert-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.7);
            z-index: 99999999999;
            align-items: center;
            justify-content: center;
        }
        .custom-alert-overlay.show {
            display: flex;
        }
        .custom-alert-box {
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 24px 20px;
            width: 85%;
            max-width: 280px;
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }
        .custom-alert-msg {
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
            line-height: 1.5;
        }
        .custom-alert-btn {
            background: #3b82f6;
            color: #ffffff;
            border: none;
            border-radius: 12px;
            padding: 10px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            transition: 0.2s;
        }
        .custom-alert-btn:active {
            background: #2563eb;
            transform: scale(0.98);
        }

        #worksScreen {
            display: none;
            flex-direction: column;
            min-height: 100vh;
            padding: 0;
            align-items: stretch;
        }
        #worksScreen.active {
            display: flex;
        }

        .works-top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 20px 10px 20px;
            width: 100%;
        }

        .works-screen-title {
            color: #ffffff;
            font-size: 20px;
            font-weight: 700;
        }

        .works-header-left-group {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .works-upgrade-badge {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 6px 14px;
            border-radius: 20px;
            color: #ffffff;
            font-size: 13px;
            font-weight: 500;
            border: 1px solid rgba(255, 255, 255, 0.2);
            cursor: pointer;
        }

        .works-robot-logo {
            width: 32px;
            height: 32px;
            background: #dbeafe;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            background-size: contain;
            cursor: pointer;
        }

        .works-body-container {
            padding: 10px 20px 20px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            flex-grow: 1;
        }

        .works-tabs-container {
            display: flex;
            background: #282f3d;
            border-radius: 30px;
            padding: 4px;
            width: 100%;
            max-width: 360px;
            margin-top: 15px;
            margin-bottom: 60px;
            border: 1px solid rgba(255,255,255,0.08);
        }

        .works-tab {
            flex: 1;
            text-align: center;
            padding: 10px 0;
            font-size: 13px;
            font-weight: 600;
            color: #cbd5e1;
            background: transparent;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
        }

        .works-tab.active {
            background: #343d50 !important;
            color: #ffffff !important;
            font-weight: 700;
        }

        .works-empty-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex-grow: 1;
            text-align: center;
            margin-top: 10px;
        }

        .works-box-icon {
            width: 90px;
            height: 90px;
            margin-bottom: 24px;
            opacity: 0.8;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23cbd5e1" stroke-width="1.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>') no-repeat center;
            background-size: contain;
        }

        .works-empty-text-sub {
            color: #cbd5e1;
            font-size: 13px;
            margin-bottom: 35px;
        }

        .works-create-btn {
            width: 100%;
            max-width: 220px;
            background: #ffffff;
            color: #1f242d;
            font-size: 14px;
            font-weight: 700;
            padding: 10px 16px;
            border-radius: 14px;
            border: none;
            cursor: pointer;
            text-align: center;
            box-shadow: 0 4px 15px rgba(255,255,255,0.15);
            transition: 0.2s;
        }
        .works-create-btn:active {
            transform: scale(0.98);
            background: #e2e8f0;
        }

        /* --- شاشة الإعدادات الجديدة المطابقة للصورة --- */
        .settings-screen {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: #1f242d;
            z-index: 999999;
            flex-direction: column;
            overflow-y: auto;
            padding: 20px;
        }
        .settings-screen.active { display: flex; }

        .settings-top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            margin-bottom: 25px;
        }
        .settings-title {
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
            text-align: center;
            flex-grow: 1;
        }
        
        .settings-close-btn {
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
            outline: none;
        }
        .settings-close-btn:active {
            background-color: #0b0f19 !important;
            transform: scale(0.95);
        }

        /* صندوق الإعدادات المماثل للصورة بالضبط */
        .settings-card-box {
            background: #171b22;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 10px 16px;
            display: flex;
            flex-direction: column;
            gap: 4px;
            margin-bottom: 30px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        }
        .settings-row-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            cursor: pointer;
        }
        .settings-row-item:last-child {
            border-bottom: none;
        }
        .settings-row-right {
            display: flex;
            align-items: center;
            gap: 14px;
            color: #ffffff;
            font-size: 15px;
            font-weight: 600;
        }
        .settings-row-left {
            color: #94a3b8;
            font-size: 16px;
        }
        .settings-row-right svg {
            width: 20px;
            height: 20px;
            fill: #cbd5e1;
        }

        /* زر تسجيل الخروج السفلي */
        .settings-logout-btn {
            background: #ffffff;
            color: #1f242d;
            font-size: 16px;
            font-weight: 700;
            padding: 14px;
            border-radius: 16px;
            border: none;
            cursor: pointer;
            text-align: center;
            width: 100%;
            box-shadow: 0 4px 15px rgba(255,255,255,0.15);
            margin-top: auto;
            margin-bottom: 20px;
            transition: 0.2s;
        }
        .settings-logout-btn:active {
            background: #cbd5e1;
            transform: scale(0.98);
        }

        /* نافذة تسجيل الدخول وحقول الإدخال المطورة */
        .login-modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.85);
            z-index: 9999999999;
            align-items: flex-end;
            justify-content: center;
        }
        .login-modal-overlay.show { display: flex; }
        .login-modal-content {
            background: #1f242d;
            border-top-left-radius: 28px;
            border-top-right-radius: 28px;
            border: 1px solid rgba(255,255,255,0.12);
            width: 100%;
            max-width: 480px;
            padding: 24px 20px 40px 20px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            position: relative;
            box-shadow: 0 -10px 30px rgba(0,0,0,0.8);
            animation: slideUpModal 0.3s ease;
            max-height: 90vh;
            overflow-y: auto;
        }
        @keyframes slideUpModal {
            from { transform: translateY(100%); }
            to { transform: translateY(0); }
        }
        .login-modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 5px;
        }
        .login-modal-title {
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
        }
        .login-close-x {
            background: none;
            border: none;
            color: #ffffff;
            font-size: 20px;
            cursor: pointer;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .login-btn-google {
            width: 100%;
            background: #ffffff;
            color: #1f242d;
            border-radius: 16px;
            padding: 14px;
            font-size: 15px;
            font-weight: 700;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            box-shadow: 0 4px 12px rgba(255,255,255,0.15);
            transition: 0.2s;
        }
        .login-btn-google:active { transform: scale(0.98); background: #e2e8f0; }

        /* قائمة الإيميلات المنسدلة عند الضغط على جوجل */
        .google-emails-dropdown {
            display: none;
            flex-direction: column;
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 14px;
            overflow: hidden;
            margin-top: -6px;
            margin-bottom: 6px;
        }
        .google-emails-dropdown.show { display: flex; }
        .email-item-row {
            padding: 12px 16px;
            color: #ffffff;
            font-size: 14px;
            text-align: right;
            cursor: pointer;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            transition: 0.15s;
        }
        .email-item-row:last-child { border-bottom: none; }
        .email-item-row:hover, .email-item-row:active { background: #343d50; }

        /* تنسيق حقول الإدخال للبريد وكلمة المرور المطلوبة */
        .input-group-field {
            display: flex;
            flex-direction: column;
            gap: 6px;
            width: 100%;
        }
        .input-label-right {
            color: #ffffff;
            font-size: 14px;
            font-weight: 600;
            text-align: right;
        }
        .custom-text-input {
            width: 100%;
            background: #282f3d;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 16px;
            padding: 14px 16px;
            color: #ffffff;
            font-size: 14px;
            outline: none;
            text-align: right;
        }
        .custom-text-input::placeholder {
            color: rgba(255, 255, 255, 0.35);
        }

        /* زر تسجيل الدخول (يتفاعل حسب الإدخال) */
        .login-submit-main-btn {
            width: 100%;
            background: rgba(255, 255, 255, 0.2);
            color: rgba(255, 255, 255, 0.4);
            border-radius: 16px;
            padding: 14px;
            font-size: 15px;
            font-weight: 700;
            border: none;
            cursor: not-allowed;
            text-align: center;
            transition: 0.3s;
            margin-top: 5px;
        }
        .login-submit-main-btn.active-login {
            background: #ffffff !important;
            color: #1f242d !important;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(255,255,255,0.25);
        }

        /* الروابط السفلية لحقول تسجيل الدخول */
        .login-bottom-links-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            margin-top: 5px;
            font-size: 13px;
        }
        .forgot-pass-link {
            color: #cbd5e1;
            cursor: pointer;
            text-align: right;
        }
        .create-acc-link {
            color: #3b82f6;
            font-weight: 600;
            cursor: pointer;
            text-align: left;
        }

        .plotcraft-nav-bar {
            position: fixed;
            bottom: 0; left: 0; width: 100%;
            background-color: #1f242d;
            padding: 10px 15px;
            display: flex; justify-content: center; align-items: center; gap: 12px;
            z-index: 999999; box-sizing: border-box;
            box-shadow: 0 -4px 15px rgba(0,0,0,0.6);
            transition: transform 0.3s ease;
        }
        .plotcraft-nav-bar.hidden { transform: translateY(120%); }
        .plotcraft-nav-pill { background-color: #282f3d; border: 1px solid #343d50; border-radius: 35px; display: flex; justify-content: space-around; align-items: center; padding: 8px 15px; flex-grow: 1; max-width: 380px; }
        .plotcraft-nav-item { display: flex; align-items: center; gap: 6px; color: #cbd5e1; font-size: 13px; text-decoration: none; cursor: pointer; white-space: nowrap; }
        .plotcraft-nav-item.active { color: #ffffff; font-weight: bold; }
        .plotcraft-nav-square { background-color: #282f3d; border: 1px solid #343d50; border-radius: 16px; width: 48px; height: 48px; display: flex; justify-content: center; align-items: center; flex-shrink: 0; cursor: pointer; position: relative; }
    </style>
</head>
<body>

    <!-- شاشة الإعدادات المطابقة للصورة -->
    <div class="settings-screen" id="settingsScreen">
        <div class="settings-top-bar">
            <button class="settings-close-btn" onclick="closeSettingsScreen(event)" title="رجوع">‹</button>
            <div class="settings-title">الإعدادات</div>
            <div style="width: 36px;"></div>
        </div>

        <div class="settings-card-box">
            <div class="settings-row-item" onclick="showCustomAlert('شروط الاستخدام')">
                <div class="settings-row-right">
                    <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                    <span>شروط الاستخدام</span>
                </div>
                <div class="settings-row-left">‹</div>
            </div>

            <div class="settings-row-item" onclick="showCustomAlert('الخصوصية')">
                <div class="settings-row-right">
                    <svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg>
                    <span>الخصوصية</span>
                </div>
                <div class="settings-row-left">‹</div>
            </div>

            <div class="settings-row-item" onclick="showCustomAlert('إلغاء الاشتراك')">
                <div class="settings-row-right">
                    <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zM7 10h10v2H7z"/></svg>
                    <span>إلغاء الاشتراك</span>
                </div>
                <div class="settings-row-left">‹</div>
            </div>

            <div class="settings-row-item" onclick="showCustomAlert('حذف الحساب')">
                <div class="settings-row-right">
                    <svg viewBox="0 0 24 24"><path d="M16 9v.1H8V9c0-2.21 1.79-4 4-4s4 1.79 4 4zm-5 6.5h2V13h-2v2.5zm1-12.5C6.48 3 2 7.48 2 13s4.48 10 10 10 10-4.48 10-10S17.52 3 12 3zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>
                    <span>حذف الحساب</span>
                </div>
                <div class="settings-row-left">‹</div>
            </div>
        </div>

        <button class="settings-logout-btn" onclick="handleLogout(event)">تسجيل الخروج</button>
    </div>

    <!-- نافذة تسجيل الدخول مع خيارات Google وإدخال البريد -->
    <div class="login-modal-overlay" id="loginModalOverlay" onclick="event.stopPropagation()">
        <div class="login-modal-content">
            <div class="login-modal-header">
                <div class="login-modal-title">تسجيل الدخول إلى Plotcraft</div>
                <button class="login-close-x" onclick="closeLoginModal()">✕</button>
            </div>

            <!-- زر تسجيل الدخول عبر Google -->
            <button class="login-btn-google" onclick="toggleGoogleEmails(event)">
                <svg width="20" height="20" viewBox="0 0 24 24"><path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/><path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.2v3.15C3.17 21.32 7.22 24 12 24z"/><path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.13-1.55.38-2.27V6.58H1.2C.44 8.12 0 9.87 0 11.73s.44 3.61 1.2 5.15l4.08-2.61z"/><path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.22 0 3.17 2.68 1.2 6.58l4.08 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/></svg>
                <span>تسجيل الدخول مع Google</span>
            </button>

            <!-- قائمة الإيميلات المنبثقة العمودية بجهة اليمين -->
            <div class="google-emails-dropdown" id="googleEmailsDropdown">
                <div class="email-item-row" onclick="selectEmail('ghassan.ridha1@gmail.com')">ghassan.ridha1@gmail.com</div>
                <div class="email-item-row" onclick="selectEmail('plotcraft.user@gmail.com')">plotcraft.user@gmail.com</div>
                <div class="email-item-row" onclick="selectEmail('director.pro@gmail.com')">director.pro@gmail.com</div>
            </div>

            <div style="text-align: center; color: #cbd5e1; font-size: 13px; margin: 4px 0;">أو باستخدام البريد الإلكتروني</div>

            <!-- حقل البريد الإلكتروني -->
            <div class="input-group-field">
                <div class="input-label-right">البريد الإلكتروني</div>
                <input type="email" class="custom-text-input" id="emailInputField" placeholder="يرجى إدخال عنوان البريد الإلكتروني" oninput="checkLoginInputs()">
            </div>

            <!-- حقل كلمة المرور -->
            <div class="input-group-field">
                <div class="input-label-right">كلمة المرور</div>
                <input type="password" class="custom-text-input" id="passwordInputField" placeholder="ادخل كلمة المرور تحتوي على أكثر من 6 احرف" oninput="checkLoginInputs()">
            </div>

            <!-- زر تسجيل الدخول (يتفاعل) -->
            <button class="login-submit-main-btn" id="loginSubmitBtn" onclick="performEmailLogin()">تسجيل الدخول</button>

            <!-- الروابط السفلية (هل نسيت كلمة السر وإنشاء حساب) -->
            <div class="login-bottom-links-row">
                <div class="forgot-pass-link" onclick="showCustomAlert('استعادة كلمة المرور')">هل نسيت كلمة السر؟</div>
                <div class="create-acc-link" onclick="showCustomAlert('إنشاء حساب جديد')">إنشاء حساب جديد</div>
            </div>
        </div>
    </div>

    <div class="custom-alert-overlay" id="customAlertOverlay" onclick="event.stopPropagation()">
        <div class="custom-alert-box">
            <div class="custom-alert-msg" id="customAlertMsgText">تنبيه</div>
            <button class="custom-alert-btn" onclick="closeCustomAlert(event)">حسناً</button>
        </div>
    </div>

    <!-- الشاشة الرئيسية -->
    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">PlotCraft</div>
                <div class="upgrade-badge" onclick="openSubscriptionModalFromBadge(event)">ترقية</div>
            </div>

            <div class="welcome-section">
                <h1>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>

            <div class="cards-row">
                <div class="interactive-card" onclick="switchScreen('stepByStepScreen', event)">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">خطوة بخطوة</div>
                            <span class="exact-bot-icon"></span>
                        </div>
                    </div>
                    <div class="card-subtitle">راجع كل خطوة</div>
                </div>

                <div class="interactive-card" onclick="showCustomAlert('ميزة سريعة تتطلب ترقية')">
                    <div class="pro-badge-top">
                        <span>Pro only</span>
                        <span class="pro-lock-icon"></span>
                    </div>
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">سريع</div>
                            <span class="speed-custom-icon"></span>
                        </div>
                    </div>
                    <div class="card-subtitle">إدخال واحد، فيديو كامل</div>
                </div>
            </div>
        </div>

        <div class="inspiration-section">
            <div class="section-header">
                <div class="section-title">إلهام بلوت كرافت</div>
                <div class="view-all">عرض الكل ></div>
            </div>

            <div class="movies-carousel">
                <div class="movie-card m1" onclick="showCustomAlert('القصة قادمة قريباً')"><div class="movie-title">THE DELIVERYMAN'S SECRET BILLIONAIRE</div></div>
                <div class="movie-card m2" onclick="showCustomAlert('القصة قادمة قريباً')"><div class="movie-title">SECRET BILLIONAIRE</div></div>
                <div class="movie-card m3" onclick="showCustomAlert('القصة قادمة قريباً')"><div class="movie-title">CYBER CITY</div></div>
            </div>
        </div>
    </div>

    <div id="worksScreen" class="screen-view">
        <div class="works-top-header">
            <div class="works-screen-title">الأعمال</div>
            <div class="works-header-left-group">
                <div class="works-upgrade-badge" onclick="openSubscriptionModalFromBadge(event)">ترقية</div>
                <div class="works-robot-logo" onclick="openSettingsScreen(event)" title="الإعدادات"></div>
            </div>
        </div>

        <div class="works-body-container">
            <div class="works-tabs-container">
                <div class="works-tab active" onclick="switchWorksTab(this)">المشاريع</div>
                <div class="works-tab" onclick="switchWorksTab(this)">مكتبة الوسائط</div>
            </div>
            <div class="works-empty-content">
                <div class="works-box-icon"></div>
                <div class="works-empty-text-sub">ستظهر هنا مشاريع القصة الخاصة بك.</div>
                <button class="works-create-btn" onclick="showCustomAlert('إنشاء قصة جديدة')">إنشاء قصة</button>
            </div>
        </div>
    </div>

    <!-- الشريط السفلي -->
    <div class="plotcraft-nav-bar" id="mainNavBar">
        <div class="plotcraft-nav-pill">
            <a href="#" class="plotcraft-nav-item active" id="navHome" onclick="switchScreen('homeScreen', event); setActiveNav('navHome')">
                <span>الرئيسية</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            </a>
            <a href="#" class="plotcraft-nav-item" id="navTools" onclick="switchScreen('toolsScreen', event); setActiveNav('navTools')">
                <span>الأدوات</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
            </a>
            <a href="#" class="plotcraft-nav-item" id="navWorks" onclick="switchScreen('worksScreen', event); setActiveNav('navWorks')">
                <span>الأعمال</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path></svg>
            </a>
        </div>

        <div class="plotcraft-nav-square" onclick="showCustomAlert('إنشاء سريع')" title="إنشاء سريع">
            <svg width="26" height="26" viewBox="0 0 24 24">
                <rect x="3" y="6" width="14" height="12" rx="3" fill="#cbd5e1"/>
                <path d="M14 6h3c1.1 0 2 .9 2 2v8c0 1.1-.9 2-2 2h-3V6z" fill="#94a3b8"/>
                <polygon points="8,10 12,12 8,14" fill="#1f242d"/>
                <path d="M8 3C8 4.65 6.65 6 5 6C6.65 6 8 7.35 8 9C8 7.35 9.35 6 11 6C9.35 6 8 4.65 8 3Z" fill="#3b82f6"/>
            </svg>
        </div>
    </div>

    <script>
        let isUserLoggedIn = false;

        function switchScreen(screenId, event) {
            if (event) event.preventDefault();
            var screens = document.querySelectorAll('.screen-view');
            screens.forEach(s => s.classList.remove('active'));
            var target = document.getElementById(screenId);
            if(target) target.classList.add('active');
            window.scrollTo(0, 0);
        }

        function setActiveNav(navId) {
            var items = document.querySelectorAll('.plotcraft-nav-item');
            items.forEach(i => i.classList.remove('active'));
            var target = document.getElementById(navId);
            if(target) target.classList.add('active');
        }

        function openSettingsScreen(event) {
            if (event) event.stopPropagation();
            if (!isUserLoggedIn) {
                openLoginModal();
            } else {
                document.getElementById('settingsScreen').classList.add('active');
                document.getElementById('mainNavBar').classList.add('hidden');
            }
        }

        function closeSettingsScreen(event) {
            if (event) event.stopPropagation();
            document.getElementById('settingsScreen').classList.remove('active');
            document.getElementById('mainNavBar').classList.remove('hidden');
        }

        function openLoginModal() {
            document.getElementById('loginModalOverlay').classList.add('show');
        }

        function closeLoginModal() {
            document.getElementById('loginModalOverlay').classList.add('hidden');
            document.getElementById('googleEmailsDropdown').classList.remove('show');
        }

        function toggleGoogleEmails(event) {
            if (event) event.stopPropagation();
            var dropdown = document.getElementById('googleEmailsDropdown');
            dropdown.classList.toggle('show');
        }

        function selectEmail(email) {
            isUserLoggedIn = true;
            closeLoginModal();
            showCustomAlert('تم تسجيل الدخول بنجاح بـ ' + email);
            document.getElementById('settingsScreen').classList.add('active');
            document.getElementById('mainNavBar').classList.add('hidden');
        }

        function checkLoginInputs() {
            var emailVal = document.getElementById('emailInputField').value.trim();
            var passVal = document.getElementById('passwordInputField').value.trim();
            var submitBtn = document.getElementById('loginSubmitBtn');

            if (emailVal !== "" && passVal.length >= 6) {
                submitBtn.classList.add('active-login');
            } else {
                submitBtn.classList.remove('active-login');
            }
        }

        function performEmailLogin() {
            var emailVal = document.getElementById('emailInputField').value.trim();
            var passVal = document.getElementById('passwordInputField').value.trim();

            if (emailVal !== "" && passVal.length >= 6) {
                isUserLoggedIn = true;
                closeLoginModal();
                showCustomAlert('تم تسجيل الدخول بنجاح!');
                document.getElementById('settingsScreen').classList.add('active');
                document.getElementById('mainNavBar').classList.add('hidden');
            }
        }

        function handleLogout(event) {
            if (event) event.stopPropagation();
            isUserLoggedIn = false;
            document.getElementById('settingsScreen').classList.remove('active');
            document.getElementById('mainNavBar').classList.remove('hidden');
            showCustomAlert('تم تسجيل الخروج بنجاح');
        }

        function showCustomAlert(message) {
            document.getElementById('customAlertMsgText').innerText = message;
            document.getElementById('customAlertOverlay').classList.add('show');
        }

        function closeCustomAlert(event) {
            if (event) event.stopPropagation();
            document.getElementById('customAlertOverlay').classList.remove('show');
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=680, scrolling=True)
