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
btn_weapons.config(command=show_weapons)
btn_vehicles = add_sidebar_button("المركبات")
btn_units = add_sidebar_button("الأقسام")
btn_reports = add_sidebar_button("التقارير")
btn_settings = add_sidebar_button("الإعدادات")

# -----------------------------
def show_weapons():
    # تنظيف منطقة المحتوى
    for widget in main_panel.winfo_children():
        widget.destroy()

    # عنوان الشاشة
    title = tk.Label(main_panel, text="قائمة الأسلحة", fg="white", bg="#1e1e1e", font=("Arial", 20))
    title.pack(pady=20)

    # جدول الأسلحة
    columns = ("name", "caliber", "quantity")
    table = ttk.Treeview(main_panel, columns=columns, show="headings", height=10)

    table.heading("name", text="اسم السلاح")
    table.heading("caliber", text="العيار")
    table.heading("quantity", text="الكمية")

    table.pack(pady=10)

    # بيانات تجريبية
    sample_data = [
        ("قاذف صواريخ", "122mm", 12),
        ("مدفع هاوتزر", "155mm", 5),
        ("رشاش ثقيل", "12.7mm", 20)
    ]

    for item in sample_data:
        table.insert("", "end", values=item)
# -----------------------------
main_panel = tk.Frame(window, bg="#1e1e1e")
main_panel.pack(fill="both", expand=True)

welcome_label = tk.Label(main_panel, text="مرحبًا بك في نظام الإمداد العسكري", fg="white", bg="#1e1e1e", font=("Arial", 20))
welcome_label.pack(pady=50)

# تشغيل الواجهة
window.mainloop()
