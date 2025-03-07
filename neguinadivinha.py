print ("****************************")
print ("Bem Vinvo ao Neguin Adivinha")
print ("****************************")

numero_secreto = 24 
total_de_tentativas = 3 


for rodada in range  (1,total_de_tentativas):
    print(f"tentativas (rodada) de {total_de_tentativas}")
    chute = int(input("digite o seu numero: "))


    numero_secreto = 24 
    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto


    print(f"Você digitou {chute}\n")

    if(acertou):
        print("Você acertou\n")
        break

    else:
        if(chute_maior):
            print("muito burro! Seu numero foi maior que o numero secreto \n")
        elif(chute_menor):
            print("inbecil! seu numero foi menor que o numero secreto")



print ("@@@@@@@@@@@")
print ("Fim de Jogo")
print ("@@@@@@@@@@@")