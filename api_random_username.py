import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)  # Corrected variable name
    data = response.json()

    # Check if the API call was successful
    if data.get('success') and data.get('statusCode') == 200:
        try:
            user_data = data["data"]
            username = user_data['login']['username']
            country = user_data['location']['country']
            return username, country
        except KeyError as e:
            raise Exception(f"Missing expected key in API response: {e}")
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username, country = fetch_random_user()
        print(f"Username : {username} \nCountry: {country}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()


