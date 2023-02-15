from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    start_button = browser.find_element(By.CSS_SELECTOR,'.btn.btn-primary')
    start_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR,'#input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR,'.btn.btn-primary')
    button.click()
    time.sleep(30)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла