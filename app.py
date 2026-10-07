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
<html lang="ar" dir="rtl" id="htmlRoot">
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
        [dir="rtl"] .welcome-section { text-align: right; }
        [dir="ltr"] .welcome-section { text-align: left; }

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
        [dir="rtl"] .movies-carousel { flex-direction: row-reverse; }
        [dir="ltr"] .movies-carousel { flex-direction: row; }
        .movies-carousel::-webkit-scrollbar { display: none; }

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
        .movie-card:active { transform: scale(0.96); }

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
        .custom-alert-overlay.show { display: flex; }
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
        .custom-alert-btn:active { background: #2563eb; transform: scale(0.98); }

        #worksScreen {
            display: none;
            flex-direction: column;
            min-height: 100vh;
            padding: 0;
            align-items: stretch;
        }
        #worksScreen.active { display: flex; }

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
        .works-create-btn:active { transform: scale(0.98); background: #e2e8f0; }

        /* --- شاشة الإعدادات --- */
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
        .settings-close-btn:active { background-color: #0b0f19 !important; transform: scale(0.95); }

        .settings-upgrade-badge {
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
        }

        .profile-header-card {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 20px;
        }
        [dir="rtl"] .profile-header-card { justify-content: flex-start; }
        [dir="ltr"] .profile-header-card { justify-content: flex-start; }

        .profile-avatar-box {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            overflow: hidden;
            border: 2px solid rgba(255,255,255,0.25);
            background: #111827;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        }
        .profile-avatar-box svg {
            width: 36px;
            height: 36px;
            fill: #60a5fa;
            filter: drop-shadow(0 0 6px rgba(96,165,250,0.6));
        }

        .profile-info-group {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 6px;
        }
        .profile-name-row {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .profile-name-text {
            color: #ffffff;
            font-size: 19px;
            font-weight: 700;
            white-space: nowrap;
        }
        .profile-edit-pencil {
            cursor: pointer;
            width: 26px;
            height: 26px;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.25);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
        }
        .profile-edit-pencil svg { width: 13px; height: 13px; fill: #ffffff; }
        .profile-edit-pencil:active { background: rgba(255, 255, 255, 0.25); }

        .profile-id-row {
            display: flex;
            align-items: center;
            gap: 6px;
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.1);
            padding: 4px 10px;
            border-radius: 12px;
            color: #cbd5e1;
            font-size: 12px;
        }

        .pro-banner-card {
            background: linear-gradient(135deg, rgba(30, 35, 50, 0.9), rgba(15, 20, 35, 0.95));
            border: 1.5px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 16px;
            position: relative;
            margin-bottom: 20px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(0,0,0,0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .pro-banner-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .pro-banner-title { color: #ffffff; font-size: 16px; font-weight: 700; }
        .pro-sparkle-icon {
            width: 45px;
            height: 45px;
            background: linear-gradient(135deg, #3b82f6, #ec4899);
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C12 7.5 16.5 12 22 12C16.5 12 12 16.5 12 22C12 16.5 7.5 12 2 12C7.5 12 12 7.5 12 2Z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C12 7.5 16.5 12 22 12C16.5 12 12 16.5 12 22C12 16.5 7.5 12 2 12C7.5 12 12 7.5 12 2Z"/></svg>') no-repeat center;
            background-size: contain;
        }
        .pro-banner-desc { color: #cbd5e1; font-size: 12px; }
        .pro-banner-btn {
            background: #3b82f6;
            color: #ffffff;
            border: none;
            padding: 8px 16px;
            border-radius: 14px;
            font-size: 13px;
            font-weight: 700;
            width: fit-content;
            cursor: pointer;
            margin-top: 4px;
        }
        .pro-banner-btn:active { background: #2563eb; }

        .settings-group-box {
            background: #282f3d;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 6px 16px;
            margin-bottom: 16px;
            display: flex;
            flex-direction: column;
        }
        .settings-item-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 10px;
            margin: 0 -10px;
            border-radius: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            cursor: pointer;
            transition: background-color 0.15s ease;
        }
        .settings-item-row:last-child { border-bottom: none; }
        .settings-item-row:active { background-color: #0b0f19 !important; }

        .settings-item-right {
            display: flex;
            align-items: center;
            gap: 12px;
            color: #ffffff;
            font-size: 15px;
            font-weight: 600;
        }
        .menu-icon { width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; }
        .menu-icon svg { width: 18px; height: 18px; fill: #94a3b8; }
        .settings-item-left {
            color: #cbd5e1;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .switch-toggle { position: relative; display: inline-block; width: 44px; height: 24px; }
        .switch-toggle input { opacity: 0; width: 0; height: 0; }
        .slider-round {
            position: absolute; cursor: pointer;
            top: 0; left: 0; right: 0; bottom: 0;
            background-color: #343d50;
            transition: .3s;
            border-radius: 24px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .slider-round:before {
            position: absolute; content: "";
            height: 18px; width: 18px;
            left: 3px; bottom: 2px;
            background-color: white;
            transition: .3s;
            border-radius: 50%;
        }
        input:checked + .slider-round { background-color: #3b82f6; }
        input:checked + .slider-round:before { transform: translateX(20px); }

        /* نافذة اختيار اللغات */
        .language-modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 999999999;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .language-modal-overlay.show { display: flex; }
        .language-modal-box {
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 24px;
            width: 100%;
            max-width: 340px;
            max-height: 80vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 15px 40px rgba(0,0,0,0.8);
        }
        .lang-modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 18px 20px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            direction: ltr;
        }
        .lang-modal-title { color: #fff; font-size: 16px; font-weight: 700; }
        .lang-modal-close {
            background: rgba(255,255,255,0.1);
            border: none;
            color: #fff;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
        }
        .lang-list-container {
            padding: 10px 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 4px;
            direction: ltr;
            text-align: left;
        }
        .lang-item-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 14px;
            border-radius: 12px;
            cursor: pointer;
            transition: 0.15s;
            color: #cbd5e1;
            font-size: 14px;
            font-weight: 600;
        }
        .lang-item-row:hover, .lang-item-row:active { background: rgba(255,255,255,0.08); color: #fff; }
        .lang-item-row.selected { background: #3b82f6; color: #fff; }

        /* نافذة التعليقات لإرسال المشكلة كمطور */
        .feedback-modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 999999999;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .feedback-modal-overlay.show { display: flex; }
        .feedback-modal-box {
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 22px;
            width: 100%;
            max-width: 340px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }
        .feedback-textarea {
            width: 100%;
            height: 130px;
            background: #1f242d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 12px;
            padding: 12px;
            color: #fff;
            font-size: 14px;
            outline: none;
            resize: none;
        }

        .notif-permission-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.75);
            z-index: 99999999;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .notif-permission-box {
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 22px;
            width: 100%;
            max-width: 300px;
            padding: 22px;
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }
        .notif-permission-title { color: #fff; font-size: 16px; font-weight: 700; line-height: 1.5; }
        .notif-allow-btn { background: #3b82f6; color: #fff; border: none; padding: 12px; border-radius: 14px; font-size: 14px; font-weight: 700; cursor: pointer; }
        .notif-deny-btn { background: #1f242d; color: #fff; border: 1px solid rgba(255,255,255,0.2); padding: 12px; border-radius: 14px; font-size: 14px; font-weight: 700; cursor: pointer; }

        .name-edit-modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.75);
            z-index: 99999999;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .name-edit-box {
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 22px;
            width: 100%;
            max-width: 320px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .name-edit-input {
            width: 100%;
            background: #1f242d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 12px;
            padding: 12px;
            color: #fff;
            font-size: 15px;
            outline: none;
        }

        .step-container { padding: 20px; display: flex; flex-direction: column; gap: 16px; max-height: calc(100vh - 90px); overflow-y: auto; }
        .ai-assistant-card { background: #282f3d; border: 1px solid #343d50; border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 8px; }
        .ai-header-row { display: flex; justify-content: space-between; align-items: center; }
        .ai-title { color: #ff2a85; font-size: 14px; font-weight: 700; }
        .ai-badge-circle { width: 32px; height: 32px; background: linear-gradient(135deg, #ff2a85, #7928ca); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 11px; }
        .ai-desc { color: #cbd5e1; font-size: 12px; line-height: 1.5; }

        .story-setup-box { background: #282f3d; border: 1px solid #343d50; border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 12px; }
        .setup-header-row { display: flex; justify-content: space-between; align-items: center; }
        .setup-main-title { color: #ffffff; font-size: 15px; font-weight: 700; }
        .counter-badge { background-color: #343d50; color: #cbd5e1; padding: 3px 10px; border-radius: 10px; font-size: 11px; font-weight: 600; }
        .setup-subtitle { color: #ffffff; font-size: 11px; font-weight: 700; }
        .setup-row-item { background: #343d50; border-radius: 12px; padding: 12px; display: flex; justify-content: space-between; align-items: center; }
        .item-info h4 { color: #ffffff; font-size: 13px; font-weight: 700; margin-bottom: 2px; }
        .item-info p { color: #cbd5e1; font-size: 11px; }
        .action-add-btn { background: rgba(255, 255, 255, 0.12); color: #ffffff; border: 1px solid rgba(255, 255, 255, 0.3); padding: 6px 14px; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer; }

        .next-step-btn { background: #ffffff !important; color: #0b0f19 !important; font-size: 16px; font-weight: 700; padding: 14px; border-radius: 24px; border: none; cursor: pointer; display: none; width: 100%; text-align: center; box-shadow: 0 6px 20px rgba(255,255,255,0.15); }
        .next-step-btn.show { display: block; }

        #storyDescriptionScreen { display: none; flex-direction: column; min-height: 100vh; background-color: #1f242d; padding: 20px; position: relative; }
        #storyDescriptionScreen.active { display: flex; }
        .story-desc-header { display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 20px; }
        .story-desc-title { color: #ffffff; font-size: 18px; font-weight: 700; }
        .story-desc-back { background: none; border: none; color: #ffffff; font-size: 18px; cursor: pointer; }
        .story-textarea { width: 100%; height: 350px; background: #282f3d; border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 16px; color: #ffffff; font-size: 15px; outline: none; resize: vertical; line-height: 1.6; }

        .story-save-btn-wrapper { position: fixed; bottom: 25px; left: 20px; right: 20px; z-index: 9999; }
        .story-save-btn { background: rgba(255, 255, 255, 0.08); color: rgba(255, 255, 255, 0.25); border: 1px solid rgba(255, 255, 255, 0.12); font-size: 15px; font-weight: 700; padding: 14px; border-radius: 24px; width: 100%; max-width: 420px; margin: 0 auto; display: block; text-align: center; cursor: not-allowed; transition: 0.3s; }
        .story-save-btn.active-save { background: #ffffff !important; color: #0b0f19 !important; border: 1px solid #ffffff !important; cursor: pointer; }

        .added-story-card-vertical { background: #282f3d; border: 1px solid rgba(255,255,255,0.12); border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 12px; margin-top: 10px; }
        .added-story-top-row { display: flex; justify-content: space-between; align-items: center; }
        .added-story-title-group { display: flex; align-items: center; gap: 8px; color: #ffffff; font-size: 15px; font-weight: 700; }
        .added-story-check-icon { width: 18px; height: 18px; background: #ffffff; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #1f242d; font-size: 11px; font-weight: bold; }
        .added-story-edit-btn { background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 8px; }
        .added-story-content-text { color: #cbd5e1; font-size: 13px; line-height: 1.6; max-height: 80px; overflow-y: auto; }

        #addCharacterScreen { display: none; flex-direction: column; min-height: 100vh; padding: 20px; position: relative; }
        #addCharacterScreen.active { display: flex; }
        .add-char-header { display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 20px; }
        .add-char-title { color: #ffffff; font-size: 18px; font-weight: 700; }
        .add-char-back { background: none; border: none; color: #fff; font-size: 20px; cursor: pointer; }

        .char-main-card { background: #282f3d; border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 16px; display: flex; flex-direction: column; gap: 16px; margin-bottom: 16px; }
        .char-section-label { color: #ffffff; font-size: 15px; font-weight: 700; }
        
        .char-big-upload-box { background: #343d50; border: 1px dashed rgba(255,255,255,0.2); border-radius: 16px; height: 180px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; cursor: pointer; position: relative; overflow: hidden; }
        .char-big-upload-box img { width: 100%; height: 100%; object-fit: contain; background-color: #000; position: absolute; top: 0; left: 0; }
        .remove-big-img { position: absolute; top: 10px; left: 10px; background: rgba(0,0,0,0.7); color: #fff; border: none; width: 28px; height: 28px; border-radius: 50%; cursor: pointer; z-index: 5; display: flex; align-items: center; justify-content: center; font-size: 14px; }

        .char-thumbs-container { display: flex; align-items: center; gap: 12px; width: 100%; }
        .char-add-role-box { width: 55px; height: 55px; border-radius: 12px; background: #343d50; border: 1.5px dashed rgba(255,255,255,0.4); display: flex; flex-direction: column; align-items: center; justify-content: center; color: #cbd5e1; font-size: 18px; cursor: pointer; flex-shrink: 0; gap: 2px; }
        .char-add-role-text { font-size: 10px; }

        .char-thumbs-scroll { display: flex; gap: 10px; overflow-x: auto; padding-bottom: 4px; scrollbar-width: none; flex-grow: 1; }
        .char-thumbs-scroll::-webkit-scrollbar { display: none; }
        .char-thumb-item { width: 55px; height: 55px; border-radius: 12px; object-fit: cover; border: 1.5px solid rgba(255,255,255,0.15); cursor: pointer; flex-shrink: 0; display: block; }
        .char-name-input { width: 100%; background: #343d50; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; padding: 14px; color: #ffffff; font-size: 14px; outline: none; }

        .char-submit-btn-wrapper { position: fixed; bottom: 20px; left: 20px; right: 20px; z-index: 20; }
        .char-submit-btn { width: 100%; background: linear-gradient(135deg, #3b82f6 0%, #ec4899 100%); color: #ffffff; font-size: 16px; font-weight: 700; padding: 16px; border-radius: 24px; border: none; cursor: pointer; text-align: center; box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4); }
        .char-submit-btn.disabled { background: #343d50 !important; color: #cbd5e1 !important; cursor: not-allowed; opacity: 0.6; }

        .added-character-preview-card { background: #343d50; border-radius: 12px; padding: 12px; display: flex; justify-content: space-between; align-items: center; margin-top: 10px; }
        .added-char-right { display: flex; align-items: center; gap: 12px; }
        .added-char-img { width: 45px; height: 45px; border-radius: 10px; object-fit: cover; border: 1px solid rgba(255,255,255,0.2); }
        .added-char-name { color: #ffffff; font-size: 13px; font-weight: 700; }
        .added-char-left { display: flex; align-items: center; gap: 10px; }
        .added-char-change-group { display: flex; align-items: center; gap: 5px; color: #ffffff; font-size: 12px; font-weight: 600; cursor: pointer; background: rgba(255, 255, 255, 0.1); padding: 5px 12px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.2); }
        .added-char-delete-btn { background: #1f242d; color: #ffffff; border: 1px solid rgba(255, 255, 255, 0.3); width: 30px; height: 30px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 13px; cursor: pointer; font-weight: bold; }

        .source-modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 999; align-items: center; justify-content: center; }
        .source-modal.show { display: flex; }
        .source-modal-content { background: #282f3d; border: 1px solid rgba(255,255,255,0.15); border-radius: 20px; padding: 20px; width: 90%; max-width: 320px; display: flex; flex-direction: column; gap: 14px; text-align: center; }
        .source-buttons-row { display: flex; gap: 10px; justify-content: space-between; }
        .source-btn { flex: 1; background: #343d50; color: #fff; border: 1px solid rgba(255,255,255,0.1); padding: 12px 8px; border-radius: 12px; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 6px; }

        #toolsScreen { overflow-y: auto; }
        .tools-header { display: flex; align-items: center; justify-content: space-between; padding: 20px; background: rgba(31, 36, 45, 0.85); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.08); }
        .tools-header-title { color: #ffffff; font-size: 20px; font-weight: 700; }
        .tools-upgrade-btn { background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; color: #ffffff; font-size: 13px; font-weight: 500; cursor: pointer; }
        .tools-body { padding: 16px; display: flex; flex-direction: column; gap: 16px; }
        
        .tool-card-item { position: relative; width: 100%; height: 180px; border-radius: 20px; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; padding: 18px; box-shadow: 0 6px 20px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); cursor: pointer; }
        .tool-card-1 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=600&auto=format&fit=crop') center/contain no-repeat, #1f242d; }
        .tool-card-2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=600&auto=format&fit=crop') center/contain no-repeat, #1f242d; }
        .tool-card-3 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=600&auto=format&fit=crop') center/contain no-repeat, #1f242d; }

        .tool-info-box { position: relative; z-index: 2; }
        .tool-main-title { color: #ffffff; font-size: 17px; font-weight: 700; margin-bottom: 4px; text-shadow: 0 2px 4px rgba(0,0,0,0.8); }
        .tool-sub-desc { color: #cbd5e1; font-size: 12px; text-shadow: 0 1px 3px rgba(0,0,0,0.8); }
        .tool-arrow-icon { position: absolute; top: 16px; color: #ffffff; font-size: 16px; font-weight: bold; background: rgba(0,0,0,0.4); width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(5px); }
        [dir="rtl"] .tool-arrow-icon { right: 16px; }
        [dir="ltr"] .tool-arrow-icon { left: 16px; transform: scaleX(-1); }

        .subscription-modal-overlay { display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 999999999; align-items: center; justify-content: center; padding: 15px; }
        .subscription-modal-overlay.hidden { display: none; }
        .subscription-modal-box { background: #1f242d; border: 1.5px solid rgba(255,255,255,0.15); border-radius: 24px; width: 100%; max-width: 420px; max-height: 90vh; overflow-y: auto; padding: 24px 20px; display: flex; flex-direction: column; gap: 16px; position: relative; box-shadow: 0 15px 40px rgba(0,0,0,0.9); }
        .sub-modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px; }
        .sub-modal-title { color: #ffffff; font-size: 18px; font-weight: 700; }
        .sub-modal-close-x { background: rgba(255,255,255,0.1); border: none; color: #ffffff; font-size: 16px; cursor: pointer; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }

        .plans-list { display: flex; flex-direction: column; gap: 12px; }
        .plan-card { background: #282f3d; backdrop-filter: blur(12px); border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 16px; padding: 16px; cursor: pointer; transition: 0.2s; position: relative; }
        .plan-card.selected { border-color: #3b82f6; background: #343d50; box-shadow: 0 0 20px rgba(59, 130, 246, 0.4); }
        .plan-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
        .plan-name { color: #ffffff; font-size: 15px; font-weight: 700; }
        .plan-price { background: rgba(255, 255, 255, 0.12); padding: 4px 10px; border-radius: 10px; color: #ffffff; font-size: 12px; font-weight: 600; }
        .plan-desc { color: #cbd5e1; font-size: 12px; }
        .new-tag { position: absolute; top: 12px; left: 12px; background: #3b82f6; color: #fff; font-size: 10px; padding: 2px 8px; border-radius: 8px; font-weight: 600; }
        .best-value-tag { position: absolute; top: 12px; left: 12px; background: linear-gradient(135deg, #f59e0b, #ec4899); color: #fff; font-size: 10px; padding: 2px 8px; border-radius: 8px; font-weight: 600; }
        .action-main-btn { width: 100%; background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); color: #ffffff; font-size: 15px; font-weight: 700; padding: 14px; border-radius: 20px; border: none; cursor: pointer; text-align: center; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4); margin-top: 10px; }

        #sparkleDialogScreen { background-color: #0b0f19; display: none; flex-direction: column; min-height: 100vh; padding: 20px; position: relative; overflow-y: auto; }
        #sparkleDialogScreen.active { display: flex; }
        .sparkle-top-bar { display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 30px; z-index: 2; }
        .sparkle-upgrade-badge { background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 6px 16px; border-radius: 20px; color: #ffffff; font-size: 13px; font-weight: 500; border: 1px solid rgba(255, 255, 255, 0.2); cursor: pointer; }
        .sparkle-close-btn { background: none; border: none; color: #ffffff; font-size: 20px; cursor: pointer; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; }
        .sparkle-center-content { display: flex; flex-direction: column; align-items: center; text-align: center; z-index: 2; margin-top: 20px; gap: 20px; }
        .sparkle-icon-svg { width: 65px; height: 65px; fill: #93c5fd; filter: drop-shadow(0 0 12px rgba(147, 197, 253, 0.5)); }
        .sparkle-greeting-text { color: #ffffff; font-size: 20px; font-weight: 700; line-height: 1.5; }
        .sparkle-rect-cards-container { display: flex; flex-direction: column; gap: 12px; width: 100%; max-width: 420px; margin-top: 15px; }
        .sparkle-rect-card { background: rgba(20, 25, 40, 0.75); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 16px; padding: 16px 18px; display: flex; align-items: center; justify-content: space-between; cursor: pointer; transition: 0.2s; }
        .sparkle-rect-card:active { background: rgba(30, 40, 65, 0.9); transform: scale(0.98); }
        .sparkle-rect-left { display: flex; align-items: center; gap: 12px; }
        .sparkle-rect-right { display: flex; align-items: center; gap: 12px; }
        .sparkle-card-titles { display: flex; flex-direction: column; gap: 2px; }
        .sparkle-card-main-title { color: #ffffff; font-size: 15px; font-weight: 700; }
        .sparkle-card-sub-title { color: #cbd5e1; font-size: 12px; }

        .login-modal-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 9999999999; align-items: flex-end; justify-content: center; }
        .login-modal-overlay.show { display: flex; }
        .login-modal-content { background: #1f242d; border-top-left-radius: 28px; border-top-right-radius: 28px; border: 1px solid rgba(255,255,255,0.12); width: 100%; max-width: 480px; padding: 24px 20px 40px 20px; display: flex; flex-direction: column; gap: 16px; position: relative; box-shadow: 0 -10px 30px rgba(0,0,0,0.8); }
        .login-modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px; }
        .login-modal-title { color: #ffffff; font-size: 18px; font-weight: 700; }
        .login-close-x { background: none; border: none; color: #ffffff; font-size: 20px; cursor: pointer; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; }
        .login-btn-google { width: 100%; background: #ffffff; color: #1f242d; border-radius: 16px; padding: 14px; font-size: 15px; font-weight: 700; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; }
        .login-btn-email { width: 100%; background: #343d50; color: #ffffff; border-radius: 16px; padding: 14px; font-size: 15px; font-weight: 700; border: 1px solid rgba(255,255,255,0.1); cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; }
        .login-footer-text { text-align: center; color: #cbd5e1; font-size: 13px; margin-top: 10px; cursor: pointer; }
        .login-footer-text span { color: #3b82f6; font-weight: 600; }
        .login-links-row { display: flex; justify-content: center; align-items: center; gap: 15px; color: #cbd5e1; font-size: 11px; margin-top: 5px; }

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

    <div class="subscription-modal-overlay hidden" id="subscriptionModal">
        <div class="subscription-modal-box" onclick="event.stopPropagation()">
            <div class="sub-modal-header">
                <div class="sub-modal-title" data-i18n="upgradeTitle">ترقية الحساب</div>
                <button class="sub-modal-close-x" onclick="closeSubscriptionModal()">✕</button>
            </div>

            <div style="text-align: center; margin-bottom: 5px;">
                <div style="color: #ffffff; font-size: 17px; font-weight: 700; margin-bottom: 4px;" data-i18n="subSubHeading">حول أفكارك إلى PlotCraft</div>
                <div style="color: #cbd5e1; font-size: 12px;" data-i18n="subDesc">أنشئ كل لقطة وعدلها وأكملها بسرعة.</div>
            </div>

            <div class="plans-list">
                <div class="plan-card selected" onclick="selectPlan(this)">
                    <div class="plan-top">
                        <div class="plan-name">PlotCraft Pro Weekly</div>
                        <div class="plan-price" data-i18n="priceWeekly">9.99 دولار أمريكي / أسبوع</div>
                    </div>
                    <div class="plan-desc" data-i18n="descWeekly">500 نقطة / أسبوعياً، جرب PlotCraft</div>
                </div>

                <div class="plan-card" onclick="selectPlan(this)">
                    <div class="new-tag" data-i18n="newTag">جديد</div>
                    <div class="plan-top">
                        <div class="plan-name">PlotCraft Pro Monthly</div>
                        <div class="plan-price" data-i18n="priceMonthly">29.99 دولار أمريكي / شهر</div>
                    </div>
                    <div class="plan-desc" data-i18n="descMonthly">1800 نقطة / شهرياً، مثالي للمبدعين</div>
                </div>

                <div class="plan-card" onclick="selectPlan(this)">
                    <div class="best-value-tag" data-i18n="bestValue">الأفضل قيمة</div>
                    <div class="plan-top">
                        <div class="plan-name">PlotCraft Pro Annual</div>
                        <div class="plan-price" data-i18n="priceAnnual">69.99 دولار أمريكي / سنة</div>
                    </div>
                    <div class="plan-desc" data-i18n="descAnnual">5000 نقطة / سنوياً، إمكانيات غير محدودة</div>
                </div>
            </div>

            <button class="action-main-btn" onclick="openLoginModal()" data-i18n="subscribeBtn">اشتراك</button>
        </div>
    </div>

    <!-- شاشة الإعدادات -->
    <div class="settings-screen" id="settingsScreen">
        <div class="settings-top-bar">
            <button class="settings-close-btn" onclick="closeSettingsScreen(event)" title="رجوع">‹</button>
            <div class="settings-title" data-i18n="settingsTitle">الإعدادات</div>
            <button class="settings-upgrade-badge" onclick="openSubscriptionModal()" data-i18n="upgradeBadge">ترقية</button>
        </div>

        <div class="profile-header-card">
            <div class="profile-avatar-box">
                <svg viewBox="0 0 24 24"><path d="M12 2a2 2 0 0 1 2 2c0 .74-.4 1.39-1 1.73V7h1a7 7 0 0 1 7 7h1a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-1H2a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h1a7 7 0 0 1 7-7h1V5.73C10.4 5.39 10 4.74 10 4a2 2 0 0 1 2-2M7.5 13a1.5 1.5 0 0 0-1.5 1.5A1.5 1.5 0 0 0 7.5 16a1.5 1.5 0 0 0 1.5-1.5A1.5 1.5 0 0 0 7.5 13m9 0a1.5 1.5 0 0 0-1.5 1.5a1.5 1.5 0 0 0 1.5 1.5a1.5 1.5 0 0 0 1.5-1.5a1.5 1.5 0 0 0-1.5-1.5M10 18v2h4v-2z"/></svg>
            </div>
            <div class="profile-info-group">
                <div class="profile-name-row">
                    <span class="profile-name-text" id="displayUserName">NewUser</span>
                    <span class="profile-edit-pencil" onclick="openNameEditModal()" title="تعديل الاسم">
                        <svg viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34a.9959.9959 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
                    </span>
                </div>
                <div class="profile-id-row">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    <span id="displayUniqueId">4422114 ID</span>
                </div>
            </div>
        </div>

        <div class="pro-banner-card">
            <div class="pro-banner-top">
                <div class="pro-banner-title" data-i18n="proBannerTitle">افتح PlotCraft Pro</div>
                <div class="pro-sparkle-icon"></div>
            </div>
            <div class="pro-banner-desc" data-i18n="proBannerDesc">حول كل فكرة إلى فيلم مكتمل</div>
            <button class="pro-banner-btn" onclick="openSubscriptionModal()" data-i18n="proBannerBtn">عرض خطط Pro ←</button>
        </div>

        <div class="settings-group-box">
            <div class="settings-item-row" onclick="handleMenuClick(event, 'points')">
                <div class="settings-item-right">
                    <div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></div>
                    <span data-i18n="pointsRecord">سجل النقاط</span>
                </div>
                <div class="settings-item-left"><span>›</span></div>
            </div>
            <!-- عنصر التعليقات يفتح نافذة كتابة الشكوى/المشكلة لتصل إليك كمطور -->
            <div class="settings-item-row" onclick="openFeedbackModal(event)">
                <div class="settings-item-right">
                    <div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 5H6v-2h8v2zm4-6H6V6h12v2z"/></svg></div>
                    <span data-i18n="feedbackMenu">التعليقات</span>
                </div>
                <div class="settings-item-left"><span>›</span></div>
            </div>
        </div>

        <div class="settings-group-box">
            <div class="settings-item-row" onclick="event.stopPropagation()">
                <div class="settings-item-right">
                    <div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.64 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2zm-2 1H8v-6c0-2.48 1.51-4.5 4-4.5s4 2.02 4 4.5v6z"/></svg></div>
                    <span data-i18n="notificationsMenu">الإشعارات</span>
                </div>
                <div class="settings-item-left">
                    <label class="switch-toggle" onclick="event.stopPropagation()">
                        <input type="checkbox" id="notifSwitch" onchange="handleNotifToggle(this)">
                        <span class="slider-round"></span>
                    </label>
                </div>
            </div>
            <div class="settings-item-row" onclick="openLanguageModal(event)">
                <div class="settings-item-right">
                    <div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95a15.65 15.65 0 0 0-1.38-3.56A8.03 8.03 0 0 1 18.92 8zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2 0 .68.06 1.34.14 2H4.26zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56A8.03 8.03 0 0 1 5.08 16zm2.95-8H5.08a8.03 8.03 0 0 1 4.33-3.56A15.65 15.65 0 0 0 8.03 8zM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96zM14.34 14H9.66c-.09-.65-.16-1.32-.16-2 0-.68.07-1.35.16-2h4.68c.09.65.16 1.32.16 2 0 .68-.07 1.35-.16 2zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95a8.03 8.03 0 0 1-4.33 3.56zM16.36 14c.08-.66.14-1.32.14-2 0-.68-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2h-3.38z"/></svg></div>
                    <span data-i18n="languageMenu">اللغة</span>
                </div>
                <div class="settings-item-left"><span id="currentLangDisplay">العربية</span><span>›</span></div>
            </div>
            <div class="settings-item-row" onclick="handleMenuClick(event, 'telegram')">
                <div class="settings-item-right">
                    <div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69.01-.03.01-.14-.07-.2-.08-.06-.19-.04-.27-.02-.12.03-1.99 1.27-5.62 3.72-.53.36-1.01.54-1.44.53-.47-.02-1.37-.26-2.03-.48-.82-.27-1.47-.42-1.42-.88.03-.24.36-.49 1-.74 3.91-1.7 6.52-2.82 7.83-3.37 3.72-1.56 4.49-1.83 4.99-1.84.11 0 .37.03.54.17.14.12.18.28.2.45-.02.07-.02.13-.05.29z"/></svg></div>
                    <span data-i18n="joinUsMenu">انضم إلينا</span>
                </div>
                <div class="settings-item-left"><span>›</span></div>
            </div>
            <!-- عنصر اتصل بنا الذي يفتح البريد الإلكتروني للمطور مباشرة -->
            <div class="settings-item-row" onclick="openContactEmail(event)">
                <div class="settings-item-right">
                    <div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div>
                    <span data-i18n="contactUsMenu">اتصل بنا</span>
                </div>
                <div class="settings-item-left"><span>›</span></div>
            </div>
        </div>
    </div>

    <!-- نافذة كتابة الشكوى/التعليق لتصل للمطور -->
    <div class="feedback-modal-overlay" id="feedbackModalOverlay" onclick="closeFeedbackModal(event)">
        <div class="feedback-modal-box" onclick="event.stopPropagation()">
            <div style="color:#fff; font-size:16px; font-weight:700;" data-i18n="feedbackModalTitle">أرسل مشكلتك أو تعليقك</div>
            <textarea class="feedback-textarea" id="feedbackTextField" placeholder="اكتب مشكلتك هنا بالتفصيل..."></textarea>
            <button class="notif-allow-btn" onclick="sendDeveloperFeedback(event)" data-i18n="sendBtn">إرسال للمطور</button>
            <button class="notif-deny-btn" onclick="closeFeedbackModal(event)" data-i18n="cancelBtn">إلغاء</button>
        </div>
    </div>

    <!-- نافذة اللغات -->
    <div class="language-modal-overlay" id="languageModalOverlay" onclick="closeLanguageModal(event)">
        <div class="language-modal-box" onclick="event.stopPropagation()">
            <div class="lang-modal-header">
                <div class="lang-modal-title">Select Language</div>
                <button class="lang-modal-close" onclick="closeLanguageModal(event)">✕</button>
            </div>
            <div class="lang-list-container" id="langListContainer">
                <div class="lang-item-row" onclick="changeAppLanguage('ar', 'العربية', this)">Arabic (العربية)</div>
                <div class="lang-item-row selected" onclick="changeAppLanguage('en', 'English', this)">English</div>
                <div class="lang-item-row" onclick="changeAppLanguage('es', 'Spanish', this)">Spanish (Español)</div>
                <div class="lang-item-row" onclick="changeAppLanguage('fr', 'French', this)">French (Français)</div>
                <div class="lang-item-row" onclick="changeAppLanguage('tr', 'Turkish', this))">Turkish (Türkçe)</div>
            </div>
        </div>
    </div>

    <div class="notif-permission-overlay" id="notifPermissionModal" onclick="event.stopPropagation()">
        <div class="notif-permission-box">
            <div class="notif-permission-title" data-i18n="notifAskMsg">هل تريد السماح لتطبيق Plotcraft بإرسال إشعارات إليك؟</div>
            <button class="notif-allow-btn" onclick="allowNotifications(event)" data-i18n="allowBtn">سماح</button>
            <button class="notif-deny-btn" onclick="denyNotifications(event)" data-i18n="denyBtn">عدم السماح</button>
        </div>
    </div>

    <div class="name-edit-modal-overlay" id="nameEditModal" onclick="event.stopPropagation()">
        <div class="name-edit-box">
            <div style="color:#fff; font-size:16px; font-weight:700;" data-i18n="editNameTitle">تعديل اسم المستخدم</div>
            <input type="text" class="name-edit-input" id="editNameInputField" placeholder="أدخل الاسم الجديد">
            <button class="notif-allow-btn" onclick="saveNewUserName(event)" data-i18n="sendBtn">إرسال</button>
            <button class="notif-deny-btn" onclick="closeNameEditModal(event)" data-i18n="cancelBtn">إلغاء</button>
        </div>
    </div>

    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">PlotCraft</div>
                <div class="upgrade-badge" onclick="openSubscriptionModalFromBadge(event)" data-i18n="upgradeBadge">ترقية</div>
            </div>

            <div class="welcome-section">
                <h1 id="greetingHeading">مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>

            <div class="cards-row">
                <div class="interactive-card" onclick="switchScreen('stepByStepScreen', event)">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title" data-i18n="stepByStepCard">خطوة بخطوة</div>
                            <span class="exact-bot-icon"></span>
                        </div>
                    </div>
                    <div class="card-subtitle" data-i18n="stepByStepSub">راجع كل خطوة</div>
                </div>

                <div class="interactive-card" id="speedCard" onclick="handleSpeedCardClick(event)">
                    <div class="pro-badge-top">
                        <span>Pro only</span>
                        <span class="pro-lock-icon"></span>
                    </div>
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title" data-i18n="fastCard">سريع</div>
                            <span class="speed-custom-icon"></span>
                        </div>
                    </div>
                    <div class="card-subtitle" data-i18n="fastSub">إدخال واحد، فيديو كامل</div>
                </div>
            </div>
        </div>

        <div class="inspiration-section">
            <div class="section-header">
                <div class="section-title" data-i18n="inspirationTitle">إلهام بلوت كرافت</div>
                <div class="view-all" data-i18n="viewAll">عرض الكل ></div>
            </div>

            <div class="movies-carousel">
                <div class="movie-card m1" onclick="showCustomAlert('يتم إضافة القصص قريباً')"><div class="movie-title">THE DELIVERYMAN'S SECRET BILLIONAIRE</div></div>
                <div class="movie-card m2" onclick="showCustomAlert('يتم إضافة القصص قريباً')"><div class="movie-title">SECRET BILLIONAIRE</div></div>
                <div class="movie-card m3" onclick="showCustomAlert('يتم إضافة القصص قريباً')"><div class="movie-title">CYBER CITY</div></div>
            </div>
        </div>
    </div>

    <div class="custom-alert-overlay" id="customAlertOverlay" onclick="event.stopPropagation()">
        <div class="custom-alert-box">
            <div class="custom-alert-msg" id="customAlertMsgText">يتم إضافة القصص قريباً</div>
            <button class="custom-alert-btn" onclick="closeCustomAlert(event)" data-i18n="okBtn">حسناً</button>
        </div>
    </div>

    <div id="sparkleDialogScreen" class="screen-view">
        <div class="sparkle-top-bar">
            <button class="sparkle-close-btn" onclick="switchScreen('homeScreen', event)">✕</button>
            <div class="brand-title">Plotcraft</div>
            <div class="sparkle-upgrade-badge" onclick="openSubscriptionModalFromBadge(event)" data-i18n="upgradeBadge">ترقية</div>
        </div>

        <div class="sparkle-center-content">
            <svg class="sparkle-icon-svg" viewBox="0 0 24 24">
                <path d="M12 2C12 7.5 16.5 12 22 12C16.5 12 12 16.5 12 22C12 16.5 7.5 12 2 12C7.5 12 12 7.5 12 2Z"/>
            </svg>
            <div class="sparkle-greeting-text" id="sparkleGreetingText">طاب مساؤك، أيها المخرج<br>أي قصة سنصنع اليوم؟</div>

            <div class="sparkle-rect-cards-container">
                <div class="sparkle-rect-card" onclick="switchScreen('stepByStepScreen', event)">
                    <div class="sparkle-rect-right">
                        <div class="sparkle-card-titles">
                            <div class="sparkle-card-main-title" data-i18n="stepByStepCard">خطوة بخطوة</div>
                            <div class="sparkle-card-sub-title" data-i18n="stepByStepSub">راجع كل خطوة</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="toolsScreen" class="screen-view">
        <div class="tools-header">
            <div class="tools-header-title" data-i18n="toolsTitle">الأدوات</div>
            <div class="tools-upgrade-btn" onclick="openSubscriptionModalFromBadge(event)" data-i18n="upgradeBadge">ترقية</div>
        </div>
        <div class="tools-body">
            <div class="tool-card-item tool-card-1" onclick="showCustomAlert('قريباً')">
                <div class="tool-arrow-icon">‹</div>
                <div class="tool-info-box"><div class="tool-main-title" data-i18n="tool1Title">تأثيرات الفيديو</div><div class="tool-sub-desc" data-i18n="tool1Sub">أضف لمسة سينمائية</div></div>
            </div>
            <div class="tool-card-item tool-card-2" onclick="showCustomAlert('قريباً')">
                <div class="tool-arrow-icon">‹</div>
                <div class="tool-info-box"><div class="tool-main-title" data-i18n="tool2Title">توليد الفيديو</div><div class="tool-sub-desc" data-i18n="tool2Sub">حول توجيهاً إلى فيديو خاص بك</div></div>
            </div>
        </div>
    </div>

    <div id="worksScreen" class="screen-view">
        <div class="works-top-header">
            <div class="works-screen-title" data-i18n="worksTitle">الأعمال</div>
            <div class="works-header-left-group">
                <div class="works-upgrade-badge" onclick="openSubscriptionModalFromBadge(event)" data-i18n="upgradeBadge">ترقية</div>
                <div class="works-robot-logo" onclick="openSettingsScreen(event)" title="الإعدادات"></div>
            </div>
        </div>

        <div class="works-body-container">
            <div class="works-tabs-container">
                <div class="works-tab active" onclick="switchWorksTab(this)" data-i18n="projectsTab">المشاريع</div>
                <div class="works-tab" onclick="switchWorksTab(this)" data-i18n="mediaTab">مكتبة الوسائط</div>
            </div>
            <div class="works-empty-content">
                <div class="works-box-icon"></div>
                <div class="works-empty-text-sub" data-i18n="emptyWorksText">ستظهر هنا مشاريع القصة الخاصة بك.</div>
                <button class="works-create-btn" onclick="openSparkleDialog(event)" data-i18n="createStoryBtn">إنشاء قصة</button>
            </div>
        </div>
    </div>

    <div class="plotcraft-nav-bar" id="mainNavBar">
        <div class="plotcraft-nav-pill">
            <a href="#" class="plotcraft-nav-item active" id="navHome" onclick="switchScreen('homeScreen', event); setActiveNav('navHome')">
                <span data-i18n="navHome">الرئيسية</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            </a>
            <a href="#" class="plotcraft-nav-item" id="navTools" onclick="switchScreen('toolsScreen', event); setActiveNav('navTools')">
                <span data-i18n="navTools">الأدوات</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
            </a>
            <a href="#" class="plotcraft-nav-item" id="navWorks" onclick="switchScreen('worksScreen', event); setActiveNav('navWorks')">
                <span data-i18n="navWorks">الأعمال</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path></svg>
            </a>
        </div>

        <div class="plotcraft-nav-square" onclick="openSparkleDialog(event)" title="إنشاء سريع">
            <svg width="26" height="26" viewBox="0 0 24 24">
                <rect x="3" y="6" width="14" height="12" rx="3" fill="#cbd5e1"/>
            </svg>
        </div>
    </div>

    <script>
        // قاموس ترجمة نصوص التطبيق الحية بالكامل
        const translations = {
            ar: {
                upgradeBadge: "ترقية",
                greeting: "مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟",
                stepByStepCard: "خطوة بخطوة",
                stepByStepSub: "راجع كل خطوة",
                fastCard: "سريع",
                fastSub: "إدخال واحد، فيديو كامل",
                inspirationTitle: "إلهام بلوت كرافت",
                viewAll: "عرض الكل >",
                toolsTitle: "الأدوات",
                worksTitle: "الأعمال",
                projectsTab: "المشاريع",
                mediaTab: "مكتبة الوسائط",
                emptyWorksText: "ستظهر هنا مشاريع القصة الخاصة بك.",
                createStoryBtn: "إنشاء قصة",
                navHome: "الرئيسية",
                navTools: "الأدوات",
                navWorks: "الأعمال",
                settingsTitle: "الإعدادات",
                proBannerTitle: "افتح PlotCraft Pro",
                proBannerDesc: "حول كل فكرة إلى فيلم مكتمل",
                proBannerBtn: "عرض خطط Pro ←",
                pointsRecord: "سجل النقاط",
                feedbackMenu: "التعليقات",
                notificationsMenu: "الإشعارات",
                languageMenu: "اللغة",
                joinUsMenu: "انضم إلينا",
                contactUsMenu: "اتصل بنا",
                upgradeTitle: "ترقية الحساب",
                subSubHeading: "حول أفكارك إلى PlotCraft",
                subDesc: "أنشئ كل لقطة وعدلها وأكملها بسرعة.",
                priceWeekly: "9.99 دولار أمريكي / أسبوع",
                descWeekly: "500 نقطة / أسبوعياً، جرب PlotCraft",
                newTag: "جديد",
                priceMonthly: "29.99 دولار أمريكي / شهر",
                descMonthly: "1800 نقطة / شهرياً، مثالي للمبدعين",
                bestValue: "الأفضل قيمة",
                priceAnnual: "69.99 دولار أمريكي / سنة",
                descAnnual: "5000 نقطة / سنوياً، إمكانيات غير محدودة",
                subscribeBtn: "اشتراك",
                okBtn: "حسناً",
                cancelBtn: "إلغاء",
                sendBtn: "إرسال",
                editNameTitle: "تعديل اسم المستخدم",
                notifAskMsg: "هل تريد السماح لتطبيق Plotcraft بإرسال إشعارات إليك؟",
                allowBtn: "سماح",
                denyBtn: "عدم السماح",
                feedbackModalTitle: "أرسل مشكلتك أو تعليقك للمطور",
                tool1Title: "تأثيرات الفيديو",
                tool1Sub: "أضف لمسة سينمائية",
                tool2Title: "توليد الفيديو",
                tool2Sub: "حول توجيهاً إلى فيديو خاص بك"
            },
            en: {
                upgradeBadge: "Upgrade",
                greeting: "Good evening, Director<br>What story shall we make today?",
                stepByStepCard: "Step-by-Step",
                stepByStepSub: "Review every step",
                fastCard: "Fast",
                fastSub: "One input, full video",
                inspirationTitle: "PlotCraft Inspiration",
                viewAll: "View All >",
                toolsTitle: "Tools",
                worksTitle: "Works",
                projectsTab: "Projects",
                mediaTab: "Media Library",
                emptyWorksText: "Your story projects will appear here.",
                createStoryBtn: "Create Story",
                navHome: "Home",
                navTools: "Tools",
                navWorks: "Works",
                settingsTitle: "Settings",
                proBannerTitle: "Unlock PlotCraft Pro",
                proBannerDesc: "Turn every idea into a complete film",
                proBannerBtn: "View Pro Plans ←",
                pointsRecord: "Points History",
                feedbackMenu: "Feedback",
                notificationsMenu: "Notifications",
                languageMenu: "Language",
                joinUsMenu: "Join Us",
                contactUsMenu: "Contact Us",
                upgradeTitle: "Account Upgrade",
                subSubHeading: "Turn your ideas into PlotCraft",
                subDesc: "Create, edit, and complete every shot quickly.",
                priceWeekly: "$9.99 USD / week",
                descWeekly: "500 points / week, try PlotCraft",
                newTag: "NEW",
                priceMonthly: "$29.99 USD / month",
                descMonthly: "1800 points / month, ideal for creators",
                bestValue: "BEST VALUE",
                priceAnnual: "$69.99 USD / year",
                descAnnual: "5000 points / year, unlimited cinematic power",
                subscribeBtn: "Subscribe",
                okBtn: "OK",
                cancelBtn: "Cancel",
                sendBtn: "Send",
                editNameTitle: "Edit Username",
                notifAskMsg: "Do you want to allow Plotcraft to send you notifications?",
                allowBtn: "Allow",
                denyBtn: "Don't Allow",
                feedbackModalTitle: "Send your feedback to developer",
                tool1Title: "Video Effects",
                tool1Sub: "Add a cinematic touch",
                tool2Title: "Video Generation",
                tool2Sub: "Turn a prompt into your video"
            },
            es: {
                upgradeBadge: "Mejorar",
                greeting: "Buenas tardes, Director<br>¿Qué historia haremos hoy?",
                stepByStepCard: "Paso a paso",
                stepByStepSub: "Revisar cada paso",
                fastCard: "Rápido",
                fastSub: "Una entrada, video completo",
                inspirationTitle: "Inspiración PlotCraft",
                viewAll: "Ver todo >",
                toolsTitle: "Herramientas",
                worksTitle: "Obras",
                projectsTab: "Proyectos",
                mediaTab: "Biblioteca",
                emptyWorksText: "Tus proyectos de historias aparecerán aquí.",
                createStoryBtn: "Crear Historia",
                navHome: "Inicio",
                navTools: "Herramientas",
                navWorks: "Obras",
                settingsTitle: "Configuración",
                proBannerTitle: "Desbloquear PlotCraft Pro",
                proBannerDesc: "Convierte cada idea en una película completa",
                proBannerBtn: "Ver planes Pro ←",
                pointsRecord: "Historial de puntos",
                feedbackMenu: "Comentarios",
                notificationsMenu: "Notificaciones",
                languageMenu: "Idioma",
                joinUsMenu: "Únete",
                contactUsMenu: "Contáctanos",
                upgradeTitle: "Mejorar Cuenta",
                subSubHeading: "Convierte tus ideas",
                subDesc: "Crea y edita rápidamente.",
                priceWeekly: "$9.99 USD / semana",
                descWeekly: "500 puntos / semana",
                newTag: "NUEVO",
                priceMonthly: "$29.99 USD / mes",
                descMonthly: "1800 puntos / mes",
                bestValue: "MEJOR VALOR",
                priceAnnual: "$69.99 USD / año",
                descAnnual: "5000 puntos / año",
                subscribeBtn: "Suscribirse",
                okBtn: "Aceptar",
                cancelBtn: "Cancelar",
                sendBtn: "Enviar",
                editNameTitle: "Editar Nombre",
                notifAskMsg: "¿Permitir notificaciones?",
                allowBtn: "Permitir",
                denyBtn: "No permitir",
                feedbackModalTitle: "Enviar comentarios al desarrollador",
                tool1Title: "Efectos de video",
                tool1Sub: "Añade toque cinemático",
                tool2Title: "Generación de video",
                tool2Sub: "Convierte texto en video"
            },
            fr: {
                upgradeBadge: "Mettre à niveau",
                greeting: "Bonsoir, Réalisateur<br>Quelle histoire ferons-nous aujourd'hui?",
                stepByStepCard: "Étape par étape",
                stepByStepSub: "Vérifier chaque étape",
                fastCard: "Rapide",
                fastSub: "Une entrée, vidéo complète",
                inspirationTitle: "Inspiration PlotCraft",
                viewAll: "Voir tout >",
                toolsTitle: "Outils",
                worksTitle: "Œuvres",
                projectsTab: "Projets",
                mediaTab: "Médiathèque",
                emptyWorksText: "Vos projets d'histoires apparaîtront ici.",
                createStoryBtn: "Créer une histoire",
                navHome: "Accueil",
                navTools: "Outils",
                navWorks: "Œuvres",
                settingsTitle: "Paramètres",
                proBannerTitle: "Débloquer PlotCraft Pro",
                proBannerDesc: "Transformez chaque idée en film",
                proBannerBtn: "Voir les offres Pro ←",
                pointsRecord: "Historique des points",
                feedbackMenu: "Commentaires",
                notificationsMenu: "Notifications",
                languageMenu: "Langue",
                joinUsMenu: "Rejoignez-nous",
                contactUsMenu: "Contactez-nous",
                upgradeTitle: "Mise à niveau",
                subSubHeading: "Transformez vos idées",
                subDesc: "Créez et éditez rapidement.",
                priceWeekly: "$9.99 USD / semaine",
                descWeekly: "500 points / semaine",
                newTag: "NOUVEAU",
                priceMonthly: "$29.99 USD / mois",
                descMonthly: "1800 points / mois",
                bestValue: "MEILLEURE OFFRE",
                priceAnnual: "$69.99 USD / an",
                descAnnual: "5000 points / an",
                subscribeBtn: "S'abonner",
                okBtn: "OK",
                cancelBtn: "Annuler",
                sendBtn: "Envoyer",
                editNameTitle: "Modifier le nom",
                notifAskMsg: "Autoriser les notifications?",
                allowBtn: "Autoriser",
                denyBtn: "Ne pas autoriser",
                feedbackModalTitle: "Envoyer vos commentaires au développeur",
                tool1Title: "Effets vidéo",
                tool1Sub: "Ajouter une touche cinématique",
                tool2Title: "Génération vidéo",
                tool2Sub: "Transformer un texte en vidéo"
            },
            tr: {
                upgradeBadge: "Yükselt",
                greeting: "İyi akşamlar, Yönetmen<br>Bugün hangi hikayeyi yapacağız?",
                stepByStepCard: "Adım Adım",
                stepByStepSub: "Her adımı gözden geçir",
                fastCard: "Hızlı",
                fastSub: "Tek girdi, tam video",
                inspirationTitle: "PlotCraft İlhamı",
                viewAll: "Tümünü Gör >",
                toolsTitle: "Araçlar",
                worksTitle: "Çalışmalar",
                projectsTab: "Projeler",
                mediaTab: "Medya Kitaplığı",
                emptyWorksText: "Hikaye projeleriniz burada görünecek.",
                createStoryBtn: "Hikaye Oluştur",
                navHome: "Ana Sayfa",
                navTools: "Araçlar",
                navWorks: "Çalışmalar",
                settingsTitle: "Ayarlar",
                proBannerTitle: "PlotCraft Pro'yu Aç",
                proBannerDesc: "Her fikri tam bir filme dönüştür",
                proBannerBtn: "Pro Planları Gör ←",
                pointsRecord: "Puan Geçmişi",
                feedbackMenu: "Geri Bildirim",
                notificationsMenu: "Bildirimler",
                languageMenu: "Dil",
                joinUsMenu: "Bize Katılın",
                contactUsMenu: "İletişim",
                upgradeTitle: "Hesabı Yükselt",
                subSubHeading: "Fikirlerinizi dönüştürün",
                subDesc: "Hızlıca oluşturun ve düzenleyin.",
                priceWeekly: "$9.99 USD / hafta",
                descWeekly: "500 puan / hafta",
                newTag: "YENİ",
                priceMonthly: "$29.99 USD / ay",
                descMonthly: "1800 puan / ay",
                bestValue: "EN İYİ DEĞER",
                priceAnnual: "$69.99 USD / yıl",
                descAnnual: "5000 puan / yıl",
                subscribeBtn: "Abone Ol",
                okBtn: "Tamam",
                cancelBtn: "İptal",
                sendBtn: "Gönder",
                editNameTitle: "Kullanıcı Adını Düzenle",
                notifAskMsg: "Bildirim gönderilmesine izin verilsin mi?",
                allowBtn: "İzin Ver",
                denyBtn: "İzin Verme",
                feedbackModalTitle: "Geri bildiriminizi geliştiriciye gönderin",
                tool1Title: "Video Efektleri",
                tool1Sub: "Sinematik dokunuş ekle",
                tool2Title: "Video Üretimi",
                tool2Sub: "Komutu videoya dönüştür"
            }
        };

        let currentLang = 'ar';
        let currentUploadedImageSrc = "";
        let characterAdded = false;
        let storyAdded = false;
        let savedStoryText = "";

        let userUniqueId = Math.floor(1000000 + Math.random() * 9000000);
        document.getElementById('displayUniqueId').innerText = userUniqueId + " ID";

        document.addEventListener('click', function(event) {
            if (event.target.tagName === 'BUTTON' || event.target.closest('button') || event.target.closest('.interactive-card') || event.target.closest('.plotcraft-nav-item') || event.target.closest('.plotcraft-nav-square') || event.target.closest('.works-tab') || event.target.closest('.plan-card') || event.target.closest('.char-thumb-item') || event.target.closest('.settings-item-row') || event.target.closest('.movie-card') || event.target.closest('.sparkle-rect-card') || event.target.closest('.lang-item-row')) {
                if ("vibrate" in navigator) {
                    navigator.vibrate(35);
                }
            }
        });

        // تغيير لغة التطبيق وتحديث النصوص والاتجاه بالكامل (RTL / LTR)
        function changeAppLanguage(langCode, langDisplayName, element) {
            currentLang = langCode;
            document.getElementById('currentLangDisplay').innerText = langDisplayName;
            
            var rows = document.querySelectorAll('.lang-item-row');
            rows.forEach(r => r.classList.remove('selected'));
            element.classList.add('selected');

            var htmlRoot = document.getElementById('htmlRoot');
            if (langCode === 'ar') {
                htmlRoot.setAttribute('dir', 'rtl');
                htmlRoot.setAttribute('lang', 'ar');
            } else {
                htmlRoot.setAttribute('dir', 'ltr');
                htmlRoot.setAttribute('lang', langCode);
            }

            // تحديث جميع النصوص التي تحمل مفتاح الترجمة data-i18n
            const dict = translations[langCode];
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dict[key]) {
                    el.innerText = dict[key];
                }
            });

            // تحديث عناصر محددة تحمل HTML (مثل التحيات)
            if (dict['greeting']) {
                document.getElementById('greetingHeading').innerHTML = dict['greeting'];
                document.getElementById('sparkleGreetingText').innerHTML = dict['greeting'];
            }

            setTimeout(() => {
                closeLanguageModal();
            }, 150);
        }

        // 3. الخطوة الثالثة: اتصل بنا (التحويل المباشر لبريدك الإلكتروني كمطور)
        function openContactEmail(event) {
            if (event) event.stopPropagation();
            const developerEmail = "your-email@example.com"; // استبدل هذا بإيميلك الشخصي الفعلي
            const subject = encodeURIComponent("Support - PlotCraft App");
            const body = encodeURIComponent("Hello Developer,\n\nI need help regarding: ");
            window.location.href = `mailto:${developerEmail}?subject=${subject}&body=${body}`;
        }

        // فتح نافذة التعليقات لإرسال المشكلة للمطور
        function openFeedbackModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('feedbackTextField').value = "";
            document.getElementById('feedbackModalOverlay').classList.add('show');
        }

        function closeFeedbackModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('feedbackModalOverlay').classList.remove('show');
        }

        function sendDeveloperFeedback(event) {
            if (event) event.stopPropagation();
            const feedbackText = document.getElementById('feedbackTextField').value.trim();
            if (feedbackText === "") {
                showCustomAlert(currentLang === 'ar' ? "يرجى كتابة المشكلة أولاً" : "Please write your feedback first");
                return;
            }
            // هنا كمطور يمكنك ربطها لاحقاً بسيرفر أو إيميل، حالياً سنعرض تأكيد للإرسال
            closeFeedbackModal();
            showCustomAlert(currentLang === 'ar' ? "تم إرسال تعليقك إلى المطور بنجاح. شكراً لك!" : "Feedback sent successfully. Thank you!");
        }

        function switchScreen(screenId, event) {
            if (event) event.preventDefault();
            var screens = document.querySelectorAll('.screen-view');
            screens.forEach(s => s.classList.remove('active'));
            document.getElementById(screenId).classList.add('active');
            
            var navBar = document.getElementById('mainNavBar');
            if (screenId === 'sparkleDialogScreen' || screenId === 'addCharacterScreen' || screenId === 'storyDescriptionScreen') {
                navBar.classList.add('hidden');
            } else {
                navBar.classList.remove('hidden');
            }
            window.scrollTo(0, 0);
        }

        function openSubscriptionModal() {
            document.getElementById('subscriptionModal').classList.remove('hidden');
        }

        function closeSubscriptionModal() {
            document.getElementById('subscriptionModal').classList.add('hidden');
        }

        function openSubscriptionModalFromBadge(event) {
            if (event) event.preventDefault();
            event.stopPropagation();
            openSubscriptionModal();
        }

        function openSparkleDialog(event) {
            if (event) event.stopPropagation();
            switchScreen('sparkleDialogScreen', event);
            document.getElementById('mainNavBar').classList.add('hidden');
        }

        function openSettingsScreen(event) {
            if (event) event.stopPropagation();
            document.getElementById('settingsScreen').classList.add('active');
            document.getElementById('mainNavBar').classList.add('hidden');
        }

        function closeSettingsScreen(event) {
            if (event) event.stopPropagation();
            document.getElementById('settingsScreen').classList.remove('active');
            document.getElementById('mainNavBar').classList.remove('hidden');
        }

        function openLanguageModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('languageModalOverlay').classList.add('show');
        }

        function closeLanguageModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('languageModalOverlay').classList.remove('show');
        }

        function handleMenuClick(event, type) {
            if (event) event.stopPropagation();
            if (type === 'points') {
                showCustomAlert(currentLang === 'ar' ? "سجل النقاط فارغ حالياً" : "Points history is currently empty");
            } else if (type === 'telegram') {
                showCustomAlert(currentLang === 'ar' ? "قريباً قناة التليجرام" : "Telegram channel coming soon");
            }
        }

        function handleNotifToggle(checkbox) {
            if (checkbox.checked) {
                document.getElementById('notifPermissionModal').style.display = 'flex';
            } else {
                showCustomAlert(currentLang === 'ar' ? "تم تعطيل الإشعارات" : "Notifications disabled");
            }
        }

        function allowNotifications(event) {
            if (event) event.stopPropagation();
            document.getElementById('notifPermissionModal').style.display = 'none';
            showCustomAlert(currentLang === 'ar' ? "تم تفعيل الإشعارات بنجاح!" : "Notifications enabled successfully!");
        }

        function denyNotifications(event) {
            if (event) event.stopPropagation();
            document.getElementById('notifPermissionModal').style.display = 'none';
            document.getElementById('notifSwitch').checked = false;
        }

        function openNameEditModal() {
            document.getElementById('editNameInputField').value = document.getElementById('displayUserName').innerText;
            document.getElementById('nameEditModal').style.display = 'flex';
        }

        function closeNameEditModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('nameEditModal').style.display = 'none';
        }

        function saveNewUserName(event) {
            if (event) event.stopPropagation();
            var val = document.getElementById('editNameInputField').value.trim();
            if (val !== "") {
                document.getElementById('displayUserName').innerText = val;
            }
            closeNameEditModal();
        }

        function setActiveNav(navId) {
            var items = document.querySelectorAll('.plotcraft-nav-item');
            items.forEach(i => i.classList.remove('active'));
            document.getElementById(navId).classList.add('active');
        }

        function switchWorksTab(element) {
            var tabs = document.querySelectorAll('.works-tab');
            tabs.forEach(t => t.classList.remove('active'));
            element.classList.add('active');
        }

        function selectPlan(element) {
            var cards = document.querySelectorAll('.plan-card');
            cards.forEach(c => c.classList.remove('selected'));
            element.classList.add('selected');
        }

        function openLoginModal() {
            document.getElementById('loginModalOverlay').classList.add('show');
        }

        function closeLoginModal() {
            document.getElementById('loginModalOverlay').classList.remove('show');
        }

        function showCustomAlert(message) {
            document.getElementById('customAlertMsgText').innerText = message;
            document.getElementById('customAlertOverlay').classList.add('show');
        }

        function closeCustomAlert(event) {
            if (event) event.stopPropagation();
            document.getElementById('customAlertOverlay').classList.remove('show');
        }

        function handleSpeedCardClick(event) {
            openSubscriptionModal();
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=680, scrolling=True)
