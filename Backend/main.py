from fastapi import FastAPI
from fasapi.middleware.cors import CORSMiddleware

app=FastAPI()
@app.get("/sumar")
def sumar_numeros(a:float, b:float):
    return a+b