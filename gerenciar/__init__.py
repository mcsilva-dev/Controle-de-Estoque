import string

from interface import cabeçalho


def opcao(n):
    while True:
        try:
            opc = int(input('Sua opção: '))
            if opc > n or opc <= 0:
                raise IndexError
        except IndexError:
            print(f'ERRO: Opção inválida, informe um valor entre 1 e {n}')
        except ValueError:
            print('ERRO: Opção inválida, digite um número inteiro!')
        except KeyboardInterrupt:
            print('O usuário solicitou interrupção.')
            return True
        else:
            if opc == 1:
                return adicionar_produto()
            elif opc == 2:
                return listar_produtos()
            elif opc == 3:
                return verificar_preco('CHECAR PREÇO')
            elif opc == 4:
                return checar_disponibilidade('DISPONIBILIDADE DE PRODUTOS')
            elif opc == 5:
                return True


def adicionar_produto():
    nome = trata_erro('Nome do produto: ', str)
    quantidade = trata_erro('Quantidade: ', int)
    preco = trata_erro('Preço: ', float)
    while True:
        try:
            arquivo = open('Estoque.txt', 'at')
            arquivo.write(f'{nome}:')
            arquivo.write(f'{quantidade}:')
            arquivo.write(f'{preco}')
            arquivo.write('\n')
            arquivo.close()
        except FileNotFoundError:
            criar_arquivo()
        except Exception as erro:
            print(f'ERRO: {erro.__class__}')
        else:
            if quantidade > 1:
                print(f'Foram adicionados(as) {quantidade} de {nome} no estoque.')
            else:
                print(f'Foi adicionado(a) {quantidade} de {nome} no estoque.')
            break


def listar_produtos():
    arquivo = open('Estoque.txt', 'rt')
    cabeçalho('PRODUTOS EM ESTOQUE')
    for linha, produto in enumerate(arquivo.readlines()):
        elemento = produto.replace('\n', '').split(':')
        print(f"{linha + 1} - {elemento[0]:<25}")


def verificar_preco(text):
    cabeçalho(text)
    return produtos(text)


def checar_disponibilidade(text):
    cabeçalho(text)
    return produtos(text)


def trata_erro(text, tipo):
    while True:
        try:
            elemento = tipo(input(text))
            if tipo == str:
                for letra in elemento:
                    if letra in string.punctuation:
                        raise TypeError
                if elemento.isdigit():
                    raise TypeError
                elemento = ' '.join(elemento.split())
            elif tipo == int:
                if elemento < 0:
                    raise IndexError
        except (ValueError, TypeError):
            print('ERRO: O dado fornecido está incorreto!')
        except KeyboardInterrupt:
            print('O usuário solicitou interrupção.')
            if tipo == str:
                return '<desconhecido>'
            elif tipo == float:
                return 0.0
            elif tipo == int:
                return 0
        except IndexError:
            print("ERRO: o valor informado é inválido.")
        except Exception as erro:
            print(f'ERRO: {erro.__class__}')
        else:
            if type(elemento) == tipo:
                return tipo(elemento)


def criar_arquivo():
    return open('Estoque.txt', 'wt+')


def produtos(text):
    arquivo = open('Estoque.txt', 'rt').readlines()
    c = 1
    for produto in arquivo:
        n = produto.replace('\n', '').split(':')
        print(f"{c} - {n[0]}")
        c += 1
    while True:
        try:
            produto = int(input('Produto: '))
            if produto == 0 or produto > c:
                raise IndexError
        except (TypeError, ValueError):
            print('ERRO: Digite um número inteiro.')
        except IndexError:
            print('ERRO: Opção inválida')
        except KeyboardInterrupt:
            print('O usuário solicitou interrupção.')
            return True
        else:
            break
    c = 1
    for linhas in arquivo:
        linha = linhas.replace('\n', '').split(':')
        if c == produto:
            if text == 'CHECAR PREÇO':
                print(f"Produto: {linha[0]:<20}preço: R${linha[2]}")
            elif text == 'DISPONIBILIDADE DE PRODUTOS':
                if int(linha[1]) == 0:
                    print('\033[31mPRODUTO INDISPONIVEL!\033[m')
                if int(linha[1]) > 0:
                    print('\033[32mPRODUTO DISPONÍVEL!\033[m')
                    print(f'Quantidade em estoque: {linha[1]}')
            break
        c += 1
