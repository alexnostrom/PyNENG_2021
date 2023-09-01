# Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt. Имя файла передается как аргумент скрипту.
# Скрипт должен возвращать на стандартный поток вывода команды из переданного конфигурационного файла, исключая строки, которые начинаются с !.
# Вывод должен быть без пустых строк.
# Ограничение: Все задания надо выполнять используя только пройденные темы.
#
# Пример вывода:
# $ python task_7_2.py config_sw1.txt
# Current configuration : 2033 bytes
# version 15.0
# service timestamps debug datetime msec
# service timestamps log datetime msec
# no service password-encryption
# hostname sw1
# interface Ethernet0/0
#  duplex auto
# interface Ethernet0/1
#  switchport trunk encapsulation dot1q
#  switchport trunk allowed vlan 100
#  switchport mode trunk
#  duplex auto
#  spanning-tree portfast edge trunk
# interface Ethernet0/2
#  duplex auto
# interface Ethernet0/3
#  switchport trunk encapsulation dot1q
#  switchport trunk allowed vlan 100
#  duplex auto
#  switchport mode trunk
#  spanning-tree portfast edge trunk

with open('config_sw1.txt', 'r', encoding='utf-8') as read_file:
    edited_file = [i.strip("\n") for i in read_file if not i.startswith('!')]

    for elem in edited_file:
        print(elem)