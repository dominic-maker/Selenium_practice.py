from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.jumia.co.ke/mobile-phones/')
driver.implicitly_wait(10)
driver.find_element_by_class_name("_more -fs12").click()
driver.find_element(By.XPATH, "//input[@id='fi-q']").send_keys("Samsung phones")
phones_names = driver.find_elements(By.XPATH, "//h3[contains(text(),'Samsung Galaxy A12, 6.5, 4GB RAM + 128GB (Dual SI')]")
prices = driver.find_elements(By.XPATH, "//body/div[@id='jm']/main[@class='has-b2top -pts']/div[@class='aim row -pbm']/div[@class='-pvs col12']/section[@class='card -fh']/div[@class='-paxs row _no-g _4cl-3cm-shs']/article[1]/a[1]/div[2]/div[2]")

for phones in phones_names:
    print(phones.text)
print('*' * 50)

for price in prices:
    print(price.text)

driver.quit()

