import asyncio
from playwright.async_api import async_playwright

async def scrape_qgenda():
    url = 'https://app.qgenda.com/Link/view?linkKey=cab8134e-3278-4260-a5a0-2138aee0dc7e'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_selector('.calendarContainerLeft', timeout=10000)

        # Get all date columns
        date_columns = await page.query_selector_all('div[data-rowindex]')

        for date_column in date_columns:
            # Extract the month and day
            month_element = await date_column.query_selector('span[style*="padding-left: 4px;"]:first-of-type')
            day_element = await date_column.query_selector('span[style*="padding-left: 4px;"]:last-of-type')

            month = await month_element.inner_text() if month_element else "N/A"
            day = await day_element.inner_text() if day_element else "N/A"

            date = f"{month} {day}"

            # Get all rows for this date
            rows = await date_column.query_selector_all('tr')

            for row in rows:
                left_cell = await row.query_selector('.calendarContainerLeft')
                right_cell = await row.query_selector('.calendarContainerRight')

                if left_cell and right_cell:
                    # Extract time
                    time_element = await left_cell.query_selector('div[style*="display: inline-block; word-break: normal;"]')
                    time = await time_element.inner_text() if time_element else "N/A"

                    # Extract name
                    name_element = await right_cell.query_selector('div[title]')
                    if name_element:
                        name = await name_element.get_attribute('title')
                        name = name.split('(')[0].strip() if name else "N/A"

                        print(f"Name: {name}, Time: {time}, Date: {date}")

        await browser.close()

asyncio.run(scrape_qgenda())
