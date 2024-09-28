from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the login page
driver.get('https://login.qgenda.com/Account/PasswordChallenge?Email=brad.gershkowitz@gmail.com&ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dhttps%253A%252F%252Fapp.qgenda.com%26redirect_uri%3Dhttps%253A%252F%252Fapp.qgenda.com%252Foidc%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520email%26code_challenge%3DF63LnEvgv0CSafPYoUQuj7lm-sw_kl5tMu8Fsyc6Pa0%26code_challenge_method%3DS256%26response_mode%3Dform_post%26state%3DCfDJ8L51OZM0efJIq0_0ng4QpnXuGyq7CSbxnEb3pHubztpdFhaQZ7TB8PPLNIcwVh7Mu7LLUIVd-zu0Cni5wkqsQvkeRt9kTrlQNNN-h1XJRk38XswKuuXcgJXpUyMJ5FU892-XLoxJh26s6Z6rIGz3wF57zRvngqBUlnuvomOPlX6xh7RGRnoXqZoPxH1DZD14swsLczlsdXp4BwfS6qMhXZdnn4lY0X8wBRg4m7Anz45SkUHhXX8rw3D0PNQWeTCUcFI4Swu3bBtq2lmrzWZVXkK8gHfuzvLeSILxvNrZ4KRyFHfNwEfXdgAoB29LwV_2AIb3AFGAnx7AqR1VNEu11rqaLIsPlqzpnn5Q-PvjUy1l91wZH4ukpO9fBqT6NqyXZA%26x-client-SKU%3DID_NET8_0%26x-client-ver%3D7.1.2.0')


# Locate the password field and fill it
password_field = driver.find_element(By.NAME, 'Input.Password')
password_field.send_keys('12025BdG!')

# Submit the form
password_field.send_keys(Keys.RETURN)

# Check the result
print("Page title after login:", driver.title)

# Quit the browser
driver.quit()
