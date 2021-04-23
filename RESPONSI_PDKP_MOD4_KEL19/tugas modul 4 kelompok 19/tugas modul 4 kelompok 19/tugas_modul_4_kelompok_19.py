import string

abjad = string.printable


def enkrip (pesan) :
    global abjad
    key = 19
    cipher = ''
    for i in pesan :
        if i in abjad :
            k = abjad.find(i)
            k = (k + key) %100
            cipher = cipher+abjad[k]
        else :
            cipher = cipher + i
        
    return cipher

def dekrip (cipher) :
    global abjad
    key= 19
    pesan = ''
    for i in cipher :
        if i in abjad :
            k = abjad.find(i)
            k = (k - key) %100
            pesan = pesan+abjad[k]
        else :
            pesan = pesan + i 
    
    return pesan

def menu():
    while True:
        print()
        print("================")
        print("    MENU  ")
        print("================")
        print("1. Enkripsi ")
        print("2. Dekripsi")
        print("3. Exit")
        print("================")

        pilihan = int(input("Pilih Menu = "))
        print("================")

        if pilihan == 1 :
            pesan = input('Masukkan kalimat = ')
            print('Hasil = ', enkrip(pesan))
            print("================")
            print()
            print("Kembali ke Menu Awal.....")
        elif pilihan == 2 :
            cipher = input('Masukkan kalimat = ')
            print('Hasil = ', dekrip(cipher))
            print("================")
            print()
            print("Kembali ke Menu Awal.....")
        elif pilihan == 3 :
            break 
        else :
            print("Error: pastikan anda memasukan angka yang benar !")

def main():
    menu()

if __name__ == '__main__':
    main()
