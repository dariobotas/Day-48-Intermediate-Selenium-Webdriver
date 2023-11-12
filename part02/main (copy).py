from time import sleep

#import chromedriver_binary
#"guessedImports":["chromedriver-binary","selenium"],
#from advanced_selenium_options import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()  #Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("python")
search_button = driver.find_element(By.NAME,"btnK")
search_button.click()
sleep(3)
driver.quit()
