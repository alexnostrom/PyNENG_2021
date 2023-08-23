# Задание 5.2a
# Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
# надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.
# Пример адреса сети (все биты хостовой части равны нулю):
#     10.0.1.0/24
#
#     190.1.0.0/16
# Пример адреса хоста:
#     10.0.1.1/24 - хост из сети 10.0.1.0/24
#
#     10.0.5.195/28 - хост из сети 10.0.5.192/28
# Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:
# Network:
# 10        0         1         0
# 00001010  00000000  00000001  00000000
# Mask:
# /24
# 255       255       255       0
# 11111111  11111111  11111111  00000000
# Проверить работу скрипта на разных комбинациях хост/маска, например: 10.0.5.195/28, 10.0.1.1/24
# Подсказка:
# Есть адрес хоста в двоичном формате и маска сети 28.
# Адрес сети это первые 28 бит адреса хоста + 4 ноля.
# То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет bin_ip = "00001010000000010000000111000011".
# А адрес сети будет первых 28 символов из bin_ip + 0000
# (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4): 00001010000000010000000111000000
# Ограничение: Все задания надо выполнять используя только пройденные темы.

ip, mask = input("Введите IP/MASK сети: ").split('/')
ip = ip.split('.')
ip_binary = [str(bin(int(i))[2:]).rjust(8, '0') for i in ip]
mask_format = f'/{mask}'
mask = '1' * int(mask) + ((32 - int(mask)) * '0')
mask_decimal = []
mask_binary = []

for i in range(0, len(mask), 8):
    mask_binary.append(mask[i:i + 8])
    mask_decimal.append(int(mask[i:i + 8], 2))

net_address_binary = [*ip_binary[:-1]]
x = ''
for j, k in zip(ip_binary[-1], mask_binary[-1]):
    x += str(int(j) & int(k))
net_address_binary.append(x)

res = ''.join(net_address_binary)
net_address = []
for i in range(0, len(res), 8):
    net_address.append(int(res[i:i + 8], 2))

print('Network  :')
print(f'{"".join("{:<10}".format(i) for i in net_address)}')
print(f'{"".join("{:<10}".format(i) for i in net_address_binary)}')
print('Mask:')
print(mask_format)
print(f'{"".join("{:<10}".format(i) for i in mask_decimal)}')
print(f'{"".join("{:<10}".format(i) for i in mask_binary)}')
