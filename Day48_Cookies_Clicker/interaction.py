from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver_path = "C:\drivers\chromedriver.exe"

s = Service(executable_path=chrome_driver_path)
#s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, service=s)

driver.get(url)
count = driver.find_element(By.CSS_SELECTOR, '#articlecount a').text
print(count)


all_portals = driver.find_element(By.LINK_TEXT, "All portals")
all_portals.click()

# driver.find_element(By.NAME, "search").send_keys("Hello")

