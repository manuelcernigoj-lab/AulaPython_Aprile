# Sistema di Gestione Ricette Mediche

Applicazione a riga di comando per la gestione delle ricette di un medico di base.
Permette di creare, visualizzare, modificare ed eliminare ricette, con salvataggio persistente su file `.csv` o `.txt`.

---

## Struttura del progetto

```
progetto/
├── main.py        # Gestore, menu e avvio
├── ricetta.py     # Modello dati (classe Ricetta)
└── Ricette/       # Cartella dei file dati (creata automaticamente)
    ├── esempio.csv
    └── esempio.txt
```

---

## Funzionalità

- **Visualizza** — stampa tutte le ricette presenti nel file
- **Aggiungi** — inserisce una nuova ricetta con ID automatico
- **Modifica** — aggiorna i campi di una ricetta esistente tramite ID
- **Elimina** — rimuove una ricetta tramite ID

---

## Formato dei dati

Ogni ricetta contiene i seguenti campi:

| Campo | Descrizione |
|---|---|
| `id` | Identificativo univoco (assegnato automaticamente) |
| `nome_paziente` | Nome del paziente |
| `cognome_paziente` | Cognome del paziente |
| `farmaco` | Nome del farmaco prescritto |
| `dose` | Dosaggio (es. `500 mg/die`) |

### CSV
```
id,nome_paziente,cognome_paziente,farmaco,dose
1,Mario,Rossi,Paracetamolo,500 mg/die
```

### TXT (separatore `|`)
```
id|nome_paziente|cognome_paziente|farmaco|dose
1|Mario|Rossi|Paracetamolo|500 mg/die
```

---

## Avvio

```bash
python main.py
```

All'avvio il programma mostra i file disponibili nella cartella `Ricette/`.
È possibile selezionare un file esistente oppure crearne uno nuovo.

---

## Requisiti

- Python 3.10+
- Nessuna libreria esterna (solo moduli stdlib: `csv`, `os`)