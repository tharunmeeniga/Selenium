from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Edge("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.meesho.com/?srsltid=AfmBOoqS29dGydXZlYNWNux1UsCgomQ-tMy7w_M6XpiW1R23V-rBMZM8")
driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div[1]/div/div[2]/div[1]/input").send_keys("kurta")
dd2=Select(driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div[1]/div/div[3]/div[3]/span"))



time.sleep(5)