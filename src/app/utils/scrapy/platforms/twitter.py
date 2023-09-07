import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class TwitterScraper:
    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options)
        # driver. get('chrome://settings/clearBrowserData')

        self.driver.get("https://twitter.com/i/flow/login")


    def __scroll_page(self):
        """Scrolls an entire page"""

        scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = self.driver.execute_script("return window.screen.height;")  # get the screen height of the web
        i = 1

        # scroll to the bottom
        while True:
            # scroll one screen height each time
            self.driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 1
            time.sleep(scroll_pause_time)

            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = self.driver.execute_script("return document.body.scrollHeight;")
            # Break the loop when the height we need to scroll to is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break


    def __get_email_element(self):
        """
        This method gets the email input element and fill in.
        It then finds the button element and click on it to navigate to the next page
        """

        # get the email element
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
        email_field.send_keys('muhammadsesay8@gmail.com')  # input the value into the form field

        # get all the buttons on the page
        next_buttons = self.driver.find_elements(By.XPATH, "//div[@role='button']")
        next_buttons[-2].click()
        print("next button clicked")

    def __get_password_element(self):
        """
        This method gets the password input element and fill in.
        It then finds the button element and click on it to login
        """

        # wait until the element is located
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        password.send_keys('Muhammad@10')  # input the value into the form field

        print("password entered successfully")

        buttons = self.driver.find_elements(By.XPATH, "//div[@role='button']")
        print("buttons:: ", buttons)
        # click on the loging button
        buttons[-1].click()
        print("login button clicked")

    def __get_phone_or_username_element(self):
        """
        This method gets the phone or username input element and fill in.
        It then finds the button element and click on it to navigate to the next page
        """
        # find the username or phone element
        phone_or_username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")))
        phone_or_username_field.send_keys('DeeMaejor')
        print("username entered successfully")
        time.sleep(2)

        # find the page button element
        page_two_buttons = self.driver.find_elements(By.XPATH, "//div[@role='button']")
        page_two_buttons[1].click()  # click on the loging button
        print("next button clicked")
        time.sleep(2)

    def get_followers(self):
        """
        This method finds the profile icon and perform a click on it.
        It then finds the followers link and navigate to it.
        A scroll event is fired to go through the entire list of followers
        """

        # access the profile like
        profile_icon = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Profile']")))
        profile_icon.click()
        print("profile icon clicked")
        time.sleep(2)

        # access the followers from the tabs
        followers_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a')))
        followers_link.click()
        print("follower link clicked")
        time.sleep(2)

        followers_parent_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div')))

        #  scroll down the page
        self.__scroll_page()

        followers = followers_parent_element.find_elements(By.XPATH, '*')

        foll = []
        for follower in followers:
            foll.append(follower)
            print("================================================")
            # print(f'Username::: {follower.text.splitlines()[1]}')
            print(follower.text)
        print(f'followersCount: {len(followers)}')

    def login(self):
        """
        This method finds all the elements required to logged successfully into twitter
        """
        self.__get_email_element()

        try:
            self.__get_password_element()
        except TimeoutException:
            self.__get_phone_or_username_element()

        # invoke the password function
        self.__get_password_element()
