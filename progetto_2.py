# Progetto 2
# Scenario reale
# Un centro di analisi mediche deve informatizzare parte della gestione dei pazienti, dei medici e dei referti di laboratorio. Si richiede la progettazione e la realizzazione di un programma in Python che permetta di gestire i dati in maniera strutturata, utilizzando programmazione a oggetti (OOP) e la libreria NumPy per l’elaborazione numerica dei dati clinici.
# Parte 1 – Variabili e Tipi di Dati
# Definire le variabili necessarie per rappresentare:
# Nome, cognome e codice fiscale di un paziente (stringhe).
# Età e peso del paziente (interi e float).
# Lista delle analisi effettuate (lista di stringhe).
# Esempio:
# nome = "Mario"
# cognome = "Rossi"
# eta = 45
# peso = 78.5
# analisi = ["emocromo", "glicemia", "colesterolo"]
# ➡️ Scrivere almeno 3 pazienti diversi con queste variabili.
# Parte 2 – Classi e OOP
# Creare una classe Paziente con:
# Attributi: nome, cognome, codice_fiscale, eta, peso, analisi_effettuate.
# Metodo scheda_personale() che restituisca una stringa con i dati principali del paziente.
# Creare una classe Medico con:
# Attributi: nome, cognome, specializzazione.
# Metodo visita_paziente(paziente) che stampi quale medico sta visitando quale paziente.
# Creare una classe Analisi che contenga:
# Tipo di analisi (es. glicemia, colesterolo).
# Risultato numerico.
# Metodo valuta() che stabilisca se il valore è nella norma (criteri inventati da voi).
# Parte 3 – Uso di NumPy
# Supponiamo che il centro raccolga i risultati di un certo esame per 10 pazienti.
# Rappresentare i valori in un array NumPy.
# Calcolare con NumPy: media, valore massimo, valore minimo e deviazione standard.
# Parte 4 – Integrazione OOP + NumPy
# Aggiornare la classe Paziente inserendo un attributo risultati_analisi che sia un array NumPy contenente i valori numerici delle analisi svolte.
# Creare un metodo statistiche_analisi() che calcoli:
# Media dei valori
# Minimo e massimo
# Deviazione standard
# utilizzando NumPy.
# Parte 5 – Applicazione completa
# Creare un piccolo programma principale (main) che:
# Inserisca almeno 3 medici e 5 pazienti.
# Ogni paziente deve avere almeno 3 risultati di analisi.
# Stampi la scheda di ogni paziente.
# Mostri quale medico visita quale paziente.
# Stampi le statistiche delle analisi per ciascun paziente.




# # # # #         PARTE 1         # # # # #

# Paziente 1
nome1 = "Pippo"
cognome1 = "Bove"
eta1 = 56
peso1 = 82.4
analisi1 = ["bambupatia","spraliconia","gelatobia"]
# Paziente 2
nome2 = "Giuditta"
cognome2 = "Siniscalco"
eta2 = 42
peso2 = 62.3
analisi2 = ["galantofonia","sprizzicornia","liporinobasilaxia"]
# Paziente 3
nome3 = "Clovis"
cognome3 = "De Rubricus"
eta3 = 72
peso3 = 42.3
analisi3 = ["rintronabialis","bradirompix","lapsuslanialis"]


# # # # #         PARTE 2         # # # # #

class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate

    def scheda_personale(self):
        return (f"* * * SCHEDA PAZIENTE * * * \n Nome: {self.nome} \n Cognome: {self.cognome} \n CF: {self.codice_fiscale} \n Età: {self.eta} \n Peso: {self.peso} \n Analisi effettuate: {self.analisi_effettuate}")


class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione
    
    def visita_paziente(self, paziente):
        return(f"Il medico {self.nome} {self.cognome} sta visitando il paziente {paziente.nome} {paziente.cognome}")


class Analisi:
    def __init__(self, tipo, risultato):
        self.tipo = tipo
        self.risultato = risultato
    
    analisi_valori_standard = {
        "fuffolinia": 123,
        "anniottantomania": 80,
        "discodancelabia": 70,
        "fobilaxia": 90,
        "mortadellaccumulabilia": 200,
        "emofarina": 10
    }
    

    def valuta(self):
        if self.tipo in self.analisi_valori_standard:
            valore_standard = self.analisi_valori_standard[self.tipo]

            if self.risultato <= valore_standard:
                return "Sopravviverai"
            else:
                return "Ti conviene sbrigare rapidamente eventuali questioni in sospeso"
        else:
            return "Tipo di analisi non riconosciuto"

        

medico1 = Medico("Bob", "Stradilongaro", "Fefalogia")

paziente1 = Paziente("Mario", "Rossi", "MRORSS76A23F023G", 72, 78.3, ["Emofarina","Glucorimbastina"])


# # # # #         PARTE 3         # # # # #

import numpy as np

risultati_emofarina = np.array([10.7, 8.3, 7.1, 12.4, 13.1, 4.4, 6.9, 6.2, 3.1, 11.6])

print(f"Media dei valori: {np.mean(risultati_emofarina)}")
print(f"Valore massimo riscontrato: {np.max(risultati_emofarina)}")
print(f"Valore minimo riscontrato: {np.min(risultati_emofarina)}")
print(f"Deviazione standard: {np.std(risultati_emofarina)}")
print("\n")


# # # # #         PARTE 4         # # # # #

class PazientePlus:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = risultati_analisi

    def scheda_personale(self):
        return (f"* * * SCHEDA PAZIENTE * * * \n Nome: {self.nome} \n Cognome: {self.cognome} \n CF: {self.codice_fiscale} \n Età: {self.eta} \n Peso: {self.peso} \n Analisi effettuate: {self.analisi_effettuate}")

    def statistiche_analisi(self):
        media = np.mean(self.risultati_analisi)
        risultato_min = np.min(self.risultati_analisi)
        risultato_max = np.max(self.risultati_analisi)
        deviazione = np.std(self.risultati_analisi)
        return (f"* * * Statistiche analisi paziente {self.nome} {self.cognome} * * * \n Media dei valori: {media} \n Valore minimo riscontrato: {risultato_min} \n Valore massimo riscontrato: {risultato_max} \n Deviazione standard: {deviazione}")

paziente_plus_1 = PazientePlus("George", "King", "GRGKNG82A12F023F", 31, 86.3, ["Emofarina"], risultati_emofarina)
print(paziente_plus_1.statistiche_analisi())


# # # # #         PARTE 5         # # # # #

def main():
    # Creazione di medici e pazienti
    m1 = Medico("Bob", "Stradilongaro", "Fefalogia")
    m2 = Medico("Fred", "Bonnet", "Salute dell'unghia dell'indice della mano sinistra")
    m3 = Medico("Jane", "Lapislazzulova", "Cuori infranti")
    p1 = PazientePlus("Mario", "Rossi", "MRORSS76A23F023G", 72, 78.3, ["emofarina"], [3.2, 7.1, 8.9])
    p2 = PazientePlus("Maria", "Rossi", "MRARSS46A07A022H", 83, 68.3, ["fobilaxia"], [12.7, 13.4, 18])
    p3 = PazientePlus("John", "Reds", "JHNRDS38B21A013K", 92, 98.1, ["extraottuagenarismo"], [89.5, 62.2, 72.1])
    p4 = PazientePlus("Louis", "Greens", "LOUGRS65C14H501", 59, 82.7, ["discodancelabia"], [71.2, 72.1, 72.5])
    p5 = PazientePlus("Anna", "Bianchi", "NNABNC88D55F205", 37, 61.2, ["anniottantomania"], [81.8, 82.2, 80.4, 89.9])

    # Raggruppamento dei pazienti per poter eseguire un ciclo di stampa delle schede personali
    gruppo_pazienti = [p1, p2, p3, p4, p5]

    # Stampa delle schede dei pazienti
    print("* * * Gruppo dei pazienti * * *")
    for p in gruppo_pazienti:
        print(p.scheda_personale())
        print("\n")
    
    # Stampa dei pazienti visitati dai medici
    print("\n")
    print("* * * Stampa dei pazienti visitati dai medici * * *")
    print(m1.visita_paziente(p1))
    print(m1.visita_paziente(p4))
    print(m2.visita_paziente(p2))
    print(m3.visita_paziente(p3))
    print(m3.visita_paziente(p5))

    # Stampa delle statistiche dei pazienti
    print("* * * Statistiche dei pazienti * * *")
    for p in gruppo_pazienti:
        print(p.statistiche_analisi())
        print("\n")


if __name__ == "__main__":
    main()

