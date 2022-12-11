from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import datetime;


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = 'COUNTDOWN {:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
  

PATH =  r"chromedriver_win32/chromedriver.exe"
driver= webdriver.Chrome(service=Service(PATH))

with open('readmex.txt',encoding="utf8") as f:
    mylist = [line.rstrip('\n') for line in f]
    
url = "https://m.facebook.com"
driver.set_window_size(500,500)
driver.get(url)

email_minny = input("ENTER YOUR EMAIL:")
password = input("ENTER YOUR PASSWORD: ")
urlpost = input("INSERT THE 'URL' FOR COMMENT: ")
round_cnt = int(input("ENTER ROUND : "))
t = input("ENTER SECOND (1HR is 3,600 SEC): ")

time.sleep(0.5)
print ("INSERTING EMAIL...")
login = driver.find_element(By.ID,"m_login_email").send_keys(email_minny)
time.sleep(0.5)

print ("INSERTING PASSWORD...")
pwd = driver.find_element(By.ID,"m_login_password").send_keys(password)
btn_login = driver.find_element(By.NAME,"login").click()

time.sleep(5)
print("REFRESH PAGE 5 SECOND...")
driver.get(url)



time.sleep(3)
driver.get(urlpost)
time.sleep(3)



emoji = "• "

for i in range(round_cnt):
    ct = datetime.datetime.now()
    print("ROUND :",i+1)
    for i in range(len(mylist)):
        # cmt = driver.find_element(By.ID,"composerInput").send_keys(emoji)
        cmt = driver.find_element(By.ID,"composerInput").send_keys(mylist[i])
        cmt = driver.find_element(By.ID,"composerInput").send_keys(Keys.ENTER)
        
    cmt = driver.find_element(By.ID,"composerInput").send_keys("# %s "%(ct))
        
    time.sleep(3)
    enter_post = driver.find_element(By.NAME,"submit").click()
    countdown(int(t))
    
print("Done!")
    




