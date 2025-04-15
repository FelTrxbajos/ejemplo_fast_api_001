#necesitamos la libreria
from fastapi import FastAPI
#creamos la variable de la API
api = FastAPI()
#Vamos a crear los metodos de la API
@api.get("/")
def root():
    return {"mensaje": "Hola mundo 2"}

@api.get("/usuarios/{id}")
def get_usuario(id: int):
    usuarios = {
        1: {"nombre": "Lalo Cura", "email": "lalo.cura@gmail.com"},
        2: {"nombre": "Elsa Pato", "email": "elsa.pato@gmail.com"},
        3: {"nombre": "Armando Murito", "email": "armando.murito@gmail.com"}
    }
    return usuarios.get(id)
