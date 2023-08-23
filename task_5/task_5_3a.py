# Задание 5.3a
# Дополнить скрипт из задания 5.3 таким образом,
# чтобы, в зависимости от выбранного режима, задавались разные вопросы в запросе о номере VLANа или списка VLANов:
#     для access: «Введите номер VLAN:»
#     для trunk: «Введите разрешенные VLANы:»
# Ограничение: Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if и циклов for/while.


interface_mode = input("Введите режим работы интерфейса (access/trunk): ")

if interface_mode.lower() == 'access':
    interfece_type = input("Введите тип и номер интерфейса: ")
    vlans_quantity = input("Введите номер VLAN: ")

    access_template = [
        "switchport mode access", "switchport access vlan {}".format(vlans_quantity),
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable"
    ]

    print(f'\ninterface {interfece_type}')
    for i in access_template:
        print(i)

elif interface_mode.lower() == 'trunk':
    interfece_type = input("Введите тип и номер интерфейса: ")
    vlans_quantity_list = input("Введите разрешенные VLANы: ").split()

    trunk_template = [
        "switchport trunk encapsulation dot1q", "switchport mode trunk",
        "switchport trunk allowed vlan {}".format(','.join(vlans_quantity_list))
    ]

    print(f'\ninterface {interfece_type}')
    for i in trunk_template:
        print(i)

else:
    print('Unknown command')
