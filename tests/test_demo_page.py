
#               ***********   הדגמה לדף בדיקה   ***********

from playwright.sync_api import Page, expect

BASE_URL = "https://devexpress.github.io/testcafe/example/"

# def test_demo_page_loaded(page: Page):
#     page.goto(BASE_URL)
#     print(page.url)
#     #assert page.url == BASE_URL+" /home-page"
#     expect(page).to_have_url(BASE_URL, timeout=7500) #הגירסה הזו מתאימה לדפים דינאמיים כי היא ממתינה לדף כמה זמן עד שיטען
#
def test_demo_page_title(page:Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("TestCafe Example Page") #בדיקת הטקסט שמופיע בלשונית של הדפדפן


def test_user_name_presented(page: Page):
    page.goto(BASE_URL)
    page.locator("#developer-name").press_sequentially("Miri Ram", delay=250)
    page.get_by_test_id("remote-testing-checkbox").check() # סימון checkbox
    page.get_by_test_id("remote-testing-checkbox").check()

    # בדיקת כותרות
    expect(page.locator("header h1")).to_have_text("Example") #בודק שהטקסט מדויק לחלוטין – בדיוק כפי שמופיע ב־HTML
    #בודק אם האלמנט מכיל את הטקסט (חלקי), לא חייב שהטקסט כולו יתאים בדיוק:)
    expect(page.locator("header p").nth(0)).to_contain_text("This webpage is used as a sample in TestCafe tutorials.")

    # page.get_by_test_id("remote-js-code-checkbox").click()
    # page.get_by_test_id("remote-js-code-checkbox").click()

    page.get_by_test_id("windows-radio").check() #כפתור radio
    page.locator('select#preferred-interface').select_option("JavaScript API") #מחפש תפריט נפתח (<select>) עם id="preferred-interface"
    page.locator('[name="tried-test-cafe"]').check() #תיבת סימון- checkbox

    page.get_by_test_id("comments-area").fill("This is a comment for the test page.") #הזנת טקסט לשדה ההערות

    page.get_by_role("button", name="Submit").click() #לחיצה על כפתור בשם "Submit"
    page.wait_for_timeout(3000)
