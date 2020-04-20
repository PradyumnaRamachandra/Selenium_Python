import time

from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_argument("headless")

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe",options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(20)
print(driver.title)
print(driver.current_url)
driver.find_element_by_name("name").send_keys("hello")
text=driver.find_element_by_name("name").get_attribute("value")
print("Text entered is",text)
print("Test Completed")


