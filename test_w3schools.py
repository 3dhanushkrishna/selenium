from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase Started")

driver.maximize_window()

driver.get("https://www.w3schools.com/")
driver.find_element_by_link_text("Tutorials").click()
time.sleep(1)
driver.find_element_by_link_text("Learn Python").click()
time.sleep(7)