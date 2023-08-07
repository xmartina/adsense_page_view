import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from concurrent import futures


def selenium_test(test_url):
    service = Service(executable_path="C:/chromedriver")
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    # navigate to the url
    driver.get(
        'https://www.google.com/search?q=click+on+link+selenium+python&oq=click+on+link+selenium+py&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIICAIQABgWGB4yCAgDEAAYFhgeMggIBBAAGBYYHjIICAUQABgWGB4yCggGEAAYhgMYigUyCggHEAAYhgMYigUyCggIEAAYhgMYigXSAQkxMjU4M2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8')
    # find element by partial link text
    myLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'python - Clicking on a link via selenium')
    myLink.click()

    # Open a new window
    driver.execute_script("window.open('');")
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])
    driver.get("http://stackoverflow.com")
    time.sleep(0.3)

    # Open a new window
    driver.execute_script("window.open('');")
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://www.reddit.com/")
    time.sleep(.3)
    # close the active tab
    driver.close()
    time.sleep(.3)

    # Switch back to the first tab
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://bing.com")
    time.sleep(.3)


# default number of threads is optimized for cpu cores
# ,but you can set with `max_workers` like `futures.ThreadPoolExecutor(max_workers=...)`
with futures.ThreadPoolExecutor() as executor:
    future_test_results = [executor.submit(selenium_test, i)
                           for i in range(6)]  # running same test 6 times, using test number as url
    for future_test_result in future_test_results:
        try:
            test_result = future_test_result.result()  # can use `timeout` to wait max seconds for each thread
            # ... do something with the test_result
        except Exception as exc:  # can give a exception in some thread, but
            print('thread generated an exception: {:0}'.format(exc))
