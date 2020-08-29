import csv
import logging
import os.path
import speedtest
from datetime import date, datetime

time_stamp = datetime.now()
today = date.today()
speedTest = speedtest.Speedtest()

logging.basicConfig(filename='SpeedTest.log', level=logging.DEBUG,
                    format='%(asctime)s -- %(levelname)s -- %(message)s')


def download_speed():
    down_speed = speedTest.download()
    return down_speed / 1000000


def upload_speed():
    up_speed = speedTest.upload()
    return up_speed / 1000000


def all_speed():
    logging.info("Download Speed : {} Mbps".format(download_speed()))
    logging.info("Upload Speed : {} Mbps".format(upload_speed()))

    today_ = today.strftime("%b-%d-%Y")
    time_stamp_ = time_stamp.strftime("%H:%M:%S")

    with open('speedTest.csv', "a") as csv_file:
        file_empty = os.stat('speedTest.csv').st_size == 0
        header = ['DATE', 'TIME', 'DOWNLOAD SPEED[Mbps]', 'UPLOAD SPEED[Mbps]']
        writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\n', fieldnames=header)
        if file_empty:
            writer.writeheader()  # file doesn't exist yet, write a header

        writer.writerow({'DATE': today_, 'TIME': time_stamp_, 'DOWNLOAD SPEED[Mbps]': download_speed(),
                         'UPLOAD SPEED[Mbps]': upload_speed()})


all_speed()

# Using Task Scheduler in windows, Schedule this Program for every day and repeat it for every 3/6/12 hour.
