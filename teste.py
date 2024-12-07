import hashlib

# Banco de dados simulado
usuarios = {}

# Função para criptografar a senha
def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para cadastrar um usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome de usuário: ")
    if nome in usuarios:
        print("Usuário já existe!")
        return
    senha = input("Senha: ")
    nivel = input("Nível de acesso (admin ou comum): ").lower()
    if nivel not in ["admin", "comum"]:
        print("Nível de acesso inválido!")
        return
    
    # Armazenar usuário no "banco de dados"
    usuarios[nome] = {
        "senha": criptografar_senha(senha),
        "nivel": nivel
    }
    print(f"Usuário '{nome}' cadastrado com sucesso!")

# Função para login
def login():
    print("\n--- Login ---")
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    senha_criptografada = criptografar_senha(senha)
    
    # Verifica se o usuário existe e a senha está correta
    if nome in usuarios and usuarios[nome]["senha"] == senha_criptografada:
        print(f"Bem-vindo, {nome}! Nível de acesso: {usuarios[nome]['nivel']}")
        return usuarios[nome]["nivel"]
    else:
        print("Usuário ou senha inválidos!")
        return None

# Função principal do sistema
def main():
    while True:
        print("\n--- Sistema de Controle de Acesso ---")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            nivel = login()
            if nivel:
                print(f"Acesso permitido como {nivel}.")
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# Iniciar o sistema
if __name__ == "__main__":
    main()