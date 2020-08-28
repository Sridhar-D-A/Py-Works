from speedtest import Speedtest

speedTest = Speedtest()


def download_speed():
    down_speed = speedTest.download()
    return down_speed / 1000000


def upload_speed():
    up_speed = speedTest.upload()
    return up_speed / 1000000


def all_speed():
    print("Download Speed : {} Mbps".format(download_speed()))
    print("Upload Speed : {} Mbps".format(upload_speed()))


all_speed()
