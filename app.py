import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="centered"
)

st.markdown("""
<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #08090b;
    color: white;
    font-family: Arial, Tahoma, sans-serif;
}

.main {
    padding: 0 !important;
}

.app {
    width: 100%;
    max-width: 480px;
    margin: auto;
    background: #090a0c;
    min-height: 100vh;
    overflow: hidden;
}

.hero {
    position: relative;
    height: 650px;
    overflow: hidden;
    background:
        linear-gradient(
            to bottom,
            rgba(0,0,0,0.05),
            rgba(0,0,0,0.2),
            #090a0c
        ),
        url("https://images.unsplash.com/photo-1519608487953-e999c86e7455?auto=format&fit=crop&w=900&q=80");

    background-size: cover;
    background-position: center;
}

.logo {
    position: absolute;
    top: 20px;
    left: 20px;
    font-size: 19px;
    font-weight: bold;
}

.upgrade {
    position: absolute;
    top: 20px;
    right: 20px;
    padding: 9px 18px;
    border-radius: 25px;
    background: rgba(255,255,255,0.12);
    color: white;
}

.title {
    position: absolute;
    top: 110px;
    width: 100%;
    text-align: center;
}

.title h1 {
    font-size: 28px;
    margin: 0;
}

.title p {
    font-size: 24px;
    margin-top: 8px;
}

.person {
    position: absolute;
    width: 290px;
    height: 340px;
    bottom: 150px;
    left: 50%;
    transform: translateX(-50%);
    border-radius: 50%;
    object-fit: cover;
}

.cards {
    position: absolute;
    bottom: 20px;
    width: 100%;
    padding: 0 20px;
    display: flex;
    gap: 14px;
}

.card {
    flex: 1;
    padding: 15px;
    border-radius: 23px;
    background: rgba(25,27,31,0.8);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
}

.card-icon {
    font-size: 28px;
}

.card h3 {
    margin: 8px 0 3px;
}

.card p {
    margin: 0;
    font-size: 11px;
    color: #999;
}

.section {
    padding: 20px;
}

.section-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.section-title h2 {
    font-size: 20px;
}

.section-title span {
    color: #888;
    font-size: 13px;
}

.movies {
    display: flex;
    gap: 15px;
    overflow-x: auto;
}

.movie {
    min-width: 190px;
    background: #151619;
    border-radius: 18px;
    overflow: hidden;
}

.movie img {
    width: 100%;
    height: 275px;
    object-fit: cover;
}

.movie-info {
    padding: 10px;
}

.movie-info h3 {
    font-size: 13px;
    margin: 0;
}

.movie-info p {
    font-size: 10px;
    color: #777;
}

.nav {
    position: fixed;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    width: calc(100% - 30px);
    max-width: 450px;
    padding: 8px;
    border-radius: 30px;
    background: rgba(30,31,34,0.95);
    border: 1px solid rgba(255,255,255,0.08);
    display: flex;
    justify-content: space-around;
    backdrop-filter: blur(15px);
}

.nav-item {
    text-align: center;
    color: #999;
    font-size: 10px;
    padding: 8px 12px;
}

.nav-item.active {
    background: rgba(255,255,255,0.1);
    border-radius: 15px;
    color: white;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="app">

    <div class="hero">

        <div class="logo">
            ✦ بلوت كرافت
        </div>

        <div class="upgrade">
            👑 ترقية
        </div>

        <div class="title">
            <h1>مساء الخير، أيها المخرج</h1>
            <p>أي قصة سنصنع اليوم؟</p>
        </div>

        <img
            class="person"
            src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=600&q=90"
        >

        <div class="cards">

            <div class="card">
                <div class="card-icon">✨</div>
                <h3>سريع</h3>
                <p>إدخال واحد، فيديو كامل</p>
                <br>
                <small>🔒 Pro only</small>
            </div>

            <div class="card">
                <div class="card-icon">💬</div>
                <h3>خطوة بخطوة</h3>
                <p>راجع كل خطوة</p>
            </div>

        </div>

    </div>


    <div class="section">

        <div class="section-title">
            <h2>إلهام بلوت كرافت</h2>
            <span>عرض الكل</span>
        </div>

        <div class="movies">

            <div class="movie">
                <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=500&q=80">
                <div class="movie-info">
                    <h3>THE WRONG DOOR</h3>
                    <p>A mysterious story</p>
                </div>
            </div>

            <div class="movie">
                <img src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=500&q=80">
                <div class="movie-info">
                    <h3>THE DELIVERYMAN'S SECRET BILLIONAIRE</h3>
                    <p>A dramatic story</p>
                </div>
            </div>

            <div class="movie">
                <img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=500&q=80">
                <div class="movie-info">
                    <h3>THE INVITATION</h3>
                    <p>Mystery</p>
                </div>
            </div>

        </div>

    </div>


    <div class="nav">

        <div class="nav-item active">
            🏠<br>
            الصفحة الرئيسية
        </div>

        <div class="nav-item">
            ✦<br>
            الأدوات
        </div>

        <div class="nav-item">
            🔥<br>
            الأعمال
        </div>

        <div class="nav-item">
            ✎<br>
            إنشاء
        </div>

    </div>

</div>
""", unsafe_allow_html=True)
