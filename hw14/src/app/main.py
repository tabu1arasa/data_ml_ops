import os
import time

import redis
from fastapi import FastAPI
from random import randint

REDIS_HOST = os.getenv("REDIS_HOST") or "localhost"
REDIS_PORT = os.getenv("REDIS_PORT") or 6379

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

app = FastAPI(title="Yet another generator app")

@app.on_event("startup")
def startup():
    pass

@app.get("/gen_filename")
def gen_tmp_filename():
    base = randint(1_000_000, 1_000_000_000)
    generated_filename = hex(base)[2:]
    r.set(generated_filename, str(time.time()))
    return {"filename": generated_filename}

@app.get("/gen_nickname")
def gen_nickname():
    colors = ["green", "orange", "purple", "yellow", "gold"]
    animals = ["elephant", "tiger", "bear", "fox", "dog", "cat", "fish"]
    generated_nickname = colors[randint(0, len(colors)-1)] + " " + animals[randint(0, len(animals) - 1)]
    r.set(generated_nickname, str(time.time()))
    return {"nickname": generated_nickname}

@app.get("/get_item_upload_time/{name}")
def get_filename_time(name: str):
    unix_time = r.get(name)
    return {"time": unix_time}