import re
import glob
import os
from tokenInformation import *
from dictionary import *

DEBUG = False

def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1

# define rules buat header
def isHeader(teks):
    rules = [
        isTokenInfoPembelianTeks()["rule"],
        isTokenInfoInfoReceiptTeks()["rule"],
        # #kontak
        isTokenInfoSocmedTeks()["rule"],
        isTokenInfoWebsiteTeks()["rule"],
        isTokenInfoWebsiteFormat()["rule"],
        isTokenInfoEmailTeks()["rule"],
        isTokenInfoEmailFormat()["rule"],
        isTokenInfoTelpTeks()["rule"],
        isTokenInfoTelpFormat()["rule"],
        isTokenInfoPajakTeksFooter()["rule"],
        # #end of kontak
        # isTokenLebihDariTujuhDigit()["rule"],
        isTokenInfoKodeTeks()["rule"],
        # #lokasi
        isTokenInfoPrefixLokasi()["rule"],
        isDictKota()["rule"],
        # #end of lokasi
        # "(\s|^)("+isDictNama()["rule"]+")(\s|$)",
        #isDictNama()["rule"],
        # #npwp
        isTokenInfoNPWPTeks()["rule"],
        isTokenInfoNPWPFormat()["rule"],
        # #endofnpwp
        isTokenInfoPegawaiTeks()["rule"],
        isTokenInfoPelangganTeks()["rule"],
        isTokenInfoOrderTeks()["rule"],
        isTokenInfoPOS()["rule"],
        isTokenInfoTerimaKasihTeks()["rule"],
        isTokenInfoPrefixPerusahaan()["rule"],
        isTokenInfoTanggalWaktuTeks()["rule"],
        isTokenInfoTanggalWaktu()["rule"],
        # isTokenInfoHeaderItemTeks()["rule"]
    ]

    rule = '|'.join([rule for rule in rules])
    
    t = re.search(rule, teks, re.IGNORECASE)
    if t:
        return t.group()

def isBody(teks):
    rules = [
        isTokenInfoKantong()["rule"],
        isTokenKataIdentik()["rule"],
        isTokenLebihDariTigaDigit()["rule"],
        isTokenMengandungDigitdanKoma()["rule"],
        isTokenMengandungDigitdanTitik()["rule"],
        isTokenMengandungDigitdanTitikKoma()["rule"],
        isTokenInfoMengandungDigitdanPersen()["rule"],
        isTokenInfoPembulatanTeks()["rule"],
        isTokenInfoVolumeTeks()["rule"],
        isTokenInfoOtherPaymentTeks()["rule"],
        isTokenInfoKembalianTeks()["rule"],
        
        isTokenInfoTotalItemTeks()["rule"],
        isTokenInfoSubTotalTeks()["rule"],

        #isTokenInfoPrefixMataUang()["rule"],
        #isTokenInfoHematTeks()["rule"],
        # isTokenInfoPajakTeks()["rule"],
        isTokenInfoTotalTeks()["rule"],
        #isTokenInfoServiceTeks()["rule"],
        #isTokenInfoTotalKuantitasTeks()["rule"],
        #isTokenInfoPembayaranTeks()["rule"],
        #isTokenInfoDiscount1Teks()["rule"],
    ]

    rule = '|'.join([rule for rule in rules])
    
    t = re.search(rule, teks, re.IGNORECASE)
    if t:
        return t.group()

def isFooter(teks):
    rules = [
        isTokenInfoTerimaKasihTeks()["rule"],
        isTokenInfoFooterTeks()["rule"], #nambah
        isTokenInfoPajakTeksFooter()["rule"],
        isTokenInfoDukunganTeks()["rule"],
        isTokenInfoMemberTeks()["rule"],
        # #dari sini sama kayak header
        isTokenInfoInfoReceiptTeks()["rule"],
        # #kontak
        isTokenInfoSocmedTeks()["rule"],
        isTokenInfoWebsiteTeks()["rule"],
        isTokenInfoWebsiteFormat()["rule"],
        isTokenInfoEmailTeks()["rule"],
        isTokenInfoEmailFormat()["rule"],
        isTokenInfoTelpTeks()["rule"],
        isTokenInfoTelpFormat()["rule"],
        #end of kontak
        # isTokenLebihDariTujuhDigit()["rule"],
        isTokenInfoKodeTeks()["rule"],
        #lokasi
        isTokenInfoPrefixLokasi()["rule"],
        isDictKota()["rule"],
        #end of lokasi
        # "(\s|^)("+isDictNama()["rule"]+")(\s|$)",
        #isDictNama()["rule"],
        #npwp
        isTokenInfoNPWPTeks()["rule"],
        isTokenInfoNPWPFormat()["rule"],
        #endofnpwp
        isTokenInfoPegawaiTeks()["rule"],
        isTokenInfoPelangganTeks()["rule"],
        isTokenInfoOrderTeks()["rule"],
        isTokenInfoPOS()["rule"],

        isTokenInfoPrefixPerusahaan()["rule"],
        isTokenInfoTanggalWaktuTeks()["rule"],
        isTokenInfoTanggalWaktu()["rule"],
    ]

    rule = '|'.join([rule for rule in rules])
    
    t = re.search(rule, teks, re.IGNORECASE)
    if t:
        return t.group()

def getBody(teks, fileName):
    teks = teks.split("\n")
    teksBaris = list()
    label = []
    for i, t in enumerate(teks):
        # tampung teks perbaris
        t = t+"\n"
        teksLine = re.sub('<.*?>', '', t)
        label.append('')

        # labelan sesuai bagian na
        header = isHeader(teksLine)
        body = isBody(teksLine)
        footer = isFooter(teksLine)
        
        if header:
            if DEBUG:
                print("Header:",header)
            label[i] += ('h')
        if body:
            if DEBUG:
                print("Body:",body)
            label[i] += ('b')
        if footer:
            if DEBUG:
                print("Footer:",footer)
            label[i] += ('f')
        
        # teksBaris.append(i)
        teksBaris.append([i, label[i]])

    if DEBUG:   
        print(len(label))
        print(" (befor delete weird) : ",[str(i)+":"+l for i,l in enumerate(label)])
    
    #print(teksBaris)
    # print([str(i+1)+":"+l for i,l in enumerate(label)])
    # exit()
    
    # kalo ga punya body
    try:
        label.index('b')

        # inisiasi index b awal dan akhir
        # for idx, val in enumerate(label):
        #     if 'b' in val:
        #         bFirst = idx 
        #         break
        
        # for i in range(len(label)):
        #     idx = i-i*2-1
        #     if 'b' in label[idx]:
        #         bLast = idx
        #         break

        bFirst = label.index('b')        
        bLast = rindex(label, 'b')
        if DEBUG:
            print(bFirst, bLast, ":", label[bFirst], label[bLast])
        
        indexWeird = list() # buat nampung header, footer atau hf kalo diantara body
        
        # cek buat yg aneh
        indexWeird = [i+bFirst for i, x in enumerate(label[bFirst:bLast]) if x == "hf" or x == "f" or x == "h"]
        if DEBUG:
            # delete weird
            print('weird : ', indexWeird)
        # print(teksBaris)
        for iw, iWeird in enumerate(indexWeird):
            del teksBaris[iWeird-iw]
            del label[iWeird-iw]
            # del teks[iWeird-iw]

        if DEBUG:
            print(label)
            print(teksBaris)
            print(" (after delete weird) : ",[l for l in teksBaris])
        
        # exit()
        # inisiasi lagi
        try:
            f = label.index('f')
        except ValueError as ve:
            # f = -1
            f = len(label)-1
        # ambil posisi h plg kanan
        try:   
            h = rindex(label,'h')
        except ValueError as ve:
            h = -1

        hf = [i for i, x in enumerate(label) if x == "hf"]

        bFirst = label.index('b')
        bLast = rindex(label, 'b')
        # last batas buat header
        hfHeader = [x for x in hf if x < bFirst]
        if len(hfHeader) < 1:hfHeader=[-1] #kalo gaada hf di header
        if DEBUG:
            print("hai : ", hfHeader)
        headerIndex = h
        for hfIndex in hfHeader:
            if hfIndex > h:
                # index last for header
                headerIndex = hfIndex
        
        if DEBUG:
            print("Header Index", headerIndex, label[headerIndex])
        
        # first batas for footer
        hfFooter = [x for x in hf if bLast < x]
        footerIndex = f
        if len(hfFooter) > 0:
            for hfna in hfFooter:
                if hfna < footerIndex:
                    if DEBUG:
                        print(hfna, 'hfna')
                    footerIndex = hfna
        
        if DEBUG:
            print(label, headerIndex, footerIndex)
            print("Footer Index", footerIndex, label[footerIndex])
            # print(label, headerIndex, footerIndex)

        hasil = ""
        # if DEBUG:
        #     print(teksBaris)
        # print(teks)
        # exit()
        for idx in range(headerIndex+1,footerIndex+1):

            # print(idx, iTeks)

            # if DEBUG:
                # print(label[(idx+headerIndex+1)], "-", teks[iTeks], "|", idx+headerIndex+2)
            
            # if(label[(idx+headerIndex+1)] == "" or 'b' in label[(idx+headerIndex+1)]):
            if DEBUG:
                print('a ',teks[idx])
                print('b ',teks[teksBaris[idx][0]])
            if idx == footerIndex:
                hasil+=teks[teksBaris[idx][0]]
            else:
                hasil+=teks[teksBaris[idx][0]]+"\n"

        return hasil
    except Exception as e:
        print(str(e))
        # print(label)
        print("Gak ada body cuy di file, jadi ga dimasukin", fileName)
        
        return "notfoundbody"