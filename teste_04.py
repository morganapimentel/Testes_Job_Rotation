faturamento = [
    ('SP' ,6783643), ('RJ' , 3667866), ('MG' , 2922988), ('ES', 2716548), ('Outros', 1984953)]
soma = 0
print('Percentual de faturamento referente a cada estado:')
print('--------------------------------------------------')
for item in faturamento:
    estado, valor = item
    soma += valor
    print(f'{estado} com {valor/ soma:.1%}')
