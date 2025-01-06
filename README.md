## PROGRAM KASIR RESTORAN ##

```
def display_menu(menu):
    print("==================== Daftar Menu =================")
    for item, price in menu.items():
        print(f"Daftar Menu: {item}\t Harga : {price}")
    print("Pembelian diatas Rp100.000,- mendapatkan diskon 15%")
    print("===================================================")

def calculate_total(menu, item, quantity):
    if item not in menu:
        raise ValueError("Menu tidak tersedia.")

    subtotal = quantity * menu[item]
    discount = subtotal * 0.15 if subtotal > 100000 else 0
    total = subtotal - discount
    return subtotal, discount, total

def display_payment_details(item, quantity, subtotal, discount, total):
    print("================== Detail Pembayaran ===============")
    print(f"Menu yang dipesan        : {item}")
    print(f"Jumlah yang dipesan      : {quantity}")
    print(f"Total biaya              : {subtotal}")
    print(f"Diskon                   : {discount}")
    print(f"Total yang harus dibayar : {total}")

def main():
    menu = {
        "fried chicken": 15000,
        "burger queen": 25000,
        "saingan goreng": 10000,
        "jasmine tea": 5000,
        "ice coca cola": 12000
    }

    display_menu(menu)

    try:
        item = input("Pilih Menu : ").strip().lower()
        quantity = int(input("Jumlah Pesanan : "))
        subtotal, discount, total = calculate_total(menu, item, quantity)
        display_payment_details(item, quantity, subtotal, discount, total)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

```
## PENJELASANNYA ##

```
display_menu
Menampilkan daftar menu beserta harga dan informasi tentang diskon 15% untuk pembelian di atas Rp100.000.

calculate_total
Menghitung total biaya berdasarkan menu yang dipilih dan jumlah pesanan. Jika total biaya lebih dari Rp100.000, diskon 15% diterapkan.

display_payment_details
Menampilkan detail pembayaran seperti menu yang dipilih, jumlah pesanan, total biaya sebelum dan sesudah diskon.

main
Fungsi utama program:

Menampilkan menu menggunakan display_menu.
Meminta input dari pengguna (menu dan jumlah pesanan).
Menghitung total biaya dan diskon dengan calculate_total.
Menampilkan rincian pembayaran menggunakan display_payment_details.
Menangani error jika pengguna memilih menu yang tidak ada.
```
## Alur Program ##

```
Daftar menu ditampilkan.
Pengguna memilih menu dan jumlah pesanan.
Total biaya dihitung:
Jika > Rp100.000 → diskon 15%.
Jika ≤ Rp100.000 → tanpa diskon.
Detail pembayaran ditampilkan.
Contohnya:
Jika pengguna memilih "fried chicken" sebanyak 10:

Subtotal: 10 × Rp15.000 = Rp150.000
Diskon: 15% dari Rp150.000 = Rp22.500
Total: Rp150.000 - Rp22.500 = Rp127.500
Hasil ini akan ditampilkan dalam format rapi.
```
