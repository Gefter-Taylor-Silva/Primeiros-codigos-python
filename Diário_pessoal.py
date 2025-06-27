def escrever_no_diario():
    texto = input("Escreva algo no diário: ")
    
    with open("diario.txt", "a") as arquivo:
        arquivo.write(texto + "\n")
    print("✅ Registro adicionado com sucesso!!")

def mostrar_registro():
    print("\n📘 Registros do Diário:")
    with open("diario.txt", "r") as arquivo:
        for linha in arquivo:
            print("-", linha.strip())

def remover_registro():
    with open("diario.txt", "r") as arquivo:
        mostrar = arquivo.readlines()

    if not mostrar:
        print("🚫 O diário está vazio.")
        return

    print("\n🗑️ Registros disponíveis para remoção:")
    for i, linha in enumerate(mostrar, start=1):
        print(f"{i} - {linha.strip()}")    

    try:
        remover = int(input("Remova um registro pelo número: "))
        if 1 <= remover <= len(mostrar):
            removido = mostrar.pop(remover - 1)
            with open("diario.txt",  "w") as arquivo:
                arquivo.writelines(mostrar)
            print(f"✅ Registro removido: {removido.strip()}")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")

# 🔁 Menu interativo
while True:    
    print("\n📒 MENU DO DIÁRIO:")
    print("1 - Escrever no diário")
    print("2 - Listar registros")
    print("3 - Remover registro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ") 

    if opcao == "1":
        escrever_no_diario()       
    elif opcao == "2":
        mostrar_registro()
    elif opcao == "3":
        remover_registro()
    elif opcao == "0":
        print("👋 Encerrando o diário. Até mais!")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")
