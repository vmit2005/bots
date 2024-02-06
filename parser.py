from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint,random

url = 'https://youla.ru/tolyatti'
try:
    driver = webdriver.Edge()
    d = driver.get(url=url)
    driver.maximize_window()
    sleep(2+4*random())
    element=driver.find_element(By.XPATH,"//div/input[@placeholder='Поиск по объявлениям' or @placeholder='Поиск объявлений']")
    # element.send_keys("монитор ")
    element.send_keys("системный блок")
    sleep(2 + 4 * random())
    element=driver.find_element(By.XPATH,'//span[text()="Найти"]//ancestor::button')
    element.click()
    sleep(3+random())
    elements=driver.find_elements(By.XPATH,'//div[@data-test-component="ProductOrAdCard"]')
    for element in elements:
        print(element.text)
        e1=element.find_element(By.XPATH,"//div/span/a" )
        print(e1.text)
        # img=element.find_element(By.XPATH,"//image")
        # print('str23')
        # print(img.get_attribute("xlink:href"))
    sleep(18+ 4 * random())
except:
    print("Error")

finally:
    driver.close()
    driver.quit()
    print("3")
