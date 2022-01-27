import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('pageid', ["236895","236896","236897","236898","236899","236903","236905"])
def test_guest_should_see_login_link(browser, pageid):
    link = f"https://stepik.org/lesson/{pageid}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    field = browser.find_element_by_css_selector(".textarea")
    answer = math.log(int(time.time()))
    field.send_keys(str(answer))
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    message1 = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    print(message1)
    time.sleep(3)

if __name__ == "__main__":
    unittest.main()