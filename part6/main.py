from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_options = webdriver.EdgeOptions()#.ChromeOptions()  #Options()
edge_options.add_argument('--no-sandbox')
edge_options.add_argument('--disable-dev-shm-usage')
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
#driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")
#driver.maximize_window()

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Alexandre")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Pereira")
email = driver.find_element(By.NAME, "email")
email.send_keys("alexander.pierson1@gmail.com")
sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()


# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# #article_count.click()
#
#
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# #all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)



sleep(3)
driver.quit()