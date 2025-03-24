from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import time

# Test cases
test_cases = [
    {
        "fullName": "User MissingPhone",
        "useName": "usernopho",
        "email": "nopho@example.com",
        "phoneNumber": "",
        "password": "password123",
        "confirmPassword": "password123",
        "gender": "male"
    },
    {
        "fullName": "User ShortPass",
        "useName": "shortpassuser",
        "email": "shortpass@example.com",
        "phoneNumber": "9999999992",
        "password": "123",
        "confirmPassword": "123",
        "gender": "female"
    },
    {
        "fullName": "Mismatch User",
        "useName": "mismatchuser",
        "email": "mismatch@example.com",
        "phoneNumber": "9999999993",
        "password": "password123",
        "confirmPassword": "different123",
        "gender": "others"
    },
    {
        "fullName": "Success User",
        "useName": "successuser",
        "email": "success@example.com",
        "phoneNumber": "9999999994",
        "password": "validpass123",
        "confirmPassword": "validpass123",
        "gender": "male"
    }
]

# Launch Chrome browser
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")

# Add wait time to ensure the page loads fully
time.sleep(5)

# Loop through all test cases
for test in test_cases:
    driver.refresh()
    time.sleep(2)

    # Wait for the username field to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "useName")))

    # Fill out the form fields
    driver.find_element(By.ID, "fullName").clear()
    driver.find_element(By.ID, "fullName").send_keys(test["fullName"])

    driver.find_element(By.ID, "useName").clear()
    driver.find_element(By.ID, "useName").send_keys(test["useName"])

    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(test["email"])

    driver.find_element(By.ID, "phoneNumber").clear()
    driver.find_element(By.ID, "phoneNumber").send_keys(test["phoneNumber"])

    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(test["password"])

    driver.find_element(By.ID, "confirmPassword").clear()
    driver.find_element(By.ID, "confirmPassword").send_keys(test["confirmPassword"])

    # Select gender radio button
    driver.find_element(By.ID, test["gender"]).click()

    # Submit the form
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(2)

    # Handle JavaScript alert if present (Success Scenario)
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Success for {test['fullName']}:\n{alert_text}\n")
        alert.accept()
        continue
    except NoAlertPresentException:
        pass

    # Check for error messages in span tags with class 'error'
    error_messages = []
    error_elements = driver.find_elements(By.CLASS_NAME, "error")

    for error_element in error_elements:
        error_msg = error_element.text.strip()
        if error_msg:
            error_messages.append(error_msg)

    # Print appropriate message based on validation
    if error_messages:
        print(f"Errors for {test['fullName']}: {', '.join(error_messages)}\n")
    else:
        print(f"No errors found for {test['fullName']} - Check if success is displayed properly.\n")

    time.sleep(3)

# Close browser after testing
driver.quit()
