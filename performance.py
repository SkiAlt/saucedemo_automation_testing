from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_performance_glitch_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("performance_glitch_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Verify if the page eventually loads, allowing extra time
    start_time = time.time()
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        load_time = time.time() - start_time
        print(f"Performance Glitch User: Login successful, page loaded in {load_time:.2f} seconds.")
    except:
        print("Performance Glitch User: Login failed or page load too slow!")

    driver.quit()

if __name__ == "__main__":
    test_performance_glitch_user()
