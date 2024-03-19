#Lista Teórica 2 - Condicionais
#Nome: Arthur Rodrigues Pansera
#Turma: C

#Exercício 6
numero = int(input("Digite um número: "))
if numero % 2 != 0:
    print("O número é ímpar")
    print(f"{numero} pertence ao conjunto I")
elif numero == 0:
    print(f"O número {numero} não pertence a nenhnhum dos conjuntos")
else:
    print("O número é par")
    print(f"{numero} pertence ao conjunto P")