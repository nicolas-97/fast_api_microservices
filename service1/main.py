from fastapi import FastAPI

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Define una ruta raíz
@app.get("/")
def read_root():
    return {"message": "¡Bienvenido al microservicio 1 de ejemplo!"}