import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

db = None

def init_firebase():
    global db
    if not firebase_admin._apps:
        try:
            creds_json = os.getenv("FIREBASE_CREDENTIALS")
            creds_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

            if creds_json:
                cred = credentials.Certificate(json.loads(creds_json))
            elif creds_path and os.path.exists(creds_path):
                cred = credentials.Certificate(creds_path)
            else:
                print("Firebase: no credentials found")
                return None

            firebase_admin.initialize_app(cred)
            db = firestore.client()
        except Exception as e:
            print("Firebase error:", e)
    else:
        db = firestore.client()
    return db
