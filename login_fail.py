from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


try:
    driver = webdriver.Chrome()
    # Open the SauceDemo login page
    driver.get('https://www.saucedemo.com/')
    
    # Wait for the login elements to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'user-name')))
    
    # Enter the username
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys('standard_user')
    
    # Enter the password
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('wrong_password')
    
    # Click the login button
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    
    
    
finally:
    # Close the WebDriver
    print("\nlogin failed, incorrect username or password")
    driver.quit()
