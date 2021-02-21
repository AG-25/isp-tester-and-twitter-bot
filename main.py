from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = r"lib\chromedriver-win.exe"

# This is the Download speed which your ISP promises (in Mb/s)
PROMISED_DOWN = '50'

# For the program to send a tweet, you need to provide an email, password, and
# the twitter handle of your internet service provider (.e.g. @TalkTalkGroup)
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
ISP_TWITTER_HANDLE = ""


class InternetSpeedTwitterBot:
    def __init__(self, driverpath):
        self.driver = webdriver.Chrome(executable_path=driverpath)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        consent_button = self.driver.find_element_by_css_selector(
            "#_evidon-banner-acceptbutton"
        )
        consent_button.click()
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()

        upload = self.driver.find_element_by_css_selector(".upload-speed")
        download = self.driver.find_element_by_css_selector(".download-speed")
        while upload.get_attribute("data-upload-status-value") == "NaN":
            time.sleep(10)
        self.up = upload.text
        self.down = download.text

    def tweet_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(1)
        username = self.driver.find_element_by_name("session[username_or_email]")
        password = self.driver.find_element_by_name("session[password]")
        if username.get_attribute("value") != "":
            username.send_keys(Keys.CLEAR)
        if password.get_attribute("value") != "":
            password.send_keys(Keys.CLEAR)
        username.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(1)
        draft_input = self.driver.find_element_by_class_name(
            "public-DraftStyleDefault-block"
        )
        draft_input.click()
        draft_input.send_keys(
            f"{ISP_TWITTER_HANDLE} Why is my download speed only "
            f"{self.down} Mb/s, when you promise {PROMISED_DOWN} Mb/s?"
        )
        tweet_button = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/'
            'div/div/div/div[2]/div/div[2]/div[1]/div/div/'
            'div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span'
        )
        tweet_button.click()

    def shutdown_web_driver(self):
        self.driver.close()


speed_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
speed_bot.get_internet_speed()
if float(speed_bot.down) < float(PROMISED_DOWN):
    print("The internet speed is slower than promised")
    if TWITTER_EMAIL:
        speed_bot.tweet_provider()
speed_bot.shutdown_web_driver()
