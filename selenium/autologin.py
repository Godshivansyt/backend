from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import  time


# Path to your ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")  # Update this with your correct path

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open the initial page
driver.get("https://in.pinterest.com/")  # Replace with the actual URL of the landing page
time.sleep(3)

# Locate and click the login button on the landing page
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")  # Update with the actual XPath or locator for the login button
login_button.click()
time.sleep(2)
# Wait for the login popup to be visible
driver.implicitly_wait(10)  # Adjust as needed for your network speed and site response time

# Locate the email field in the login popup
email_field = driver.find_element(By.NAME, "email")  # Update with the actual name, id, or class for the email field

# Locate the password field in the login popup
password_field = driver.find_element(By.NAME, "password")  # Update with the actual name, id, or class for the password field

# Enter your credentials
email_field.send_keys("kapilsharmax24@proton.me")  # Replace with your email address
password_field.send_keys("easiestpassword24")  # Replace with your password

# Locate the login button in the popup
login_submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Update with the actual XPath or locator for the submit button in the popup
login_submit_button.click()

time.sleep(3)
# Example: Check if the user is redirected to a specific page or element
try:
    # Wait until a specific element is visible after login
    driver.implicitly_wait(10)  # seconds
    success_element = driver.find_element(By.ID, "welcome-message")  # Replace with an actual element visible after login
    print("Login successful")
except:
    print("Login failed")

time.sleep(3)
# Close the browser
driver.quit()
