from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set up the Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the login page
driver.get('https://login.qgenda.com/Account/PasswordChallenge?Email=brad.gershkowitz@gmail.com')

# Locate the password field and fill it
password_field = driver.find_element(By.NAME, 'Input.Password')
password_field.send_keys('12025BdG!')

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for the dashboard page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lnkScheduleTab')))
print("Logged in successfully")

# Navigate to the schedule page
schedule_link = driver.find_element(By.ID, 'lnkScheduleTab')
schedule_link.click()
print("Clicked on Schedule Tab")

# Wait for the schedule page to load fully
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'content')))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'calendarContainerLeft')))
print("Schedule page loaded")

# Add a delay to ensure dynamic content is loaded
time.sleep(10)
print("Waited for 10 seconds")

# Get the page source
page_html = driver.page_source
print("Page source retrieved")

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page_html, 'html.parser')
print("HTML parsed with BeautifulSoup")

# Get all date columns
date_columns = soup.select('div[data-rowindex]')

for date_column in date_columns:
    # Extract the month and day
    month_element = date_column.select_one('span[style*="padding-left: 4px;"]:first-of-type')
    day_element = date_column.select_one('span[style*="padding-left: 4px;"]:last-of-type')

    month = month_element.get_text(strip=True) if month_element else "N/A"
    day = day_element.get_text(strip=True) if day_element else "N/A"
    date = f"{month} {day}"

    # Get all rows for this date
    rows = date_column.select('tr')

    for row in rows:
        left_cell = row.select_one('.calendarContainerLeft')
        right_cell = row.select_one('.calendarContainerRight')

        if left_cell and right_cell:
            # Extract time
            time_element = left_cell.select_one('div[style*="display: inline-block; word-break: normal;"]')
            time = time_element.get_text(strip=True) if time_element else "N/A"

            # Extract name
            name_element = right_cell.select_one('div[title]')
            if name_element:
                name = name_element['title'].split('(')[0].strip() if name_element['title'] else "N/A"
                print(f"Name: {name}, Time: {time}, Date: {date}")

# Quit the browser
driver.quit()
print("Browser closed")
