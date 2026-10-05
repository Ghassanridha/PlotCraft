import streamlit as st

# كود شريط الأزرار السفلي فقط
st.markdown("""
    <style>
    .nav-container {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 380px;
        background-color: #16171d;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 40px;
        padding: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 999;
        box-shadow: 0 10px 25px rgba(0,0,0,0.8);
    }
    
    .nav-btn {
        flex: 1;
        text-align: center;
        color: #888;
        font-size: 12px;
        font-weight: 600;
        padding: 8px;
        cursor: pointer;
        user-select: none;
        transition: transform 0.1s ease;
    }
    
    .nav-btn:active {
        transform: scale(0.92);
        opacity: 0.8;
    }
    
    .nav-btn-active {
        flex: 1;
        text-align: center;
        background-color: #ffffff;
        color: #121318;
        font-size: 12px;
        font-weight: bold;
        padding: 8px 12px;
        border-radius: 30px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        cursor: pointer;
        user-select: none;
        transition: transform 0.1s ease;
    }
    
    .nav-btn-active:active {
        transform: scale(0.92);
        background-color: #e0e0e0;
    }
    </style>

    <div class="nav-container">
        <div class="nav-btn">الصفحة الرئيسية</div>
        <div class="nav-btn">الأعمال</div>
        <div class="nav-btn-active">الأدوات</div>
    </div>
""", unsafe_allow_html=True)
