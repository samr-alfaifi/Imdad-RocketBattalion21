# Vehicles Module
# وحدة المركبات العسكرية

class Vehicle:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity

    def info(self):
        return f"المركبة: {self.name} | النوع: {self.type} | الحمولة: {self.capacity}"
