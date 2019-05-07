'''
 Autora: Ludmyla Oliveira Soares
 Data: 28/04/19
 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
   
   >>> ÍNDICE DE MASSA CORPORAL <<<
   Após a realização do cálculo, deve-se observar o resultado de acordo com os seguintes valores:
    - Abaixo de 18,5 = desnutrição
    - Entre 18,5 e 24,5 = peso normal
    - Entre 25,0 e 29,9 = sobrepeso
    - Entre 30,0 e 39,9 = Obesidade
    - Acima de 40,0 = Obesidade Mórbida
'''
altura = float(input("Informe a altura: "))
pesoh = float(72.7*altura) - 58.0
pesom = float(62.1*altura) - 44.7
print("O peso ideal para homem é: ", pesoh)
print("O peso ideal para mulher é: ", pesom)