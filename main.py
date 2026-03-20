from fastapi import FastAPI
app = FastAPI() # tramite con cui interagiamo con l'app web
# vogliamo aggiungere gli endpoint all 'applicazione, ogni endpoit fa riferimento a una risorsa che stiamo
#esponenendo
#definiamo per ogni endpoint una funzione python
# mettiamo un decoratore -> inizia con @
#@app.get ("/")

#@app.get("/hello") # ho cambiato percorso, se andiamo su localhost:8000 ci da errore, se vado su hello, trova il risultato, questo permette di specificare una applicazione per ongi percorso
#def hello_world(q):
    #return "Hello Word"
# @ + pezzo a cui vogliamo aggiungere l'endoint + il metodo http che vogliamo implementare + percorso dell'endpoint
#facendo return qwualocsa, viene convertito in json
# mettiamo l'endpoint sul percorso radice
#per lanciare l'app usiamo fastapi dev
# 2 comandi possibili fastapi dev-> development mode, se modificihiamo il cpdice, fastapi si accorge che l'ho modificato, stoppa l'app e la riesegue
# fastapi run -> se non dobbiamo modificare??
# gli endpoint sono i vari url
# se qualcosa non puo essere traasformato in json, l'app crasha
# possiamo anche ricevere degli input, quando riceviamo una richiestaa http, si possono inserire vari parametri
# 1 modo è tramite le query string http://<host>[:<port>][/<path>[?<query>]
# porta su cui siamo in ascolto (default 80)
#path -> endpoint, il persorso nel programma tramite cui rispondiamo al metodo
# ? dopo questo possiamo mettere dei parametri composti da chiave= valore, le coppie sono separare da &
# l'uso dei parametri è modificare dinamicamnete schermate
# i parametri vengono messi nella funzione di end point

#@app.get("/") # ho cambiato percorso, se andiamo su localhost:8000 ci da errore, se vado su hello, trova il risultato, questo permette di specificare una applicazione per ongi percorso
#def hello_world(q, sort=False):
    #return {"q" : q, "sort" : sort}
# qui l'app web protest, dice che non gli stiamo passando il parametro quindi nella barra aggiungo http://localhost:8000/?q=hello_world
# se vogliamo mettere uun parametro opzionale, quindi usiamo un valore di default
# typing -> python non è tipizzato-> non è necessario definire il tipo di dato che conterra la variabile in fase di inizializzazione
# crea dei problemi di bug e vulnerabilità e rende difficile la comprensione
# funzione type hints: possiamo dire che tipo di dato ci aspettiamo sia contenuto in un altra variabile

@app.get("/")
def hello_world(
        q: str,
        sort : bool = False
) -> dict [str, str]:
    return {"q" : q, "sort" : sort}

#casting automatico, fastapi converte nel formato giusto
# parametri di percorso: il percorso è parametrico; definiamo all'interno del decoratore il perscorso parametrico tramite {}

@app.get("/home")
def home():
    return "This is the homepage" # l'ordine con cui definiamo le funzioni è importante
# definiamo gli endpoint non parametrici e poi dopo quelli parametrici



@app.get("/{username}")
def username_webpage(
        username: str
):
    return f"This is the webpage of user {username}." # quando trova le parentesi graffe riconosce che c'è una variabile dentro

@app.get("/{username}/orders/{order_id}")
def repository_webpage(
        username: str,
        order_id:  int,
        sort: bool = False
):
    return f"Order {order_id} for user {username}. Sorted: {sort}."

#i parametri opzionali vanno sempre dopo i valori obbligatori


