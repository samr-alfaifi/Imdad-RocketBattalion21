# Units Module
# وحدة الأقسام العسكرية

class Unit:
    def __init__(self, name, commander, personnel):
        self.name = name
        self.commander = commander
        self.personnel = personnel

    def info(self):
        return f"القسم: {self.name} | القائد: {self.commander} | عدد الأفراد: {self.personnel}"
