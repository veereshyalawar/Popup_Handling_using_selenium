import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://www.selenium.dev/downloads/")
time.sleep(3)
driver.find_element(By.LINK_TEXT,'32 bit Windows IE').click()
time.sleep(6)
driver.close()