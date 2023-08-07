from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Selenium Wire configuration to use a proxy
proxy_username = 'ugowhite'
proxy_password = 'QquGEvCYUDqGcBbz_country-UnitedStates'
seleniumwire_options = {
    'proxy': {
        'http': f'http://{proxy_username}:{proxy_password}@3.212.129.192:31112',
        'verify_ssl': False,
    },
}

driver = webdriver.Chrome(
    seleniumwire_options=seleniumwire_options
)
driver.get('http://httpbin.org/ip')
print(driver.find_element(By.TAG_NAME, 'body').text) # { "origin": "185.199.229.156" }
