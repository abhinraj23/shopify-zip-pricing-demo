from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRICE_MAP = {
    "75028": 1499,
    "10001": 1699,
    "90210": 1799
}

@app.get("/price")
def get_price(zip_code: str):
    return {
        "price": PRICE_MAP.get(zip_code, 1999)
    }

@app.get("/proxy")
def proxy(zip_code: str):
    return {
        "price":PRICE_MAP.get(zip_code, 1999)
    }
