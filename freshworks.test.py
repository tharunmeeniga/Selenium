from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver=webdriver.Edge("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.freshworks.com/")

driver.find_element(By.LINK_TEXT,"Customer Service").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"").click()

time.sleep(5)


