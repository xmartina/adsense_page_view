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

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

driver.get('https://tech.carfod.com/')

driver.execute_script("window.onload = function(){var anchors = document.getElementsByTagName('a');for (var i=0; i<anchors.length; i++){anchors[i].setAttribute('target', '_blank');}}")

# store the current url in a variable
current_page = driver.current_url


def rep():
    # create an infinite loop
    while True:
        try:
            # find element using css selector
            links = driver.find_elements(By.TAG_NAME, 'a')

            # create a list and chose a random link
            l = links[randint(0, len(links) - 2)]

            # click link
            l.click()

            # create a list and chose a random link
            g = links[randint(0, len(links) - 2)]

            # click link
            g.click()

            # create a list and chose a random link
            v = links[randint(0, len(links) - 2)]

            # click link
            v.click()

            # check link
            new_page = driver.current_url

            # if link is the same, keep looping
            if new_page == current_page:
                time.sleep(1)
                continue
            else:
                time.sleep(1)
                # break loop if you are in a new url
                break
        except:
            continue


# async def main():
#     rep()
#     await asyncio.sleep(1)
#
#
# # Python 3.7+
# asyncio.run(main())
def dura():
    duration_rep = timeit.timeit(rep, number=10)


sched = BackgroundScheduler()


def pause_job():
    sched.pause_job('dura1')


sched.add_job(dura, 'interval', seconds=6)
sched.add_job(pause_job, 'interval', seconds=17)

sched.start()

Event().wait(10)

exit()
# duration_rep = timeit.timeit(rep, number=1)
