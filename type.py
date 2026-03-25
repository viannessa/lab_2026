# il tipying si compone di : 'tipo' = valore
x : int = "ciao"
print(x)


# se metto una stringa in un qualcosa che non è di tipo stringa, ho un warning
# quando è utile? quando definiamo una funzione, possiamo specifiare per ogni parametro il suo tipo
# se spec il tipo di dato nella signature di una funzione, quando chiamimao le funzione, possiamo avere un alert che stiamo passando dei dati non valiti
# posso anceh definire il tipo di ritorno
def compute_sum(
        x: float,
        y: float
) -> float:
   return x + y
s: str = compute_sum(1, 2) # sto mettendo un qualcosa che restituisce un float, dentro una stringa
print(s)

# comportamento di default: typing utile in fase di sviluppo
# a: list[int] variabile che contiene una lista di interi
# a: dict [str, int] dizionario di stringhe e interi
# possiamo definire anche + tipi per una variabile, usiamo il carattere | a: list | tuple | None | int
# se nelle funzioni vogliamo definire dei parametri di default possiamo definirlo con il tipying z: float = 0.0
# in fastapi è fondamentale; usa in backgroung usa una libreria che obbliga a rispettare i tipi di dati che definiamo
# se non si rispetta da errore 422
# la validazione dell'input da sicurezza, robustezza    t