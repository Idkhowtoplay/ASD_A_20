class Person:
    def __init__(self, name, parent1, parent2):
        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2


class FamilyTree:
    def __init__(self):
        self.members = {}

    def load_from_file(self, file):
        try:
            with open(file, "r") as f:
                for line in f:
                    name, p1, p2 = line.strip().split(",")
                    self.members[name] = Person(name, p1, p2)
        except FileNotFoundError:
            pass

    def save_all(self, file):
        with open(file, "w") as f:
            for person in self.members.values():
                f.write(f"{person.name},{person.parent1},{person.parent2}\n")

    def create(self, name, parent1, parent2, file):
        self.members[name] = Person(name, parent1, parent2)
        self.save_all(file)
        print("Data berhasil ditambahkan!")

    def read(self):
        print("\n=== POHON KELUARGA (1 LEVEL) ===")

        if not self.members:
            print("Belum ada data.")
            return

        for p in self.members.values():
            print(f"\n{p.name}")
            
            # Ayah
            if p.parent1 != "-":
                print(f"├── Ayah: {p.parent1}")
            else:
                print("├── Ayah: -")

            # Ibu
            if p.parent2 != "-":
                print(f"└── Ibu : {p.parent2}")
            else:
                print("└── Ibu : -")

    def update(self, name, new_p1, new_p2, file):
        if name in self.members:
            self.members[name].parent1 = new_p1
            self.members[name].parent2 = new_p2
            self.save_all(file)
            print("Data berhasil diupdate!")
        else:
            print("Data tidak ditemukan!")

    def delete(self, name, file):
        if name in self.members:
            del self.members[name]
            self.save_all(file)
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")


def main():
    file = "bleh.csv"
    ft = FamilyTree()
    ft.load_from_file(file)

    while True:
        print("\n=== MENU FAMILY TREE ===")
        print("1. Tambah Data")
        print("2. Lihat Semua Data (Tree)")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            name = input("Nama: ")
            p1 = input("Ayah (isi '-' jika tidak ada): ")
            p2 = input("Ibu (isi '-' jika tidak ada): ")
            ft.create(name, p1, p2, file)

        elif pilihan == "2":
            ft.read()

        elif pilihan == "3":
            name = input("Nama: ")
            p1 = input("Ayah baru: ")
            p2 = input("Ibu baru: ")
            ft.update(name, p1, p2, file)

        elif pilihan == "4":
            name = input("Nama: ")
            ft.delete(name, file)

        elif pilihan == "5":
            print("Keluar program...")
            break

        else:
            print("Pilihan tidak valid!")


main()
