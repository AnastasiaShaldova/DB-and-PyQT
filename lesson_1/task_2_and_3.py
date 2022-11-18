'''
Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только
последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
'''

import platform

from ipaddress import ip_address
from subprocess import Popen, PIPE

from tabulate import tabulate


def get_ip_address(hostname):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '5', hostname]
    code = Popen(command, stdout=PIPE, stderr=PIPE)
    if code.wait() == 0:
        return f'{str(hostname)} - Узел доступен'
    return f'{str(hostname)} - Узел недоступен'


hostname = ip_address(input('Введите адрес: '))
val = int(input('Введите число: '))
for i in range(val):
    hostname += 1
    print(get_ip_address(str(hostname)))


# DICTS_LIST = [{'Узел доступен': [],
#                'Узел недоступен': [],
#               }]
#
# print(tabulate(DICTS_LIST, headers='keys'))