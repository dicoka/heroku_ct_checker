from apscheduler.schedulers.blocking import BlockingScheduler
from checker import checker

sched = BlockingScheduler()

#This job is run every day at 6-00 and 15-00
sched.add_job(checker, 'cron', hour='6,15')

print 'Starting Scheduler...\n'
sched.start()
