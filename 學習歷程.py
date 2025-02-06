#學習歷程#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # for test

driver = webdriver.Chrome()

driver.get('https://login.live.com/')

def log_in():
#get my element
    elem = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/button"))
        )
    elem.click()

    time.sleep(1)
#sign in with github
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button")
    elem.click()
#end
    print("log in\t")

def write_in():
#write in account
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[3]/form/input[3]")
    elem.clear()
    account = "(account)" #安全考量
    elem.send_keys(f"{account}")
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[3]/form/div/input[1]")
    elem.clear()
    password = "(password)" #安全考量
    elem.send_keys(f"{password}")
    elem.send_keys(Keys.RETURN)

    try:
        time.sleep(1)
        elem = driver.find_element(By.XPATH, '//*[@id="declineButton"]')
    except:
        pass

#click in
    time.sleep(3)                          
    elem = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[2]/button')
    elem.click()
#end
    print("write in\t")

def do_request():
#do request*3
    driver.get('https://rewards.bing.com/')
    time.sleep(5)

    elem = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a')
    elem.click()
    time.sleep(3)
    ##1
    driver.get('https://rewards.bing.com/')
    elem = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a')
    elem.click()
    time.sleep(3)
    ##2
    driver.get('https://rewards.bing.com/')
    elem = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a')
    elem.click()
    time.sleep(3)
    ##3

#main():
log_in()
try:
    write_in()
except:
    print("error")
    time.sleep(30)
do_request()

#end:D
print("finish")
driver.close()
driver.quit()