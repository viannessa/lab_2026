from fastapi import FastAPI # è come se fosse una classe di Python
app = FastAPI() # qui stiamo creando l'istanza; è il tramite con cui interagiamo con l'app web
@app.get("/") #decoratore che permette di traformare una funzione in una risorsa web
            #Dice al server: "Se qualcuno visita l'indirizzo principale (la root /) usando il metodo GET,
            #esegui la funzione qui sotto".
def hello_world():
    return "Hello World!!"