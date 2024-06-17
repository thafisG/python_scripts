def acesso_a_fortaleza(login, senha):
    login_str = ''.join(str(num) for num in login)  # converte converte converte
    senha_str = ''.join(str(num) for num in senha) # converte converte converte
    # eita como gosta de exibir 
    print("As credenciais de acesso da área secreta da fortaleza foram decodificadas com sucesso!")
    print(f"Login: {login_str}")
    print(f"Senha: {senha_str}")

# login usuario da diva
def login_usuario(entrada_codigo):
    login = []
    for numero in entrada_codigo:
        somatorio = 0
        for i in range(numero, -1, -1):
            if i % 2 == 0:
                somatorio += i * 2
            else:
                somatorio += i * 3
        login.append(somatorio)
    
    return login

# Função fatorial_senha para auxiliar na fatoração (se é q essa palavra existe)
def fatorial_senha(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fatorial_senha(numero - 1)

# função para a senha dessa querida
def senha_usuario(entrada_codigo):
    senha = []
    for numero in entrada_codigo:
        numero_fatorado = fatorial_senha(numero)
        senha.append(numero_fatorado)
    return senha

# Entrada do usuário
entrada_codigo = input().split(":")
entrada_codigo = [int(numero) for numero in entrada_codigo]

# Chamada das funções 
login_decifrado = login_usuario(entrada_codigo)
senha_decifrada = senha_usuario(entrada_codigo)
acesso_a_fortaleza(login_decifrado, senha_decifrada)
