# Задание 5.2
# Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
# Затем вывести информацию о сети и маске в таком формате:
# Network:
# 10        1         1         0
# 00001010  00000001  00000001  00000000
# Mask:
# /24
# 255       255       255       0
# 11111111  11111111  11111111  00000000
# Проверить работу скрипта на разных комбинациях сеть/маска.
# Подсказка: Получить маску в двоичном формате можно так:
# In [1]: "1" * 28 + "0" * 4
# Out[1]: "11111111111111111111111111110000"
# Ограничение: Все задания надо выполнять используя только пройденные темы.

ip, mask = input("Введите IP/MASK сети: ").split('/')
ip = ip.split('.')
ip_binary = [str(bin(int(i))[2:]).rjust(8, '0') for i in ip]
mask_format = f'/{mask}'
mask = '1' * int(mask) + ((32 - int(mask)) * '0')
mask_decimal = []
mask_binary = []

for i in range(0, len(mask), 8):
    mask_binary.append(mask[i:i+8])
    mask_decimal.append(int(mask[i:i+8], 2))
print('Network:')
print(f'{"".join("{:<10}".format(i) for i in ip)}')
print(f'{"".join("{:<10}".format(i) for i in ip_binary)}')
print('Mask:')
print(mask_format)
print(f'{"".join("{:<10}".format(i) for i in mask_decimal)}')
print(f'{"".join("{:<10}".format(i) for i in mask_binary)}')