from speedtest import Speedtest
from operator import itemgetter

speedTest = Speedtest()


def best_provider():
    all_server = speedTest.get_best_server()
    return all_server, all_server['name'], all_server['sponsor']


detailed, Location, Provider = best_provider()
print("Best server near by : {}".format(Provider))
print("Best server Location near by : {}".format(Location))
print("Best server near by Detail : {}".format(detailed))
print('\n')


def closest_internet_providers():
    sponsors_close = speedTest.get_closest_servers()
    sponsor = list(map(itemgetter('sponsor'), sponsors_close))
    return sponsor


print("Closest Internet Server Name : {}".format(closest_internet_providers()))
print('\n')


def detailed_closest_internet_providers():
    providers = speedTest.get_closest_servers()
    return providers


print("Closest Internet Server Details are {}".format(closest_internet_providers()))
print('\n')


def all_internet_providers():
    all_server = speedTest.get_servers()
    return all_server


print("All Internet Service Providers by SpeedTest is {}".format(all_internet_providers()))
print('\n')
