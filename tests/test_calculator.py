import unittest
from pathlib import Path
from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from appium.options.android import UiAutomator2Options
from screens.main import MainScreen


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.appium_service = AppiumService()
        cls.appium_service.start()


    def setUp(self):
        app_name = 'calculator.apk'
        path = str(Path(__file__).parent.parent.joinpath(app_name))
        appium_url = 'http://127.0.0.1:4723'

        capabilities = dict(
            automationName='uiautomator2',
            platformName='Android',
            app=path,
            newCommandTimeout=600
        )
        self.driver = webdriver.Remote(appium_url, options=UiAutomator2Options().load_capabilities(capabilities))
        self.main_screen = MainScreen(self.driver)

    def test_add_2_values(self):
        self.main_screen.add_values(1, 2)
        result = self.main_screen.get_result()
        self.assertEqual(int(result), 3)

    def test_add_multiple_numbers(self):
        self.main_screen.add_values(1, 20, 100)
        result = self.main_screen.get_result()
        self.assertEqual(int(result), 121)

    def test_division_by_zero(self):
        self.main_screen.divide_values(1, 0)
        error_message = self.main_screen.get_preview_message()
        self.assertEqual(error_message, "Can't divide by 0")

    def test_scroll_and_check_history(self):
        self.main_screen.expand_history_view()
        self.main_screen.add_values(1, 2)
        self.main_screen.wait_until_empty_history_disappear()

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.appium_service.stop()
