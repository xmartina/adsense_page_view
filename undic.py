import undetected_chromedriver as uc
import seleniumwire.undetected_chromedriver as uc
import multiprocessing
import time
from random import randint
import random
import datetime
import timeit
from threading import Event
from itertools import repeat
import subprocess
import rand_ua
from extensions import proxies

username = 'ugowhite'
password = 'QquGEvCYUDqGcBbz_country-UnitedStates'
endpoint = '3.212.129.192'
port = '31112'


def cooll():
    options = uc.ChromeOptions()
    proxies_extension = proxies(username, password, endpoint, port)
    options.add_extension(proxies_extension)
    # options.add_argument(f'--proxy-server={PROXY}')
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
    # proxy_options = {
    #     'proxy': {
    #         'http': 'http://ugowhite:QquGEvCYUDqGcBbz_country-UnitedStates@3.212.129.192:31112'
    #         # 'https': 'https://ugowhite:QquGEvCYUDqGcBbz_country-UnitedStates@3.212.129.192:31112',
    #         # 'no_proxy': 'localhost,127.0.0.1'
    #     }
    # }
    options.add_argument(f'user-agent={rand_ua.user_agent}')
    driver = uc.Chrome(
        options=options
        # seleniumwire_options=proxy_options
    )
    driver.get("http://www.matagram.com")

    print(driver.current_url)  # https://www.nowsecure.nl/
    print(driver.title)  # nowSecure


while True:
    cooll()
    time.sleep(8)
