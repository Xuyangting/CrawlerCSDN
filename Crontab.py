# -*- coding:utf-8 -*-
import os
from apscheduler.schedulers.blocking import BlockingScheduler


def scrapy():
    print os.system("scrapy crawl csdn")


def execute():
    sched = BlockingScheduler()
    sched.add_job(scrapy, "interval", minutes=3)
    sched.start()

if __name__ == '__main__':
    execute()


