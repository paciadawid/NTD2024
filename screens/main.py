from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class MainScreen:
    # static selectors
    __plus_selector = (AppiumBy.ACCESSIBILITY_ID, 'plus')
    __equals_selector = (AppiumBy.ACCESSIBILITY_ID, 'equals')
    __divide_selector = (AppiumBy.ACCESSIBILITY_ID, 'divide')
    __result_selector = (AppiumBy.ID, 'result_final')
    __result_preview_selector = (AppiumBy.ID, 'result_preview')

    # dynamic selectors
    __digit_selector_strategy = AppiumBy.ACCESSIBILITY_ID

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def add_values(self, *numbers):
        for i, number in enumerate(numbers):
            self.__enter_number(number)
            if i < len(numbers) - 1:
                self.driver.find_element(*self.__plus_selector).click()
        self.driver.find_element(*self.__equals_selector).click()

    def divide_values(self, digit_1: int, digit_2: int):
        self.driver.find_element(self.__digit_selector_strategy, str(digit_1)).click()
        self.driver.find_element(*self.__divide_selector).click()
        self.driver.find_element(self.__digit_selector_strategy, str(digit_2)).click()
        self.driver.find_element(*self.__equals_selector).click()

    def get_result(self) -> str:
        return self.driver.find_element(*self.__result_selector).text

    def get_preview_message(self) -> str:
        return self.driver.find_element(*self.__result_preview_selector).text

    def __enter_number(self, number):
        for digit in str(number):
            self.driver.find_element(self.__digit_selector_strategy, str(digit)).click()
