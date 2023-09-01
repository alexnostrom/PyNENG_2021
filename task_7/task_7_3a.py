with open('CAM_table.txt', 'r', encoding='utf-8') as read_file:
    mac_address_table = []
    for w in read_file.readlines():
        if w.split() and w.split()[0].isdigit():
            vlan, mac, _, intf = w.strip().split()
            mac_address_table.append([int(vlan), mac, intf])

    for vlan, mac, intf in sorted(mac_address_table):
        print(f"{vlan:<8}{mac:<20}{intf}")
