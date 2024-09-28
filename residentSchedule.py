from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

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

# Navigate to the schedule page
schedule_link = driver.find_element(By.ID, 'lnkScheduleTab')
schedule_link.click()

# Wait for the schedule page to load fully
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'content')))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'calendarContainerLeft')))

# Print the current page URL and title
print("Current page URL:", driver.current_url)
print("Page title:", driver.title)

# Get the page source
page_html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page_html, 'html.parser')

# Find all div elements with title attributes that match the name pattern
name_divs = soup.find_all('div', title=re.compile(r'^[A-Z][a-z]+,\s[A-Z][a-z]+\s\([A-Z][a-z]+\s[A-Z]+\d+\)'))

# Extract and print the names
print("Extracted names:")
for div in name_divs:
    print(div['title'].split('\n')[0])  # Split by newline and take the first part (the name)

# Quit the browser
driver.quit()
