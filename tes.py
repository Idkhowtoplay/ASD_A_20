class Person:

    def __init__(self, name, parent1="-", parent2="-"):

        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2


class FamilyTree:

    def __init__(self):

        self.members = {}

    # LOAD DATA
    def load_from_file(self, file):

        try:

            with open(file, "r") as f:

                for line in f:

                    data = line.strip().split(",")

                    if len(data) == 3:

                        name, p1, p2 = data

                        self.members[name] = Person(
                            name,
                            p1,
                            p2
                        )

        except FileNotFoundError:

            pass

    # SAVE DATA
    def save_all(self, file):

        with open(file, "w") as f:

            for person in self.members.values():

                f.write(
                    f"{person.name},"
                    f"{person.parent1},"
                    f"{person.parent2}\n"
                )

    # CREATE
    def create(self, name, parent1, parent2, file):

        if name in self.members:

            print("Data sudah ada!")
            return

        self.members[name] = Person(
            name,
            parent1,
            parent2
        )

        self.save_all(file)

        print("Data berhasil ditambahkan!")

    # READ
    def read(self):

        print("\n============== DATA KELUARGA ============== ")

        if not self.members:

            print("Belum ada data.")
            return

        # HEADER TABEL
        print("=" * 45)
        print(f"{'Anak':<15} {'Ayah':<15} {'Ibu':<15}")
        print("=" * 45)

        # ISI TABEL
        for p in self.members.values():

            print(
                f"{p.name:<15} "
                f"{p.parent1:<15} "
                f"{p.parent2:<15}"
            )

        print("=" * 45)

    # UPDATE
    def update(self, name, new_p1, new_p2, file):

        if name in self.members:

            self.members[name].parent1 = new_p1
            self.members[name].parent2 = new_p2

            self.save_all(file)

            print("Data berhasil diupdate!")

        else:

            print("Data tidak ditemukan!")

    # DELETE
    def delete(self, name, file):

        if name in self.members:

            del self.members[name]

            self.save_all(file)

            print("Data berhasil dihapus!")

        else:

            print("Data tidak ditemukan!")

    # SEARCH
    def search(self, name):

        if name in self.members:

            p = self.members[name]

            print("\n=== DATA DITEMUKAN ===")

            print(f"Anak     : {p.name}")
            print(f"Ayah     : {p.parent1}")
            print(f"Ibu      : {p.parent2}")

        else:

            print("Data tidak ditemukan!")

    # CARI ANAK
    def get_children(self, name):

        children = []

        for p in self.members.values():

            if (
                p.parent1 == name
                or
                p.parent2 == name
            ):

                children.append(p.name)

        return children

    # CARI SAUDARA
    def get_siblings(self, name):

        if name not in self.members:

            return []

        target = self.members[name]

        siblings = []

        for p in self.members.values():

            if p.name != name:

                same_parent1 = (
                    p.parent1 == target.parent1
                    and
                    p.parent1 != "-"
                )

                same_parent2 = (
                    p.parent2 == target.parent2
                    and
                    p.parent2 != "-"
                )

                if same_parent1 or same_parent2:

                    siblings.append(p.name)

        return siblings

    # TAMPILKAN SILSILAH
    def show_family(self, name, level=0):

        if (
            name == "-"
            or
            name not in self.members
        ):
            return

        print("  " * level + f"- {name}")

        person = self.members[name]

        self.show_family(
            person.parent1,
            level + 1
        )

        self.show_family(
            person.parent2,
            level + 1
        )

    # TAMPILKAN KETURUNAN
    def show_descendants(self, name, level=0):

        print("  " * level + f"- {name}")

        children = self.get_children(name)

        for child in children:

            self.show_descendants(
                child,
                level + 1
            )
            
