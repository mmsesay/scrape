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
# options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
# driver. get('chrome://settings/clearBrowserData') 

# https://twitter.com/DeeMaejor
driver.get("https://twitter.com/i/flow/login")
# time.sleep(3)


def login_to_twitter():
  # get the email element
  email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
  email_field.send_keys('muhammadsesay8@gmail.com') # input the value into the form field

  # get all the buttons on the page
  page_one_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
  page_one_buttons[-2].click()

  # on username or phone page
  phone_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")))
  phone_username.send_keys('DeeMaejor')
  page_two_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
  # click on the loging button
  page_two_buttons[1].click()

  # wait until the element is locate
  password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
  password.send_keys('Muhammad@10') # input the value into the form field

  print("password entered successfully")
  page_three_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
  page_three_buttons[-1].click() # click on the login button

  # access the profile like
  profile_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Profile']")))
  profile_icon.click()

  # access the followers from the tabs
  followers_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a')))
  followers_link.click()


  followers_parent_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div')))
  followers = followers_parent_element.find_elements(By.XPATH, '*')

  for follower in followers:
      print("================================================")
      print(f'Username::: {follower.text.splitlines()[1]}')
      print(follower.text)
  print(f'followersCount: {len(followers)}')
  # print(f'followers: {followers}')
  # soup = BeautifulSoup(resp, 'lxml')

  # print(soup.prettify())

def login_with_email_and_password():
  # get the email element
  email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
  email_field.send_keys('muhammadsesay8@gmail.com') # input the value into the form field

  # get all the buttons on the page
  next_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
  next_buttons[-2].click()
  print("next button clicked")

  # wait until the element is locate
  password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
  password.send_keys('Muhammad@10') # input the value into the form field

  print("password entered successfully")

  buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
  print("buttons:: ", buttons)
  # click on the loging button
  buttons[-1].click()
  print("login button clicked")

  time.sleep(1000)

login_to_twitter()

time.sleep(1000)

driver.close()
# print(resp)