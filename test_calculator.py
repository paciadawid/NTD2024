import unittest
from pathlib import Path
from appium import webdriver

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy




class TestCalculator(unittest.TestCase):


    def test_add_2_values(self):
        app_name = 'calculator.apk'
        # path = os.path.join(os.path.abspath(__file__).split(), app_name)

        path = str(Path(__file__).parent.joinpath(app_name))

        appium_url = 'http://127.0.0.1:4723'

        capabilities = dict(
            automationName='uiautomator2',
            platformName='Android',
            app=path,
            newCommandTimeout=600
        )

        driver = webdriver.Remote(appium_url, options=UiAutomator2Options().load_capabilities(capabilities))

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, '1').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plus').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, '2').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equals').click()

        result = driver.find_element(AppiumBy.ID, 'result_final').text
        self.assertEqual(int(result), 3)
