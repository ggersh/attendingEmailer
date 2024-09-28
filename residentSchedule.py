from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'content')))  # Adjust as needed
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'calendarContainerLeft')))  # Example of a specific element

# Print the current page URL and title
print("Current page URL:", driver.current_url)
print("Page title:", driver.title)

# Print the HTML of the page
page_html = driver.page_source
print("Page HTML:", page_html)

# Quit the browser
driver.quit()
