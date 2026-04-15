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
            with open(self.file, "r") as f:
                data = f.readlines()
                print("\n=== DATA KELUARGA ===")
                for line in data:
                    name, p1, p2 = line.strip().split(",")
                    print(f"Nama: {name}, Parent1: {p1}, Parent2: {p2}")
        except FileNotFoundError:
            print("File belum ada")

    def delete(self, target_name):
        try:
            with open(self.file, "r") as f:
                data = f.readlines()

            with open(self.file, "w") as f:
                for line in data:
                    name, p1, p2 = line.strip().split(",")

                    if name != target_name:
                        f.write(line)

            print("Data berhasil dihapus")

        except FileNotFoundError:
            print("File belum ada")

        
file = "bleh.csv"
ft = FamilyTree()
ft.create("Alaya", 1, 2, file)
    
