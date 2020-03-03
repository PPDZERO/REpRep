from appium import webdriver
from app.application import Application

def before_scenario(context, scenario):
    desired_capabilities = {
        'platformName': 'Android',
        'platformVersion': '7.1.1',
        'deviceName': 'Android Simulator',
#MAC OS 'app': '/Users/ruslan-sab/Downloads/YaMapsAndroid/yandexmaps-android.apk',
        'app': 'C:\Ya.Maps\yandexmaps-android.apk',
        'autoGrantPermissions': 'true',
        'appPackage': 'ru.yandex.yandexmaps.debug',
        'appActivity': 'ru.yandex.yandexmaps.SplashScreen'

    }
    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()