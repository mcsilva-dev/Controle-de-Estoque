from interface import *

while True:
    cabeçalho('MENU PRINCIPAL')
    menu = opcoes(['Adicionar produto', 'Listar produtos', 'Verificar preço', 'Checar disponibilidade',
                   'Fechar sistema'])
    if menu:
        break
