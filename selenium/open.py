from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# Initialize WebDriver (Chrome in this case)
# Create a Service object and provide the path to your ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")  # Update this with your correct path

# Initialize WebDriver using the Service object
driver = webdriver.Chrome(service=service)

# Open YouTube
driver.get("https://www.youtube.com")
time.sleep(4)
driver.quit()