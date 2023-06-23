import string

from interface import header


def option(n):
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
                return add_products()
            elif opc == 2:
                return list_products()
            elif opc == 3:
                return check_price('CHECAR PREÇO')
            elif opc == 4:
                return check_availability('DISPONIBILIDADE DE PRODUTOS')
            elif opc == 5:
                return True


def add_products():
    name = manage_errors('Nome do produto: ', str)
    quantidade = manage_errors('Quantidade: ', int)
    price = manage_errors('Preço: ', float)
    while True:
        try:
            file = open('Estoque.txt', 'at')
            file.write(f'{name}:')
            file.write(f'{quantidade}:')
            file.write(f'{price}')
            file.write('\n')
            file.close()
        except FileNotFoundError:
            create_file()
        except Exception as erro:
            print(f'ERRO: {erro.__class__}')
        else:
            if quantidade > 1:
                print(f'Foram adicionados(as) {quantidade} de {name} no estoque.')
            else:
                print(f'Foi adicionado(a) {quantidade} de {name} no estoque.')
            break


def list_products():
    while True:
        try:
            file = open('Estoque.txt', 'rt')
        except FileNotFoundError:
            create_file()
        except Exception as erro:
            print(f'ERRO: {erro.__class__}')
        else:
            break
    header('PRODUTOS EM ESTOQUE')
    for line, product in enumerate(file.readlines()):
        element = product.replace('\n', '').split(':')
        print(f"{line + 1} - {element[0]:<25}")


def check_price(text):
    header(text)
    return products(text)


def check_availability(text):
    header(text)
    return products(text)


def manage_errors(text, txt_type):
    while True:
        try:
            element = txt_type(input(text))
            if txt_type == str:
                for letra in element:
                    if letra in string.punctuation:
                        raise TypeError
                if element.isdigit():
                    raise TypeError
                element = ' '.join(element.split())
            elif txt_type == int:
                if element < 0:
                    raise IndexError
        except (ValueError, TypeError):
            print('ERRO: O dado fornecido está incorreto!')
        except KeyboardInterrupt:
            print('O usuário solicitou interrupção.')
            if txt_type == str:
                return '<desconhecido>'
            elif txt_type == float:
                return 0.0
            elif txt_type == int:
                return 0
        except IndexError:
            print("ERRO: o valor informado é inválido.")
        except Exception as erro:
            print(f'ERRO: {erro.__class__}')
        else:
            if txt_type(element) == type:
                return txt_type(element)


def create_file():
    return open('Estoque.txt', 'wt+')


def products(text):
    file = open('Estoque.txt', 'rt').readlines()
    c = 1
    for product in file:
        n = product.replace('\n', '').split(':')
        print(f"{c} - {n[0]}")
        c += 1
    while True:
        try:
            product = int(input('Produto: '))
            if product == 0 or product > c:
                raise IndexError
        except (TypeError, ValueError):
            print('ERRO: Digite um número inteiro.')
        except IndexError:
            print('ERRO: Opção inválida')
        except FileNotFoundError:
            create_file()
        except KeyboardInterrupt:
            print('O usuário solicitou interrupção.')
            return True
        else:
            break
    c = 1
    for lines in file:
        line = lines.replace('\n', '').split(':')
        if c == product:
            if text == 'CHECAR PREÇO':
                print(f"Produto: {line[0]:<20}preço: R${line[2]}")
            elif text == 'DISPONIBILIDADE DE PRODUTOS':
                if int(line[1]) == 0:
                    print('\033[31mPRODUTO INDISPONIVEL!\033[m')
                if int(line[1]) > 0:
                    print('\033[32mPRODUTO DISPONÍVEL!\033[m')
                    print(f'Quantidade em estoque: {line[1]}')
            break
        c += 1
