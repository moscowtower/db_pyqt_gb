from tabulate import tabulate
from task2 import host_range_ping


def host_range_ping_tab(subnet_address, start_address=None, end_address=None):
    headers = ["address", "status"]
    addresses_dict = {'reachable': [],
                      'unreachable': []}

    for adr in host_range_ping(subnet_address, start_address=start_address, end_address=end_address, info=False):
        address_dict = dict(zip(headers, adr))
        if address_dict['status'] == True:
            addresses_dict['reachable'].append(str(adr[0]))
        else:
            addresses_dict['unreachable'].append(str(adr[0]))
    return tabulate(addresses_dict, tablefmt="pipe", headers='keys', stralign="center")


if __name__ == '__main__':
    subnet_address = '192.168.0.0/24'
    start_address = '192.168.0.4'
    end_address = '192.168.0.10'
    print('МОЛНИЕНОСНЫЕ ТЕХНОЛОГИИ!!!!!')
    res = host_range_ping_tab(subnet_address, start_address=start_address, end_address=end_address)
    print(res)