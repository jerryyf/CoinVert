import requests

# Public API is rate limited to 10-30 calls per minute
base_url = "https://api.coingecko.com/api/v3"

def ping():
    """
    Check CoinGecko API status.
    """
    try:
        response = requests.get(f"{base_url}/ping")
        return response.status_code

    except Exception:
        print(Exception.__traceback__)
        

def get_price(coin:str, vs:str) -> int:
    """
    Fetches price of a coin pair against a specified currency.

    @param coin: the coin price to fetch (from /coins/list) e.g. "bitcoin"
    @param vs: the currency to convert against e.g. "usd"
    @return: the price as an integer
    """
    response = requests.get(f"{base_url}/simple/price?ids={coin}&vs_currencies={vs}&precision=2")
    price = response.json()[coin][vs]
    return price

def convert(coin:str, vs:str, amount:float) -> float:
    """
    Converts an amount to its equivalent fiat/coin value.

    @param coin: the coin to convert from (must be from /coins/list) e.g. "bitcoin"
    @param vs: the currency to convert against e.g. "usd"
    @param amount: the amount to convert
    @return: the converted amount rounded to 2 d.p.
    """
    return round((get_price(coin, vs) * amount), 2)

