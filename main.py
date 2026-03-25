from fastapi import FastAPI, Request # è come se fosse una classe di Python
from fastapi.responses import HTMLResponse
# inizializzare il motore di templeting
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")# dobbiamo dire dove sono i nostri templates
@app.get("/", response_class=HTMLResponse) # qui nel decoratore possiamo inserire dei parametri, stiamo impostando una tipologia di risposta; la risposta deve essere html
def home(request: Request ): # il parametro request conterà la richiesta http get, ma non gliela passiamo noi, ma direttamente fastapi; gli stiamo dando il type
    """Renders the home page"""
    text = {
        "title": "Home page",
        "context": "Welcome to the home page",
    }
    context = {"text": text,  "sequence": ["a", "b", "c"]}
# dobbiamo costruire la nostra risposta: 1 parametro: richiesta che riceviamo cioe la get, il 2: quale template renderizzre, quale file hatml mostrare nell'ednpoint
    return templates.TemplateResponse(
        request = request,
        name = "home.html",
        context = context
    )
