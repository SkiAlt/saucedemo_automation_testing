from selenium import webdriver
from selenium.webdriver.common.by import By

def test_locked_out_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("locked_out_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Check for error message
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    if "Epic sadface" in error_message.text:
        print("Locked Out User: Login failed as expected!")
    else:
        print("Locked Out User: Unexpected behavior!")

    driver.quit()

if __name__ == "__main__":
    test_locked_out_user()
