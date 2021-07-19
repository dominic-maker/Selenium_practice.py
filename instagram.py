import time
from config import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver

browser = webdriver.Chrome()
url = "https://www.instagram.com/"
browser.get(url)

time.sleep(2)
username_el = browser.find_element_by_name("username")
username_el.send_keys(INSTA_USERNAME)
password_el = browser.find_element_by_name("password")
password_el.send_keys(INSTA_PASSWORD)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit]")
submit_btn_el.click()
