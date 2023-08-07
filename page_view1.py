from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import *

import multiprocessing
import time
from random import randint
import random
import datetime
import timeit
from threading import Event
from itertools import repeat
import subprocess
from apscheduler.schedulers.background import BackgroundScheduler

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from concurrent import futures
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import rand_ua
from extensions import proxies


def run_pg_view():
    # ua = UserAgent()
    # userAgent = ua.random
    # print(userAgent)
    PROXY = "ugowhite:QquGEvCYUDqGcBbz_country-UnitedStates@3.212.129.192:31112"

    username = 'ugowhite'
    password = 'QquGEvCYUDqGcBbz_country-UnitedStates'
    endpoint = '3.212.129.192'
    port = '31112'

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument(f'user-agent={userAgent}')
    options.add_argument(f'user-agent={rand_ua.user_agent}')
    options.add_experimental_option("detach", True)

    proxies_extension = proxies(username, password, endpoint, port)

    options.add_extension(proxies_extension)

    options.add_argument(f'--proxy-server={PROXY}')
    # options.add_argument(f'--proxy-server=socks5://212.83.142.131:28519')
    # # options.add_argument('--proxy-server=http://%s' % PROXY)
    # options.add_argument('--disable-rtc-mdns')
    # options.add_argument('--disable-rtcpeerconnection')
    options.add_argument("--webrtc.public_location=false")
    options.add_argument('--disable-webrtc')
    preferences = {
        "webrtc.ip_handling_policy": "disable_non_proxied_udp",
        "webrtc.multiple_routes_enabled": False,
        "webrtc.nonproxied_udp_enabled": False,
        "media.peerconnection.turn.disable": True,
        "media.peerconnection.enabled": False,
        "media.peerconnection.identity.timeout": "0.005"
    }
    options.add_experimental_option("prefs", preferences)

    # Step 3: Create a WebDriver instance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # Make sure you have ChromeDriver installed and in the system PATH
    # store the current url in a variable
    # current_page = driver.current_url
    # driver.execute_script("window.onload = function(){var anchors = document.getElementsByTagName('a');for (var i=0; i<anchors.length; i++){anchors[i].setAttribute('target', '_blank');}}")
    # Step 4: Navigate to the webpage
    driver.get("https://tech.carfod.com/")  # Replace with the URL of the webpage containing the links you want to click

    while True:
        try:
            # find element using css selector
            links = driver.find_elements(By.TAG_NAME, 'a')

            def linkii():
                # create a list and chose a random link
                l = links[randint(0, len(links) - 1)]

                # # click link
                # l.click()

                action_chains = ActionChains(driver)
                action_chains.key_down(Keys.CONTROL).click(l).key_up(Keys.CONTROL).perform()

                # Note: On macOS, use Keys.COMMAND instead of Keys.CONTROL to simulate Command+click.

                # Step 5: Switch to the new tab (optional)
                driver.switch_to.window(driver.window_handles[-1])  # Switch to the last opened tab

            # duration_rep = timeit.timeit(linkii, number=1)
            linkii()

            # new_page = driver.current_url

            num_active_tabs = len(driver.window_handles)

            # if link is the same, keep looping
            # if new_page == current_page:
            limit_tab = random.randrange(3, 6)
            if num_active_tabs < limit_tab:
                continue
            else:
                # break loop if you are in a new url
                break
        except:
            continue

    Event().wait(4)

    switch_btw_open_tab = random.randrange(20, 30)

    def switch_btn_tabs():
        # Open new tabs and switch between them
        for i in range(len(driver.window_handles)):
            # Switch to the current tab
            driver.switch_to.window(driver.window_handles[i])
            Event().wait(switch_btw_open_tab)

            try:
                # Step 3: Define a smooth scroll function using JavaScript
                scroll_js = """
                function smoothScrollToBottom(duration) {
                    const start = window.pageYOffset || document.documentElement.scrollTop;
                    const end = document.body.scrollHeight - window.innerHeight;
                    const startTime = performance.now();

                    function scroll(timestamp) {
                        const currentTime = timestamp - startTime;
                        const scrollDistance = end - start;
                        const easeInOutCubic = t => t<.5 ? 4*t*t*t : (t-1)*(2*t-2)*(2*t-2)+1;
                        const scrollPosition = start + scrollDistance * easeInOutCubic(currentTime / duration);

                        if (currentTime < duration) {
                            window.scrollTo(0, scrollPosition);
                            requestAnimationFrame(scroll);
                        } else {
                            window.scrollTo(0, end);
                        }
                    }

                    requestAnimationFrame(scroll);
                }
                """

                # Step 4: Execute the smooth scroll function with the desired duration
                duration_ms = 17000  # Change this value to set the duration of the smooth scroll in milliseconds
                driver.execute_script(scroll_js + f"smoothScrollToBottom({duration_ms});")

            except Exception as e:
                print("An error occurred:", e)

    switch_btn_tabs()

    Event().wait(90)
    driver.quit()


run_pg_view()
