# Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
#
# Prefix                10.0.24.0/24
# AD/Metric             110/41
# Next-Hop              10.0.13.3
# Last update           3d18h
# Outbound Interface    FastEthernet0/0
#
# Ограничение: Все задания надо выполнять используя только пройденные темы.

# ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0".split()
new_d = {
    'Prefix': ospf_route[0],
    'AD/Metric': ospf_route[1].strip("[]"),
    'Next-Hop': ospf_route[3][:-1],
    'Last update': ospf_route[4][:-1],
    'Outbound Interface': ospf_route[5]
}

for key, val in new_d.items():
    print(f'{key:<23}{val}')