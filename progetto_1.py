# Progetto 1

# Progetto: Gestione Biblioteca Digitale

# Traccia
# In una biblioteca digitale si vuole realizzare un piccolo sistema software per gestire libri, utenti e prestiti.
# Il programma deve sfruttare variabili, tipi di dati, strutture di controllo e soprattutto la programmazione orientata agli oggetti (OOP).

#  Consegna 

    # Parte 1 – Variabili e tipi di dati

        # 1) Dichiarare e stampare alcune variabili di esempio:
        # 2) Titolo di un libro (stringa)
        # 3) Numero di copie disponibili (intero)
        # 4) Prezzo medio di un libro (float)
        # 5) Stato "disponibile/non disponibile" (booleano)(Esempio: titolo = "Il Signore degli Anelli", copie = 5, ecc.)

    # Parte 2 – Strutture dati

        # 1) Creare una lista con almeno 5 titoli di libri.
        # 2) Creare un dizionario che mappi il titolo del libro al numero di copie disponibili.
        # 3) Creare un insieme (set) che contenga tutti gli utenti registrati alla biblioteca.

    # Parte 3 – Classi e OOP

        # 1) Creare una classe Libro con attributi:
        # 2) titolo
        # 3) autore
        # 4) anno
        # 5) copie_disponibili

    # Aggiungere un metodo info() che restituisca una stringa descrittiva del libro.
        # 1) Creare una classe Utente con attributi:
        # 2) nome
        # 3)eta
        # 4) id_utente

    # Aggiungere un metodo scheda() che stampi i dati dell’utente.
        # 1) Creare una classe Prestito che colleghi un Utente a un Libro e contenga:
        # 2) utente (oggetto Utente)
        # 3) libro (oggetto Libro)
        # 4) giorni (numero di giorni del prestito)

    # Aggiungere un metodo dettagli() che stampi tutte le informazioni sul prestito.

    # Parte 4 – Funzionalità

        # 1) Creare una funzione presta_libro(utente, libro, giorni) che:
        # 2) Verifichi se il libro ha almeno 1 copia disponibile
        # 3) Se sì → riduca il numero di copie e crei un nuovo oggetto Prestito
        # 4) Se no → stampi un messaggio di errore
        # 5) Simulare almeno 3 prestiti con utenti e libri diversi.
        # 6) Stampare a video:
        #       L’elenco aggiornato delle copie disponibili per ciascun libro
        #       I dettagli di ogni prestito effettuato



# Parte 1 - Variabili e tipi di dati

print("Stampa delle variabili di esempio: " + "\n")

titolo_stringa = "Il Buio oltre la Siepe"
numero_copie = 12
prezzo_libro = 12.99
disponibile = True

print("Titolo di un libro (stringa):", titolo_stringa)
print("Numero di copie disponibili (intero):", numero_copie)
print("Prezzo medio di un libro (float):", prezzo_libro)
print("Disponibilità (booleano):", disponibile)


# Parte 2 - Strutture dati

# Lista dei titoli
titoli_libri = [
    "Il Signore degli Anelli",
    "1984",
    "Il Nome della Rosa",
    "Dune",
    "Fondazione"
]

# Dizionario: titolo -> copie disponibili
copie_disponibili = {
    "Il Signore degli Anelli": 3,
    "1984": 5,
    "Il Nome della Rosa": 2,
    "Dune": 4,
    "Fondazione": 1
}

# Set degli utenti registrati
utenti = {"Anna", "Marco", "Luca", "Giulia"}


# Parte 3 - Classi e OOP

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili
    
    def info(self):
        return f"Titolo del libro: {self.titolo}"+ "\n" + f"Autore: {self.autore}" + "\n" + f"Anno di pubblicazione: {self.anno}" + "\n" + f"Copie disponibili: {self.copie_disponibili}"


class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        return f"ID_utente: {self.id_utente}" + "\n" + f"Nome utente: {self.nome}" + "\n" + f"Età: {self.eta}" + "\n"


class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni


    def dettagli(self):
        print(f"- Dettagli del prestito - \n" + "\n" + f"* Utente * \n" + f"{self.utente.scheda()}" + "\n" + f"* Libro * \n" + f"{self.libro.info()}" + "\n" + f"Giorni di prestito: {self.giorni}")

# Creo una lista per gestire dinamicamente l'elenco dei libri
libri = []

libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 12)
utente1 = Utente("Geronimo", 43, 100001)
prestito1 = Prestito(utente1, libro1, 10)

libro2 = Libro("Tre Uomini in Barca", "J.K. Jerome", 1889, 7)
libro3 = Libro("Oceano Mare", "Alessandro Baricco", 1993, 10)
libro4 = Libro("Dieci piccoli indiani", "Agatha Christie", 1939, 1)
libro5 = Libro("Neuromante", "William Gibson", 1984, 3)

utente2 = Utente("Gilberta", 38, 100002)
utente3 = Utente("Bob", 21, 100003)


# Aggiungo i libri alla lista
libri.append(libro1)
libri.append(libro2)
libri.append(libro3)
libri.append(libro4)
libri.append(libro5)



# Metodo info che restituisce una stringa descrittiva del libro
print(libro1.info())
# Metodo scheda che stampa i dati dell'utente
print(utente1.scheda())
# Metodo dettagli che stampa tutte le informazioni sul prestito
prestito1.dettagli()
print("\n")

# Creo una lista per gestire dinamicamente la creazione di nuovi oggetti Prestito nella funzione presta_libro
prestiti = []
# Per completezza, aggiungo il prestito creato in precedenza
prestiti.append(prestito1)

# Parte 4 - Funzionalità

def presta_libro(utente, libro, giorni):
    # 1) Verifica se il libro ha almeno 1 copia disponibile; 2) Se sì -> riduce il numero di copie e crea un nuovo oggetto Prestito (classe Prestito); Se no -> stampa un messaggio di errore
    if(libro.copie_disponibili > 0):
        libro.copie_disponibili -= 1
        nuovo_prestito = Prestito(utente, libro, giorni)
        prestiti.append(nuovo_prestito)

    else:
        print("Nessuna copia disponibile per il prestito")


# Simulare almeno 3 prestiti con utente e libri diversi:

presta_libro(utente2, libro2, 7)
presta_libro(utente3, libro4, 20)
presta_libro(utente1, libro5, 30)

# Stampare a video:

# L'elenco aggiornato delle copie disponibili per ciascun libro

print("Elenco aggiornato delle copie disponibili per ciascun libro: " + "\n")
for libro in libri:
    print(f"{libro.titolo}: {libro.copie_disponibili} copie")


print("\n")

# I dettagli di ogni prestito effettuato

print("Dettagli di ogni prestito effettuato: " + "\n")
for prestito in prestiti:
    prestito.dettagli()
    print("\n")
    print("* * * * * *")
    print("\n")
