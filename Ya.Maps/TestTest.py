from appium import webdriver

desired_capabilities = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'Android Simulator',
    'app': '/Users/ruslan-sab/Downloads/YaMapsAndroid/yandexmaps-android.apk',
    'autoGrantPermissions': 'true'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)

driver.find_element_by_id('ru.yandex.yandexmaps.debug:id/tab_navigation_tab_menu').click();