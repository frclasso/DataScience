#!/usr/bin/env python3

# Cálculo do IMC

familia = [
    ['Fabio', 1.82, 82],
    ['Juliana', 1.78,80],
    ['Taíssa', 1.77, 78],
    ['Erick', 1.20, 45],
    ['Gigi', 1.00, 25]
]

for linha in familia:
    nome = linha[0]
    altura = linha[1]
    peso = linha[2]
    imc = round(altura / peso**2, 5)
    print('Nome:{}, Altura:{}, Peso:{}, IMC:{}'.format(nome, altura, peso, imc))

print()

# from numpy import array
#
# np_fam = array(familia)
#
# print(np_fam)