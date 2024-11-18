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



# -------------------------------------------
# import requests

# def stack_details():
#     url = "https://api.freeapi.app/api/v1/public/stocks"
#     try:
    #     response = requests.get(url)
    #     data = response.json()

    #     if data["success"] and "data" in data :
    #         user_data = data["data"]["data"]
    #         symbolName = user_data[1]["Symbol"]
    #         name = user_data[1]["Name"]
    #         marketCap = user_data[1]["MarketCap"]
    #         currentPrice = user_data[1]["CurrentPrice"]
    #         return symbolName, name, marketCap, currentPrice
    #     else:
    #         raise Exception("faild to fetch user data")

# def main():
#     try:
#         symbolName = stack_details()
#         print(f"SymbolName: {symbolName}\n name: {name}\n marketCap: {marketCap} \n currentPrice: {currentPrice}")
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()