from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\chromedriver.exe")
# driver=webdriver.Firefox(executable_path="C:\\PythonProjects\\Selenium_Python\\drivers\\geckodriver.exe")
# driver=webdriver.Ie("C:\\PythonProjects\\Selenium_Python\\drivers\\IEDriverServer.exe")
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.minimize_window()
# driver.maximize_window()
# driver.refresh()
# driver.close()