import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
# driver.implicitly_wait(20)
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(3)
items_count=driver.find_elements_by_xpath("//div[@class='products']/div[@class='product']")
assert len(items_count)==3
items=driver.find_elements_by_xpath("//div[@class='product-action']/button[text()='ADD TO CART']")
for item in items:
    item.click()

time.sleep(2)
driver.find_element_by_css_selector("img[alt='Cart']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'PROCEED')]").click()
wait=WebDriverWait(driver,25)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.promoCode")))
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[text()='Apply']").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
message=driver.find_element_by_css_selector("span.promoInfo").text
assert "applied" in message
print(message)
