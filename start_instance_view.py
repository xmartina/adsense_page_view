import os
import random
import time
import multiprocessing
from page_view import run_pg_view
from undic import cooll


pg_viw_stat_tim = random.randrange(3, 5)
wait_time_1 = random.randrange(10, 17)
live_wait_infinity_loop = random.randrange(15*60, 4*60)
exe_time = 5
test_loop_tim = random.randrange(10, 25)


def stat_pg_viw():
    # for i in range(pg_viw_stat_tim):
    #     run_pg_view()
    #     time.sleep(wait_time_1)
    run_pg_view()


def start_auto():
    for i in range(pg_viw_stat_tim):
        stat_pg_viw()
        # time.sleep(wait_time_1)


def live_server():
    while True:
        # start_auto()
        stat_pg_viw()
        time.sleep(live_wait_infinity_loop)
        time.sleep(2)


def test_server():
    for i in range(exe_time):
        # time.sleep(test_loop_tim)
        # start_auto()
        stat_pg_viw()


live_server()
