from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")


while True:
    if len(driver.window_handles)==0:
        break


driver.close()