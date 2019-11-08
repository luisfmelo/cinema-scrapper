import re
import time
from abc import ABC, abstractmethod
from json import dumps

from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config import CHROME_DRIVER
from data.Session import Session
from services.mqtt_producer import mqtt_publish


class Crawler(ABC):
    regex = re.compile(r"\s+", re.IGNORECASE)

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
        chrome_options.add_experimental_option("prefs", prefs)

        if CHROME_DRIVER:
            # prod - chromedriver setting is set up
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_driver = CHROME_DRIVER
        else:
            # development
            chrome_driver = ChromeDriverManager().install()

        self.browser = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
        self.max_wait_Sec = 30
        time.sleep(5)

        self.infinite_scroll_script = """
            window.scrollTo(0, document.body.scrollHeight);
            let lenOfPage = document.body.scrollHeight;
            return lenOfPage;
        """
        self.soup = None

    def get_single_page(self, url: str) -> BeautifulSoup:
        self.browser.get(url)

        # Now that the page is fully scrolled, grab the source code.
        source_data = self.browser.page_source

        # Throw your source into BeautifulSoup and start parsing!
        self.soup = BeautifulSoup(source_data, features='lxml')

        return self.soup

    def get_infinite_scroll_page(self, url: str) -> BeautifulSoup:
        self.browser.get(url)

        # Selenium script to scroll to the bottom, wait 3 seconds for the next batch of data to load,
        # then continue scrolling.  It will continue to do this until the page stops loading new data.
        page_length = self.browser.execute_script(self.infinite_scroll_script)
        match = False

        while not match:
            last_count = page_length
            time.sleep(3)
            page_length = self.browser.execute_script(self.infinite_scroll_script)
            if last_count == page_length:
                match = True

        # Now that the page is fully scrolled, grab the source code.
        source_data = self.browser.page_source

        # Throw your source into BeautifulSoup and start parsing!
        self.soup = BeautifulSoup(source_data, features='lxml')

        return self.soup

    @abstractmethod
    def scrap_sessions(self):
        raise NotImplemented('This method should be implemented')

    @staticmethod
    def publish_new_session(session: Session):
        mqtt_publish(dumps(session.to_json()))

    def trim(self, string):
        return self.regex.sub('', string).strip()

    def close(self):
        self.browser.stop_client()
        self.browser.quit()
