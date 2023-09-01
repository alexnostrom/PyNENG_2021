# Задание 7.2a
# Сделать копию скрипта задания 7.2.
# Дополнить скрипт: Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore.
# При этом скрипт также не должен выводить строки, которые начинаются на !.
# Проверить работу скрипта на конфигурационном файле config_sw1.txt. Имя файла передается как аргумент скрипту.
# Ограничение: Все задания надо выполнять используя только пройденные темы.
# ignore = ["duplex", "alias", "configuration"]


ignore = ["duplex", "alias", "configuration"]

with open('config_sw1.txt', 'r', encoding='utf-8') as read_file:
    edited_file = [i.strip("\n") for i in read_file if not i.startswith('!')]

    for elem in edited_file:
        if not set(elem.split()) & set(ignore):
            print(elem)
