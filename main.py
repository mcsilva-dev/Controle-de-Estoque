from interface import *

while True:
    header('MENU PRINCIPAL')
    menu = options(['Adicionar produto', 'Listar produtos', 'Verificar preço', 'Checar disponibilidade',
                   'Fechar sistema'])
    if menu:
        break
