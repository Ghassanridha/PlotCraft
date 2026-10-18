import os
import firebase_admin
from firebase_admin import credentials, firestore

db = None

def init_firebase():
    global db
    if not firebase_admin._apps:
        try:
            firebase_creds_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
            if firebase_creds_path and os.path.exists(firebase_creds_path):
                cred = credentials.Certificate(firebase_creds_path)
                firebase_admin.initialize_app(cred)
                db = firestore.client()
        except Exception as e:
            pass
    return db
