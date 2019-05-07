'''
 Autora: Ludmyla Oliveira Soares
 Data: 28/04/19
 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a 
    seguinte fórmula: (72.7*altura) - 58
   
   >>> ÍNDICE DE MASSA CORPORAL <<<
   Após a realização do cálculo, deve-se observar o resultado de acordo com os seguintes valores:
    - Abaixo de 18,5 = desnutrição
    - Entre 18,5 e 24,5 = peso normal
    - Entre 25,0 e 29,9 = sobrepeso
    - Entre 30,0 e 39,9 = Obesidade
    - Acima de 40,0 = Obesidade Mórbida
'''
altura = float(input("Informe a altura: "))
peso = float(72.7*altura) - 58
print("Seu peso ideal é: ", peso)

