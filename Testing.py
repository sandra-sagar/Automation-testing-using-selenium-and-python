import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def browser_setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Maximize the browser window
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_contact(browser_setup):
    browser_setup.get("https://automation-testing.odoo.com/")

    # Wait for the login form to be visible
    WebDriverWait(browser_setup, 10).until(
        EC.visibility_of_element_located((By.ID, "login"))
    )
    print("Login form is visible")

    # Find and fill in email and password fields
    email_input = browser_setup.find_element(By.ID, "login")
    email_input.send_keys("sandrasagar00@gmail.com")

    password_input = browser_setup.find_element(By.ID, "password")
    password_input.send_keys("dingus2004")

    # Submit the form
    login_button = browser_setup.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("Login button clicked")

    # Select CRM
    crm_button = WebDriverWait(browser_setup, 30).until(
    EC.element_to_be_clickable((By.ID, "result_app_3"))
    )
    crm_button.click()
    print("CRM button is clicked")

    # Find and fill in contact details
    
    new_button = WebDriverWait(browser_setup, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/button[1]"))
    )
    new_button.click()
    print("New button is clicked")

    organization=WebDriverWait(browser_setup,10).until(
        EC.visibility_of_element_located((By.ID,"partner_id_0"))
    )
    organization.send_keys("John Doe")
    print("Name entered")

    opportunity=WebDriverWait(browser_setup,10).until(
        EC.visibility_of_element_located((By.ID,"name_0"))
    )
    opportunity.send_keys("John Doe")
    print("Opportunity entered")

    email_input = WebDriverWait(browser_setup, 10).until(
            EC.visibility_of_element_located((By.ID, "email_from_0"))
        )
    email_input.send_keys("john.doe@example.com")
    print("Email entered")

    phone_input=WebDriverWait(browser_setup,10).until(
        EC.visibility_of_element_located((By.ID,"phone_0"))
    )
    phone_input.send_keys("1234567890")
    print("Phone number entered")

    # Click the "Add" button to save the contact
    add_button = WebDriverWait(browser_setup, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "o_kanban_add"))
    )
    add_button.click()
    print("Add button is clicked")

    # Verify that the contact is added
    contact_name_element = WebDriverWait(browser_setup, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'o_kanban_group') and contains(@class, 'o_group_draggable')]//*[contains(text(), 'John Doe')]"))
    )
    assert contact_name_element.text == "John Doe"
    print("The contact has been added successfully")

