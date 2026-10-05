import streamlit as st
import streamlit.components.v1 as components

# إعداد صفحة ستريمليت لإزالة الهوامش واستغلال الشاشة بالكامل
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

        .screen-view {
            display: none;
            width: 100%;
            min-height: 100vh;
            background-color: #0b0f19;
            flex-direction: column;
            padding-bottom: 90px;
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

        .exact-bot-icon {
            width: 22px;
            height: 22px;
            background: #dbeafe;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            background-size: contain;
        }

        .card-title-group-left {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .magic-wand-icon {
            width: 22px;
            height: 22px;
            background: #dbeafe;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M7.5 5.6c-.3-.3-.8-.3-1.1 0-.3.3-.3.8 0 1.1 1.2 1.2 1.9 2.8 1.9 4.5 0 1.7-.7 3.3-1.9 4.5-.3.3-.3.8 0 1.1.3.3.8.3 1.1 0 1.5-1.5 2.3-3.5 2.3-5.6s-.8-4.1-2.3-5.6zm4.3-2.3c-.3-.3-.8-.3-1.1 0-.3.3-.3.8 0 1.1 2.2 2.2 3.4 5.1 3.4 8.2s-1.2 6-3.4 8.2c-.3.3-.3.8 0 1.1.3.3.8.3 1.1 0 2.6-2.6 4-6 4-9.3s-1.4-6.7-4-9.3zm4.4-2.3c-.3-.3-.8-.3-1.1 0-.3.3-.3.8 0 1.1 3.1 3.1 4.9 7.3 4.9 11.6s-1.8 8.5-4.9 11.6c-.3.3-.3.8 0 1.1.3.3.8.3 1.1 0 3.5-3.5 5.4-8.1 5.4-12.7s-1.9-9.2-5.4-12.7zm-7.6 15.6l-8.5 8.5c-.4.4-.4 1 0 1.4s1 .4 1.4 0l8.5-8.5c.4-.4.4-1 0-1.4s-1-.4-1.4 0zm11.4-11.4l-3.5 3.5c-.4.4-.4 1 0 1.4s1 .4 1.4 0l3.5-3.5c.4-.4.4-1 0-1.4s-1-.4-1.4 0zm-15 3.5l-3.5 3.5c-.4.4-.4 1 0 1.4s1 .4 1.4 0l3.5-3.5c.4-.4.4-1 0-1.4s-1-.4-1.4 0z"/></svg>') no-repeat center;
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
            transition: 0.2s;
        }

        .movie-card:active {
            transform: scale(0.96);
        }

        .movie-card.emily-cover { 
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(11,15,25,0.92) 100%), 
                        url('https://images.unsplash.com/photo-1509967419530-da38b4704bc6?q=80&w=300&auto=format&fit=crop') center/cover; 
            border: 1.5px solid rgba(59, 130, 246, 0.5);
        }
        .movie-card.m2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m3 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=300&auto=format&fit=crop') center/cover; }

        .movie-title {
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
            line-height: 1.2;
        }

        /* نافذة عرض القصة المنبثقة (Modal) */
        .story-modal-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(11, 15, 25, 0.85);
            backdrop-filter: blur(8px);
            z-index: 9999999;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .story-modal-overlay.active {
            display: flex;
        }

        .story-modal-content {
            background: #141824;
            border: 1px solid rgba(59, 130, 246, 0.3);
            border-radius: 20px;
            width: 100%;
            max-width: 500px;
            max-height: 85vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }

        .story-modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 20px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            background: #1a2234;
        }

        .story-modal-title {
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
        }

        .story-modal-close {
            background: rgba(255,255,255,0.1);
            border: none;
            color: #fff;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .story-modal-body {
            padding: 20px;
            overflow-y: auto;
            color: #cbd5e1;
            font-size: 13px;
            line-height: 1.8;
            text-align: left;
            direction: ltr;
            white-space: pre-line;
        }

        .story-modal-footer {
            padding: 14px 20px;
            background: #1a2234;
            border-top: 1px solid rgba(255,255,255,0.08);
            display: flex;
            justify-content: flex-end;
        }

        .copy-story-btn {
            background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
        }

        /* الشاشات الأخرى للتنقل */
        .step-container { padding: 20px; display: flex; flex-direction: column; gap: 16px; }
        .ai-assistant-card { background: #141824; border: 1px solid #1e293b; border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 8px; }
        .ai-header-row { display: flex; justify-content: space-between; align-items: center; }
        .ai-title { color: #ff2a85; font-size: 14px; font-weight: 700; }
        .ai-badge-circle { width: 32px; height: 32px; background: linear-gradient(135deg, #ff2a85, #7928ca); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 11px; }
        .ai-desc { color: #94a3b8; font-size: 12px; }
        .story-setup-box { background: #141824; border: 1px solid #1e293b; border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 12px; }
        .setup-header-row { display: flex; justify-content: space-between; align-items: center; }
        .setup-main-title { color: #ffffff; font-size: 15px; font-weight: 700; }
        .counter-badge { background-color: #1e293b; color: #94a3b8; padding: 3px 10px; border-radius: 10px; font-size: 11px; }
        .setup-row-item { background: #1a2234; border-radius: 12px; padding: 12px; display: flex; justify-content: space-between; align-items: center; }
        .item-info h4 { color: #ffffff; font-size: 13px; font-weight: 700; margin-bottom: 2px; }
        .item-info p { color: #94a3b8; font-size: 11px; }
        .action-add-btn { background: rgba(59, 130, 246, 0.15); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.3); padding: 6px 14px; border-radius: 8px; font-size: 12px; cursor: pointer; }
        .upload-section-hidden, .story-textarea-hidden { display: none; background: #111827; border: 1px solid #374151; border-radius: 10px; padding: 12px; color: #ffffff; font-size: 13px; }
        .upload-section-hidden.show, .story-textarea-hidden.show { display: block; }
        .story-textarea-hidden { width: 100%; min-height: 100px; outline: none; resize: vertical; text-align: right; }
        .bottom-next-row { display: flex; justify-content: flex-end; margin-top: 10px; }
        .side-next-btn { background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); color: #ffffff; font-size: 14px; font-weight: 700; padding: 10px 24px; border-radius: 12px; border: none; cursor: pointer; }

        #subscriptionScreen { background: #0b0f19; overflow: hidden; position: relative; }
        .page-header { display: flex; align-items: center; justify-content: space-between; padding: 20px; border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(11, 15, 25, 0.75); }
        .back-btn { background: rgba(255,255,255,0.1); border: none; color: #fff; width: 36px; height: 36px; border-radius: 50%; font-size: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
        .page-title-text { color: #ffffff; font-size: 18px; font-weight: 700; }
        .content-body { padding: 20px; display: flex; flex-direction: column; gap: 16px; }
        .plans-list { display: flex; flex-direction: column; gap: 12px; }
        .plan-card { background: rgba(20, 25, 40, 0.85); border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 16px; padding: 16px; cursor: pointer; position: relative; }
        .plan-card.selected { border-color: #3b82f6; background: rgba(30, 41, 75, 0.95); }
        .plan-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
        .plan-name { color: #ffffff; font-size: 15px; font-weight: 700; }
        .plan-price { background: rgba(255, 255, 255, 0.12); padding: 4px 10px; border-radius: 10px; color: #ffffff; font-size: 12px; }
        .plan-desc { color: #94a3b8; font-size: 12px; }
        .action-main-btn { width: 100%; background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); color: #ffffff; font-size: 15px; font-weight: 700; padding: 14px; border-radius: 20px; border: none; cursor: pointer; margin-top: 10px; }

        /* نافذة Google Play */
        .gplay-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            z-index: 99999999;
            align-items: flex-end;
        }
        .gplay-overlay.active {
            display: flex;
        }
        .gplay-sheet {
            background: #121316;
            width: 100%;
            border-top-left-radius: 28px;
            border-top-right-radius: 28px;
            padding: 16px 20px 28px 20px;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 -10px 30px rgba(0,0,0,0.8);
            border-top: 1px solid rgba(255,255,255,0.08);
        }
        .gplay-top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .gplay-close {
            background: none;
            border: none;
            color: #e8eaed;
            font-size: 20px;
            cursor: pointer;
        }
        .gplay-store-title {
            color: #e8eaed;
            font-size: 15px;
            font-weight: 500;
        }
        .gplay-app-header {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 8px;
            margin-top: 4px;
            margin-bottom: 6px;
        }
        .gplay-app-icon {
            width: 48px;
            height: 48px;
            background: #202124;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .gplay-app-icon img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .gplay-app-details h3 {
            font-size: 16px;
            font-weight: 700;
            color: #e8eaed;
            margin-bottom: 2px;
        }
        .gplay-app-details p {
            font-size: 12px;
            color: #9aa0a6;
        }
        .gplay-price-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 15px;
            font-weight: 600;
            color: #e8eaed;
            margin-top: 4px;
        }
        .gplay-tax-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
            color: #9aa0a6;
            padding-bottom: 14px;
            border-bottom: 1px solid #2d3139;
        }
        .gplay-notes {
            display: flex;
            flex-direction: column;
            gap: 10px;
            font-size: 12px;
            color: #9aa0a6;
            line-height: 1.5;
            padding-bottom: 14px;
            border-bottom: 1px solid #2d3139;
        }
        .gplay-points-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
            color: #e8eaed;
            padding: 4px 0;
        }
        .gplay-points-diamond {
            display: flex;
            gap: 3px;
            align-items: center;
        }
        .gplay-payment-box {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 6px 0;
            cursor: pointer;
        }
        .gplay-payment-info {
            display: flex;
            align-items: center;
            gap: 12px;
            text-align: right;
            direction: rtl;
        }
        .gplay-subscribe-btn {
            width: 100%;
            background: #8ab4f8;
            color: #202124;
            font-size: 15px;
            font-weight: 700;
            padding: 14px;
            border-radius: 28px;
            border: none;
            cursor: pointer;
            text-align: center;
            margin-top: 8px;
        }

        /* قائمة اختيار طريقة الدفع الفرعية */
        .payment-selector-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 999999999;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .payment-selector-modal.active {
            display: flex;
        }
        .payment-selector-content {
            background: #1f2228;
            border-radius: 16px;
            width: 100%;
            max-width: 380px;
            padding: 20px;
            color: #fff;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .payment-option-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: #282c34;
            border-radius: 12px;
            cursor: pointer;
        }

        /* شريط التنقل السفلي */
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 75px;
            background: rgba(15, 20, 32, 0.95);
            backdrop-filter: blur(20px);
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 0 10px;
            z-index: 99999;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 4px;
            color: #64748b;
            font-size: 11px;
            font-weight: 500;
            cursor: pointer;
            flex: 1;
            transition: 0.2s;
        }

        .nav-item.active {
            color: #3b82f6;
        }

        .nav-icon {
            width: 24px;
            height: 24px;
            background-color: currentColor;
            mask-size: contain;
            -webkit-mask-size: contain;
            mask-repeat: no-repeat;
            -webkit-mask-repeat: no-repeat;
            mask-position: center;
            -webkit-mask-position: center;
        }

        .icon-home { mask-url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>'); -webkit-mask-url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>'); }
        .icon-create { mask-url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>'); -webkit-mask-url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>'); }
        .icon-library { mask-url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4 6H2v14c0 1.1.9 2 2 2h14v-2H4V6zm16-4H8c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0-2-.9-2-2V4c0-1.1-.9-2-2-2zm0 14H8V4h12v12z"/></svg>'); -webkit-mask-url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4 6H2v14c0 1.1.9 2 2 2h14v-2H4V6zm16-4H8c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0-2-.9-2-2V4c0-1.1-.9-2-2-2zm0 14H8V4h12v12z"/></svg>'); }
        .icon-profile { mask-url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg>'); -webkit-mask-url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg>'); }

    </style>
</head>
<body>

    <!-- الشاشة الرئيسية (Home) -->
    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">PlotCraft</div>
                <div class="upgrade-badge" onclick="switchScreen('subscriptionScreen')">
                    <span>⚡ ترقية الباقة</span>
                </div>
            </div>
            
            <div class="welcome-section">
                <h1>اصنع قصتك السينمائية<br>الاحترافية بالذكاء الاصطناعي</h1>
            </div>

            <div class="cards-row">
                <div class="interactive-card" onclick="switchScreen('createScreen')">
                    <div class="card-header-row">
                        <div class="card-title">إنشاء فيلم</div>
                        <div class="exact-bot-icon"></div>
                    </div>
                    <div class="card-subtitle">توليد تلقائي بالكامل</div>
                </div>

                <div class="interactive-card" onclick="switchScreen('createScreen')">
                    <div class="card-header-row">
                        <div class="card-title">مساعد السيناريو</div>
                        <div class="magic-wand-icon"></div>
                    </div>
                    <div class="card-subtitle">تطوير الأفكار والحوارات</div>
                </div>
            </div>
        </div>

        <div class="inspiration-section">
            <div class="section-header">
                <span class="section-title">إلهام الأفلام</span>
                <span class="view-all">عرض الكل</span>
            </div>

            <div class="movies-carousel">
                <div class="movie-card emily-cover" onclick="openStoryModal('Emily in Paris - Season 4', 'المشهد الافتتاحي:\nتبدأ الأحداث في مقهى فرنسي ساحر بمدينة باريس مع أجواء هادئة.\n\nالحوار:\nإميلي: «لم أكن أتوقع أن تكون الحياة هنا بهذا الجمال والتعقيد في نفس الوقت.»\nبيير: «باريس لا تعطي أسرارها لمن يطلبها بسرعة، يا إميلي.»\n\nالوصف البصري:\nكاميرا تتحرك بسلاسة لإظهار تفاصيل الشارع الفرنسي العريق مع انعكاس أضواء الصباح على النوافذ الزجاجية.')">
                    <div class="movie-title">Emily in Paris</div>
                </div>

                <div class="movie-card m2" onclick="openStoryModal('Cyberpunk Odyssey', 'المشهد الافتتاحي:\nمدينة مستقبلية تضيئها ألوان النيون المطرية وصوت الطائرات المسيرة في الأفق.\n\nالحوار:\nزاك: «النظام يراقب كل خطوة نخطوها في هذه الشبكة.»\nنايا: «إذن سنقوم بإسقاط جدار الحماية من الداخل.»')">
                    <div class="movie-title">Cyberpunk Odyssey</div>
                </div>

                <div class="movie-card m3" onclick="openStoryModal('The Lost Kingdom', 'المشهد الافتتاحي:\nأطلال مدينة قديمة وسط الغابات الاستوائية المعتمة.\n\nالحوار:\nالباحث: «المفتاح ليس هنا، بل في البرج القديم.»')">
                    <div class="movie-title">The Lost Kingdom</div>
                </div>
            </div>
        </div>
    </div>

    <!-- شاشة إنشاء فيلم (Create) -->
    <div id="createScreen" class="screen-view">
        <div class="page-header">
            <button class="back-btn" onclick="switchScreen('homeScreen')">✕</button>
            <div class="page-title-text">استوديو الإبداع</div>
            <div style="width: 36px;"></div>
        </div>
        <div class="step-container">
            <div class="ai-assistant-card">
                <div class="ai-header-row">
                    <div class="ai-title">مساعد الذكاء الاصطناعي الخارق</div>
                    <div class="ai-badge-circle">AI</div>
                </div>
                <div class="ai-desc">اختر إعدادات فيلمك وسيقوم المساعد ببناء القصة وتوليد كافة التفاصيل بدقة سينمائية مذهلة.</div>
            </div>

            <div class="story-setup-box">
                <div class="setup-header-row">
                    <div class="setup-main-title">خيارات السيناريو</div>
                    <div class="counter-badge">خطوة 1 من 3</div>
                </div>

                <div class="setup-row-item">
                    <div class="item-info">
                        <h4>رفع صور مرجعية</h4>
                        <p>أضف صور الشخصيات أو الأماكن</p>
                    </div>
                    <button class="action-add-btn" onclick="toggleUploadBox()">إضافة</button>
                </div>
                <div id="uploadBox" class="upload-section-hidden">
                    <input type="file" accept="image/*" style="width:100%; color:#94a3b8; font-size:12px;">
                </div>

                <div class="setup-row-item">
                    <div class="item-info">
                        <h4>نص القصة الأساسي</h4>
                        <p>اكتب فكرة أو ملخص الفيلم</p>
                    </div>
                    <button class="action-add-btn" onclick="toggleStoryBox()">اكتب</button>
                </div>
                <textarea id="storyText" class="story-textarea-hidden" placeholder="اكتب تفاصيل القصة هنا..."></textarea>
            </div>

            <div class="bottom-next-row">
                <button class="side-next-btn" onclick="alert('جاري البدء بتوليد القصة السينمائية...')">إنشاء السيناريو الآن</button>
            </div>
        </div>
    </div>

    <!-- شاشة مكتبة الأفلام (Library) -->
    <div id="libraryScreen" class="screen-view">
        <div class="page-header">
            <div style="width: 36px;"></div>
            <div class="page-title-text">مكتبة الأعمال</div>
            <div style="width: 36px;"></div>
        </div>
        <div class="step-container" style="text-align: center; color: #94a3b8; padding-top: 60px;">
            <p style="font-size: 15px; font-weight: 700; color: #fff; margin-bottom: 6px;">لا توجد أعمال محفوظة حالياً</p>
            <p style="font-size: 12px;">ابدأ بإنشاء قصتك الأولى عبر استوديو الإبداع وسيتم حفظها هنا تلقائياً.</p>
        </div>
    </div>

    <!-- شاشة الملف الشخصي (Profile) -->
    <div id="profileScreen" class="screen-view">
        <div class="page-header">
            <div style="width: 36px;"></div>
            <div class="page-title-text">الملف الشخصي</div>
            <div style="width: 36px;"></div>
        </div>
        <div class="step-container">
            <div class="ai-assistant-card" style="align-items: center; text-align: center; padding: 24px;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #3b82f6, #8b5cf6); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; color: #fff; font-weight: 700; margin-bottom: 12px;">G</div>
                <div style="color: #fff; font-size: 16px; font-weight: 700; margin-bottom: 4px;">Ghassan Jbbasi</div>
                <div style="color: #94a3b8; font-size: 12px;">باقة المبدع المحترف</div>
            </div>
        </div>
    </div>

    <!-- شاشة الاشتراكات والترقية -->
    <div id="subscriptionScreen" class="screen-view">
        <div class="page-header">
            <button class="back-btn" onclick="switchScreen('homeScreen')">✕</button>
            <div class="page-title-text">ترقية الباقة</div>
            <div style="width: 36px;"></div>
        </div>

        <div class="content-body">
            <div class="plans-list">
                <div class="plan-card selected" onclick="selectPlan(this)">
                    <div class="plan-top">
                        <div class="plan-name">باقة المبدع الفائق</div>
                        <div class="plan-price">$9.99 / شهرياً</div>
                    </div>
                    <div class="plan-desc">توليد غير محدود للقصص، جودة سينمائية فائقة، أولوية قصوى في المعالجة.</div>
                </div>
            </div>

            <button class="action-main-btn" onclick="openGPlaySheet()">اشتراك الآن عبر Google Play</button>
        </div>
    </div>

    <!-- نافذة تفاصيل القصة المنبثقة -->
    <div id="storyModal" class="story-modal-overlay">
        <div class="story-modal-content">
            <div class="story-modal-header">
                <div id="modalTitle" class="story-modal-title">عنوان القصة</div>
                <button class="story-modal-close" onclick="closeStoryModal()">✕</button>
            </div>
            <div id="modalBody" class="story-modal-body">
                نص القصة والتفاصيل السينمائية...
            </div>
            <div class="story-modal-footer">
                <button class="copy-story-btn" onclick="copyStoryText()">نسخ النص السينمائي</button>
            </div>
        </div>
    </div>

    <!-- نافذة Google Play السفلية للدفع -->
    <div id="gplayOverlay" class="gplay-overlay" onclick="closeGPlaySheet(event)">
        <div class="gplay-sheet" onclick="event.stopPropagation()">
            <div class="gplay-top-bar">
                <span class="gplay-store-title">Google Play</span>
                <button class="gplay-close" onclick="closeGPlaySheet()">✕</button>
            </div>

            <div class="gplay-app-header">
                <div class="gplay-app-icon">
                    <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop" alt="App Icon">
                </div>
                <div class="gplay-app-details">
                    <h3>PlotCraft - AI Story & Movie</h3>
                    <p>PlotCraft Inc.</p>
                </div>
            </div>

            <div class="gplay-price-row">
                <span>باقة المبدع الفائق (اشتراك شهري)</span>
                <span>$9.99</span>
            </div>
            <div class="gplay-tax-row">
                <span>الضريبة متضمنة إن وجدت</span>
                <span></span>
            </div>

            <div class="gplay-notes">
                <div>• سيتم تجديد الاشتراك تلقائياً ما لم يتم إلغاؤه قبل 24 ساعة من نهاية الفترة الحالية.</div>
            </div>

            <div class="gplay-points-row">
                <span>نقاط Google Play Points</span>
                <div class="gplay-points-diamond">
                    <span style="color:#34a853; font-weight:700;">+99 نقطة</span>
                </div>
            </div>

            <div class="gplay-payment-box" onclick="openPaymentSelector()">
                <div class="gplay-payment-info">
                    <span style="font-size:18px;">💳</span>
                    <div>
                        <div style="font-size:14px; font-weight:600; color:#e8eaed;">بطاقة ائتمان / خصم مباشر</div>
                        <div style="font-size:11px; color:#9aa0a6;">•••• 4589</div>
                    </div>
                </div>
                <span style="color:#9aa0a6; font-size:14px;">‹</span>
            </div>

            <button class="gplay-subscribe-btn" onclick="confirmSubscription()">اشتراك بضغطة واحدة</button>
        </div>
    </div>

    <!-- شاشة اختيار طريقة الدفع -->
    <div id="paymentSelectorModal" class="payment-selector-modal" onclick="closePaymentSelector(event)">
        <div class="payment-selector-content" onclick="event.stopPropagation()">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h4 style="font-size:15px;">طرق الدفع</h4>
                <button onclick="closePaymentSelector()" style="background:none; border:none; color:#fff; font-size:18px; cursor:pointer;">✕</button>
            </div>
            <div class="payment-option-item" onclick="selectPaymentMethod('Google Play Balance')">
                <span>💰</span>
                <div>
                    <div style="font-size:13px; font-weight:600;">رصيد Google Play</div>
                    <div style="font-size:11px; color:#9aa0a6;">المتوفر: $15.00</div>
                </div>
            </div>
            <div class="payment-option-item" onclick="selectPaymentMethod('Credit Card')">
                <span>💳</span>
                <div>
                    <div style="font-size:13px; font-weight:600;">بطاقة ائتمان / خصم مباشر</div>
                    <div style="font-size:11px; color:#9aa0a6;">•••• 4589</div>
                </div>
            </div>
        </div>
    </div>

    <!-- شريط التنقل السفلي الثابت -->
    <div class="bottom-nav">
        <div class="nav-item active" id="navHome" onclick="switchScreen('homeScreen'); setActiveNav(this)">
            <div class="nav-icon icon-home"></div>
            <span>الرئيسية</span>
        </div>
        <div class="nav-item" id="navCreate" onclick="switchScreen('createScreen'); setActiveNav(this)">
            <div class="nav-icon icon-create"></div>
            <span>إنشاء</span>
        </div>
        <div class="nav-item" id="navLibrary" onclick="switchScreen('libraryScreen'); setActiveNav(this)">
            <div class="nav-icon icon-library"></div>
            <span>المكتبة</span>
        </div>
        <div class="nav-item" id="navProfile" onclick="switchScreen('profileScreen'); setActiveNav(this)">
            <div class="nav-icon icon-profile"></div>
            <span>حسابي</span>
        </div>
    </div>

    <script>
        function switchScreen(screenId) {
            document.querySelectorAll('.screen-view').forEach(el => el.classList.remove('active'));
            document.getElementById(screenId).classList.add('active');
            window.scrollTo(0, 0);
        }

        function setActiveNav(element) {
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            element.classList.add('active');
        }

        function toggleUploadBox() {
            const box = document.getElementById('uploadBox');
            box.classList.toggle('show');
        }

        function toggleStoryBox() {
            const box = document.getElementById('storyText');
            box.classList.toggle('show');
        }

        function openStoryModal(title, text) {
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalBody').innerText = text;
            document.getElementById('storyModal').classList.add('active');
        }

        function closeStoryModal() {
            document.getElementById('storyModal').classList.remove('active');
        }

        function copyStoryText() {
            const text = document.getElementById('modalBody').innerText;
            navigator.clipboard.writeText(text).then(() => {
                alert('تم نسخ النص السينمائي بنجاح!');
            });
        }

        function selectPlan(card) {
            document.querySelectorAll('.plan-card').forEach(el => el.classList.remove('selected'));
            card.classList.add('selected');
        }

        function openGPlaySheet() {
            document.getElementById('gplayOverlay').classList.add('active');
        }

        function closeGPlaySheet(e) {
            if (!e || e.target.id === 'gplayOverlay' || e.target.classList.contains('gplay-close')) {
                document.getElementById('gplayOverlay').classList.remove('active');
            }
        }

        function openPaymentSelector() {
            document.getElementById('paymentSelectorModal').classList.add('active');
        }

        function closePaymentSelector(e) {
            if (!e || e.target.id === 'paymentSelectorModal') {
                document.getElementById('paymentSelectorModal').classList.remove('active');
            }
        }

        function selectPaymentMethod(methodName) {
            document.getElementById('paymentSelectorModal').classList.remove('active');
            alert('تم اختيار طريقة الدفع: ' + methodName);
        }

        function confirmSubscription() {
            document.getElementById('gplayOverlay').classList.remove('active');
            alert('تهانينا! تم تفعيل اشتراكك بنجاح عبر متجر جوجل بلاي.');
            switchScreen('homeScreen');
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=850, scrolling=True)
