from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
# import math
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    x = num1.text
    y = num2.text
    sum = int(x) + int(y)
    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(str(sum))
    # input = browser.find_element(By.CSS_SELECTOR, '#answer')
    # input.send_keys(y)
    # checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    # checkbox.click()
    # radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    # radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла