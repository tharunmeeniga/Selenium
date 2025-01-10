from selenium import webdriver
from selenium.webdriver.common.by import By
#locate webdriver from the local drive
driver=webdriver.Edge("C://Drivers\\edgedriver_win64\\msedgedriver.exe")
#call a website to which you want to test or validate
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("spb")
time.sleep(10)