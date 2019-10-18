import re
import glob
import os

folders = glob.glob("data/alfa*")

for folder in folders:
    try:
        files = glob.glob(folder+"/*")
        temp = []
        for filee in files:
            try:
                textF = open(filee, "r", encoding="utf-8")
                namaItem=re.compile('<namaItem>(.*?)</namaItem>', re.DOTALL).findall(textF.read())
                hargaItem=re.compile('<hargaItem>(.*?)</hargaItem>', re.DOTALL).findall(textF.read())
                subtotalItem=re.compile('<subtotalItem>(.*?)</subtotalItem>', re.DOTALL).findall(textF.read())
                totalPembayaran=re.compile('<totalPembayaran>(.*?)</totalPembayaran>', re.DOTALL).findall(textF.read())
                temp.append({
                    'namaFile' : filee.replace(folder+'\\', ''),
                    'tagNamaItem' : namaItem,
                    'tagHargaItem' : hargaItem,
                    'tagSubtotalItem' : subtotalItem,
                    'tagTotalPembayaran' : totalPembayaran
                })

            except Exception as e:
                print('Failed to open file: '+ str(e))
        
        print("Folder:", folder)
        for i,t in enumerate(temp):
            print("Nama File:",t["namaFile"])
            print("Nama Item :")
            for ni in t["tagNamaItem"]:
                print("-", ni)
    except Exception as e:
        print('Failed to open folder: '+ str(e))
