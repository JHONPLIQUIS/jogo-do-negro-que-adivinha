print ("****************************")
print ("Bem Vinvo ao Neguin Adivinha")
print ("****************************")


chute = int(input("Digite o numero secreto: "))

numero_secreto = 24 
acertou = numero_secreto == chute
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto


print(f"Você digitou {chute}\n")

if(acertou):
    print("Você acertou\n")
else:
    if(chute > numero_secreto):
        print("muito burro! Seu numero foi maior que o numero secreto \n")
    elif(chute < numero_secreto):
        print("inbecil! seu numero foi menor que o numero secreto")


print ("@@@@@@@@@@@")
print ("Fim de Jogo")
print ("@@@@@@@@@@@")