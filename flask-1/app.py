from flask import Flask, render_template, request
from utils import convert_currency, is_valid_currency

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

       
        if not is_valid_currency(from_currency) or not is_valid_currency(to_currency):
            error_message = 'Invalid currency code(s). Please enter valid codes.'
            return render_template('index.html', error_message=error_message)

        try:
            amount = float(amount)
        except ValueError:
            error_message = 'Invalid amount. Please enter a valid number.'
            return render_template('index.html', error_message=error_message)

        
        result, to_currency_symbol = convert_currency(from_currency, to_currency, amount)

        
        converted_message = f'{to_currency_symbol} {result:.2f}'
        return render_template('index.html', converted_message=converted_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
