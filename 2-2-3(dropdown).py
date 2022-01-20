from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    arg1 = browser.find_element_by_id('num1').text
    arg2 = browser.find_element_by_id('num2').text
    sum = str(int(arg1) + int(arg2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()