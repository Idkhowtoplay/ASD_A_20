class Person:
    def __init__(
        self,
        anak,
        ayah,
        ibu,
        kakek_ayah,
        nenek_ayah,
        kakek_ibu,
        nenek_ibu
    ):
        self.anak = anak
        self.ayah = ayah
        self.ibu = ibu
        self.kakek_ayah = kakek_ayah
        self.nenek_ayah = nenek_ayah
        self.kakek_ibu = kakek_ibu
        self.nenek_ibu = nenek_ibu


class Node:
    def __init__(self, person):
        self.person = person
        self.next = None


class FamilyTree:
    def __init__(self):
        self.head = None
        self.history = []  # Stack

    def find(self, anak):
        current = self.head

        while current:
            if current.person.anak.lower() == anak.lower():
                return current

            current = current.next

        return None

    def load_from_file(self, file):
        try:
            with open(file, "r") as f:
                for line in f:
                    data = line.strip().split(",")

                    if len(data) != 7:
                        continue

                    person = Person(*data)
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

                f.write(
                    f"{p.anak},"
                    f"{p.ayah},"
                    f"{p.ibu},"
                    f"{p.kakek_ayah},"
                    f"{p.nenek_ayah},"
                    f"{p.kakek_ibu},"
                    f"{p.nenek_ibu}\n"
                )

                current = current.next

    def create(
        self,
        anak,
        ayah,
        ibu,
        kakek_ayah,
        nenek_ayah,
        kakek_ibu,
        nenek_ibu,
        file
    ):
        if self.find(anak):
            print("Data sudah ada!")
            return


        # Validasi nama
        data_nama = [
            anak,
            ayah,
            ibu,
            kakek_ayah,
            nenek_ayah,
            kakek_ibu,
            nenek_ibu
        ]

        for nama in data_nama:
            if any(char.isdigit() for char in nama):
                print("Nama tidak boleh mengandung angka/simbol")
                return

        person = Person(
            anak,
            ayah,
            ibu,
            kakek_ayah,
            nenek_ayah,
            kakek_ibu,
            nenek_ibu
        )

        new_node = Node(person)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        self.history.append(("create", anak))

        self.save_all(file)

        print("Data berhasil ditambahkan!")

    def display_tree(self, p):
        print("\n" + "═" * 55)
        print(f" SILSILAH KELUARGA : {p.anak.upper()} ".center(55, " "))
        print("═" * 55)

        print("\n 👨 [KELUARGA PIHAK AYAH]")
        print(f"    👴 {p.kakek_ayah} ── 👵 {p.nenek_ayah}")
        print("           │")
        print(f"           └── 👨 {p.ayah}")

        print("\n 👩 [KELUARGA PIHAK IBU]")
        print(f"    👴 {p.kakek_ibu} ── 👵 {p.nenek_ibu}")
        print("           │")
        print(f"           └── 👩 {p.ibu}")

        print("\n 👨‍👩‍👦 [KELUARGA INTI]")
        print(f"    👨 {p.ayah} ── 👩 {p.ibu}")
        print("           │")
        print(f"           └── 🧒 {p.anak}")

        print("\n" + "═" * 55)

    def count_data(self):
        total = 0
        current = self.head

        while current:
            total += 1
            current = current.next

        return total

    def read(self):
        if self.head is None:
            print("Belum ada data.")
            return

        total = self.count_data()
        current = self.head

        shown = 0
        per_page = 2

        while current:
            self.display_tree(current.person)

            shown += 1

            if shown % per_page == 0 and shown < total:
                lanjut = input(
                    f"Tampil {shown}/{total} data. "
                    "Tekan Enter untuk lanjut "
                    "(atau q untuk keluar): "
                )

                if lanjut.lower() == "q":
                    return

            current = current.next

    def update(
        self,
        anak,
        ayah,
        ibu,
        kakek_ayah,
        nenek_ayah,
        kakek_ibu,
        nenek_ibu,
        file
    ):
        node = self.find(anak)

        if not node:
            print("Data tidak ditemukan!")
            return

        p = node.person

        self.history.append(
            (
                "update",
                p.anak,
                p.ayah,
                p.ibu,
                p.kakek_ayah,
                p.nenek_ayah,
                p.kakek_ibu,
                p.nenek_ibu
            )
        )

        p.ayah = ayah
        p.ibu = ibu
        p.kakek_ayah = kakek_ayah
        p.nenek_ayah = nenek_ayah
        p.kakek_ibu = kakek_ibu
        p.nenek_ibu = nenek_ibu

        self.save_all(file)

        print("Data berhasil diupdate!")

    def delete(self, anak, file):
        current = self.head
        prev = None

        while current:

            if current.person.anak.lower() == anak.lower():

                p = current.person

                self.history.append(
                    (
                        "delete",
                        p.anak,
                        p.ayah,
                        p.ibu,
                        p.kakek_ayah,
                        p.nenek_ayah,
                        p.kakek_ibu,
                        p.nenek_ibu
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

            if keyword.lower() in current.person.anak.lower():
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

        elif action[0] == "delete":

            self.create(
                action[1],
                action[2],
                action[3],
                action[4],
                action[5],
                action[6],
                action[7],
                file
            )

            if self.history:
                self.history.pop()

        elif action[0] == "update":

            node = self.find(action[1])

            if node:
                p = node.person

                p.ayah = action[2]
                p.ibu = action[3]
                p.kakek_ayah = action[4]
                p.nenek_ayah = action[5]
                p.kakek_ibu = action[6]
                p.nenek_ibu = action[7]

                self.save_all(file)

        print("Undo berhasil!")

    def _get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.person.anak.lower() <= b.person.anak.lower():
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def sort_data(self, file):
        if self.head is None or self.head.next is None:
            print("Data terlalu sedikit untuk diurutkan (minimal butuh 2 data).")
            return

        self.head = self._merge_sort(self.head)
        
        self.save_all(file)
        print("Data berhasil diurutkan berdasarkan nama anak (A-Z)!")
        
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
        print("7. Urutkan Data Anak (A-Z)")
        print("8. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":

            anak = input("Nama Anak       : ")
            ayah = input("Ayah            : ")
            ibu = input("Ibu             : ")
            kakek_ayah = input("Kakek Ayah      : ")
            nenek_ayah = input("Nenek Ayah      : ")
            kakek_ibu = input("Kakek Ibu       : ")
            nenek_ibu = input("Nenek Ibu       : ")

            ft.create(
                anak,
                ayah,
                ibu,
                kakek_ayah,
                nenek_ayah,
                kakek_ibu,
                nenek_ibu,
                file
            )

        elif pilihan == "2":
            ft.read()

        elif pilihan == "3":

            anak = input("Nama Anak yang ingin diupdate: ")

            ayah = input("Ayah baru       : ")
            ibu = input("Ibu baru        : ")
            kakek_ayah = input("Kakek Ayah baru : ")
            nenek_ayah = input("Nenek Ayah baru : ")
            kakek_ibu = input("Kakek Ibu baru  : ")
            nenek_ibu = input("Nenek Ibu baru  : ")

            ft.update(
                anak,
                ayah,
                ibu,
                kakek_ayah,
                nenek_ayah,
                kakek_ibu,
                nenek_ibu,
                file
            )

        elif pilihan == "4":

            anak = input("Nama Keluarga yang ingin dihapus: ")
            ft.delete(anak, file)

        elif pilihan == "5":

            keyword = input("Cari nama Keluarga: ")
            ft.search(keyword)

        elif pilihan == "6":
            ft.undo(file)

        elif pilihan == "7":
            ft.sort_data(file)

        elif pilihan == "8":
            print("Keluar program...")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
