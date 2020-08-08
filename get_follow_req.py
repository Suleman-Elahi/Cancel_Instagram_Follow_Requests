from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import loginInfo
import os

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--incognito")
chromedriver_path = './chromedriver'

f = open("follow_req.txt","w")

browser = webdriver.Chrome(executable_path=chromedriver_path, options=options) #Star Browser

browser.get("https://www.instagram.com/")

time.sleep(3) #Waiting 3 seconds after we open the page.

#IG Login -->

username=browser.find_element_by_name ("username")
username.send_keys (loginInfo.username)

password =browser.find_element_by_name ("password")
password.send_keys(loginInfo.password)

login_button = browser.find_element_by_xpath ("//button[@type='submit']")
login_button.click()
time.sleep(6)

browser.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")

while True:
    try:
        vm_button = browser.find_element_by_xpath ("//button[@type='button']")
        vm_button.click()
        time.sleep(2)
    except NoSuchElementException:
        break

cfreq_source = browser.find_elements_by_xpath("//div[@class='-utLf']") 

for x in cfreq_source:
    f.write(x.text+"\n")
f.close()

print("Got the users you have sent follow request in \"follow_req.txt\" file, now exiting browser...")
browser.quit()
os.system('python cancel_req.py')
