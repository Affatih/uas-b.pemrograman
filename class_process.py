# class_process.py

def calculate_total(beli, jumlah, menu):
    bayar = jumlah * menu[beli]
    if bayar > 100000:
        diskon = bayar * 15 / 100
        total = bayar - diskon
    else:
        total = bayar
    return bayar, total