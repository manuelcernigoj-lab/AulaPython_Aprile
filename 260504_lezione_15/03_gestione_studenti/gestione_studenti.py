
class Utente:

    def __init__(self, nome: str, pwd: str):
        self.__nome = nome
        self.__pwd = pwd
    
    # properties
    @property
    def nome(self):
        return self.__nome
    @property
    def pwd(self):
        return self.__pwd
    
    def registrazione(self):
        try:
            with open("credenziali.csv", "r+") as f:
                credenziali = f.read()


        except FileNotFoundError:
            print("File non trovato")

    def login(self):
        pass

    def ins_mod(self):
        pass

    def stampa_aula(self):
        pass

class Admin(Utente):

    def login(self):
        pass

    def reset(self):
        pass

    def log_inventario(self):
        pass
