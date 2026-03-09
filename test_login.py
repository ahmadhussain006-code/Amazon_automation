import pytest
from playwright.sync_api import sync_playwright


def test_demo(request):

    browser_name = request.config.getoption("browser")

    with sync_playwright() as p:

        # Cross browser launch
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        else:
            browser = p.webkit.launch(headless=True)

        context = browser.new_context(viewport=None)
        page = context.new_page()

        # Open website
        page.goto("https://www.saucedemo.com/")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Handle popup if appears
        try:
            page.locator("//button[text()='OK']").click(timeout=3000)
        except:
            print("No popup appeared")

        # Wait inventory page
        page.wait_for_url("**/inventory.html")

        # Add product
        page.locator("text=Sauce Labs Bike Light").locator("xpath=ancestor::div[@class='inventory_item']//button").click()

        # Cart
        page.click(".shopping_cart_link")

        # Checkout
        page.click("#checkout")

        # Fill details
        page.fill("#first-name", "hussain")
        page.fill("#last-name", "ahmad")
        page.fill("#postal-code", "123456")

        page.click("#continue")

        # Finish
        page.click("#finish")

        print("Test completed successfully")
        print("Hussain")

        browser.close()