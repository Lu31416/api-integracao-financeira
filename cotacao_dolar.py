from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_usd_brl():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'rates' in data and 'BRL' in data['rates']:
            return {"USD_to_BRL": round(data['rates']['BRL'], 2)}
        else:
            return {"error": "BRL rate not found in response"}, 404
    else:
        return {"error": "Failed to fetch data from API"}, 500

@app.route('/cotacao', methods=['GET'])
def get_cotacao():
    result = fetch_usd_brl()
    if "error" in result:
        return jsonify(result), result.get("code", 500)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
