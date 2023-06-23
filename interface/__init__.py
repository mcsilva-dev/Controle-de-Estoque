def header(text):
    print(line())
    print(f'{text}'.center(50))
    print(line())


def line(tam=50):
    return '-' * tam


def options(text):
    from manage import option
    for x in range(0, len(text)):
        print(f"{x + 1} - {text[x]}")
    print(line())
    return option(len(text))
