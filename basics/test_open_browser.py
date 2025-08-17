from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    assert "Google" in driver.title
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "q")
    time.sleep(2)
    search_box.send_keys("Selenium automation python")
    time.sleep(2)
    driver.quit()
    
