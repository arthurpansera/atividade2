#Lista Teórica 2 - Condicionais
#Nome: Arthur Rodrigues Pansera
#Turma: C

#Exercício 10
universidade = int(input("Escolha sua universidade: 1 - PUCPR ou 2 - UNICAMP: "))
nota1 = int(input("Digite a nota do 1º bimestre: "))
nota2 = int(input("Digite a nota do 2º bimestre: "))
media = (nota1 + nota2)/2
if universidade == 1:
    if media >= 7:
        print("Aprovado!")
    elif 4 <= media < 7:
        print("Em exame!")
    else:
        print("Reprovado!")
if universidade == 2:
    if media >= 5:
        print("Aprovado!")
    else:
        print("Em exame!")