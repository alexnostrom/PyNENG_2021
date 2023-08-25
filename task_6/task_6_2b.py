# Задание 6.2b
# Сделать копию скрипта задания 6.2a.
# Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.
# Ограничение: Все задания надо выполнять используя только пройденные темы.


# 255.255.255.255
# 255.2a5.255.255
# 0.255.255.255
# 256.255.255.255

result = True

while result:
    ip_address = input("Введите IP-address: ").split('.')

    if len(ip_address) == 4:
        for elem in range(len(ip_address)):
            try:
                ip_address[elem] = int(ip_address[elem])
            except:
                print("Неправильный IP-адрес")
                break
        else:
            for elem in ip_address:
                if elem not in range(0, 256):
                    print("Неправильный IP-адрес")
                    break
            else:
                result = False
    else:
        print("Неправильный IP-адрес")

print("Правильный IP-адрес")
