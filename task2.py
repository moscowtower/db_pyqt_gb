from ipaddress import ip_network, ip_address
from task1 import host_ping


def host_range_ping(_subnet_address, start_address=None, end_address=None, info=True):
    start_index = -1
    end_index = 254
    try:
        subnet = ip_network(_subnet_address)
        ips = [subnet.network_address + i for i in range(1, subnet.num_addresses)]
        if start_address:
            start_address = ip_address(start_address)
            if start_address in ips:
                start_index = ips.index(start_address) - 1
        if end_address:
            end_address = ip_address(end_address)
            if end_address in ips:
                end_index = ips.index(end_address)+1
    except Exception:
        print("Bad news...")
    else:
        if start_address and not end_address:
            ip_addresses = [adr for adr in ips if ips.index(adr) > start_index]
        elif end_address and not start_address:
            ip_addresses = [adr for adr in ips if ips.index(adr) < end_index]
        else:
            ip_addresses = [adr for adr in ips if start_index < ips.index(adr) < end_index]

        return host_ping(ip_addresses, info=info)

if __name__ == '__main__':
    subnet_address = '192.168.0.0/24'
    start_address = '192.168.0.4'
    end_address = '192.168.0.10'
    host_range_ping(subnet_address, start_address=start_address, end_address=end_address)
