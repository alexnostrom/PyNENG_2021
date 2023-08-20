nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

new_nat = nat.replace('Fast', 'Gigabit')
print(new_nat)
