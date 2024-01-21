import requests
import time
import locale

# Configurando a localização para o Brasil
locale.setlocale(locale.LC_MONETARY, 'pt_BR')

def obter_preco_em_brl(codigo_moeda):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": codigo_moeda,
        "vs_currencies": "brl"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data[codigo_moeda]["brl"]
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter preço da criptomoeda: {e}")
        return None

def formatar_moeda(valor):
    return locale.currency(valor, grouping=True)

def main():
    codigo_moeda = "bitcoin"  # Altere para o código da criptomoeda desejada (por exemplo, "ethereum" para Ethereum)

    print(f"Obtendo preço da criptomoeda em BRL. Pressione Ctrl+C para encerrar.")

    while True:
        preco_brl = obter_preco_em_brl(codigo_moeda)

        if preco_brl is not None:
            preco_formatado = formatar_moeda(preco_brl)
            print(f"Preço da criptomoeda em BRL: {preco_formatado}")
        else:
            print("Não foi possível obter o preço.")

        time.sleep(5)  # Atualiza a cada 5 segundos

if __name__ == "__main__":
    main()
