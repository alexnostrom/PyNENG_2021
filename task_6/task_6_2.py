# Задание 6.2
#     Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
#     В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
#         «unicast» - если первый байт в диапазоне 1-223
#         «multicast» - если первый байт в диапазоне 224-239
#         «local broadcast» - если IP-адрес равен 255.255.255.255
#         «unassigned» - если IP-адрес равен 0.0.0.0
#         «unused» - во всех остальных случаях

ip_address = input("Введите IP-address: ").split('.')

result = ''

if len(ip_address) == 4:
    if ip_address == "255.255.255.255".split('.'):
        result = "local broadcast"
    elif ip_address == "0.0.0.0".split('.'):
        result = "unassigned"
    elif int(ip_address[0]) in range(1, 224):
        result = "unicast"
    elif int(ip_address[0]) in range(224, 240):
        result = "multicast"
    else:
        result = "unused"
else:
    result = "unused"

print(result)
