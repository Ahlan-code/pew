
    while True:
        print("1. Deret Aritmatika")
        print("2. Deret Geometri")
        print("3. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            a = int(input("Masukkan suku pertama (a): "))
            b = int(input("Masukkan beda antara suku (b): "))
            n = int(input("Masukkan jumlah suku (n): "))

            deret = deret_aritmatika(a, b, n)
            print("Deret Aritmatika:", deret)

        elif pilihan == "2":
            a = int(input("Masukkan suku pertama (a): "))
            r = int(input("Masukkan rasio antara suku (r): "))
            n = int(input("Masukkan jumlah suku (n): "))

            deret = deret_geometri(a, r, n)
            print("Deret Geometri:", deret)

        elif pilihan == "3":
            print("Keluar dari program.")
            break

        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
