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
    password_input.send_keys('secret_sauce')
    
    # Click the login button
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    
    # Wait for the products page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item')))
    
    # Add the first product to the cart
    add_to_cart_button = driver.find_element(By.CLASS_NAME, 'btn_inventory')
    add_to_cart_button.click()
    
    # Click on the cart icon
    cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.click()
    
    # Verify the item is in the cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cart_item')))
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    
    if len(cart_items) > 0:
        print("Item successfully added to the cart!")
    else:
        print("Cart is empty!")
    
finally:
    # Close the WebDriver
    driver.quit()
