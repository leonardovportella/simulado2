# 1- Faca um for loop no dicionario e exiba os valores de cada tipo: 
tipos_cores = {
    'primaria': ['vermelho', 'azul', 'amarelo'],
    'secundaria': ['verde', 'laranja', 'roxo'],
    }

for key, value in tipos_cores.items():
    print(value)
for key, value in tipos_cores.items():
    for cor in value:
        print(cor)


# 2 - Faca um for loop na lista e mostre qual tipo ela é
lst_cores = ['vermelho', 'roxo', 'preto'] 
for cor in lst_cores:
    if cor in tipos_cores['primaria']:
        print(f"{cor} é primaria")
    elif cor in tipos_cores['secundaria']:
        print(f"{cor} é secundaria")
    else:
        print(f"{cor} é neutra")




# 3 – Verifique o total da compra baseado no preco
precos = {
    'camiseta': 100.00,
    'tenis': 900.00,
    'meia': 45.00,
    'blusa': 245.00,
    'calça': 145.00,
    'luva': 18.00,
    }

compra = ['luva', 'blusa', 'tenis']
valor_compra = precos['luva'] + precos['blusa'] + precos['tenis']
print(valor_compra)

total_compra = 0
for item in compra:
    preco = precos[item]
    total_compra = total_compra + preco
print(f"O total da compra é {total_compra}")


# 4 – Faca uma funcao que entre 3 notas e calcule a media final de acordo com o crirterio de nota do ibmec
# Crie uma pasta meu_pacote e grava essa funcao la dentro
# Importe a funcao, e chame ela, calculando a media final
p1 = 8.5
p2 = 9.0
ac = 1.0
from meu_pacote.modulo import calcular_nota
nota_final = calcular_nota(p1, p2, ac)
print(f"A nota final foi {nota_final}")