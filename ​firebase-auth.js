    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
        import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";
        import { 
            getAuth, 
            GoogleAuthProvider, 
            signInWithPopup 
        } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
        import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js";

        const firebaseConfig = {
          apiKey: "AIzaSyC0yqVlGpM159foKmpMFiuySgF5uFxOA_k",
          authDomain: "plotcraft2.firebaseapp.com",
          projectId: "plotcraft2",
          storageBucket: "plotcraft2.firebasestorage.app",
          messagingSenderId: "338171528711",
          appId: "1:338171528711:web:f13544fb4e496fe39e8ca2",
          measurementId: "G-T2ZXFTGD5H"
        };

        const app = initializeApp(firebaseConfig);
        const analytics = getAnalytics(app);
        const auth = getAuth(app);
        const db = getDatabase(app);

        function saveUserToDatabase(user) {
            if (!user) return;

            const userEmail = user.email || '';
            const userHandle = userEmail ? '@' + userEmail.split('@')[0] : '@user_' + user.uid.substring(0, 5);
            const userName = user.displayName || userEmail.split('@')[0] || 'مخرج PlotCraft';
            const userPicture = user.photoURL || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100';

            const userData = {
                uid: user.uid,
                name: userName,
                email: userEmail,
                handle: userHandle,
                picture: userPicture,
                lastLogin: Date.now()
            };

            set(ref(db, 'users/' + user.uid), userData)
                .then(() => {
                    localStorage.setItem('plotcraft_user_session', JSON.stringify(userData));
                    localStorage.setItem('plotcraft_user_uid', user.uid);
                    
                    const loginBtn = document.getElementById('btnLoginText');
                    if (loginBtn) {
                        loginBtn.innerText = userName;
                    }
                })
                .catch((error) => {
                    console.error("خطأ الحفظ:", error);
                });
        }

        // هذا هو التعديل الوحيد والمهم: إضافة إجبار ظهور نافذة اختيار الحسابات
        window.handleLoginAction = function() {
            const provider = new GoogleAuthProvider();
            provider.setCustomParameters({
                prompt: 'select_account' // هذا السطر هو اللي يجبر النافذة تطلع فوراً وما يعلق الزر
            });
            
            signInWithPopup(auth, provider)
                .then((result) => {
                    let user = result.user;
                    saveUser(user);
                    alert("✅ تم تسجيل الدخول بنجاح!");
                })
                .catch((error) => {
                    console.error("خطأ المصادقة:", error);
                    alert("❌ حدث خطأ أثناء تسجيل الدخول: " + error.message);
                });
        };

        window.addEventListener('DOMContentLoaded', () => {
            const savedSession = localStorage.getItem('plotcraft_user_session');
            if (savedSession) {
                try {
                    const userData = JSON.parse(savedSession);
                    const loginBtn = document.getElementById('btnLoginText');
                    if (loginBtn && userData.name) {
                        loginBtn.innerText = userData.name;
                    }
                } catch(e) {}
            }
        });
    </script>
