# --- Modulo per le ricette mediche ---

class Ricetta:
    # --- Costruttore ---
    def __init__(self, id: int, nome_paziente: str, cognome_paziente: str, farmaco: str, dose: float):
        self.id = id
        self.__nome_paziente = nome_paziente
        self.__cognome_paziente = cognome_paziente
        self.farmaco = farmaco
        self.dose = dose

    # --- Getter/setter ---
    @property
    def nome_paziente(self):
        return self.__nome_paziente
    @nome_paziente.setter
    def set_nome_paziente(self, nuovo_nome):
        self.__nome_paziente = nuovo_nome

    @property
    def cognome_paziente(self):
        return self.__cognome_paziente
    @cognome_paziente.setter
    def set_cognome_paziente(self, nuovo_cognome):
        self.__cognome_paziente = nuovo_cognome

     # --- Rappresentazione leggibile ---
    def __str__(self):
        return (f"ID: {self.id} | Paziente: {self.nome_paziente} {self.cognome_paziente} "
                f"| Farmaco: {self.farmaco} | Dose: {self.dose}")

    # --- Serializzazione: oggetto → dizionario (per scrivere su file) ---
    def to_dict(self):
        return {
            "id":               self.id,
            "nome_paziente":    self.nome_paziente,
            "cognome_paziente": self.cognome_paziente,
            "farmaco":          self.farmaco,
            "dose":             self.dose
        }

    # --- Deserializzazione: dizionario → oggetto (dopo lettura da file) ---
    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id               = int(d["id"]),
            nome_paziente    = d["nome_paziente"],
            cognome_paziente = d["cognome_paziente"],
            farmaco          = d["farmaco"],
            dose             = d["dose"]
        )