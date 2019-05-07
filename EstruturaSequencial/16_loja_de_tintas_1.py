
'''
 Data: 06/05/19
 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
 quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 
 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
 Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''
tamanho = int(input('Informe a área a ser pintada em metros quadrados: '))
litros = tamanho / 3

if tamanho % 54 == 0: # % operador módulo extraí o resto da divisão e é igual a 0.
	latas = tamanho / 54
else: 
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ('Necessária(s) %d lata(s).' %latas)
print ('Valor total da(s) lata(s): R$ %.2f' %preco)

