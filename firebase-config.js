// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-analytics.js";
// استيراد قاعدة البيانات Firestore من سيرفرات جوجل
import { getFirestore, doc, setDoc } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyC0yqVlGpM159foKmpMFiuySgF5uFxOA_k",
  authDomain: "plotcraft2.firebaseapp.com",
  projectId: "plotcraft2",
  storageBucket: "plotcraft2.firebasestorage.app",
  messagingSenderId: "338171528711",
  appId: "1:338171528711:web:f13544fb4e496fe39e8ca2",
  measurementId: "G-T2ZXFTGD5H"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// تفعيل قاعدة البيانات وربطها بالمتصفح ليستخدمها ملف app.js
const db = getFirestore(app);
window.db = db;
window.firestoreMethods = { doc, setDoc };
