import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(20)
radioboxes=driver.find_elements_by_xpath("//input[@type='radio']")
for radiobox in radioboxes:
    if radiobox.get_attribute("value")=="radio2":
        radiobox.click()
        assert radiobox.is_selected(),"Radio Box is Selected"

check_ele=driver.find_elements_by_css_selector("input[type='checkbox']")
for checkbox in check_ele:
    if checkbox.get_attribute("value")=="option3":
        checkbox.click()
        assert checkbox.is_selected(),"Check Box is not Selected"

