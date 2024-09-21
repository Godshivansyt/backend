from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")  # Update this with your correct path

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open YouTube
driver.get("https://www.youtube.com")

# Locate the search box using 'name' attribute
search_box = driver.find_element(By.NAME, "search_query")
time.sleep(3)

# Enter a search query
search_box.send_keys("Python tutorials")
time.sleep(3)
# Simulate pressing the Enter key
search_box.send_keys(Keys.RETURN)
time.sleep(4)
# Close the browser
driver.quit()
