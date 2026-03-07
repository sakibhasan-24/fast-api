from fastapi import FastAPI

# create an instance of FastAPI
app = FastAPI()

# create a simple endpoint
@app.get("/")
def home():
    return {"message": "FastAPI is running successfully!😒"}

# create another endpoint
@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello {name}, welcome to FastAPI isolation learning!"}