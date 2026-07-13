import tkinter as tk
from tkinter import ttk

# نافذة البرنامج
window = tk.Tk()
window.title("نظام الإمداد العسكري")
window.geometry("1000x600")
window.configure(bg="#1e1e1e")

# -----------------------------
# الشريط العلوي (Topbar)
# -----------------------------
topbar = tk.Frame(window, bg="#2b2b2b", height=60)
topbar.pack(fill="x")

title_label = tk.Label(topbar, text="نظام الإمداد العسكري", fg="white", bg="#2b2b2b", font=("Arial", 18))
title_label.pack(side="left", padx=20)

settings_btn = tk.Button(topbar, text="⚙️", bg="#2b2b2b", fg="white", borderwidth=0, font=("Arial", 16))
settings_btn.pack(side="right", padx=20)

# -----------------------------
# القائمة الجانبية (Sidebar)
# -----------------------------
sidebar = tk.Frame(window, bg="#252525", width=200)
sidebar.pack(fill="y", side="left")

def add_sidebar_button(text):
    btn = tk.Button(sidebar, text=text, bg="#252525", fg="white", font=("Arial", 14), borderwidth=0, anchor="w")
    btn.pack(fill="x", pady=5, padx=10)
    return btn

btn_weapons = add_sidebar_button("الأسلحة")
btn_vehicles = add_sidebar_button("المركبات")
btn_units = add_sidebar_button("الأقسام")
btn_reports = add_sidebar_button("التقارير")
btn_settings = add_sidebar_button("الإعدادات")

# -----------------------------
# منطقة المحتوى (Main Panel)
# -----------------------------
main_panel = tk.Frame(window, bg="#1e1e1e")
main_panel.pack(fill="both", expand=True)

welcome_label = tk.Label(main_panel, text="مرحبًا بك في نظام الإمداد العسكري", fg="white", bg="#1e1e1e", font=("Arial", 20))
welcome_label.pack(pady=50)

# تشغيل الواجهة
window.mainloop()
