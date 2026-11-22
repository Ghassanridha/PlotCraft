import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-app.js";
import {
  getAuth,
  onAuthStateChanged,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signOut
} from "https://www.gstatic.com/firebasejs/11.6.0/firebase-auth.js";
import {
  getFirestore,
  doc,
  getDoc,
  setDoc,
  serverTimestamp
} from "https://www.gstatic.com/firebasejs/11.6.0/firebase-firestore.js";

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
const auth = getAuth(app);
const db = getFirestore(app);

// رابط السيرفر الخلفي لتأكيد الدفع وتفعيل الاشتراك (استبدله برابط السيرفر الفعلي عندك)
const SUBSCRIPTION_ENDPOINT = "/api/subscriptions/request";

async function ensureUserProfile(user) {
  const userRef = doc(db, "users", user.uid);
  const snap = await getDoc(userRef);

  if (!snap.exists()) {
    await setDoc(userRef, {
      email: user.email || "",
      createdAt: serverTimestamp(),
      role: "user"
    });
  }

  const updatedSnap = await getDoc(userRef);
  return updatedSnap.exists() ? updatedSnap.data() : null;
}

// أداة ربط Firebase مع واجهة الاشتراك وتسجيل الدخول عبر الجسر
function attachPlotcraftAuthBridge() {
  const bridge = window.plotcraftAuthBridge = window.plotcraftAuthBridge || {};

  bridge.login = async function (email, password) {
    const cred = await signInWithEmailAndPassword(auth, email, password);
    const profile = await ensureUserProfile(cred.user);
    return {
      uid: cred.user.uid,
      email: cred.user.email,
      ...(profile || {})
    };
  };

  bridge.signIn = bridge.login;

  bridge.register = async function (email, password) {
    const cred = await createUserWithEmailAndPassword(auth, email, password);
    const profile = await ensureUserProfile(cred.user);
    return {
      uid: cred.user.uid,
      email: cred.user.email,
      ...(profile || {})
    };
  };

  bridge.logout = async function () {
    await signOut(auth);
  };

  bridge.getCurrentUserProfile = async function () {
    const user = auth.currentUser;
    if (!user) return null;
    const snap = await getDoc(doc(db, "users", user.uid));
    return snap.exists() ? { uid: user.uid, ...snap.data() } : null;
  };

  // إرسال طلب الاشتراك إلى السيرفر مع توكن المستخدم للتحقق والحفظ الآمن
  bridge.requestSubscription = async function (selectedPlan) {
    const user = auth.currentUser;
    if (!user) {
      throw new Error("يجب تسجيل الدخول أولاً لإتمام الاشتراك.");
    }

    const idToken = await user.getIdToken();
    const response = await fetch(SUBSCRIPTION_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + idToken
      },
      body: JSON.stringify({
        planId: selectedPlan.planId,
        credits: selectedPlan.credits,
        title: selectedPlan.title
      })
    });

    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      throw new Error(data.message || "فشل إرسال طلب الاشتراك إلى السيرفر.");
    }

    return data;
  };

  onAuthStateChanged(auth, async (user) => {
    if (!user) {
      if (typeof bridge.setAuthState === "function") {
        bridge.setAuthState(null);
      }
      if (typeof bridge.onLogout === "function") {
        bridge.onLogout();
      }
      return;
    }

    const profile = await ensureUserProfile(user);
    const payload = {
      uid: user.uid,
      email: user.email,
      ...(profile || {})
    };

    if (typeof bridge.setAuthState === "function") {
      bridge.setAuthState(payload);
    }
    if (typeof bridge.onLoginSuccess === "function") {
      bridge.onLoginSuccess(payload);
    }
  });
}

attachPlotcraftAuthBridge();
