# Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде на стандартный поток вывода:
#
# Prefix                10.0.24.0/24
# AD/Metric             110/41
# Next-Hop              10.0.13.3
# Last update           3d18h
# Outbound Interface    FastEthernet0/0


with open('ospf.txt', 'r', encoding='utf-8') as read_file:
    data = [i.strip().split() for i in read_file]
    fast_list = []
    for elem in data:
        fast_list.append({
            'Prefix': elem[1],
            'AD/Metric': elem[2].strip("[]"),
            'Next-Hop': elem[4][:-1],
            'Last update': elem[5][:-1],
            'Outbound Interface': elem[6]
        })

    for elem in fast_list:
        for key, val in elem.items():
            print(f"{key:<20}{val}")
        print()
