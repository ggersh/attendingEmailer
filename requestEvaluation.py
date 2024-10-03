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

            # Wait for the input box to be visible before filling it
            await page.wait_for_selector("input[name='search']")  # Wait for the search input field

            # Fill in the search box with "Liu"
            await page.fill("input[name='search']", "Liu")  # Fill the input box with "Liu"

            # Simulate pressing the Enter key
            await page.keyboard.press("Enter")  # Simulate Enter key press

            # Optionally wait for a moment to see the result of the Enter key press
            await page.wait_for_timeout(3000)

            # Wait for the image element to be visible
            await page.wait_for_selector("img.onDemandSessionRowImage", state="visible")  # Wait for the image to be visible

            # Attempt to directly invoke the modal opening function
            await page.evaluate("""
                () => {
                    const img = document.querySelector('img.onDemandSessionRowImage');
                    console.log('Image found:', img);
                    if (img) {
                        img.click();  // Simulate a click event to try opening the modal
                    } else {
                        console.log('Image not found');
                    }
                }
            """)

            # Wait a moment to see if the modal appears
            await page.wait_for_timeout(1000)

            # Check if modal is open by waiting for the modal selector
            await page.wait_for_selector(".modal-class-selector", state="visible", timeout=10000)  # Replace with actual modal selector

            # If modal is not found, try keyboard interaction
            if not await page.is_visible(".modal-class-selector"):
                await page.keyboard.press("Tab")  # Move focus to the image
                await page.keyboard.press("Enter")  # Attempt to open modal via keyboard

                # Wait for the modal again
                await page.wait_for_selector(".modal-class-selector", state="visible", timeout=10000)  # Replace with actual modal selector

            # Optionally wait for a moment after opening the modal
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
