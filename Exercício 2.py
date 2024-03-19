#Lista Teórica 2 - Condicionais
#Nome: Arthur Rodrigues Pansera
#Turma: C

#Exercício 2
print("Para a equação ax²+bx+c=0, digite os valores de a, b e c.")
a = int(input("Digite o primeiro coeficiente (deve ser diferente de 0): "))
b = int(input("Digite o segundo coeficiente: "))
c = int(input("Digite o terceiro coeficiente: "))
delta = b**2 - 4*a*c
valorx1 = (-b + delta**(1/2))/(2*a)
valorx2 = (-b - delta**(1/2))/(2*a)
if delta > 0:
    print(f"Há duas raízes reais distintas: {valorx1} e {valorx2}")
elif delta < 0:
    print(f"Há duas raízes imaginárias conjugadas: {valorx1} e {valorx2}")
else:
    print(f"Há duas raízes reais iguais: {valorx1} e {valorx2}")