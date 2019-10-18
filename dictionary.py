import re

'''
Dictionary

[corpus kota]       :	https://github.com/nolimitid/nama-tempat-indonesia/tree/master/txt
[corpus nama]       :   https://github.com/fzaninotto/Faker/blob/master/src/Faker/Provider/id_ID/Person.php
[corpus restoran]   :   https://pergikuliner.com/restoran/bandung/
'''

def isDictKota():
    # inisiasi tag token informasi
    nama = "DaftarKota"

    path = 'corpus/kota.txt'

    with open(path, 'r') as myfile:
        rule = '|'.join([line.replace('\n', '') for line in myfile.readlines()])
    rule = r'(^|\s)('+rule+')\s'
    return {
        "tag" : nama,
        "rule" : rule
    }

def isDictNama():
    # inisiasi tag token informasi
    nama = "DaftarNama"

    path = 'corpus/nama.txt'

    with open(path, 'r') as myfile:
        rule = '|'.join([line.replace('\n', '') for line in myfile.readlines()])

    return {
        "tag" : nama,
        "rule" : rule
    }