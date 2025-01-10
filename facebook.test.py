from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver=webdriver.Edge("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.facebook.com/login/")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("tharunmeeniga@gmail.com")
driver.find_element(By.ID,"pass").send_keys("tharun@123")

#driver.find_element(By.XPATH,"//input[@type='password']").send_keys("tharun@123")

time.sleep(5)