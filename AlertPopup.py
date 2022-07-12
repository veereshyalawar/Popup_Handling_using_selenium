import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://nxtgenaiacademy.com/alertandpopup/")
driver.find_element(By.XPATH,"//button[@name ='alertbox']").click()
time.sleep(5)
alert = driver.switch_to.alert
time.sleep(5)
#print(alert.text)
alert.accept()
time.sleep(3)
driver.close()