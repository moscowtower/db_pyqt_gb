from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(ips, timeout=1, requests=1, info=True):
    result = []
    for address in ips:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        ping = Popen(f"ping {address} -t {timeout} -W {requests}", shell=True, stdout=PIPE)
        ping.wait()
        if ping.returncode == 0:
            if info:
                print(f"Узел '{address}' доступен.")
            result.append((address, True))
        else:
            if info:
                print(f"Узел '{address}' недоступен.")
            result.append((address, False))
    return result


if __name__ == '__main__':
    ip_addresses = ['google.com', '1.2.3.4.5', '193.124.63.214', 'localhost']
    host_ping(ip_addresses)