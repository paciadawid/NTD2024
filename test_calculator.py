import unittest
from pathlib import Path
from appium import webdriver

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy




class TestCalculator(unittest.TestCase):

    def setUp(self):
        app_name = 'calculator.apk'
        path = str(Path(__file__).parent.joinpath(app_name))
        appium_url = 'http://127.0.0.1:4723'

        capabilities = dict(
            automationName='uiautomator2',
            platformName='Android',
            app=path,
            newCommandTimeout=600
        )
        self.driver = webdriver.Remote(appium_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def test_add_2_values(self):

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '1').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plus').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '2').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equals').click()

        result = self.driver.find_element(AppiumBy.ID, 'result_final').text
        self.assertEqual(int(result), 3)

    def test_division_by_zero(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '1').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'divide').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '0').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equals').click()
        error_message = self.driver.find_element(AppiumBy.ID, 'result_preview').text
        self.assertEqual(error_message, "Can't divide by 0")

    def tearDown(self):
        self.driver.quit()
