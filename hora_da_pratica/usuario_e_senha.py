usuario_correto = "gabriel"
senha_correta = "gabriel123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Informalçoes inválidas. Tente novamente.")