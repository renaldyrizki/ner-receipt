import re
import glob
import os
import string
from getBody import getBody

def getValueTags(teks):
    namaItem=re.compile('<namaItem>(.*?)</namaItem>', re.DOTALL).findall(teks)
    hargaItem=re.compile('<hargaItem>(.*?)</hargaItem>', re.DOTALL).findall(teks)
    subtotalItem=re.compile('<subtotalItem>(.*?)</subtotalItem>', re.DOTALL).findall(teks)
    totalPembayaran=re.compile('<totalPembayaran>(.*?)</totalPembayaran>', re.DOTALL).findall(teks)

    return {
                'namaFile' : filee.replace(folder+'\\', ''),
                'tagNamaItem' : namaItem,
                # 'tagHargaItem' : hargaItem,
                'tagSubtotalItem' : subtotalItem,
                'tagTotalPembayaran' : totalPembayaran
            }

def saveKeTxt(path, filename, teks):
    try:
        # Create target Directory
        os.mkdir(path)
        # print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        # print("Directory " , dirName ,  " already exists")
        False

    # remove file
    try:
        os.remove(path+filename)
    except Exception as e:
        False

    # cuma ascii aja di filternya, kalo ada symbol kek bahasa china/jepang di ilangin
    printable = set(string.printable)
    hasilTeks = filter(lambda x: x in printable, teks)

    wFile = open(path+filename, "w+", encoding="utf-8")
    wFile.write(''.join(hasilTeks))
    wFile.close()

def cleanTag(teks):
    hasil = teks.replace("<namaItem>", "").replace("</namaItem>", "")
    hasil = hasil.replace("<hargaItem>", "").replace("</hargaItem>", "")
    hasil = hasil.replace("<subtotalItem>", "").replace("</subtotalItem>", "")
    hasil = hasil.replace("<totalPembayaran>", "").replace("</totalPembayaran>", "")

    return hasil

def cekGt(teksBody, tag):

    predict = getValueTags(teksBody)
    
    for gt in predict['tagNamaItem']:
        tag['tagNamaItem'].remove(gt)
    for gt in predict['tagSubtotalItem']:
        tag['tagSubtotalItem'].remove(gt)
    for gt in predict['tagTotalPembayaran']:
        tag['tagTotalPembayaran'].remove(gt)
    tagNotFound = []
    for gt in tag['tagNamaItem']:
        tagNotFound.append(("namaItem", gt))
    for gt in tag['tagSubtotalItem']:
        tagNotFound.append(("subtotalItem", gt))
    for gt in tag['tagTotalPembayaran']:
        tagNotFound.append(("totalPembayaran", gt))

    return {
        "notfound" : tagNotFound
    }

folders = glob.glob("data/*")
filesBody = []
for folder in folders:
    try:
        files = glob.glob(folder+"/*.txt")
        groundTruth = []
        for filee in files:
            try:
                textF = open(filee, "r", encoding="utf-8")
                
                teks = textF.read()
                valTags = getValueTags(teks)
                
                teksBody = getBody(teks, filee.split("\\"))

                if teksBody!="notfoundbody" :
                    gt = cekGt(teksBody, valTags)
                    # exit()
                    # gt = cekGroundTruth(cleanTag(teksBody), valTags)

                    # print(gt)
                    # print(valTags["namaFile"])

                    # print('"'+filee.split("\\")[2]+'"',",", '"'+repr(teksBody)+'"', ',"adaw", "awaa"')

                    filesBody.append((folder, valTags["namaFile"], gt, teksBody))
                    groundTruth.append(valTags)
                else:
                    print(folder, valTags["namaFile"])
                    exit()
            except Exception as e:
                print('Failed to open file: '+ str(e))
        
        # print("Folder:", folder)
        # for i,t in enumerate(groundTruth):
        #     print("Nama File:",t["namaFile"])
        #     print("Nama Item :")
        #     for ni in t["tagNamaItem"]:
        #         print("-", ni)
        #     print("Harga Item :")
        #     for hi in t["tagHargaItem"]:
        #         print("-", hi)
        #     print("Subtotal Item :")
        #     for si in t["tagSubtotalItem"]:
        #         print("-", si)
        #     print("Total Pembayaran :")
        #     for tp in t["tagTotalPembayaran"]:
        #         print("-", tp)
    except Exception as e:
        print('Failed to open folder: '+ str(e))

for fb in filesBody:
    if len(fb[2]["notfound"]) < 1:
        # save
        # print("save ke", fb[0].replace("data", "output_body")+"\\"+fb[1])
        saveKeTxt(fb[0].replace("data", "output_body"),"\\"+fb[1], fb[3])
        # print(fb[3])
        print("Saved!")
    else:
        print("---")
        print(fb[3])
        print(fb[0], fb[1], fb[2]["notfound"])
        # print(fb[0], fb[1])
        exit()
