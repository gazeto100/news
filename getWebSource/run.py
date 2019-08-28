#!/usr/bin/python

import os

from IPython.utils.py3compat import execfile
from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    print("Decorated job")
    os.system('python dnes.py')
    os.system('python vesti.py')
    os.system('python blitz.py')
    os.system('python getActualno.py')
    os.system('python novinibg.py')
    os.system('python 24chasa.py')

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=1)
scheduler.start()