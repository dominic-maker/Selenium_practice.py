import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/selenium web driver/chromedriver.exe")


def login():
    driver.get('https://www.instagram.com/')

    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    time.sleep(1)

    username.click()
    username.send_keys('testuseraccount24')
    time.sleep(1)

    password.click()
    password.send_keys('testuser')
    time.sleep(1)

    log_in = driver.find_element_by_xpath('//div[contains(text()="Log In")]')
    log_in.click()


login()

