import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

wait=WebDriverWait(driver,25)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[text()='Click Here']")))

parent_window=driver.current_window_handle
driver.find_element_by_xpath("//a[text()='Click Here']").click()
time.sleep(2)


driver.switch_to.window(driver.window_handles[1])
print(driver.find_element_by_xpath("//h3[text()='New Window']").text)
driver.close()

driver.switch_to.window(parent_window)
print(driver.find_element_by_xpath("//h3[text()='Opening a new window']").text)


