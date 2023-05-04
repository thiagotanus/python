
import os


palavra_secreta = "laura"
numero_tentativas = 0
caract = "*"
letra_acertadas = ""
incorreta = ""


while True:
    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1  
    
    
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue
    
          
    if letra_digitada in palavra_secreta:
       letra_acertadas += letra_digitada
    
    palavra_formada = ""
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
        
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("Você ganhou")
    
    
    
    
    

    
    
        
    
    
    
    
        
       
    
    
    


