
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
    
    # setters
    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome
    
    def set_pwd(self, nuova_pwd):
        self.__pwd = nuova_pwd
    
    def registrazione(self):
        try:
            with open("credenziali.csv", "r") as f:
                credenziali = []
                for riga in f:
                    n, p = riga.strip().split(",")
                    credenziali.append((n, p))

        except FileNotFoundError:
            open("credenziali.csv", "w").close()
            credenziali = []
        
        self.set_nome(input("Inserire il nome utente: "))
        nomi = [n for n, p in credenziali]
        if self.nome in nomi:
            print("Utente già presente, effettuare il Login")
        else:
            self.set_pwd(input("Inserire la password: "))
            with open("credenziali.csv", "a") as f:
                f.write(f"{self.nome},{self.pwd}\n")

    def login(self):
        try:
            with open("credenziali.csv", "r") as f:
                credenziali = []
                for riga in f:
                    n, p = riga.strip().split(",")
                    credenziali.append((n, p))

        except FileNotFoundError:
            print("Nessun utente registrato, effettuare la registrazione")
            return False
    
        self.set_nome(input("Inserire il nome utente: "))
        self.set_pwd(input("Inserire la password: "))
    
        if (self.nome, self.pwd) in credenziali:
            print(f"Benvenuto {self.nome}!")
            return True
        else:
            print("Credenziali errate")
            return False
    
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
