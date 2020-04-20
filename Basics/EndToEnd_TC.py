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

items_list=[]

items=driver.find_elements_by_xpath("//div[@class='product-action']/button[text()='ADD TO CART']")
for item in items:
    item_text=item.find_element_by_xpath("parent::div/parent::div/h4").text
    items_list.append(item_text)
    item.click()

time.sleep(2)
driver.find_element_by_css_selector("img[alt='Cart']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'PROCEED')]").click()
wait=WebDriverWait(driver,25)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.promoCode")))

items_list1=[]
cart_items=driver.find_elements_by_xpath("//p[@class='product-name']")
for item in cart_items:
    item_text=item.text
    items_list1.append(item_text)

assert items_list==items_list1,"Items are not matching"

price_before=driver.find_element_by_xpath("//span[@class='discountAmt']").text
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_xpath("//button[text()='Apply']").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
message=driver.find_element_by_css_selector("span.promoInfo").text
assert "applied" in message
print(message)

price_after=driver.find_element_by_xpath("//span[@class='discountAmt']").text
assert float(price_after) < float(price_before)