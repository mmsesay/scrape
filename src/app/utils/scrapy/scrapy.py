import time
import os
import sys
from platforms.twitter import TwitterScraper
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def stop_script_gracefully():
    """This function stops the script from running gracefully if their is an error"""
    try:
        sys.exit()
    except SystemExit:
        print("Exiting the program...")
        raise


def restart():
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")


    os.execv(sys.executable, ['python'] + sys.argv)

def init():
    """This method initialize the scraper"""

    twitter_scraper_instance = TwitterScraper()
    twitter_scraper_instance.login()
    twitter_scraper_instance.get_followers()

    # try:
    #
    # except TimeoutException:
    #     stop_script_gracefully()
    #     restart()
    #     twitter.login_type_one()
    #     print("An exception occurred::")
    # except NoSuchElementException:
    #     print("An NoSuchElementException occurred:: ")


init()

time.sleep(1000)

driver.close()
