# Currency Converter

A Python script that converts an amount from one currency to another using real-time exchange rates from the [ExchangeRate-API](https://www.exchangerate-api.com/).

## Overview

The program prompts the user to enter:
- A base currency (e.g. EUR)
- A target currency (e.g. USD)
- An amount to convert

It then fetches the current exchange rate using the exchangerate-api and displays the converted amount.

## Example

Input:
```
Base currency: EUR  
Target currency: USD  
Amount: 30
```

Output:
```
30.0 EUR = 34.56 USD
```

*(Output will vary based on real-time exchange rates.)*

## Requirements

- Python 3  
- `requests` library (`pip install requests`)  
- Free API key from [https://www.exchangerate-api.com](https://www.exchangerate-api.com)

## Setup

Replace the `api_key` variable in the script with your own key:
```python
api_key = "your_api_key_here"
```

## License

MIT License
