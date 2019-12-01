import datetime
from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from django.contrib.auth.models import User
from django.test.client import Client
from polls.models import Question
from polls.models import Choice
from django.utils import timezone

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
        self.web = FunctionTest.browser
        self.user = Client()
        Question.objects.create(question_text="Test?", pub_date=timezone.now())
        Choice.objects.create(question=Question.objects.all()[0], choice_text='TEST!')
        User.objects.create_user(username='Tester', email='tester@hotmail.com', password='test')
        self.user.login(username='Tester', password='test')
        user_cookie = self.user.cookies['sessionid']
        self.web.get('%s' % self.live_server_url)
        self.web.add_cookie({'name': 'sessionid', 'value': user_cookie.value})
        super().setUp()

    def test_find_h1(self):
        self.web.get('%s' % self.live_server_url)
        text_with_h1 = self.web.find_element_by_tag_name('h1')
        self.assertEqual(text_with_h1.text, "This is homepage")

    def test_find_question(self):
        self.web.get('%s' % self.live_server_url)
        question = self.web.find_element_by_id('question1')
        self.assertEqual(question.text, "Test?")

    def test_to_vote(self):
        self.web.get('%s' % self.live_server_url)
        self.web.find_element_by_id('question1').click()
        self.assertURLEqual(self.web.current_url, '%s%s' %
                            (self.live_server_url, f'/polls/{Question.objects.all()[0].id}/'))

    def test_first_choice(self):
        self.web.get('%s%s' % (self.live_server_url, f'/polls/{Question.objects.all()[0].id}/'))
        self.web.find_element_by_id('choice1').click()
        self.web.find_element_by_id('submit_button').click()

        self.assertURLEqual(self.web.current_url, self.live_server_url +
                            f'/polls/{Question.objects.all()[0].id}/results/')

