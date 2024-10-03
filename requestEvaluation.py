import asyncio
from playwright.async_api import async_playwright, TimeoutError

async def run(headless=True):
    async with async_playwright() as playwright:
        # Launch the browser
        browser = await playwright.chromium.launch(headless=headless)
        # Create a new browser context
        context = await browser.new_context()

        # Open a new page
        page = await context.new_page()

        try:
            # Navigate to the login page
            await page.goto("https://www.new-innov.com/Login/Login.aspx")

            # Wait for the institution dropdown to be visible and fill it
            await page.wait_for_selector("#txtClientName")
            await page.select_option("#txtClientName", "jmh")  # Select "Jackson Memorial Hospital - JMH"

            # Fill out the username and password
            await page.fill("#txtUsername", "bgershkowitz")  # Replace with your username
            await page.fill("#txtPassword", "12025BdG!123")  # Replace with your password

            # Simulate a click on the page to trigger any necessary events
            await page.click("body")  # Click on the body or another appropriate element

            # Wait for the login button to be visible and enabled
            await page.wait_for_selector("#btnLoginNew", state="visible")
            await page.wait_for_function("() => !document.querySelector('#btnLoginNew').disabled", timeout=60000)  # Wait for the button to be enabled

            # Click the login button
            await page.click("#btnLoginNew")

            # Wait for the page to load after login
            await page.wait_for_load_state("networkidle")  # Wait for the network to be idle

            # Navigate to the specified evaluation forms page
            await page.goto("https://www.new-innov.com/EvaluationForms/EvaluationFormsHost.aspx?Control=CompleteEvals")

            # Wait for a moment to see the result on the first evaluation page
            await page.wait_for_timeout(3000)

            # Now navigate to the next specified URL
            await page.goto("https://www.new-innov.com/EvaluationForms/EvaluationFormsHost.aspx?Data=ILAI7Qy3xO0dH9QDopSbrxA5jlRdAqOqm13MqYV3T6m0HTzrXZKtjuZgi84gUQQEPSreplacedPSkgI2swRBdV3jc64HzYI2ye2lVBLrBbF")

            # Wait for a moment to see the result on the second evaluation page
            await page.wait_for_timeout(3000)

        except TimeoutError as e:
            print("An element took too long to appear:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            # Close the browser
            await browser.close()

# Run the asynchronous function
asyncio.run(run(headless=False))  # Set headless=True for headless mode
