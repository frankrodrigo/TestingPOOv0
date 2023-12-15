import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def driver_setup(request):
    service = Service("resources/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(15)
    driver.get("http://todo.ly/")

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
    return driver


def test_verify_CRUD_project(driver_setup):
    driver = driver_setup

    # Login
    driver.find_element(By.XPATH, "//img[contains(@src,'pagelogin')]").click()
    driver.find_element(By.ID, "ctl00_MainContent_LoginControl1_TextBoxEmail").send_keys("frank@frank.com")
    driver.find_element(By.ID, "ctl00_MainContent_LoginControl1_TextBoxPassword").send_keys("123456")
    driver.find_element(By.ID, "ctl00_MainContent_LoginControl1_ButtonLogin").click()

    # Explicit Wait
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ctl00_HeaderTopControl1_LinkButtonLogout")))

    assert driver.find_element(By.ID,
                               "ctl00_HeaderTopControl1_LinkButtonLogout").is_displayed(), "ERROR: login was incorrect"

    # Create
    name_project = "Mojix" + str(int(datetime.now().timestamp()))
    driver.find_element(By.XPATH, "//td[text()='Add New Project']").click()
    driver.find_element(By.ID, "NewProjNameInput").send_keys(name_project)
    driver.find_element(By.ID, "NewProjNameButton").click()
    time.sleep(1)
    actual_result = len(driver.find_elements(By.XPATH, "//td[text()='" + name_project + "']"))
    assert actual_result >= 1, "ERROR: The project was not created"

    # Update
    name_project = "Update" + str(int(datetime.now().timestamp()))
    driver.find_element(By.XPATH, "//div[contains(@style,'block')]/img").click()
    driver.find_element(By.XPATH, "//ul[@id=\"projectContextMenu\"]//a[text()='Edit']").click()
    edit_input = driver.find_element(By.XPATH, "//td/div/input[@id='ItemEditTextbox']")
    edit_input.clear()
    edit_input.send_keys(name_project)
    driver.find_element(By.XPATH, "//td/div/img[@id='ItemEditSubmit']").click()
    time.sleep(1)
    actual_result = len(driver.find_elements(By.XPATH, "//td[text()='" + name_project + "']"))
    assert actual_result >= 1, "ERROR: The project was not updated"

    # Delete
    driver.find_element(By.XPATH, "//div[contains(@style,'block')]/img").click()
    driver.find_element(By.ID, "ProjShareMenuDel").click()
    driver.switch_to.alert.accept()
    time.sleep(1)

    actual_result = len(driver.find_elements(By.XPATH, "//td[text()='" + name_project + "']"))
    assert actual_result == 0, "ERROR: The project was not removed"
