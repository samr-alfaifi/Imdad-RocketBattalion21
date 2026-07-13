# Weapons Module
# وحدة الأسلحة داخل نظام الإمداد العسكري

class Weapon:
    def __init__(self, name, caliber, quantity):
        self.name = name
        self.caliber = caliber
        self.quantity = quantity

    def info(self):
        return f"السلاح: {self.name} | العيار: {self.caliber} | الكمية: {self.quantity}"
