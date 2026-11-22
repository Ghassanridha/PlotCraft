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

async function saveUserData(user) {
  if (!user) return null;
  const userRef = doc(db, "users", user.uid);
  const snap = await getDoc(userRef);

  const baseData = {
    uid: user.uid,
    email: user.email || "",
    lastLoginAt: serverTimestamp(),
    updatedAt: serverTimestamp()
  };

  if (!snap.exists()) {
    await setDoc(userRef, {
      ...baseData,
      createdAt: serverTimestamp(),
      role: "user",
      credits: 0
    });
  } else {
    await setDoc(userRef, baseData, { merge: true });
  }

  const updatedSnap = await getDoc(userRef);
  return updatedSnap.exists() ? updatedSnap.data() : null;
}

function attachPlotcraftAuthBridge() {
  const bridge = window.plotcraftAuthBridge = window.plotcraftAuthBridge || {};

  bridge.login = async function (email, password) {
    const cred = await signInWithEmailAndPassword(auth, email, password);
    const profile = await saveUserData(cred.user);
    return {
      uid: cred.user.uid,
      email: cred.user.email,
      ...(profile || {})
    };
  };

  bridge.signIn = bridge.login;

  bridge.register = async function (email, password) {
    const cred = await createUserWithEmailAndPassword(auth, email, password);
    const profile = await saveUserData(cred.user);
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

    await saveUserData(user);

    const subscriptionData = {
      userId: user.uid,
      email: user.email || "",
      planId: selectedPlan?.planId || "monthly",
      credits: Number(selectedPlan?.credits || 0),
      title: selectedPlan?.title || "PlotCraft Pro",
      status: "active",
      updatedAt: serverTimestamp()
    };

    await setDoc(doc(db, "users", user.uid), {
      subscription: subscriptionData,
      credits: subscriptionData.credits,
      updatedAt: serverTimestamp()
    }, { merge: true });

    const subDoc = await addDoc(collection(db, "subscriptions"), {
      ...subscriptionData,
      createdAt: serverTimestamp()
    });

    return {
      id: subDoc.id,
      ...subscriptionData
    };
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

    try {
      const profile = await saveUserData(user);
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
    } catch (error) {
      console.error("PlotCraft Firestore save error:", error);
    }
  });
}

attachPlotcraftAuthBridge();
