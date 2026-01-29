from fastapi import FastAPI
from random import randint

app = FastAPI(title="Yet another generator app")

@app.on_event("startup")
def startup():
    pass

@app.get("/gen_filename")
def gen_tmp_filename():
    base = randint(1_000_000, 1_000_000_000)
    generated_filename = hex(base)[2:]
    return {"filename": generated_filename}

@app.get("/gen_nickname")
def gen_nickname():
    colors = ["green", "orange", "purple", "yellow", "gold"]
    animals = ["elephant", "tiger", "bear", "fox", "dog", "cat", "fish"]
    generated_nickname = colors[randint(0, len(colors)-1)] + " " + animals[randint(0, len(animals) - 1)]
    return {"nickname": generated_nickname}
