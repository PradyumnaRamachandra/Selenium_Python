import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_xpath("//input[@id='fromCity']").click()
time.sleep(2)
ele=driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("del")
time.sleep(1)
# //p[contains(@class,'blackText')]
from_ele=driver.find_elements_by_xpath("//p[contains(@class,'blackText')]")
print(len(from_ele))
for cities in from_ele:
    # print(cities.text)
    if cities.text=="Denver, United States":
        cities.click()
        break

driver.find_element_by_xpath("//input[@placeholder='To']").send_keys("del")
time.sleep(1)
driver.find_element_by_xpath("//p[contains(text(),'Delhi, India')]").click()