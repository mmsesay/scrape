import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
driver = webdriver.Chrome(options=options)
# driver. get('chrome://settings/clearBrowserData') 

# https://twitter.com/DeeMaejor
driver.get("https://twitter.com/i/flow/login")


def login_to_twitter():
  # get the email element
  email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
  email_field.send_keys('muhammadsesay8@gmail.com') # input the value into the form field
  print("email entered successfully")
  time.sleep(2)

  # get all the buttons on the page
  page_one_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
  page_one_buttons[-2].click()
  print("next button clicked")
  time.sleep(2)

  # on username or phone page
  phone_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")))
  phone_username.send_keys('DeeMaejor')
  print("username entered successfully")
  time.sleep(2)

  page_two_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
  page_two_buttons[1].click() # click on the loging button
  print("next button clicked")
  time.sleep(2)

  # wait until the element is locate
  password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
  password.send_keys('Muhammad@10') # input the value into the form field
  print("password entered successfully")
  time.sleep(2)

  page_three_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
  page_three_buttons[-1].click() # click on the login button
  print("login button clicked")
  time.sleep(2)

  # access the profile like
  profile_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Profile']")))
  profile_icon.click()
  print("profile icon clicked")
  time.sleep(2)

  # access the followers from the tabs
  followers_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a')))
  followers_link.click()
  print("follower link clicked")
  time.sleep(2)


  followers_parent_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div')))
  followers = followers_parent_element.find_elements(By.XPATH, '*')

  for follower in followers:
      print("================================================")
      print(f'Username::: {follower.text.splitlines()[1]}')
      print(follower.text)
  print(f'followersCount: {len(followers)}')

login_to_twitter()

time.sleep(1000)

driver.close()