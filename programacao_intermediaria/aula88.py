# valores Truthy e Falsy, tipos mutaveis e imutaveis
# Mutaveis: list(), dict(), set()
# Imutaveis: int, float, str, bool, None, range()

# valores considerados False
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste {falsy('teste')}')
print(f'{lista=} {falsy(lista)}')
print(f'{dicionario=} {falsy(dicionario)}')
print(f'{conjunto=} {falsy(conjunto)}')
print(f'{tupla=} {falsy(tupla)}')
print(f'{string=} {falsy(string)}')
print(f'{inteiro=} {falsy(inteiro)}')
print(f'{flutuante=} {falsy(flutuante)}')
print(f'{nada=} {falsy(nada)}')
print(f'{falso=} {falsy(falso)}')
print(f'{intervalo=} {falsy(intervalo)}')