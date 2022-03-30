from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test Case Started")

driver.maximize_window()
driver.get("https://www.google.co.in/")
driver.find_element_by_name("q").send_keys("HARMAN")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
print("Test Case Completed")