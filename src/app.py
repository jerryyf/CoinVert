import fetcher

def main():
    """
    Main script to run on the command line.
    """
    print("Checking API status...")
    if fetcher.ping() == 200:
        print("OK")
        coin:str
        vs:str
        amount:float

        coin = str(input("Enter the coin to convert from, e.g. 'bitcoin':\n"))
        # TODO error handling: check against coinlist
        vs = str(input("Enter the coin/currency to convert to e.g. 'usd':\n"))
        # TODO error handling: check against vs_currencies

        while True:
            try:
                amount = float(input("Enter the amount to convert:\n"))
                break
            except ValueError:
                print("Please enter a numerical value.")
                continue

        print(f"{amount} {coin} = {fetcher.convert(coin, vs, amount)} {vs}")
    
    else:
        print(f"API error {fetcher.ping()}")

if __name__ == "__main__":
    main()