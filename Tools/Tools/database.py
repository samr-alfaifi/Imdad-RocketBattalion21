# Database Tools
# أدوات التعامل مع قاعدة البيانات في نظام الإمداد العسكري

import sqlite3

def connect(db_name="military.db"):
    try:
        conn = sqlite3.connect(db_name)
        print("تم الاتصال بقاعدة البيانات بنجاح.")
        return conn
    except Exception as e:
        print("خطأ في الاتصال بقاعدة البيانات:", e)
        return None
