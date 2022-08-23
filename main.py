from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

shop_list = ['hetm', 'amazon', 'darty']
global final_result
final_result = []

def open_shop(shop=""):
  print('start open_shop')

  driver.get("https://fr.igraal.com/codes-promo/" + shop) # Go to the url of the shop
  time.sleep(20)

def accept_cookies():
  print('start cookies')

  cookie_button = driver.find_element(By.ID, 'cookies-banner-btn-accept') # Find the button to accept cookies
  cookie_button.click()