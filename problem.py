from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_problem_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("problem_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Verify if the page loads, but check for broken elements
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        print("Problem User: Login successful, but check for issues on the page.")
        
        # Check if the image is broken (just an example issue)
        image = driver.find_element(By.XPATH, "//img[@alt='Sauce Labs Backpack']")
        if "sl-404" in image.get_attribute("src"):
            print("Problem User: Broken image detected!")
        else:
            print("Problem User: No obvious issues detected.")

    except:
        print("Problem User: Login failed!")

    driver.quit()

if __name__ == "__main__":
    test_problem_user()
