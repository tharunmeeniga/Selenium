import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge("C://Drivers\\edgedriver_win64\\msedgedriver.exe")
#call a website to which you want to test or validate
driver.get("C:/Users/tharun/PycharmProjects/selenium_projects/test cases.py.html")
driver.find_element(By.ID,"pateintname").send_keys("Tharun")
driver.find_element(By.ID,"phoneno").send_keys("9390685200")
driver.find_element(By.XPATH,"/html/body/center[2]/input[3]").send_keys("4")
driver.find_element(By.XPATH,"/html/body/center[2]/select").send_keys("fever")
driver.find_element(By.XPATH,"/html/body/center[2]/input[4]").click()
time.sleep(5)