entrada = input('[E]ntrar [S]air:')
senha_digitada = input("senha:")

senha_permitida = "123"

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")