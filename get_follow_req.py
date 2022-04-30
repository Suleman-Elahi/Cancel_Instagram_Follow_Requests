from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import loginInfo
import os

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920x1080")
options.add_argument("--incognito")
chromedriver_path = './chromedriver'

f = open("follow_req.txt","w")

s=Service('./chromedriver.exe')
browser = webdriver.Chrome(service=s, options=options)

browser.get("https://www.instagram.com/")

time.sleep(3) #Waiting 3 seconds after we open the page.

#IG Login -->

username=browser.find_element(By.NAME, "username")
username.send_keys (loginInfo.username)

password =browser.find_element(By.NAME, "password")
password.send_keys(loginInfo.password)

login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(6)

browser.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")

while True:
    try:
        vm_button = browser.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/article/main/button')
        vm_button.click()
        time.sleep(2)
    except NoSuchElementException:
        break

cfreq_source = browser.find_elements(By.XPATH, "//div[@class='-utLf']") 

count=0

for x in cfreq_source:
    f.write(x.text+"\n")
    count+=1
f.close()

print("Got "+str(count)+" users you have sent follow request in \"follow_req.txt\" file, now exiting browser...")
browser.quit()
os.system('python cancel_req.py')
