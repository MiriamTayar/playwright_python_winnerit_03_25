from playwright.sync_api import expect, Page

BASE_URL = "https://devexpress.github.io/testcafe/example/"
name = "Miri Ram"

def test_demo_page_title(page:Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("TestCafe Example Page") #בדיקת הטקסט שמופיע בלשונית של הדפדפן

def test_user_name_presented(page: Page):
    page.goto(BASE_URL)
    page.locator("#developer-name").press_sequentially(name, delay=350)
    page.get_by_test_id("remote-testing-checkbox").check() # סימון checkbox
    # page.get_by_test_id("reusing-js-code-checkbox").check()  # סימון
    # page.get_by_test_id("parallel-testing-checkbox").check()
    # page.get_by_test_id("ci-checkbox").check()
    # page.get_by_test_id("analysis-checkbox").check()
    # page.get_by_test_id("reusing-js-code-checkbox").uncheck() # ביטול הסימון

    page.get_by_test_id("macos-radio").check()
    page.locator('select#preferred-interface').select_option("Both")
    page.locator('[name="tried-test-cafe"]').check()

    # page.wait_for_timeout(3000)
    #
    # handle = page.locator(".ui-slider-handle") #מעבר על הסלאידר
    # box = handle.bounding_box()
    # if box:
    #     page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
    #     page.mouse.down()
    #     page.mouse.move(box["x"] + box["width"] / 2 + 150, box["y"] + box["height"] / 2)
    #     page.mouse.up()
    #
    # page.wait_for_timeout(3000)


    page.get_by_test_id("comments-area").fill("This is a comment for the test page.")

    page.get_by_role("button", name="Submit").click()
    page.wait_for_timeout(3000)


#לאחר המעבר לדף הבא
    expect(page).to_have_url(BASE_URL + "thank-you.html")

    # expect(page.locator("thank-you-header")).to_have_text("Thank you, Miri Ram!") #בודק שהטקסט מדויק לחלוטין – בדיוק כפי שמופיע ב־HTML
    expect(page.get_by_test_id("thank-you-header")).to_have_text("Thank you, Miri Ram!")
