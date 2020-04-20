import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/frames")
driver.maximize_window()

wait=WebDriverWait(driver,25)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[text()='iFrame']")))

driver.find_element_by_xpath("//a[text()='iFrame']").click()

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_xpath("//body[@id='tinymce']").clear()
driver.find_element_by_xpath("//body[@id='tinymce']").send_keys("Working with Iframe")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
