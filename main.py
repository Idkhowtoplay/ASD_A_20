from tes import FamilyTree


def main():

    file = "bleh.csv"

    ft = FamilyTree()

    ft.load_from_file(file)

    while True:

        print("\n========= MENU FAMILY TREE ========= ")
        print("1. Tambah Data")
        print("2. Lihat Semua Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Cari Data")
        # print("6. Cari Saudara")
        # print("7. Tampilkan Silsilah")
        # print("8. Tampilkan Keturunan")
        print("9. Keluar")

        pilihan = input("Pilih menu: ")

        # MENU 1
        if pilihan == "1":

            name = input("Nama: ")
            p1 = input("Ayah (- jika tidak ada): ")
            p2 = input("Ibu (- jika tidak ada): ")

            ft.create(name, p1, p2, file)

        # MENU 2
        elif pilihan == "2":

            ft.read()

         # MENU 3
        elif pilihan == "3":

            name = input("Nama: ")

            p1 = input("Ayah baru (- jika tidak ada): ")
            p2 = input("Ibu baru (- jika tidak ada): ")

            ft.update(name, p1, p2, file)


        # MENU 4
        elif pilihan == "4":

            name = input("Nama: ")

            ft.delete(name, file)

        # MENU 5
        elif pilihan == "5":

            name = input("Nama yang dicari: ")

            ft.search(name)

        # # MENU 6
        # elif pilihan == "6":

        #     name = input("Nama: ")

        #     siblings = ft.get_siblings(name)

        #     if siblings:

        #         print(
        #             "Saudara:",
        #             ", ".join(siblings)
        #         )

        #     else:

        #         print(
        #             "Tidak ada saudara ditemukan."
        #         )

        # # MENU 7
        # elif pilihan == "7":

        #     name = input("Nama: ")

        #     print("\n=== SILSILAH KELUARGA ===")

        #     ft.show_family(name)

        # # MENU 8
        # elif pilihan == "8":

        #     name = input("Nama: ")

        #     print("\n=== KETURUNAN ===")

        #     ft.show_descendants(name)

        # MENU 9
        elif pilihan == "9":

            print("Keluar program...")
            break

        else:

            print("Pilihan tidak valid!")


main()
