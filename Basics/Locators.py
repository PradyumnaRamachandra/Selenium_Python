import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(20)
# driver.find_element_by_name("name").send_keys("Prady")
# driver.find_element_by_id("exampleCheck1").click()
#driver.find_element_by_css_selector("input[name='name']").send_keys("Prady")
# driver.find_element_by_xpath("(//input[@name='name'])[1]").send_keys("Prady")
# driver.find_element_by_name("email").send_keys("Prady")
# driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_css_selector("input[name='name']").send_keys("Prady")
driver.find_element_by_css_selector("input[name='email']").send_keys("Prady")
gender_ele=driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']")
dropdown=Select(gender_ele)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
time.sleep(2)
msg=driver.find_element_by_class_name("alert-success").text
# print(msg)
assert "success" in msg
