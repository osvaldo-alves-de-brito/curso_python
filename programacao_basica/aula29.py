
# try , except


numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2 :.2f}')
    
except:
    print('Isso não é um número')



# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2 :.2f}')

# else:
#     print('Isso não é um número')