import webview
import os

# هذا السطر يحدد مسار المجلد الحالي الذي يوجد به البرنامج
current_path = os.path.dirname(os.path.abspath(__file__))
cache_dir = os.path.join(current_path, 'cache')

# التأكد من إنشاء المجلد إذا لم يكن موجوداً
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

window = webview.create_window(
    'Taiping Search', 
    'https://sayedabobakr-droid.github.io/taiping-search/',
    private_mode=False
)

# هنا نمرر المسار الكامل للمجلد
webview.start(storage_path=cache_dir)