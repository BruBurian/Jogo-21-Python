Jogo de 21 Brasileiro

Este é um jogo de 21 em Python, utilizando a API do Deck of Cards (baralho de cartas) para embaralhar e distribuir as cartas. O objetivo do jogo é somar 21 pontos ou o mais próximo possível sem ultrapassar esse valor. O jogador compete contra o dealer (computador).
Como Jogar

    Iniciar o Jogo: Ao iniciar o jogo, o baralho é embaralhado e distribuído entre o jogador e o dealer.

    Rodada do Jogador: O jogador recebe duas cartas viradas para cima e pode pedir mais cartas até decidir parar ou ultrapassar 21 pontos.

    Rodada do Dealer: Após o jogador parar, o dealer revela suas cartas e pede mais cartas até atingir pelo menos 15 pontos.

    Resultado: O vencedor é determinado pela soma das pontuações de cada jogador. Se um jogador tiver 21 pontos, ele ganha automaticamente. Se ambos os jogadores tiverem a mesma pontuação, ocorre um empate.

Funcionalidades

    novo_baralho(): Cria um novo baralho utilizando a API do Deck of Cards.
    retirar_carta(baralho_id, quantidade): Retira uma ou mais cartas do baralho.
    calcular_valor(mao): Calcula o valor total de uma mão de cartas, considerando as regras do jogo.
    mostrar_mao(jogador, mao): Mostra as cartas na mão de um jogador.

Execução do Jogo

Para executar o jogo, basta chamar a função jogo_21(). O jogo começará automaticamente, e você será solicitado a pedir ou parar de receber cartas. Ao final do jogo, o resultado será exibido.
