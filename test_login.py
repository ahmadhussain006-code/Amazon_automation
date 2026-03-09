from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        # Open Amazon website
        page.goto("https://www.amazon.in/", timeout=60000)

        # Wait for homepage
        page.wait_for_selector("//span[text()='Hello, sign in']", timeout=60000)

        # Click Sign In
        page.locator("//span[text()='Hello, sign in']").click()

        # Wait for email field
        page.wait_for_selector("//input[@type='email']", timeout=60000)

        # Enter email
        page.fill("//input[@type='email']", "shizahasan63@gmail.com")

        # Click Continue
        page.click("//input[@type='submit']")

        # Wait for password field
        page.wait_for_selector("//input[@type='password']", timeout=60000)

        # Enter password
        page.fill("//input[@type='password']", "Mind@12345")

        # Click Sign In
        page.click("//input[@id='signInSubmit']")

        # Wait a few seconds for redirect or login processing
        page.wait_for_timeout(8000)

        # Print page title safely
        try:
            title = page.title()
            print("Page Title is:", title)
        except Exception as e:
            print("Could not get page title:", e)

        print("Login test completed successfully.")

        page.wait_for_timeout(5000)
        browser.close()


if __name__ == "__main__":
    test_login()