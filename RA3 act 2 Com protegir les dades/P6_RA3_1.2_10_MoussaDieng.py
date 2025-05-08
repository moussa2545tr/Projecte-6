class CompteUsuari:
    def __init__(self, email):
        self.__email = email  # Atribut privat

    def set_email(self, nou_email):
        if "@" in nou_email and "." in nou_email:
            self.__email = nou_email
        else:
            print("Email no vàlid")

    def get_email(self):
        return self.__email