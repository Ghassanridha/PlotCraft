import streamlit as st

st.markdown("""
    <style>
    /* حاوية القائمة السفلية الموحدة */
    .nav-container {
        position: fixed;
        bottom: 25px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 370px;
        background-color: #16171d;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 50px;
        padding: 5px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 10px 25px rgba(0,0,0,0.8);
        z-index: 99999;
        box-sizing: border-box;
    }
    
    /* الأزرار العادية داخل القالب */
    .nav-btn {
        flex: 1;
        text-align: center;
        color: #888888;
        font-size: 11px;
        font-weight: 600;
        padding: 8px 4px;
        cursor: pointer;
        user-select: none;
        white-space: nowrap;
    }
    
    /* زر الأدوات النشط (أبيض مع نص أسود داكن) داخل نفس القالب */
    .nav-btn-active {
        flex: 1;
        text-align: center;
        background-color: #ffffff;
        color: #121318;
        font-size: 11px;
        font-weight: bold;
        padding: 8px 6px;
        border-radius: 40px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        cursor: pointer;
        user-select: none;
        white-space: nowrap;
    }
    </style>

    <div class="nav-container">
        <div class="nav-btn">الصفحة الرئيسية</div>
        <div class="nav-btn">الأعمال</div>
        <div class="nav-btn-active">الأدوات</div>
    </div>
""", unsafe_allow_html=True)
