import requests

def stack_details():
    url = "https://api.freeapi.app/api/v1/public/stocks"
    try:
        response = requests.get(url)
        data = response.json()

        # Check API response structure
        if data.get("success") and "data" in data:
            # Extract nested data
            user_data = data["data"]["data"]
            
            # Fetch details for the second stock (index 1)
            symbolName = user_data[0]["Symbol"]
            name = user_data[0]["Name"]
            marketCap = user_data[0]["MarketCap"]
            currentPrice = user_data[0]["CurrentPrice"]
            return symbolName, name, marketCap, currentPrice
        return _extracted_from_stack_details_10(data)
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")
def main():
    try:
        # Unpack returned values from stack_details()
        symbolName, name, marketCap, currentPrice = stack_details()
        print(f"SymbolName: {symbolName}\nName: {name}\nMarketCap: {marketCap}\nCurrentPrice: {currentPrice}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
