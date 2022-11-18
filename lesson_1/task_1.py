'''
Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего
сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться
с помощью функции ip_address().
'''

import platform
import socket
from subprocess import Popen, PIPE

DICTS_LIST = [
    'yandex.ru', 'a', '8.8.8.8'
]


def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        args = ['ping', param, '5', ip_address]
        reply = Popen(args, stdout=PIPE, stderr=PIPE)
        code = reply.wait()
        if code == 0:
            return f'{ip_address} - Узел доступен'
    except socket.gaierror as error:
        return f'Неверный адрес: "{hostname}" - {error}'


for i in DICTS_LIST:
    print(get_ip_address(i))
