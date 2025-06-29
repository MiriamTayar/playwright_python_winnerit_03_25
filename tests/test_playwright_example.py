import re
from playwright.sync_api import Page, expect, BrowserContext, APIRequestContext


# Structure
#
# Playwright
# Browser + Context
# Page - tab inside browser - Incognito mode


#  פונקציית בדיקה 1: בדיקת כותרת העמוד
def test_has_title(page: Page):

    page.set_viewport_size({"width": 1600, "height": 1200}) # שינוי גודל החלון

    page.goto("https://playwright.dev/")# ניווט לאתר

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))# בדיקת כותרת


# פונקציית בדיקה 2: לחיצה על קישור והופעת כותרת
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


# פונקציית בדיקה 3: דוגמה מורחבת
def test_example(page: Page, context: BrowserContext, api_context: APIRequestContext):
    page.goto("https://playwright.dev/")
    context.clear_cookies() #ניקוי של cookies לדמות משתמש חדש

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()



    # api_context: APIRequestContext
    #מאפשר לבצע בקשות API (HTTP) ישירות בלי לפתוח את הדפדפן.
