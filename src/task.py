import requests
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='MST')


def timed_job():
    page = requests.get("https://evn-crawl.herokuapp.com/api/v1/news/crawl")


sched.add_job(timed_job, 'cron', minute='30')
sched.start()
