
# 💸 API Integração Financeira

Este projeto fornece uma API simples em Flask para consultar a cotação atual do dólar (USD) em relação ao real brasileiro (BRL), utilizando a ExchangeRate-API.

## 🚀 Como usar

1. Instale as dependências:
```
pip install flask requests
```

2. Execute o servidor:
```
python cotacao_dolar.py
```

3. Acesse a rota no navegador ou via curl:
```
http://localhost:5000/cotacao
```

## 📦 Exemplo de resposta
```
{
  "USD_to_BRL": 5.23
}
```

Ideal para quem deseja consumir dados financeiros de forma prática e rápida, sem necessidade de autenticação ou registro.
