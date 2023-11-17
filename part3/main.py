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
driver.get("https://www.amazon.com/Apple-2022-MacBook-512GB-Storage/dp/B0BB8SK52N/ref=psdc_565108_t1_B0BB8BHKB8/")#?language=pt_BR&currency=EUR")
driver.maximize_window()
sleep(2)
price_eur = driver.find_element(By.CLASS_NAME,"a-offscreen")
print("Price: ",price_eur.text)
#search_box.send_keys("python")
#search_button = driver.find_element(By.NAME,"btnK")
#search_button.click()
sleep(3)
driver.quit()