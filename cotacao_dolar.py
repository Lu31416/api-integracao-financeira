import requests

# URL da nova API para obter a cotação do dólar
url = 'https://api.exchangerate-api.com/v4/latest/USD'

# Fazendo a requisição GET
response = requests.get(url)

# Checando se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    print("Dados retornados pela API:", data)  # Exibir dados para diagnóstico
    
    # Verifica se 'rates' está presente na resposta
    if 'rates' in data:
        cotacao_dolar = data['rates']['BRL']
        print(f"A cotação do dólar (USD) para o real (BRL) é: R$ {cotacao_dolar:.2f}")
    else:
        print("Não há cotações disponíveis no momento.")
else:
    print("Erro ao acessar a API. Código de status:", response.status_code)
