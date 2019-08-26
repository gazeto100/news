import os

from IPython.utils.py3compat import execfile
from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    print("Decorated job")
    os.system('python vesti.py')

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=1)
scheduler.start()