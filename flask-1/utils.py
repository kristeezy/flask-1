import requests

def is_valid_currency(currency_code):
    return len(currency_code) == 3

def convert_currency(from_currency, to_currency, amount):
    api_key = 'YOUR_EXCHANGERATE_HOST_API_KEY'  # which URL do I use?
    base_url = 'https://open.er-api.com/v6/latest'

    params = {'base': from_currency, 'symbols': to_currency}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][to_currency]
        result = amount * rate

       
        to_currency_symbol = get_currency_symbol(to_currency)

        return result, to_currency_symbol
    else:
        
        error_message = 'Error fetching exchange rate. Please try again later.'
        raise Exception(error_message)

def get_currency_symbol(currency_code):
    
    currency_symbols = {'USD': '$', 'EUR': '€', 'JPY': '¥'}
    return currency_symbols.get(currency_code, currency_code)
