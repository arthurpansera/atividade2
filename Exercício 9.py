#Lista Teórica 2 - Condicionais
#Nome: Arthur Rodrigues Pansera
#Turma: C

#Exercício 9
idade = int(input("Digite a sua idade: "))
tempo_de_servico = int(input("Digite o seu tempo de serviço: "))
if idade >= 65:
    print("Aposentadoria por idade")
elif tempo_de_servico >= 30:
    print("Aposentadoria por tempo de serviço")
elif idade >= 60 and tempo_de_servico >= 25:
    print("Aposentadoria por idade e tempo de serviço")
else:
    print("Aposentadoria não permitida")