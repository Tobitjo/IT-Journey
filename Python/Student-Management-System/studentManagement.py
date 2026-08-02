class Student:
    def __init__(self, id, first_name, last_name, age, program, email ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.program = program
        self.email = email

    def __str__(self):
        return f"First-name: {self.first_name} | Last-name: {self.last_name} | Age: {self.age} | ID: {self.id} | Program: {self.program} | Email: {self.email}"

def display_menu():
    title = f"{30 *'='}\n Student Management System\n{30 *'='}\n"
    menu = "1. Ajouter un étudiant\n" \
    "2. Afficher les étudiants\n" \
    "3. Rechercher un étudiant\n" \
    "4. Modifier un étudiant"
    "5. Supprimer un étudiant\n" \
    "6. Sauvegarder\n" \
    "7. Quitter\n"
    dispay = title + menu
    return dispay

def main():
    while True:
        print(display_menu())
        input_user = input("Veuillez choisir une opttion (1-6): ")
        if input_user == '1':
            print("Ajouter")
            break
        if input_user == '2':
            
            break
        if input_user == '3':
            print("Rechercher")
            break
        if input_user == '4':
            print("Supprimer")
            break
        if input_user == '5':
            print('Sauvegarder')
            break
        if input_user == '6':
            print("Quitter")
            break

if __name__ =="__main__":
    main()
    