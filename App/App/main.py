# Main Application File
# نظام الإمداد العسكري – نقطة التشغيل الرئيسية

from Tools.database import connect
from Tools.utils import log
from Themes.theme_manager import load_theme
from Modules.weapons import Weapon
from Modules.vehicles import Vehicle
from Modules.units import Unit

# تشغيل النظام
log("تشغيل نظام الإمداد العسكري...")

# تحميل الثيم
theme = load_theme()

# الاتصال بقاعدة البيانات
db = connect()

# مثال على استخدام الوحدات العسكرية
weapon = Weapon("قاذف صواريخ", "122mm", 12)
vehicle = Vehicle("مدرعة تكتيكية", "عسكرية", 4)
unit = Unit("كتيبة الدعم", "النقيب سامر", 85)

print(weapon.info())
print(vehicle.info())
print(unit.info())
