import requests

def novo_baralho():
    response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    data = response.json()
    return data['deck_id']

# Função para retirar uma carta do baralho
def retirar_carta(baralho_id, quantidade=1):
    url = f'https://deckofcardsapi.com/api/deck/{baralho_id}/draw/?count={quantidade}'
    response = requests.get(url)
    data = response.json()
    return data['cards']

# Função para calcular o valor de uma mão de cartas
def calcular_valor(mao):
    valor = 0
    for carta in mao:
        if carta['value'] in ['JACK', 'QUEEN', 'KING']:
            valor += 10
        elif carta['value'] == 'ACE':
            valor += 1
        else:
            valor += int(carta['value'])
    return valor

# Função para mostrar a mão de um jogador
def mostrar_mao(jogador, mao):
    print(f'{jogador} tem as seguintes cartas:')
    for carta in mao:
        print(f"{carta['value']} de {carta['suit']}")

# Função principal do jogo
def jogo_21():
    baralho_id = novo_baralho()
    mao_jogador = retirar_carta(baralho_id)
    mao_dealer = retirar_carta(baralho_id)

    print("Jogo 21!")

    # Mostrar a carta do jogador e uma carta do dealer
    mostrar_mao("Jogador", mao_jogador)
    print(f"O dealer tem a seguinte carta: {mao_dealer[0]['value']} de {mao_dealer[0]['suit']}")

    # Verificar se o jogador já ganhou
    if calcular_valor(mao_jogador) == 21:
        print("Você fez 21! Ganhou!")
        return

    # Continuar o jogo
    while True:
        decisao = input("Deseja pedir outra carta? (s/n): ").lower()
        if decisao == 's':
            mao_jogador.extend(retirar_carta(baralho_id))
            mostrar_mao("Jogador", mao_jogador)
            if calcular_valor(mao_jogador) > 21:
                print("Você estourou 21! Você perdeu.")
                return
        else:
            break

    # Turno do dealer
    print("Turno do dealer:")
    while calcular_valor(mao_dealer) < 15:
        mao_dealer.extend(retirar_carta(baralho_id))
        mostrar_mao("Dealer", mao_dealer)

    # Verificar quem ganhou
    valor_jogador = calcular_valor(mao_jogador)
    valor_dealer = calcular_valor(mao_dealer)

    if valor_dealer > 21 or valor_jogador > valor_dealer:
        print("Parabéns! Você ganhou!")
    elif valor_jogador == valor_dealer:
        print("Empate!")
    else:
        print("Você perdeu. O dealer ganhou.")

# Iniciar o jogo
jogo_21()