import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://nervgh.github.io/pages/angular-file-upload/examples/simple/")
driver.find_element(By.XPATH,"//input[@multiple ='']").send_keys("C:\\Users\\veeresh\\Documents\\veer.txt")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@ng-click=\"item.upload()\"]")
time.sleep(5)