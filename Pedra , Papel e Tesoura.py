import random
import time

pepate = ["Pedra", "Papel", "Tesoura"]

escolha = input("Escolha entre Pedra, Papel e Tesoura (Coloque as duas primeiras letras aqui): ")

print("Pedra!")

time.sleep(0.7)

print("Papel!")

time.sleep(0.7)

print("Tesoura!")

time.sleep(0.7)

cpu = random.choice(pepate)
print("=" * 30)

if escolha == "Pe" and cpu == "Tesoura" or escolha == "Te" and cpu == "Papel" or escolha == "Pa" and cpu == "Pedra":

    print(cpu)
    print("Parabéns você ganhou O.O")

elif cpu == "Tesoura" and escolha == "Pa" or cpu == "Papel" and escolha == "Pe" or cpu == "Pedra" and escolha == "Te":

    print(cpu)
    print("Você perdeu hehehe :D")

else:
    print(cpu)
    print("Que pena, foi empate :(")

