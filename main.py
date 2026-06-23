from fastapi import FastAPI

app = FastAPI()

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
