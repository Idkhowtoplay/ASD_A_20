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

    def read(self, file):
        print("\n=== DATA KELUARGA ===")
        if not self.members:
            print("Belum ada data.")
        for p in self.members.values():
            print(f"Nama: {p.name}, Parent1: {p.parent1}, Parent2: {p.parent2}")

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


    def search(self, name):
        if name in self.members:
            p = self.members[name]
            print("\n=== DATA DITEMUKAN ===")
            print(f"Nama: {p.name}")
            print(f"Parent1: {p.parent1}")
            print(f"Parent2: {p.parent2}")
        else:
            print("Data tidak ditemukan")


    def get_children(self, name):
        children = []
        for p in self.members.values():
            if p.parent1 == name or p.parent2 == name:
                children.append(p.name)
        return children

    def get_siblings(self, name):
        if name not in self.members:
            return []

        target = self.members[name]
        siblings = []

        for p in self.members.values():
            if p.name != name:
                if (p.parent1 == target.parent1 and p.parent1 != "-") or \
                   (p.parent2 == target.parent2 and p.parent2 != "-"):
                    siblings.append(p.name)
        return siblings

    def show_family(self, name, level=0):
        if name == "-" or name not in self.members:
            return

        print("  " * level + f"- {name}")
        person = self.members[name]

        self.show_family(person.parent1, level + 1)
        self.show_family(person.parent2, level + 1)

    def show_descendants(self, name, level=0):
        print("  " * level + f"- {name}")
        children = self.get_children(name)

        for child in children:
            self.show_descendants(child, level + 1)


def main():
    file = "bleh.csv"
    ft = FamilyTree()
    ft.load_from_file(file)

    while True:
        print("\n=== MENU FAMILY TREE ===")
        print("1. Tambah Data")
        print("2. Lihat Semua Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            name = input("Nama: ")
            p1 = input("Parent 1 (isi '-' jika tidak ada): ")
            p2 = input("Parent 2 (isi '-' jika tidak ada): ")
            ft.create(name, p1, p2, file)

        elif pilihan == "2":
            ft.read(file)

        elif pilihan == "3":
            name = input("Nama: ")
            p1 = input("Parent1 baru: ")
            p2 = input("Parent2 baru: ")
            ft.update(name, p1, p2, file)

        elif pilihan == "4":
            name = input("Nama: ")
            ft.delete(name, file)

        elif pilihan == "5":
            name = input("Nama: ")
            ft.search(name)

        elif pilihan == "10":
            print("Keluar program...")
            break

        else:
            print("Pilihan tidak valid!")

main()
