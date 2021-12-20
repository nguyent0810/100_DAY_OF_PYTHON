from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\drivers\chromedriver.exe"
url = "https://www.python.org/"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url)
#content = driver.find_elements(By.CSS_SELECTOR, 'div .shrubbery ul li .menu')
#content = driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
contents = driver.find_elements(By.CSS_SELECTOR, ".list-widgets .menu li")
upcoming_events = {}
for i in contents:
    event = i.text.split('\n')
    upcoming_events[contents.index(i)] = {
        "time": event[0],
        "name": event[1]
    }
    


print(upcoming_events)
#driver.close()
#driver.quit()