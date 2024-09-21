import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the webdriver (automatically downloads the correct version)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to Amazon.in and search for Redmi phones
driver.get("https://www.amazon.in/")
time.sleep(2)  # Give the page time to load

# Search for 'Redmi phones'
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Redmi phones")
search_box.submit()

time.sleep(3)  # Allow search results to load

# Fetch product names and prices
phones = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")

# Create a dictionary to store the data
phone_data = {}

# Extracting names and prices and storing in the dictionary
for phone, price in zip(phones, prices):
    phone_name = phone.text
    phone_price = price.text
    phone_data[phone_name] = f"₹{phone_price}"

# Save the data to a JSON file
with open("amazon.json", "w", encoding="utf-8") as json_file:
    json.dump(phone_data, json_file, ensure_ascii=False, indent=4)

# Quit the driver
driver.quit()

print("Data has been saved to amazon.json file.")
