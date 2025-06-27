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

def avaliar_forca(senha):
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero    = any(c.isdigit() for c in senha)
    tem_simbolo   = any(c in string.punctuation for c in senha)

    pontuacao = sum([tem_maiuscula, tem_minuscula, tem_numero, tem_simbolo])

    if len(senha) >= 12 and pontuacao == 4:
        return "💪 Forte"
    elif len(senha) >= 8 and pontuacao >= 3:
        return "🟡 Média"
    else:
        return "🔴 Fraca"        
        
  
def menu():
    senha_gerada = None
    while True:  
        print(f"\n=== MENU DE OPÇÕES ===\n")
        print(f"- 1 Gerar senha")
        print(f"- 2 Mostrar histórico")
        print(f"- 3 Salvar senha gerada")
        print(f"- 4 Gerar várias senhas")
        print(f"- 5 Avaliar força de senha salva")
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
        
        elif opcao == "5":
            try:
                with open("gerador.txt", "r") as arquivo:
                    senhas = arquivo.readlines()
                    if not senhas:
                        print("⚠️ Nenhuma senha salva no histórico.")
                        continue
                    
                    print("\n📜 Senhas salvas:")
                    for i, senha in enumerate(senhas, start=1):
                        print(f"{i} - {senha.strip()}")

                    escolha = int(input("Digite o número da senha que deseja avaliar: "))
                    if 1 <= escolha <= len(senhas):
                        senha_escolhida = senhas[escolha - 1].strip()
                        resultado = avaliar_forca(senha_escolhida)
                        print(f"🔎 Senha: {senha_escolhida}\n📊 Força: {resultado}")
                    else:
                        print("❌ Número inválido.")
            except FileNotFoundError:
                print("⚠️ Nenhum histórico encontrado.")              

        elif opcao == "0":
            print("👋 Encerrando o programa...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")
            
            
menu()
