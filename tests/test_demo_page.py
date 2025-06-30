from playwright.sync_api import Page, expect

BASE_URL = "https://devexpress.github.io/testcafe/example/"

# def test_demo_page_loaded(page: Page):
#     page.goto(BASE_URL)
#     print(page.url)
#     #assert page.url == BASE_URL+" /home-page"
#     expect(page).to_have_url(BASE_URL, timeout=7500) #הגירסה הזו מתאימה לדפים דינאמיים כי היא ממתינה לדף כמה זמן עד שיטען
#
# def test_demo_page_title(page:Page):
#     page.goto(BASE_URL)
#     expect(page).to_have_title("TestCafe Example Page")


def test_user_name_presented(page: Page):
    page.goto(BASE_URL)
    page.locator("#developer-name").press_sequentially("Miri Ram", delay=250)
    page.get_by_test_id("remote-testing-checkbox").check()
    page.get_by_test_id("remote-testing-checkbox").check()

    expect(page.locator("header h1")).to_have_text("Example")
    expect(page.locator("header p").nth(0)).to_contain_text("This webpage is used as a sample in TestCafe tutorials.")

    # page.get_by_test_id("remote-js-code-checkbox").click()
    # page.get_by_test_id("remote-js-code-checkbox").click()

    page.get_by_test_id("windows-radio").check()
    page.locator('select#preferred-interface').select_option("JavaScript API")

    page.locator('[name="tried-test-cafe"]').check()

    page.get_by_test_id("comments-area").fill("This is a comment for the test page.")

    page.get_by_role("button", name="Submit").click()
    page.wait_for_timeout(3000)
