import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_css_selector("input[id='name']").send_keys("pradyumna")
driver.find_element_by_id("alertbtn").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
driver.find_element_by_css_selector("input[id='name']").send_keys("pradyumna")