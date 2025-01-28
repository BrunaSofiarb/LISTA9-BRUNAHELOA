import random
def jogoadvinhação():
    numero = random.randint(1,100)

    print("Advinhe o número de 1 a 100")

    tentativas = 0

    while True:
        palpite = int(input("Qual é o seu palpite? "))
        tentativas += 1

        if palpite < numero:
            print("Seu palpite foi muito baixo!.")
        elif palpite > numero:
            print("Seu palpite foi muito alto!.")
        else:
            print("Parabéns, você acertou o número!")


jogoadvinhação()