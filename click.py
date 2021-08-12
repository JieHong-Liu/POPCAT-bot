import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(
    'https://popcat.click/')


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH, '//*[@id="app"]/div')
    ))


click_point = driver.find_element_by_xpath('//*[@id="app"]/div')
count = 1
while(1):
    start_time = time.time()
    # print("start_time: ", start_time)
    for i in range(0, 800):
        click_point.click()
    end_time = time.time()
    print("This is the", count, "times and we cost:", end_time-start_time)
    print("You have already click for : ", count*800)
    time.sleep(35-(end_time-start_time))
    count += 1
