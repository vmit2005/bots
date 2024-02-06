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
    element.send_keys("hdd")
    sleep(2 + 4 * random())
    element=driver.find_element(By.XPATH,'//span[text()="Найти"]//ancestor::button')
    element.click()
    sleep(3+random())
    elements=driver.find_elements(By.XPATH,"//div/span/a")
    list_adress=[]
    for element in elements[1:-1]:
        e=element.get_attribute("href")
        list_adress+=[e]
    # for adress in list_adress[0:3]:
    for adress in list_adress:
        print(adress)
        d = driver.get(url=adress)
        sleep(3*random())
        # element=driver.find_element(By.XPATH,"//div/dl/dd/p")
        print("30")
        # print(element.text)
        elements=driver.find_elements(By.XPATH,'//div/img')
        print(len(elements))
        for element in elements:

            e=element.get_attribute("src")
            # print(e[35:42])
            if e[35:42]=="720_720":
                print(e)

            print("=====")

        # img=element.find_element(By.XPATH,"//image")
        # print('str23')
        # print(img.get_attribute("xlink:href"))
    sleep(18+ 4 * random())
except:
    print("Error")

finally:
    # driver.close()
    driver.quit()
    print("3")