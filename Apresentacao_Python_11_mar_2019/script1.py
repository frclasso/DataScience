

# variaveis
#
nome = input('Digite seu nome')
s_nome = input('Digite sobrenome')
cargo = input('Digite cargo')
email = nome+s_nome+'@email.com'

pessoas = []
pessoas.append(nome)
pessoas.append(s_nome)
pessoas.append(cargo)
pessoas.append(email)

print(pessoas)

with open('cadastro.csv', 'a') as f:
        for line in pessoas:
            f.write(line + ',')
        f.write('\n')

print('Ok..')