#Lista Teórica 2 - Condicionais
#Nome: Arthur Rodrigues Pansera
#Turma: C

#Exercício 8
idade = int(input("Digite a sua idade: "))
if 18 <= idade <= 65:
    print("Eleitor obrigatório")
elif 16 <= idade < 18 or idade > 65:
    print("Eleitor facultativo")
else:
    print("Não eleitor")