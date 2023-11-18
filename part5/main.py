from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()#.ChromeOptions()  #Options()
edge_options.add_argument('--no-sandbox')
edge_options.add_argument('--disable-dev-shm-usage')
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
#driver.maximize_window()

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

sleep(3)
driver.quit()