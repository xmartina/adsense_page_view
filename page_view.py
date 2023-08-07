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

# Load Strings
live_wait_infinity_loop = random.randrange(15 * 60, 24 * 60)
username = 'ugowhite'
password = 'QquGEvCYUDqGcBbz_country-UnitedStates'
endpoint = '3.212.129.192'
port = '31112'
PROXY = "ugowhite:QquGEvCYUDqGcBbz_country-UnitedStates@3.212.129.192:31112"
page_site_name = "https://akelicious.net/insurance"
zoom_level = 25
text_to_avoid = "google"


# Install WebDriver
# service = Service(ChromeDriverManager().install())


def run_pg_view():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument(f'user-agent={rand_ua.user_agent}')
    options.add_experimental_option("detach", True)
    proxies_extension = proxies(username, password, endpoint, port)
    options.add_extension(proxies_extension)
    options.add_argument(f'--proxy-server={PROXY}')
    options.add_argument('--start-maximized')
    preferences = {
        "webrtc.ip_handling_policy": "disable_non_proxied_udp",
        "webrtc.multiple_routes_enabled": False,
        "webrtc.nonproxied_udp_enabled": False,
        "media.peerconnection.turn.disable": True,
        "media.peerconnection.enabled": False,
        "media.peerconnection.identity.timeout": "0.005"
    }
    options.add_experimental_option("prefs", preferences)
    # End Load Chromes Options
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options=options)
    driver.get(page_site_name)
    zoom_25 = f"document.body.style.zoom = '{25}%';"
    while True:
        try:
            links = driver.find_elements(By.TAG_NAME, 'a')

            def link_click_n_switch():
                l = links[randint(0, len(links) - 1)]
                action_chains = ActionChains(driver)

                for link in links:
                    link_text = link.text
                    if text_to_avoid in link_text:
                        print(f"Avoiding link with text: {link_text}")
                    else:
                        print(f"Clicking on link with text: {link_text}")
                        action_chains.key_down(Keys.CONTROL).click(l).key_up(Keys.CONTROL).perform()
                        driver.switch_to.window(driver.window_handles[-1])
                        num_active_tabs1 = len(driver.window_handles)

                        limit_tab1 = random.randrange(3, 6)
                        if num_active_tabs1 < limit_tab1:
                            continue
                        else:
                            # break loop if you are in a new url
                            break

                    # time.sleep(5)

                # action_chains.key_down(Keys.CONTROL).click(l).key_up(Keys.CONTROL).perform()
                # driver.switch_to.window(driver.window_handles[-1])

            link_click_n_switch()
            num_active_tabs = len(driver.window_handles)

            limit_tab = random.randrange(3, 6)
            if num_active_tabs < limit_tab:
                continue
            else:
                # break loop if you are in a new url
                break

        except:
            continue

    delay_brow_open = random.randrange(10, 30)
    Event().wait(delay_brow_open)
    switch_btw_open_tab = random.randrange(22, 35)

    def switch_btn_tabs():
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

                scroll_to_top = """
                    function scrollToTop() {
                        const currentScrollY = window.scrollY;
                        if (currentScrollY > 0) {
                            window.requestAnimationFrame(scrollToTop);
                            window.scrollTo(0, currentScrollY - currentScrollY / 290);
                        }
                    }
                
                scrollToTop();
                """
                # Step 4: Execute the smooth scroll function with the desired duration
                duration_ms = 17000  # Change this value to set the duration of the smooth scroll in milliseconds
                driver.execute_script(scroll_js + f"smoothScrollToBottom({duration_ms});")
                Event().wait(45)
                driver.execute_script(scroll_to_top)

            except Exception as e:
                print("An error occurred:", e)

    switch_btn_tabs()
    quit_instance_dur = random.randrange(17 * 60, 24 * 60)
    # Event().wait(quit_instance_dur)
    driver.quit()


# def live_server1():
while True:
    # start_auto()
    run_pg_view()
    time.sleep(live_wait_infinity_loop)
    # time.sleep(9)


# live_server1()
# run_pg_view()
