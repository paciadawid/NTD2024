from pathlib import Path
from appium import webdriver
from appium.options.android import UiAutomator2Options

app_name = 'calculator.apk'
# path = os.path.join(os.path.abspath(__file__).split(), app_name)

path = str(Path(__file__).parent.joinpath(app_name))

appium_url = 'http://127.0.0.1:4723'

capabilities = dict(
    automationName = 'uiautomator2',
    platformName = 'Android',
    app = path
)

driver = webdriver.Remote(appium_url, options=UiAutomator2Options().load_capabilities(capabilities))
