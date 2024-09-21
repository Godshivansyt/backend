from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Create a Service object and provide the path to your ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")  # Update this with your correct path

# Initialize WebDriver using the Service object
driver = webdriver.Chrome(service=service)
time.sleep(2)
# Open a website
driver.get("https://www.google.com")
time.sleep(3)
# Close the browser
driver.quit()
