import time

from selenium import webdriver

# options=webdriver.ChromeOptions()
# options.add_argument("headless")
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element_by_css_selector("a[href*='shop']").click()

products=driver.find_elements_by_xpath("//div[contains(@class,'h-100')]")
for product in products:
    text=product.find_element_by_xpath("div/h4").text
    if text=="Blackberry":
        product.find_element_by_xpath("div[@class='card-footer']/button[contains(text(),'Add')]").click()
        break

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
time.sleep(3)
driver.find_element_by_css_selector("button[class*='btn-success']").click()

wait=WebDriverWait(driver,25)
wait.until(expected_conditions.presence_of_element_located((By.ID,"country")))

driver.find_element_by_id("country").send_keys("Ind")

wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//a[text()='India']")))

driver.find_element_by_xpath("//a[text()='India']").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[class*='alert-dismissible']")))

text=driver.find_element_by_css_selector("div[class*='alert-dismissible']").text
assert "Success" in text
driver.get_screenshot_as_file("ScreenShot.png")
print("Test Completed")
driver.close()
