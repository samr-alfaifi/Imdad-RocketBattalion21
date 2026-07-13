# Utils Tools
# أدوات مساعدة عامة للنظام

def log(message):
    print(f"[LOG] {message}")

def validate_text(text):
    return isinstance(text, str) and len(text) > 0
