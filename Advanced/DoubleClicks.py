import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()
driver.implicitly_wait(20)
#
action=ActionChains(driver)
# action.move_to_element(driver.find_element_by_xpath("//button[@class='dropbtn']")).perform()
#
# action.move_to_element(driver.find_element_by_link_text("Google")).click().perform()
action.context_click(driver.find_element_by_id("double-click")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()

alert=driver.switch_to.alert
print(alert.text)
alert.accept()