#Lista Teórica 2 - Condicionais
#Nome: Arthur Rodrigues Pansera
#Turma: C

#Exercício 5
sexo = int(input("Escolha o seu sexo: 1 - Masculino ou 2 - Feminino: "))
h = float(input("Informe a sua altura em metros: "))
if sexo == 1:
    peso_ideal = (72.7 * h) - 58
    print(f"Seu peso ideal é: {peso_ideal}")
elif sexo == 2:
    peso_ideal = (62.1 * h) - 44.7
    print(f"Seu peso ideal é: {peso_ideal}")
else:
    print("Erro")