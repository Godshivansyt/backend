from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# Path to your ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")  # Update this with your correct path

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.google.com")
time.sleep(3)
# Find element using the new syntax
search_box = driver.find_element(By.NAME, "q")  # Example using 'name' attribute

# Perform actions like typing a query and pressing Enter
search_box.send_keys("Selenium automation with Python")
time.sleep(2)
search_box.submit()
time.sleep(3)
# Close the browser
driver.quit()
