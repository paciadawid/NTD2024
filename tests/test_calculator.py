import unittest
from pathlib import Path
from appium import webdriver

from appium.options.android import UiAutomator2Options
from screens.main import MainScreen


class TestCalculator(unittest.TestCase):

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

    def test_division_by_zero(self):
        self.main_screen.divide_values(1, 0)
        error_message = self.main_screen.get_preview_message()
        self.assertEqual(error_message, "Can't divide by 0")

    def tearDown(self):
        self.driver.quit()
