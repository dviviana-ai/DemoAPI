from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

#CORS: Para habilitar peticiones de clientes que no están en mi dominio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/sumar")
def sumar_numeros(a:float, b:float):
    return a+b


#python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload.\