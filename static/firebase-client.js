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
  addDoc,
  collection,
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

async function saveUserProfile(user) {
  if (!user) return null;

  const userRef = doc(db, "users", user.uid);
  const snap = await getDoc(userRef);

  const payload = {
    uid: user.uid,
    email: user.email || "",
    lastSeenAt: serverTimestamp(),
    updatedAt: serverTimestamp()
  };

  if (!snap.exists()) {
    await setDoc(userRef, {
      ...payload,
      createdAt: serverTimestamp(),
      role: "user",
      credits: 0
    });
  } else {
    await setDoc(userRef, payload, { merge: true });
  }

  const freshSnap = await getDoc(userRef);
  return freshSnap.exists() ? freshSnap.data() : null;
}

function bindUiHooks(bridge) {
  // ربط أحداث الواجهة تلقائياً إذا كانت موجودة
  if (typeof window.setEmailLoggedIn === "function") {
    const prevLogin = bridge.onLoginSuccess;
    const prevLogout = bridge.onLogout;

    bridge.onLoginSuccess = function (data) {
      window.isUserLoggedIn = true;
      window.setEmailLoggedIn(true);
      if (typeof prevLogin === "function") prevLogin(data);
    };

    bridge.onLogout = function () {
      window.isUserLoggedIn = false;
      window.setEmailLoggedIn(false);
      if (typeof prevLogout === "function") prevLogout();
    };
  }
}

function setupFirebaseBridge() {
  const bridge = window.plotcraftAuthBridge = window.plotcraftAuthBridge || {};
  bridge.ready = true;
  bridge.auth = auth;
  bridge.db = db;

  bridge.login = async function (email, password) {
    const cred = await signInWithEmailAndPassword(auth, email, password);
    const profile = await saveUserProfile(cred.user);
    return {
      uid: cred.user.uid,
      email: cred.user.email,
      ...(profile || {})
    };
  };

  bridge.signIn = bridge.login;

  bridge.register = async function (email, password) {
    const cred = await createUserWithEmailAndPassword(auth, email, password);
    const profile = await saveUserProfile(cred.user);
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

  bridge.requestSubscription = async function (selectedPlan) {
    const user = auth.currentUser;
    if (!user) {
      throw new Error("يجب تسجيل الدخول أولاً لإتمام الاشتراك.");
    }

    await saveUserProfile(user);

    const subData = {
      userId: user.uid,
      email: user.email || "",
      planId: selectedPlan?.planId || "monthly",
      credits: Number(selectedPlan?.credits || 0),
      title: selectedPlan?.title || "PlotCraft Pro",
      status: "active",
      updatedAt: serverTimestamp()
    };

    await setDoc(doc(db, "users", user.uid), {
      subscription: subData,
      credits: subData.credits,
      updatedAt: serverTimestamp()
    }, { merge: true });

    const created = await addDoc(collection(db, "subscriptions"), {
      ...subData,
      createdAt: serverTimestamp()
    });

    return {
      id: created.id,
      ...subData
    };
  };

  bindUiHooks(bridge);
  window.dispatchEvent(new CustomEvent("plotcraft:firebase-ready", { detail: bridge }));

  onAuthStateChanged(auth, async (user) => {
    bindUiHooks(bridge);

    if (!user) {
      window.isUserLoggedIn = false;
      if (typeof bridge.setAuthState === "function") bridge.setAuthState(null);
      if (typeof bridge.onLogout === "function") bridge.onLogout();
      return;
    }

    try {
      const profile = await saveUserProfile(user);
      const userPayload = {
        uid: user.uid,
        email: user.email,
        ...(profile || {})
      };

      window.isUserLoggedIn = true;
      if (typeof bridge.setAuthState === "function") bridge.setAuthState(userPayload);
      if (typeof bridge.onLoginSuccess === "function") bridge.onLoginSuccess(userPayload);
    } catch (err) {
      console.error("PlotCraft Save Error:", err);
    }
  });
}

setupFirebaseBridge();
