// ==========================================
// 5. قسم البرامج والوظائف التفاعلية JavaScript (مؤمن ومحدث مع Firebase)
// ==========================================

// استيراد مكتبات Firebase (التوثيق، التطبيق، قاعدة البيانات، وتحليل البيانات)
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";
import { 
    getAuth, 
    createUserWithEmailAndPassword, 
    signInWithEmailAndPassword, 
    GoogleAuthProvider, 
    signInWithPopup 
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js";

// إعدادات Firebase الخاصة بمشروعك
const firebaseConfig = {
  apiKey: "AIzaSyC0yqVlGpM159foKmpMFiuySgF5uFxOA_k",
  authDomain: "plotcraft2.firebaseapp.com",
  projectId: "plotcraft2",
  storageBucket: "plotcraft2.firebasestorage.app",
  messagingSenderId: "338171528711",
  appId: "1:338171528711:web:f13544fb4e496fe39e8ca2",
  measurementId: "G-T2ZXFTGD5H"
};

// تهيئة Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app); // تفعيل نظام المصادقة
const db = getDatabase(app); // تفعيل قاعدة البيانات الحية

// دالة تثبيت وحفظ بيانات المستخدم كاملة (البريد، المعرف، الاسم، الصورة، والـ UID)
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
        handle: userHandle,       // المعرف المستخرج تلقائياً من الإيميل
        picture: userPicture,
        lastLogin: Date.now()
    };

    // حفظ البيانات في مسار users/{uid} داخل Realtime Database
    set(ref(db, 'users/' + user.uid), userData)
        .then(() => {
            console.log("✅ تم حفظ البريد والمعرف والبيانات في قاعدة البيانات بنجاح");
            localStorage.setItem('plotcraft_user_session', JSON.stringify(userData));
            localStorage.setItem('plotcraft_user_uid', user.uid);
        })
        .catch((error) => {
            console.error("❌ خطأ في حفظ بيانات المستخدم:", error);
        });
}

// دالة التنقل بين الشاشات
function switchScreen(screenId, event) {
    var screens = document.querySelectorAll('.screen-view');
    screens.forEach(s => s.classList.remove('active'));
    
    let targetScreen = document.getElementById(screenId);
    if (targetScreen) {
        targetScreen.classList.add('active');
    }
}

// دالة تغيير اللغة (عربي / إنجليزي وباقي اللغات)
function applySelectedLanguage() {
    if (typeof tempSelectedLangName !== 'undefined') {
        var langName = tempSelectedLangName;
        let displayEl = document.getElementById('currentLangDisplay');
        if (displayEl) {
            displayEl.innerText = langName;
        }
    }
}

// ==========================================
// وظائف الحسابات والاتصال الفعلي بـ Firebase Auth
// ==========================================

// 1. دالة إنشاء حساب جديد بالبريد الإلكتروني وكلمة المرور
window.handleRegister = function() {
    let emailField = document.getElementById('registerEmailField') || document.getElementById('loginEmailField');
    let passField = document.getElementById('registerPasswordField') || document.getElementById('loginPasswordField');
    
    if (!emailField || !passField) {
        alert("⚠️ حقول المدخلات غير متوفرة في هذه الشاشة.");
        return;
    }

    let email = emailField.value.trim();
    let pass = passField.value.trim();

    if (email === "" || pass === "") {
        alert("⚠️ يرجى ملء جميع الحقول المطلوبة.");
        return;
    }

    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("⚠️ يرجى إدخال بريد إلكتروني صالح.");
        return;
    }

    // إرسال البيانات إلى Firebase لإنشاء الحساب
    createUserWithEmailAndPassword(auth, email, pass)
        .then((userCredential) => {
            let user = userCredential.user;
            saveUserToDatabase(user); // حفظ بيانات الحساب والمعرف في القاعدة
            alert("✅ تم إنشاء الحساب بنجاح!");
            switchScreen('mainDashboardScreen');
        })
        .catch((error) => {
            alert("❌ خطأ في إنشاء الحساب: " + error.message);
        });
};

// 2. دالة تسجيل الدخول للحسابات الموجودة مسبقاً
window.handleExistingLogin = function() {
    let emailField = document.getElementById('loginEmailField');
    let passField = document.getElementById('loginPasswordField');
    
    if (!emailField || !passField) return;

    let email = emailField.value.trim();
    let pass = passField.value.trim();

    if (email === "" || pass === "") {
        alert("⚠️ يرجى ملء جميع الحقول المطلوبة.");
        return;
    }

    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("⚠️ يرجى إدخال بريد إلكتروني صالح.");
        return;
    }

    // التحقق وتسجيل الدخول عبر Firebase
    signInWithEmailAndPassword(auth, email, pass)
        .then((userCredential) => {
            let user = userCredential.user;
            saveUserToDatabase(user); // تحديث وتثبيت البيانات في القاعدة
            alert("مرحباً بك مجدداً! تم تسجيل الدخول بنجاح.");
            switchScreen('mainDashboardScreen');
        })
        .catch((error) => {
            alert("❌ فشل تسجيل الدخول: تأكد من البريد أو كلمة المرور.");
        });
};

// 3. دالة تسجيل الدخول عبر جوجل (باستخدام النافذة المنبثقة السريعة والآمنة)
window.handleGoogleLogin = function() {
    const provider = new GoogleAuthProvider();
    
    signInWithPopup(auth, provider)
        .then((result) => {
            let user = result.user;
            saveUserToDatabase(user); // حفظ البريد والمعرف والصورة الخاصة بجوجل في القاعدة
            alert("✅ تم تسجيل الدخول بواسطة جوجل بنجاح!");
            switchScreen('mainDashboardScreen');
        })
        .catch((error) => {
            alert("❌ حدث خطأ أثناء تسجيل الدخول بجوجل: " + error.message);
        });
};
