class Person:
    def __init__(self, name, parent1, parent2):
        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2
        

class FamilyTree:
    def __init__(self):
        self.head = None

    def create(self, name, parent1, parent2, file):
        with open(file, "w") as file:
            person = Person(name, parent1, parent2)
            file.write(f"{person.name}, {person.parent1}, {person.parent2}\n")

    def read(self, file):
        try:
            with open(file, "r") as f:
                data = f.readlines()
                print("\n=== DATA KELUARGA ===")
                for line in data:
                    name, p1, p2 = line.strip().split(",")
                    print(f"Nama: {name}, Parent1: {p1}, Parent2: {p2}")
        except FileNotFoundError:
            print("File belum ada")

    def delete(self, file,  target_name):
        try:
            with open(file, "r") as f:
                data = f.readlines()

            with open(file, "w") as f:
                for line in data:
                    name, p1, p2 = line.strip().split(",")

                    if name != target_name:
                        f.write(line)

            print("Data berhasil dihapus")

        except FileNotFoundError:
            print("File belum ada")

    def update(self, file, target_name, new_p1, new_p2):
        try:
            with open(file, "r") as f:
                lines = f.readlines()

            found = False
            with open(file, "w") as f:
                for line in lines:
                    name, p1, p2 = line.strip().split(",")
                    if name == target_name:
                        f.write(f"{name},{new_p1},{new_p2}\n")
                        found = True
                    else:
                        f.write(line)

            if found:
                print(f"Data {target_name} berhasil diperbarui.")
            else:
                print(f"Data {target_name} tidak ditemukan.")
        except FileNotFoundError:
            print("File tidak ditemukan.")

      
file = "bleh.csv"
ft = FamilyTree()
ft.update(file, "Alaya", "lll", "00")   
ft.delete(file,"Alaya")
