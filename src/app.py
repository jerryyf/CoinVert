import fetcher
import sys

def main():
    """
    Main script to run on the command line.
    """
    print(f"API status: {fetcher.ping()}")
    if len(sys.argv) == 4:
        coin = str(sys.argv[1])
        vs = str(sys.argv[2])
        amount = float(sys.argv[3])
        print(f"${fetcher.convert(coin, vs, amount)} {vs}")

    else:
        print("Usage:\npython app.py <coin> <currency> <amount>")

if __name__ == "__main__":
    main()