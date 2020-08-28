from speedtest import Speedtest
from operator import itemgetter

speedTest = Speedtest()


def best_provider():
    all_server = speedTest.get_best_server()
    return all_server


print("Best server near by is {}".format(best_provider()))


def closest_internet_providers():
    sponsors_close = speedTest.get_closest_servers()
    sponsor = list(map(itemgetter('sponsor'), sponsors_close))
    return sponsor


print(closest_internet_providers())


def detailed_closest_internet_providers():
    providers = speedTest.get_closest_servers()
    return providers


print(detailed_closest_internet_providers())


def all_internet_providers():
    all_server = speedTest.get_servers()
    return all_server


print(all_internet_providers())
