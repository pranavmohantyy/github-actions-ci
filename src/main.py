from fastapi import FastAPI
from mathutils import add, subtract, multiply, divide

app = FastAPI()

@app.get("/add")
def api_add(x: float, y: float):
    return {"result": add(x, y)}

@app.get("/subtract")
def api_subtract(x: float, y: float):
    return {"result": subtract(x, y)}

@app.get("/multiply")
def api_multiply(x: float, y: float):
    return {"result": multiply(x, y)}

@app.get("/divide")
def api_divide(x: float, y: float):
    return {"result": divide(x, y)}