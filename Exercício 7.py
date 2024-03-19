#Lista Teórica 2 - Condicionais
#Nome: Arthur Rodrigues Pansera
#Turma: C

#Exercício 7
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
if idade > 15 and peso <= 120:
    print("Liberado para andar na montanha-russa")
elif idade <= 15 and peso > 120:
    print("Proibido de andar na montanha-russa")