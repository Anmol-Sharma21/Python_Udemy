from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

# Find elements
fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

# Send keys
fname.send_keys("anmol")
lname.send_keys("sharma")
email.send_keys("anmol@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
