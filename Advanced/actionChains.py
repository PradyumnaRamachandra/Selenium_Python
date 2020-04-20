import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")
driver.maximize_window()
driver.implicitly_wait(20)
ele=driver.find_element_by_xpath("(//button[text()='Search'])[1]")
action=ActionChains(driver)
action.move_to_element(ele).click().perform()
time.sleep(2)
action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

