import datetime
from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from polls.views import *
from polls.models import Question
import requests

from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        super(FunctionTest, cls).setUpClass()
        try:
            cls.browser = WebDriver()
        except WebDriverException:
            cls.browser = WebDriver(executable_path='E:/chrome_driver/chromedriver.exe')
        finally:
            cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(FunctionTest, cls).tearDownClass()

    def setUp(self):
        """
        :return:
        """
        super().setUp()
        self.web = FunctionTest.browser

    def test_find_h1(self):
        self.web.get('%s' % self.live_server_url)
        text_with_h1 = self.web.find_element_by_tag_name('h1')
        self.assertEqual(text_with_h1.text, "This is homepage")

    def test_find_question(self):
        self.web.get('%s' % self.live_server_url)
        text_question = self.web.find_element_by_tag_name('p')
        self.assertEqual(text_question.text, "No polls are available.")

    def test_hyperlink(self):
        self.web.get('%s' % self.live_server_url)
        self.web.find_element_by_link_text('login').click()
        self.assertEqual(self.web.current_url, '%s%s' % (self.live_server_url, 'accounts/login/'))

    def test_first_choice(self):
        pass