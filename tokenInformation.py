import re

'''
Token Information
'''
def isTokenInfoTeks():
    # inisiasi tag token informasi
    nama = "Teks"

    rules = [
        r"(^|\s)([a-z]+(\s|\n))+"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoAlphanumerik():
    # inisiasi tag token informasi
    nama = "Alphanumerik"

    rules = [
        r"(^|\s)([a-z0-9.]+(\s|\n))+"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoMengandungDigitdanPersen():
    # inisiasi tag token informasi
    nama = "MengandungDigitdanPersen"

    rules = [
        r"(%\d+|% \d+|\d+%|\d+%|\d+ %|[(]%[)]|[(]\d+%[)])"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoNPWPTeks():
    # inisiasi tag token informasi
    nama = "NPWPTeks"

    rules = [
        "npwp",
        "(no npwp)|(npwp no)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoNPWPFormat():
    # inisiasi tag token informasi
    nama = "NPWPFormat"

    rules = [
        r"(0[1-9].\d{3}.\d{3}.\d{1}-\d{3}.\d{3})"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

# date,tanggal,tgl,time,jam,waktu,close,closed,namahari
def isTokenInfoTanggalWaktuTeks():
    # inisiasi tag token informasi
    nama = "TanggalWaktuTeks"

    rules = [
        "(senin|selasa|rabu|kamis|jumat|sabtu|minggu|sun(day)?|mon(day)?|tue(sday)?|wed(nesday)?|thu(rsday)?|fri(day)?|sat(urday)?)?!(\w)",
        r"(trx(\s?date))",
        r"(date(\s?time)?)",
        r"(tgl|tanggal)(.\s?)?(pkp|pengukuhan)?",
        r"(time|jam|waktu|close|closed)?!(\w)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoTanggalWaktu():
    # inisiasi tag token informasi
    nama = "TanggalWaktu"

    separator = r"((\/)|[.]|\s|-)" # separator / . - space or no separator
    # separator = r"((\/)|[.]|-)" # separator / . - or no separator

    tanggal = "(([0-2][0-9]|[0-9])|(3)[0-1])"
    bulan = "((((0)?[0-9])|((1)[0-2]))|((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)|(Jan(uari)?|Feb(uari)?|Mar(et)?|Apr(il)?|Mei|Jun(i)?|Jul(i)?|Agu(stus)?|Sep(tember)?|Okt(ober)?|Nov(ember)?|Des(ember)?)))"
    tahun = r"((20)\d{2}|\d{2})"
    waktu = r"(\d{2}:\d{2}(:\d{2})?)"

    rules = [
        "("+tanggal+separator+bulan+separator+tahun+")",
        waktu
    ]

    rule = '|'.join([rule for rule in rules])
    rule = r"(^|\s)("+rule+")(\n|\s|$)"
    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoPrefixPerusahaan():
    # inisiasi tag token informasi
    nama = "PrefixPerusahaan"

    rules = [
        "cv([.])?",
        r"(^)?pt(\s)?[.](\s\w|\w)+",
        "company name",
        "company"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoPrefixLokasi():
    # inisiasi tag token informasi
    nama = "PrefixLokasi"

    rules = [
        "^(block|blok|kavling|kav|komp|komplek|outlet|kawasan|mall| jl |jalan|jln|plaza|gd|gedung|perum|perumahan)([.])?",
        r"^((lt|lantai)([.]|\s)?(\d+)?)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoWebsiteTeks():
    # inisiasi tag token informasi
    nama = "WebsiteTeks"

    rules = [
        "(website|visit our website|we can deliver now|info lowongan|shop online|lowongan|click|klik)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoWebsiteFormat():
    # inisiasi tag token informasi
    nama = "WebsiteFormat"

    rules = [
        # Jieun we
        r"((https?):\/\/)(www.)?[a-z0-9]+(\.[a-z]{2,}){1,3}(#?\/?[a-zA-Z0-9#]+)*\/?(\?[a-zA-Z0-9-_]+=[a-zA-Z0-9-%]+&?)?$"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoEmailTeks():
    # inisiasi tag token informasi
    nama = "EmailTeks"

    rules = [
        "(email|e-mail|info|customercare|customer care|kontak)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoEmailFormat():
    # inisiasi tag token informasi
    nama = "EmailFormat"

    rules = [
        r"[\w\.-]+@([\w-]+\.)+[\w-]{2,4}"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

# Info/Jenis Pembelian
def isTokenInfoPembelianTeks():
    # inisiasi tag token informasi
    nama = "PembelianTeks"

    rules = [
        "(take|away|take away|takeout|take out|dine in|dine|meja|pembayaran|table|dining|area|room|sale|ruangan|sales include)"
        r"(^|\s)bar(\n|\s)[:#]"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoKodeTeks():
    # inisiasi tag token informasi
    nama = "KodeTeks"

    rules = [
        r"((^|\s)no([.]|\n|\s)|nota|number|nomor| id |kode|transaksi|serial)",
        r"#(\s)*(\d|\w)+",
        r"((\d|\w)+[/:](\d|\w)+)[/:]"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

# Pegawai atau Kasir
def isTokenInfoPegawaiTeks():
    # inisiasi tag token informasi
    nama = "PegawaiTeks"

    rules = [
        "(kasir|cashier|staff|admin|kassa|counter|operator|waiter|shift|crew|open|host)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoOrderTeks():
    # inisiasi tag token informasi
    nama = "OrderTeks"

    rules = [
        "(order|order by|order no|no order|order id)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoTerimaKasihTeks():
    # inisiasi tag token informasi
    nama = "TerimaKasihTeks"

    rules = [
        "(kamsahamnida|terima kasih|terimakasih|thankyou|thank you|kunjungan|atas kunjungan anda|kunjungannya)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoTelpTeks():
    # inisiasi tag token informasi
    nama = "TelpTeks"

    rules = [
        r"(hotline|sms|(^|\s)wa(\n|\s)|hubungi|layanan|call|customer care|antar|keluhan|konsumen|delivery|fax|hub|informasi|info|pesan|phone|telp|delivery order|kemitraan|layanan|pesan antar|konsumen|layanan pesan antar|customer care|pusat informasi|saran / keluhan|saran dan kritik|saran dan keluhan|no hp|no telp|kritik & saran)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoTelpFormat():
    # inisiasi tag token informasi
    nama = "TelpFormat"

    rules = [
        r"08\d{9,10}",
        r"08\d{1,2}(\s\d{4}){2}",
        r"08\d{1}(\s\d{3}){3}",
        r"021([-]|\s)\d{3}[.]\d{4}",
        r"022([-]|\s)\d{3}[.]\d{4}",
        r"021([-]|\s)\d{7}",
        r"022([-]|\s)\d{7}",
        r"[(]022[)](\s)?\d{7,8}",
        r"[(]021[)](\s)?\d{7,8}"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoMemberTeks():
    # inisiasi tag token informasi
    nama = "MemberTeks"

    rules = [
        r"(poin(t(s)?)?|member|point|khusus pengguna)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoPelangganTeks():
    # inisiasi tag token informasi
    nama = "PelangganTeks"

    rules = [
        r"(customer|cust|guest|pax|tamu|umum|nama|name|pelanggan)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoPajakTeksFooter():
    # inisiasi tag token informasi
    nama = "PajakTeksFooter"

    rules = [
        r"(harga (diatas |di atas )?sudah termasuk)|(pajak|harga termasuk|include ppn|termasuk ppn|(^|\s)pb(\n|\s)|barang kena pajak|price are subject to taxes)|barang yang"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoSocmedTeks():
    # inisiasi tag token informasi
    nama = "SocmedTeks"

    rules = [
        r"(facebook|twitter|instagram|(^|\s)fb(\n|\s)|(^|\s)ig(\n|\s)|follow|update|info promo|add di|lebih banyak info|info promosi|add line|di line)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoDukunganTeks():
    # inisiasi tag token informasi
    nama = "DukunganTeks"

    rules = [
        r"(dukung|brand indonesia|lokal|kebanggaan|dukung brand|brand lokal|dukung brand lokal indonesia)(\s|\n)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoFooterTeks():
    # inisiasi tag token informasi
    nama = "FooterTeks"

    rules = [
        r"(^|\s)(all prices|rayakan|wifi|simpan bukti pembelian|minimal pesanan \d+ box|powered by|daftar jadi member|pembelian anda gratis|to redeem|refer to website|presettlement|this is presettlement rcpt|donation for|please re-check your item|follow us for|tori fingers|by olsera POS|bon ini merupakan bukti|dapatkan info lowongan|dapatkan penawaran khusus|we are looking for|notes|ditunggu kedatangannya kembali|kami senang melayani|lebih banyak info)(\s|\n|$)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

# PaymentRef
def isTokenInfoInfoReceiptTeks():
    # inisiasi tag token informasi
    nama = "InfoReceiptTeks"

    rules = [
        r"(invoice|penjualan|ref\n|bukti|sales|bill|receipt|payment ref|receipt number|receipt no|penjualan tunai|bukti bayar|purchase|transaksi|transaction|vers|versi|version)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenNomer():
    # inisiasi tag token informasi
    nama = "Nomer"

    rules = [
        r"(\s|^)[0][1-9]{1,5}",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenDigit():
    # inisiasi tag token informasi
    nama = "Digit"

    rules = [
        r"((\s|^)[1-9][0-9]{0,2}(\s|\n))",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenLebihDariTigaDigit():
    # inisiasi tag token informasi
    nama = "LebihDariTigaDigit"

    rules = [
        r"(\s|^)[1-9][0-9]{3,6}(\s|\n)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenLebihDariTujuhDigit():
    # inisiasi tag token informasi
    nama = "LebihDariTujuhDigit"

    rules = [
        r"(\s|^)[1-9][0-9]{7,}(\s|\n)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenMengandungSlash():
    # inisiasi tag token informasi
    nama = "MengandungSlash"

    rules = [
        r"(\s|^)(\w+|\d+)[/](\w+|\d+)(\s|\n)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenMengandungNumerikdanPagar():
    # inisiasi tag token informasi
    nama = "MengandungNumerikdanPagar"

    rules = [
        r"(\s|^)([#]\d+)(\s|\n)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenMengandungDigitdanSatuan():
    # inisiasi tag token informasi
    nama = "MengandungDigitdanSatuan"

    rules = [
        r"(\s|^)[@ea](\s)?[1-9]{1}[oi0-9]{0,2}(\s*[,.]\s*([oi0-9]{3}))+(\s|\n)*",
        r"((\s|^)[@ea](\s)?[1-9][0-9]{0,2}(\s|\n))",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenMengandungDigitdanKoma():
    # inisiasi tag token informasi
    nama = "MengandungDigitdanKoma"

    rules = [
        r"(\s|^)[1-9]{1}[oi0-9]{0,2}(\s*[,]\s*([oi0-9]{3}))+(\s|\n)*",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenMengandungDigitdanTitik():
    # inisiasi tag token informasi
    nama = "MengandungDigitdanTitik"

    rules = [
        r"(\s|^)[1-9]{1}[oi0-9]{0,2}(\s*[.]\s*([oi0-9]{3}))+(\s|\n)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenMengandungDigitdanPagar():
    # inisiasi tag token informasi
    nama = "MengandungDigitdanPagar"

    rules = [
        r"(\s|^)#(\s)*[1-9]{1}[0-9]{0,2}(\s|\n)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenAngkaNol():
    # inisiasi tag token informasi
    nama = "AngkaNol"

    rules = [
        r"(\s|^)0(\s|\n)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }
    
def isTokenMengandungNegatifDigitdanStrip():
    # inisiasi tag token informasi
    nama = "MengandungNegatifDigitdanStrip"

    rules = [
        r"(\s|^)(((-)(\s)*([1-9]{1}[0-9]{0,}))|(([1-9]{1}[0-9]{0,})(\s)*(-)))(\s|\n)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }
    
def isTokenMengandungDigitdanTitikKoma():
    # inisiasi tag token informasi
    nama = "MengandungDigitdanTitikKoma"

    rules = [
        r"(\s|^)[1-9]{1}[0-9]{0,2}([.](\d{3}))+[,](\d{2})(\s|\n)",
        r"(\s|^)[1-9]{1}[0-9]{0,2}([,](\d{3}))+[.](\d{2})(\s|\n)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoPOS():
    # inisiasi tag token informasi
    nama = "POS"

    rules = [
        r"((^|\s)po(\d+)?(\n|\s)|(^|\s)pos(\d+)?(\n|\s)|title)",
        r"((^|\s)[pf][ou0][s5](\s)?(\d+)?)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoHeaderItemTeks():
    # inisiasi tag token informasi
    nama = "HeaderItemTeks"

    rules = [
        r"(description|item|qty|price|amount|disc|subtotal|jumlah|harga|satuan|code)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

''' 
Buat body biasanya
'''
def isTokenInfoHematTeks():
    # inisiasi tag token informasi
    nama = "HematTeks"

    rules = [
        r"(saving|anda hemat|total saving|total savings)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoPajakTeks():
    # inisiasi tag token informasi
    nama = "PajakTeks"

    rules = [
        r"(tax|pb1|pb 1|(^|\s)pb(\s|$)|pajak|ppn|vat|gst|tx|pjk|pajak resto|pjk resto|dasar pengenaan pajak)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoPrefixMataUang():
    # inisiasi tag token informasi
    nama = "PrefixMataUang"

    rules = [
        r"(Rp([.])?|IDR)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoKantong():
    # inisiasi tag token informasi
    nama = "Kantong"

    rules = [
        r"(kresek|plastik|sb size|kantong plastik|kk kantong|(^|\s)bag(\n|\s)|shopping bag|shipping bag|plastic|plastic bag)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenKataIdentik():
    # inisiasi tag token informasi
    nama = "KataIdentik"

    rules = [
        r"(paket spesial|paket|original|warna|regular|reguler|cetak|ukuran|(^|\s)uk(\n|\s)|size|polos|level(\s)*\d)",
        r"(merah|hitam|htm|pth|biru|kuning|putih|abu|hijau)",
        r"(red|black|gold|blue|yellow|white|grey|green)",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoVolumeTeks():
    # inisiasi tag token informasi
    nama = "VolumeTeks"

    rules = [
        # r"(gram|liter|bsr|besar|sedang|kecil|small|medium|large|xl)(\n|$|\s)",
        r"(\s)+([1-9][oi0-9]{0,2})(\s)?(r|g|ml|gr|kg|gram|liter|lt|bsr|besar|sedang|kecil|small|medium|large|xl)(\n|$|\s)",
        r"(^|\s|[(])+(ml|gr|kg|gram|liter|bsr|besar|sedang|kecil|small|medium|large|xxl|xl|xs)(\n|$|\s|[)])",
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoTotalTeks():
    # inisiasi tag token informasi
    nama = "TotalTeks"

    rules = [
        r"^((total( yang harus dibayar| incl| sales)?)|balance due|harga jual|cash|tl|net total)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoSubTotalTeks():
    # inisiasi tag token informasi
    nama = "SubTotalTeks"

    rules = [
        r"(subtotal|total sum|gross total|sub total|checks paid)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoPembulatanTeks():
    # inisiasi tag token informasi
    nama = "PembulatanTeks"

    rules = [
        r"(rounding|pembulatan)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoServiceTeks():
    # inisiasi tag token informasi
    nama = "ServiceTeks"

    rules = [
        r"(service(s)?|servis)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoTotalKuantitasTeks():
    # inisiasi tag token informasi
    nama = "TotalKuantitasTeks"

    rules = [
        r"(total qty|total piece|total pieces|totaly qty|quantity purchased|qty total|qty)([:])?(\d*)?"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoPembayaranTeks():
    # inisiasi tag token informasi
    nama = "PembayaranTeks"

    rules = [
        r"(bayar|kas outlet|pembayaran|received|taken|tunai|cash|payment taken|cash tendered|payment)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoTotalItemTeks():
    # inisiasi tag token informasi
    nama = "TotalItemTeks"

    rules = [
        r"(number|totaly|item(s)?|total item(s)?|item(s)? purchased)([:])?(\d+)?"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoDiscount1Teks():
    # inisiasi tag token informasi
    nama = "Discount1Teks"

    rules = [
        r"(free|hemat|get|but|disc toko|disc("+isTokenInfoMengandungDigitdanPersen()["rule"]+")?)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoDiscount2Teks():
    # inisiasi tag token informasi
    nama = "Discount1Teks"

    rules = [
        r"(disc|discount|diskon|total discount|total diskon|total disc|disc total|discount price|disc product|disc("+isTokenInfoMengandungDigitdanPersen()["rule"]+"))"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoOtherPaymentTeks():
    # inisiasi tag token informasi
    nama = "OtherPaymentTeks"

    rules = [
        r"((^|\s)ovo(\n|\s)|voucher|debit card|debit non|non tunai|kupon|card payment)"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }

def isTokenInfoKembalianTeks():
    # inisiasi tag token informasi
    nama = "KembalianTeks"

    rules = [
        r"(total change|uang kembali|change back|change due|cash change|change cash|change given|change|kembali|kembalian|(^|\s)(st|ch|ca)(\s|\n|$))"
    ]

    rule = '|'.join([rule for rule in rules])

    return {
        "tag" : nama,
        "rule" : rule
    }
