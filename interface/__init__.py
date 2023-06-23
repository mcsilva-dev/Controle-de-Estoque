def cabeçalho(text):
    print(linha())
    print(f'{text}'.center(50))
    print(linha())


def linha(tam=50):
    return '-' * tam


def opcoes(text):
    from gerenciar import opcao
    for x in range(0, len(text)):
        print(f"{x + 1} - {text[x]}")
    print(linha())
    return opcao(len(text))
