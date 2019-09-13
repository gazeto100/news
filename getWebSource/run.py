#!/usr/bin/python

import os

from IPython.utils.py3compat import execfile
from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    os.system('python dnes.py')
    #os.system('python vesti.py')
    #os.system('python blitz.py')
    #os.system('python getActualno.py')
    #os.system('python novinibg.py')
    os.system('python 24chasa.py')
    #os.system('python novabg.py')
    #os.system('python dirbg.py')
    #os.system('python dariknews.py')
    os.system('python btv.py')
    #os.system('python dnevnik.py')

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=3)
scheduler.start()