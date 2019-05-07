'''
 Autora: Ludmyla Oliveira Soares
 Data: 28/04/19
 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo >>> A = 2(n1+n2/2))
    b. a soma do triplo do primeiro com o terceiro >>> B = (3*n1)+n3
    c. o terceiro elevado ao cubo >>> C = n3*n3*n3
'''
n1 = int(input("Informe o primeiro número inteiro: "))
n2 = int(input("Informe o segundo número inteiro: "))

n3 = float(input("Informe o número real: "))
e1 = float(2 *(n1+n2/2))
e2 = float((3*n1)+n3)
e3 = float(n3*n3*n3)
print("O produto do dobro do primeiro com metade do segundo: ", e1)
print("A soma do triplo do primeiro com o terceiro: ", e2)
print("O terceiro elevado ao cubo: ", e3)




