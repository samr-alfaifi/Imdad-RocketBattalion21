# Theme Manager
# إدارة الثيمات داخل نظام الإمداد العسكري

import json

def load_theme(theme_file="Themes/default.json"):
    try:
        with open(theme_file, "r", encoding="utf-8") as file:
            theme = json.load(file)
            print(f"تم تحميل الثيم: {theme['name']}")
            return theme
    except Exception as e:
        print("خطأ في تحميل الثيم:", e)
        return None
