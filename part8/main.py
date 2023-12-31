from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--no-sandbox')
edge_options.add_argument('--disable-dev-shm-usage')
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on
cookie = driver.find_element(by=By.ID, value= "cookie")

#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 30
ten_min = time.time() + 60*5 # 5 minutes = 60 seconds times 5
action = ActionChains(driver)

while True:
    #cookie.click()
    action.double_click(on_element=cookie)

    #every 5 seconds:
    if time.time() > timeout:

        #Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(f"The higest price affordable: {highest_price_affordable_upgrade}")
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        #Add another 5 seconds until the next check
        timeout = time.time() + 15

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > ten_min:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(f"Cookies per second: {cookie_per_s}")
        break
