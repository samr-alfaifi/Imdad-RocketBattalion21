import tkinter as tk
from tkinter import ttk

# نافذة البرنامج
window = tk.Tk()
window.title("نظام الإمداد العسكري")
window.geometry("800x500")

# عنوان رئيسي
title = ttk.Label(window, text="نظام الإمداد العسكري", font=("Arial", 20))
title.pack(pady=20)

# زر مثال
btn = ttk.Button(window, text="عرض الأسلحة")
btn.pack(pady=10)

# تشغيل الواجهة
window.mainloop()
