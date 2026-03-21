from fastapi import FastAPI # è come se fosse una classe di Python
app = FastAPI() # qui stiamo creando l'istanza; è il tramite con cui interagiamo con l'app web
@app.get("/hello") #decoratore che permette di traformare una funzione in una risorsa web
            #Dice al server: "Se qualcuno visita l'indirizzo principale (la root /) usando il metodo GET,
            #esegui la funzione qui sotto".
def hello_world():
    return "Hello World!!"
# lo / permette di specificare per ogni applicazione un percorso diverso


#parametri di query
@app.get("/")
def prova(
        q: str, # q non ha un valore di default quindi se non lo inseriamo nell'url ci darà errore
        sort : bool = False # sort ha un valore di default quindi se non lo mettiamo continuerà ad avere come valore false
):
    return {"q" : q, "sort" : sort}

# parametri di percorso

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
