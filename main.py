from class_data import menu
from class_process import calculate_total
from class_view import display_menu, display_payment_details

def main():
    display_menu(menu)
    beli = input("Pilih Menu : ")
    jumlah = int(input("Jumlah Pesanan : "))
    
    if beli in menu:
        bayar, total = calculate_total(beli, jumlah, menu)
        display_payment_details(beli, jumlah, bayar, total)
    else:
        print("Menu tidak tersedia.")

if __name__ == "__main__":
    main()
