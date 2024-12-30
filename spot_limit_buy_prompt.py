from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient
import logging
import json

# Path to your JSON file
json_file_path = 'cdp_api_key.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)


# Extract the API key
api_key = data['name']
api_secret = data['privateKey']

client = EnhancedRESTClient(api_key=api_key, api_secret=api_secret)

try:
    # Prompt the user for the amount to buy
    amount = input("Enter the amount in USD to buy BTC: ")

    # Perform a limit buy
    response = client.fiat_limit_buy("BTC-USDC", amount)
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Response Body:", response.text)

except Exception as e:
    print(f"An error occurred while creating the client: {e}")
