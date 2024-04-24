from defs import mostrar_mao
from defs import calcular_valor
from defs import retirar_carta
from defs import novo_baralho   

def jogo_21():
    baralho_id = novo_baralho()
    mao_jogador = retirar_carta(baralho_id)
    mao_dealer = retirar_carta(baralho_id)

    print("Bem-vindo ao jogo de 21 brasileiro!")

    # Mostrar a carta do jogador e uma carta do dealer
    mostrar_mao("Jogador", mao_jogador)
    print(f"O dealer tem a seguinte carta: {mao_dealer[0]['value']} de {mao_dealer[0]['suit']}")

    # Verificar se o jogador já ganhou
    if calcular_valor(mao_jogador) == 21:
        print("Você fez 21! Parabéns, você ganhou!")
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