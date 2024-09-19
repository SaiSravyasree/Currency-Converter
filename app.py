from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to get exchange rates using a public API (e.g., exchangeratesapi.io)
def get_exchange_rate(base_currency, target_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(api_url)
    data = response.json()
    return data['rates'][target_currency]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_currency():
    base_currency = request.form['base_currency'].upper()
    target_currency = request.form['target_currency'].upper()
    amount = float(request.form['amount'])

    # Fetch exchange rate
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate

    return render_template('index.html', 
                           base_currency=base_currency, 
                           target_currency=target_currency, 
                           amount=amount, 
                           converted_amount=converted_amount)

if __name__ == '__main__':
    app.run(debug=True)
