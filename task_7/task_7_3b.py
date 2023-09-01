get_vlan = input("Enter Vlan: ")

with open('CAM_table.txt', 'r', encoding='utf-8') as read_file:
    mac_address_table = []
    for w in read_file.readlines():
        if w.split() and w.split()[0].isdigit() and w.split()[0] == get_vlan:
            vlan, mac, _, intf = w.strip().split()
            print(f"{vlan:<8}{mac:<20}{intf}")
