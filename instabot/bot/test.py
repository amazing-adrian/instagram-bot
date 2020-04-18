import datetime as dt
import pandas as pd
import schedule

from time import sleep

DAYS_TO_UNFOLLOW = 4

date = (dt.datetime.today() - dt.timedelta(days=DAYS_TO_UNFOLLOW)).date().strftime("%Y-%m-%d")
print(date)

follows = pd.read_csv("../logs/follows.csv")

today = follows.loc[follows['Date'] == str(date)]
users = today['User'].unique()

# print(users)


# print(dt.datetime.today())

def hello():
    print("Hello sir! " + str(dt.datetime.now()))

def hi():
    print("Hi there!")

schedule.every().second.do(hello)
schedule.every(2).seconds.do(hi)

while True:
    schedule.run_pending()
    sleep(1)