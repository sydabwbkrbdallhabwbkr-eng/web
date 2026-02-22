import flet as ft

def main(page: ft.Page):
    page.title = "Taiping Search"
    
    # إنشاء WebView مدعوم من Flet للموبايل والسطح المكتب
    # ملاحظة: Flet يتعامل مع عرض المواقع داخلياً
    wv = ft.WebView(
        "https://sayedabobakr-droid.github.io/taiping-search/",
        expand=True,
    )
    
    page.add(wv)

ft.app(target=main)
