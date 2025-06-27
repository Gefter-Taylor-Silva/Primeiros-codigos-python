import random 
import string 


def gerador_de_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choices(caracteres, k=tamanho))
    print(f"senha gerada: {senha}")
    return senha

def gerar_varias_senhas(qtd, tamanho):
    senhas = []
    for _ in range(qtd):
        senha = gerador_de_senha(tamanho)
        senhas.append(senha)
    return senhas
    
def mostrar_historico():
    with open("gerador.txt",  "r") as arquivo:
        for i, linha in enumerate(arquivo, start=1):
            print(f"{i} - {linha.strip()}")

def salvar_senhas(senha):
    with open("gerador.txt", "a") as arquivo:
        arquivo.write(senha + "\n")
        print(f"Senha {senha} salva com sucesso!!")
        
  
  
def menu():
    senha_gerada = None
    while True:  
        print(f"\n=== MENU DE OPÇÕES ===\n")
        print(f"- 1 Gerar senha")
        print(f"- 2 Mostrar histórico")
        print(f"- 3 Salvar senha gerada")
        print(f"- 4 Gerar várias senhas")
        print(f"- 0 Sair do programa\n")
    
        opcao = input("- Escolha a Opção: ")
    
        if opcao == "1":
            tamanho = int(input("Qual o tamanho da senha que deseja gerar? "))
            senha_gerada = gerador_de_senha(tamanho)

        elif opcao == "2":  
            mostrar_historico() 

        elif opcao == "3":
            if senha_gerada:
                salvar_senhas(senha_gerada)
            else:
                print("⚠️ Nenhuma senha foi gerada ainda!")

        elif opcao == "4":
            try:
                qtd = int(input("Quantidade de senhas que deseja: "))
                tamanho = int(input("Qual o tamanho das senhas que deseja gerar? "))
                senhas = gerar_varias_senhas(qtd, tamanho)
                for s in senhas:
                    salvar_senhas(s)
            except ValueError:
                print(f"❌ Digite apenas números válidos!!")       

        elif opcao == "0":
            print("👋 Encerrando o programa...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")
menu()
