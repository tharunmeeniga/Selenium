import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Test_facebook:
    driver=webdriver.Edge("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
    driver.get("https://www.facebook.com/login/")
@pytest.mark.parametrize("email,password",[("tharunmeeniga@gmail.com","tharun@123"),("tharunmeeniga3@gmail.com","tharun@143")])
def test_login(self,email,password):
    assert email=="tharunmeeniga@gmail.com"
    assert email==password,"Unequal"

time.sleep(5)