import locale
import os
import subprocess
from ipaddress import ip_address

args = ['123.47.56.2', '223.123.47.56', '34.56.78.23', '178.248.232.209', '138.255.255.255']
# for arg in args:
#     # print('Адрес не доступен') if os.system('ping -n 1 ' + arg) else print('Адрес живой')
#     proc = subprocess.Popen(('ping -n 1 ' + arg).split(), stdout=subprocess.PIPE)
#     my_public_ip = proc.stdout.read().decode(locale.getpreferredencoding())
#     print('m ', my_public_ip)

import platform    # For getting the operating system name


def ping(hosts):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    for host in hosts:
        command = ['ping', param, '1', host]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        result = proc.stdout.read().decode(locale.getpreferredencoding())
        print(result)

# ping(args)


def isUp(hostname):
    giveFeedback = False

    if platform.system() == "Windows":
        response = os.system("ping " + hostname + " -n 1")
    else:
        response = os.system("ping -c 1 " + hostname)

    isUpBool = False
    if response == 0:
        if giveFeedback:
            print(hostname, 'is up!')
        isUpBool = True
    else:
        if giveFeedback:
            print(hostname, 'is down!')

    return isUpBool


# print(isUp("example.com"))  # Example domain
# print(isUp("localhost"))  # Your computer
# print(isUp("invalid.example.com"))  # Unresolvable hostname: https://tools.ietf.org/html/rfc6761
# print(isUp("192.168.1.1"))  # Pings local router
# print(isUp("192.168.1.135"))  # Pings a local computer - will differ for your network

def host_ping(lst):
    result = []
    for host in lst:
        verified_ip = ip_address(host)
        if verified_ip:
            with open(os.devnull, 'w') as DNULL:
                response = subprocess.call(
                    ["ping", "-n", "2", "-w", "2", host], stdout=DNULL
                )
            if response == 0:
                result.append(('Доступен', str(host), f'[{verified_ip}]'))
                print(f'Доступен    {host} [{verified_ip}]')
                continue
        result.append(('Не доступен', str(host),
                       f'[{verified_ip if verified_ip else "Не определён"}]'))
        print(f'Не доступен {host} '
              f'[{verified_ip if verified_ip else "Не определён"}]')
    return result

host_ping(args)