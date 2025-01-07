# class_view.py

def display_menu(menu):
    print("==================== Daftar Menu =================")
    for item, price in menu.items():
        print("Daftar Menu: ", item, "\t Harga : ", price)
    print("Pembelian diatas Rp100.000,- mendapatkan diskon 15%")
    print("===================================================")

def display_payment_details(beli, jumlah, bayar, total):
    print("================== Detail Pembayaran ===============")
    print("Menu yang dipesan        : ", beli)
    print("Jumlah yang dipesan       : ", jumlah)
    print("Total biaya              : ", bayar)
    print("Total yang harus dibayar : ", total)