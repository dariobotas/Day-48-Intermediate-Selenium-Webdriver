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
#driver.get("https://www.amazon.com/Apple-2022-MacBook-512GB-Storage/dp/B0BB8SK52N/ref=psdc_565108_t1_B0BB8BHKB8/")#?language=pt_BR&currency=EUR")
driver.get("https://www.python.org")
driver.maximize_window()
sleep(2)
#price_eur = driver.find_element(By.CLASS_NAME,"a-offscreen")
#print("Price: ",price_eur.text)
#search_box.send_keys("python")
#search_button = driver.find_element(By.NAME,"btnK")
#search_button.click()
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

#Search by xpath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

sleep(3)
driver.quit()