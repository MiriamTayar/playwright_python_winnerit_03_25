#דוגמא ליצירת דפדפן

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()   #מפעיל את Playwright ומחזיר אובייקט שמאפשר לעבוד עם דפדפנים כמו Chromium, Firefox ו־WebKit
browser = playwright.chromium.launch(headless=False) #פותח דפדפן מסוג Chromium עם פתיחה של חלון ממשי
context = browser.new_context () #פותח קונטקסט חדש – סביבת גלישה חדשה עם session נפרד, cookies נפרדים, וכד'.
page = context.new_page () #יוצר דף (page) חדש

page. goto("") #מעביר את הדף לכתובת URL כלשהי