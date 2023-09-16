"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    access_ports_dict = {}
    trunk_ports_dict = {}
    with open(config_filename, 'r', encoding='utf-8') as read_file:
        for elem in read_file:
            line = elem.strip()
            if line.startswith('interface'):
                intrf = line.split()[1]
            elif "switchport trunk allowed" in line:
                trunk_ports_dict[intrf] = list(map(int, line.split()[-1].split(",")))
            elif "switchport access vlan" in line:
                access_ports_dict[intrf] = int(line.split()[-1])
            elif "switchport mode access" in line:
                access_ports_dict[intrf] = 1
    print(access_ports_dict)
    print(trunk_ports_dict)
    return access_ports_dict, trunk_ports_dict


file_name = 'config_sw2.txt'

get_int_vlan_map(file_name)
