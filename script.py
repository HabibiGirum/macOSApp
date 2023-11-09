# import the selenium.webdriver module
from selenium import webdriver

# create an instance of the Chrome class
driver = webdriver.Chrome()

# navigate to google.com
driver.get("https://www.google.com")

# wait for the user to close the tab
while True:
    if len(driver.window_handles) == 0:
        break

# close the browser window
driver.close()
