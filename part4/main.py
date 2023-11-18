from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#chrome_options = webdriver.ChromeOptions()  #Options()
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_experimental_option("detach", True)

edge_options = webdriver.EdgeOptions()#.ChromeOptions()  #Options()
edge_options.add_argument('--no-sandbox')
edge_options.add_argument('--disable-dev-shm-usage')
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://www.python.org")
#driver.maximize_window()
sleep(2)
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
sleep(3)
driver.quit()