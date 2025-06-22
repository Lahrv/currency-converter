import requests

def convert_currency(base_currency, target_currency, amount, api_key):
    """
    Convert a currency amount from base to target using real-time exchange rates.

    Parameters:
    - base_currency (str): e.g. 'USD'
    - target_currency (str): e.g. 'EUR'
    - amount (float): amount to convert
    - api_key (str): API key for exchangerate-api

    Returns:
    - float: converted amount
    """
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}/{amount}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("conversion_result")
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    print("Currency Converter")

    base = input("Enter base currency (e.g. USD): ").upper()
    target = input("Enter target currency (e.g. EUR): ").upper()

    try:
        amount = float(input("Enter amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        exit()

    api_key = "daaaa50dac7b1d171518ecae"

    result = convert_currency(base, target, amount, api_key)
    if result is not None:
        print(f"{amount} {base} = {round(result, 2)} {target}")
    else:
        print("Conversion failed.")
