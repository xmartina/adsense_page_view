from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager

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

import time

ua = UserAgent()
userAgent = ua.random
print(userAgent)

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument(f'user-agent={userAgent}')
options.add_experimental_option("detach", True)

# Step 1: Set up the environment
driver = webdriver.Chrome(options=options)  # Make sure you have ChromeDriver installed and in the system PATH

# Step 2: Navigate to the webpage where you want to add the JavaScript
driver.get("https://tech.carfod.com/")  # Replace with the URL of the webpage you want to work with
driver.execute_script("window.onload = function(){for (var i=0; i<document.getElementsByTagName('a').length; i++){document.getElementsByTagName('a')[i].setAttribute('target', '_blank');}}")
# try:
#     # Step 3: Add JavaScript to the webpage
#     js_code = """window.onload = function(){var anchors = document.getElementsByTagName('a');for (var i=0;
#     i<anchors.length; i++){anchors[i].setAttribute('target', '_blank');}}"""
#     driver.execute_script(js_code)
#
# except Exception as e:
#     print("An error occurred:", e)

# Step 4: Close the WebDriver (optional)
# driver.quit()  # Uncomment this line if you want to close the WebDriver after the script execution
