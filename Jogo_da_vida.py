import json
import os

# === Funções de utilidade ===

def salvar_jogo(dados, nome_arquivo="progresso_jogo.json"):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f)

def carregar_jogo(nome_arquivo="progresso_jogo.json"):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    else:
        return None

def calcular_nivel(renda):
    if renda <= 50:
        return "Nível 1 - Sobrevivente"
    elif renda <= 150:
        return "Nível 2 - Iniciante"
    elif renda <= 300:
        return "Nível 3 - Explorador"
    elif renda <= 600:
        return "Nível 4 - Construtor"
    elif renda <= 1000:
        return "Nível 5 - Estável"
    elif renda <= 2000:
        return "Nível 6 - Desenvolvedor"
    else:
        return "Nível 7 - Mestre da Jornada"

# === Ações do jogo ===

def realizar_acao(jogador):
    print("\nO que você quer fazer hoje?")
    print("1. Trabalhar")
    print("2. Estudar")
    print("3. Descansar")
    print("4. Socializar")
    print("5. Ver status")
    print("6. Sair e salvar")

    escolha = input("Escolha sua ação: ")

    if escolha == '1':
        jogador["dinheiro"] += 50
        jogador["saude"] -= 10
        jogador["relacionamentos"] -= 5
        print("Você trabalhou! Ganhou R$50.")
    
    elif escolha == '2':
        jogador["conhecimento"] += 10
        jogador["disciplina"] += 5
        jogador["saude"] -= 5
        jogador["dinheiro"] -= 20
        print("Você estudou! Aprendeu algo novo.")
    
    elif escolha == '3':
        jogador["saude"] += 10
        jogador["disciplina"] += 5
        print("Você descansou bem. Recuperou saúde.")
    
    elif escolha == '4':
        jogador["relacionamentos"] += 10
        jogador["disciplina"] -= 5
        jogador["dinheiro"] -= 15
        print("Você socializou e fortaleceu laços.")
    
    elif escolha == '5':
        mostrar_status(jogador)
    
    elif escolha == '6':
        salvar_jogo(jogador)
        print("Progresso salvo. Até a próxima!")
        exit()

    else:
        print("Opção inválida.")

def mostrar_status(jogador):
    nivel = calcular_nivel(jogador["dinheiro"])
    print("\n=== STATUS ATUAL ===")
    print(f"Nível: {nivel}")
    print(f"💰 Dinheiro: R$ {jogador['dinheiro']}")
    print(f"💪 Saúde: {jogador['saude']}")
    print(f"🧠 Conhecimento: {jogador['conhecimento']}")
    print(f"⏱️ Disciplina: {jogador['disciplina']}")
    print(f"❤️ Relacionamentos: {jogador['relacionamentos']}")
    print("====================\n")

# === Início do jogo ===

def novo_jogo():
    return {
        "dinheiro": float(input("Digite sua renda semanal inicial (R$): ")),
        "saude": 50,
        "conhecimento": 10,
        "disciplina": 10,
        "relacionamentos": 10
    }

def menu():
    print("=== JOGO DA VIDA ===")
    print("1. Novo Jogo")
    print("2. Continuar Jogo")
    print("3. Sair")
    return input("Escolha uma opção: ")

# === Loop principal ===

while True:
    opcao = menu()

    if opcao == '1':
        jogador = novo_jogo()
        break
    elif opcao == '2':
        progresso = carregar_jogo()
        if progresso:
            jogador = progresso
            print("Jogo carregado com sucesso.")
            break
        else:
            print("Nenhum jogo salvo encontrado.")
    elif opcao == '3':
        print("Até a próxima!")
        exit()
    else:
        print("Opção inválida.")

# Loop do jogo
while True:
    realizar_acao(jogador)
    salvar_jogo(jogador)
