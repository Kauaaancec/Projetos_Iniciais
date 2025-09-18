import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").strip().lower()

if jogador not in opcoes:
    print("Escolha inválida! Tente novamente.")
else:
    computador = random.choice(opcoes)
    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
