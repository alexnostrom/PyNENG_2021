from sys import argv

ignore = ["duplex", "alias", "configuration"]

source_file, dst_file = argv[1], argv[2]

with open(source_file, 'r', encoding='utf-8') as read_file, open(dst_file, 'w', encoding='utf-8') as write_file:
    edited_file = [i.strip("\n") for i in read_file if not i.startswith('!')]

    for elem in edited_file:
        if not set(elem.split()) & set(ignore):
            write_file.write(elem + '\n')
