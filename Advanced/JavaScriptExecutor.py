import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(20)

# driver.find_element_by_name("name").send_keys("Prady")
# driver.find_element_by_name("name").clear()

# print(driver.find_element_by_name("name").get_attribute("value"))

name=driver.execute_script("return document.getElementsByName('name')[0];")
name.send_keys("hello")


shop=driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",shop)

time.sleep(2)

driver.execute_script("window.scrollBy(0,5);")

ele=driver.find_element_by_xpath("(//button[contains(@class,'btn-info')])[4]")
driver.execute_script("arguments[0].scrollIntoView(true);",ele)
