import asyncio
from playwright.async_api import async_playwright

async def scrape_qgenda():
    url = 'https://app.qgenda.com/Link/view?linkKey=cab8134e-3278-4260-a5a0-2138aee0dc7e'

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to the URL
        await page.goto(url)

        # Wait for the specific element(s) to load
        await page.wait_for_selector('.c000000F5FAF5', timeout=10000)  # Adjust the selector and timeout as needed

        # Find all elements with the specified class
        elements = await page.query_selector_all('.c000000F5FAF5')

        # Extract the title attribute from each element
        titles = []
        for element in elements:
            title = await element.get_attribute('title')
            if title:
                titles.append(title)

        # Print the titles
        for title in titles:
            print(title)

        # Close the browser
        await browser.close()

# Run the scrape function
asyncio.run(scrape_qgenda())
