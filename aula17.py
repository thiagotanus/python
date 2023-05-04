
import os

lista = []

while True:
   
    inicio = input("O que você deseja?" '\n'
    "[a] apagar [i] inserir, [l] listar") 
   
    if len(inicio) > 1:
       print("Digite apenas [a], [i] ou [l]")
       os.system("cls")
       
    elif inicio == "i":
        inserir = input("Digite o item a ser inserido ")
        lista.append (inserir)                   
        print(f"O item {inserir} foi adicionado")
        os.system("cls")
            
            
    elif inicio == "a":
        apagar = input("Digite o código do item a ser apagado ")
        apagar_01 = int(apagar)
        del lista[apagar_01]
        os.system("cls")
        
        
    elif inicio == "l":
        for item in enumerate(lista):
            print(item)
        
        



