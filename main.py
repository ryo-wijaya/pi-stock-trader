from typing import Union

from fastapi import FastAPI

app = FastAPI(root_path="/api")


@app.get("/")
def health_check():
    return {"Health-check for pi-stock-trader."}
