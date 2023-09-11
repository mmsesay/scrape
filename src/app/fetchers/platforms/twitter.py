"""
Filename        :   twitter.py
Description     :   This file has a class with methods to authenticate and scrape twitter
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from lxml import etree


class TwitterScraper:
    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        time.sleep(5)
        # driver. get('chrome://settings/clearBrowserData')

        self.driver.get("https://twitter.com/i/flow/login")

    def __scroll_page(self):
        """Scrolls an entire page"""

        for twusernames in self.driver.find_elements(By.XPATH,
                                                     '//div[@aria-label="Timeline: Followers"]//a[@role="link" and '
                                                     'not(@aria-hidden) and not(contains(@href,"search")) and not('
                                                     'contains(@href,"Live")) and not(@rel)]'):
            file = open("scrapedlist.txt", "a")
            file.write(twusernames.get_property('href'))
            file.write("\n")
            file.close()

        scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = self.driver.execute_script("return window.screen.height;")  # get the screen height of the web
        i = 1

        # scroll to the bottom
        while True:
            # scroll one screen height each time
            self.driver.execute_script(
                "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 1
            time.sleep(scroll_pause_time)

            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = self.driver.execute_script("return document.body.scrollHeight;")
            # Break the loop when the height we need to scroll to is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break

            for twusernames in self.driver.find_elements(By.XPATH,
                                                         '//div[@aria-label="Timeline: Followers"]//a[@role="link" '
                                                         'and not(@aria-hidden) and not(contains(@href,"search")) and '
                                                         'not(contains(@href,"Live")) and not(@rel)]'):
                file = open("scrapedlist.txt", "a")
                file.write(twusernames.get_property('href'))
                file.write("\n")
                file.close()

    def __scroll_down_the_page(self, followers_count, followers_per_page=23):
        """Scrolls an entire page"""
        # scroll down the page iteratively with a delay
        for _ in range(0, int(int(followers_count) / followers_per_page + 1)):
            self.driver.execute_script("window.scrollTo(0, 10000);")
            time.sleep(2)

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

    def extract_followers_func(self):
        # access the profile like
        profile_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Profile']")))
        profile_icon.click()
        print("profile icon clicked")
        time.sleep(2)

        # access the followers from the tabs
        followers_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a'
                 )))

        # get the total followers count
        total_followers = followers_link.text.split(" ")[0]
        print(f'Total followers::: {total_followers}')

        followers_link.click()
        print("follower link clicked")
        time.sleep(2)

        print("scroll down....")
        #  scroll down the page
        self.__scroll_page()
        time.sleep(2)

        print("done writing....")

    def get_followers(self):
        """
        This method finds the profile icon and perform a click on it.
        It then finds the followers link and navigate to it.
        A scroll event is fired to go through the entire list of followers
        """

        # access the profile like
        profile_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Profile']")))
        profile_icon.click()
        print("profile icon clicked")
        time.sleep(2)

        # access the followers from the tabs
        followers_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a'
                 )))

        # get the total followers count
        total_followers = followers_link.text.split(" ")[0]
        print(f'Total followers::: {total_followers}')

        followers_link.click()
        print("follower link clicked")
        time.sleep(2)

        #  scroll down the page
        self.__scroll_page()
        # self.__scroll_down_the_page(total_followers)
        time.sleep(2)

        # html = self.driver.page_source

        # soup = BeautifulSoup(html, 'lxml')
        #
        # # dom = etree.HTML(str(soup))  # Parse the HTML content of the page
        # xpath_str = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[' \
        #             '1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/a/div/div/span'  # The XPath
        # # # expression for the blog's title
        # # print(dom.xpath(xpath_str).text)
        #
        # user_tags = self.driver.find_elements(By.XPATH, "//div[@data-testid='cellInnerDiv']")
        #     # WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
        #     #     (By.XPATH, xpath_str)))
        #
        # # user_tags = soup.find_all("div", dir_="ltr")
        #
        # # user_tags = soup.find_all("span", class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
        # print("user_tags_length:: ", len(user_tags))
        # print("user_tags::: ", user_tags)
        #
        # # print(html)
        # time.sleep(1000)
        #

        fl = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH,
             '//div[@aria-label="Timeline: Followers"]//a[@role="link" and not(@aria-hidden) and not(contains(@href,'
             '"search"))'
             'and not(contains(@href,"Live")) and not(@rel)]')))
        # followers_parent_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
        #     (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div')))
        #
        # # //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div
        # followers = followers_parent_element.find_elements(By.XPATH, '*')
        # # f = followers.find_elements(By.XPATH, '*')
        # #
        # foll = []
        # for follower in followers:
        #     foll.append(follower)
        #     print("================================================")
        #     # print(f'Username::: {follower.text.splitlines()[1]}')
        #     print(follower.text)
        print(f'followersCount: {fl}')

        # print(f'followersCount: {len(fl)}')
        # print(f'follCount: {len(foll)}')

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
