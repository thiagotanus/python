# def imprimir(a, b, c):
#     print(a, b, c)
    
# imprimir(1, 2, 3)
# imprimir(4, 5, 6)


# def saudacao(nome):
#     print(f'Olá, {nome}')

# saudacao("Murilo")

# def soma(x, y):
#     print(f'{x=} + {y=}', '|', 'x + y = ', x + y)
    
# soma(1, 2)
# print(1, 2, 3, sep="-")


# def soma(x, y, z=None):
#     if z is not None:
#       print(x + y + z)
#     else:
#       print(x + y)
  
  

# soma(1, 2, 3)
# soma( 3, 5)
# soma(100, 200)

# def escopo():
#     x = 1
#     print(x)
    
# escopo()


# def soma(x, y, z=None):
#     if z is not None:
#       print(x + y + z)
#     else:
#       print(x + y)
  
  

# soma(1, 2, 3)
# soma( 3, 5)
# soma(100, 200)




def multriplicar (*args):
    total = 1
    for numero in args:
        total += numero
        return total

multiplicacao = multriplicar(1, 2, 3, 4, 5)
print(multiplicacao)
     
