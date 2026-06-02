class Person:
    def __init__(self, name, parent1, parent2):
        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2


class Node:
    def __init__(self, person):
        self.person = person
        self.next = None


class FamilyTree:
    def __init__(self):
        self.head = None
        self.history = []  # Stack

    def find(self, name):
        current = self.head

        while current:
            if current.person.name == name:
                return current

            current = current.next

        return None

    def load_from_file(self, file):
        try:
            with open(file, "r") as f:
                for line in f:
                    data = line.strip().split(",")

                    if len(data) != 3:
                        continue

                    name, p1, p2 = data

                    person = Person(name, p1, p2)
                    new_node = Node(person)

                    if self.head is None:
                        self.head = new_node
                    else:
                        current = self.head

                        while current.next:
                            current = current.next

                        current.next = new_node

        except FileNotFoundError:
            pass

    def save_all(self, file):
        with open(file, "w") as f:
            current = self.head

            while current:
                p = current.person
                f.write(f"{p.name},{p.parent1},{p.parent2}\n")
                current = current.next

    def create(self, name, parent1, parent2, file):
        if self.find(name):
            print("Nama sudah ada!")
            return

        person = Person(name, parent1, parent2)
        new_node = Node(person)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        self.history.append(("create", name))

        self.save_all(file)

        print("Data berhasil ditambahkan!")

    def display_tree(self, person):
        ayah_node = self.find(person.parent1)
        ibu_node = self.find(person.parent2)

        kakek_ayah = "-"
        nenek_ayah = "-"
        kakek_ibu = "-"
        nenek_ibu = "-"

        if ayah_node:
            kakek_ayah = ayah_node.person.parent1
            nenek_ayah = ayah_node.person.parent2

        if ibu_node:
            kakek_ibu = ibu_node.person.parent1
            nenek_ibu = ibu_node.person.parent2

        print(f"Anak: {person.name}")
        print(f"├── Ayah: {person.parent1}")
        print(f"│   ├── Kakek: {kakek_ayah}")
        print(f"│   └── Nenek: {nenek_ayah}")
        print(f"└── Ibu: {person.parent2}")
        print(f"    ├── Kakek: {kakek_ibu}")
        print(f"    └── Nenek: {nenek_ibu}")
        print("-" * 35)

    def count_data(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def read(self):
        print("\n=== POHON KELUARGA ===")

        if self.head is None:
            print("Belum ada data.")
            return

        per_page = 2
        shown = 0

        current = self.head
        total = self.count_data()

        while current:
            self.display_tree(current.person)

            shown += 1

            if shown % per_page == 0 and shown < total:
                lanjut = input(
                    f"Tampil {shown}/{total} data. "
                    "Tekan Enter untuk lanjut "
                    "(atau ketik 'q' untuk berhenti): "
                )

                if lanjut.lower() == "q":
                    print("Kembali ke menu utama.")
                    return

            current = current.next

    def update(self, name, new_p1, new_p2, file):
        node = self.find(name)

        if node:
            old_p1 = node.person.parent1
            old_p2 = node.person.parent2

            self.history.append(
                ("update", name, old_p1, old_p2)
            )

            node.person.parent1 = new_p1
            node.person.parent2 = new_p2

            self.save_all(file)

            print("Data berhasil diupdate!")
        else:
            print("Data tidak ditemukan!")

    def delete(self, name, file):
        current = self.head
        prev = None

        while current:

            if current.person.name == name:

                self.history.append(
                    (
                        "delete",
                        current.person.name,
                        current.person.parent1,
                        current.person.parent2
                    )
                )

                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                self.save_all(file)

                print("Data berhasil dihapus!")
                return

            prev = current
            current = current.next

        print("Data tidak ditemukan!")

    def search(self, keyword):
        current = self.head
        found = False

        while current:

            if keyword.lower() in current.person.name.lower():
                self.display_tree(current.person)
                found = True

            current = current.next

        if not found:
            print("Data tidak ditemukan!")

    def undo(self, file):
        if not self.history:
            print("Tidak ada riwayat!")
            return

        action = self.history.pop()

        if action[0] == "create":
            self.delete(action[1], file)

            if self.history:
                self.history.pop()

        elif action[0] == "update":
            node = self.find(action[1])

            if node:
                node.person.parent1 = action[2]
                node.person.parent2 = action[3]

        elif action[0] == "delete":

            person = Person(
                action[1],
                action[2],
                action[3]
            )

            new_node = Node(person)

            if self.head is None:
                self.head = new_node
            else:
                current = self.head

                while current.next:
                    current = current.next

                current.next = new_node

        self.save_all(file)

        print("Undo berhasil!")


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
        print("5. Cari Data")
        print("6. Undo")
        print("7. Keluar")

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
            name = input("Nama yang ingin dihapus: ")
            ft.delete(name, file)

        elif pilihan == "5":
            keyword = input("Cari nama: ")
            ft.search(keyword)

        elif pilihan == "6":
            ft.undo(file)

        elif pilihan == "7":
            print("Keluar program...")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()