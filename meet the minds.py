import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Edge("C://Drivers\\edgedriver_win64\\msedgedriver.exe")
#call a website to which you want to test or validate
driver.get("http://www.meettheminds.com/signup")
driver.find_element(By.ID,"mat-input-0").send_keys("Tharun")
driver.find_element(By.ID,"mat-input-1").send_keys("kumar")
driver.find_element(By.ID,"mat-input-2").send_keys("Meeniga")
driver.find_element(By.ID,"mat-input-3").send_keys("8328467650")
driver.find_element(By.ID,"mat-input-4").send_keys("tharunmeeniga@gmail.com")
driver.find_element(By.ID,"mat-input-5").send_keys("Automation Engineer")
driver.find_element(By.ID,"mat-input-6").send_keys("Kphb")
driver.find_element(By.ID,"mat-input-7").send_keys("Hyderabad")
#dropdown=Select(driver.find_element_by_class_name(""))
#dropdown.select_by_visible_text("1")
driver.find_element(By.ID,"mat-input-8").send_keys("510033")
driver.find_element(By.ID,"mat-input-9").send_keys("tharun")
driver.find_element(By.ID,"mat-input-10").send_keys("Tharun@123")
driver.find_element(By.ID,"mat-input-11").send_keys("Tharun@123")