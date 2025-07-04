import csv
import os

# ====== CONFIGURAÇÃO INICIAL ======

ARQUIVO_GASTOS = "gastos_semanais.csv"
renda = 3500.00

gastos_fixos = {
    "Netflix": 22.00,
    "Internet": 70.00,
    "Água": 60.00,
    "Luz": 250.00,
    "Gás": 100.00,
    "Compras Atacado": 800.00
}

gastos_variaveis_estimados = 2500.00
meta_economia = 400.00
gastos_semanais = []

# ====== FUNÇÕES DE ARQUIVO ======

def salvar_gastos_csv(gastos, arquivo=ARQUIVO_GASTOS):
    with open(arquivo, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Semana", "Valor"])
        for i, valor in enumerate(gastos, start=1):
            writer.writerow([i, valor])

def carregar_gastos_csv(arquivo=ARQUIVO_GASTOS):
    gastos = []
    if os.path.exists(arquivo):
        with open(arquivo, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    gastos.append(float(row["Valor"]))
                except:
                    pass
    return gastos

# ====== FUNÇÕES DE TABELA ======

def imprimir_tabela(titulo, dados):
    print("\n" + titulo)
    print("=" * len(titulo))
    for item, valor in dados:
        print(f"{item:<25} R$ {valor:>10.2f}")
    print()

def mostrar_tabela_1():
    total_fixos = sum(gastos_fixos.values())
    total_geral = total_fixos + gastos_variaveis_estimados
    excedente = total_geral - renda
    tabela1 = [
        ("Renda Mensal", renda),
        ("Gastos Fixos", total_fixos),
        ("Gastos Variáveis (estimados)", gastos_variaveis_estimados),
        ("Total Gasto", total_geral),
        ("Excedente / Dívida", excedente)
    ]
    imprimir_tabela("TABELA 1: RESUMO DOS GASTOS ATUAIS", tabela1)

def mostrar_tabela_2():
    total_fixos = sum(gastos_fixos.values())
    limite_total_variavel = renda - total_fixos - meta_economia
    limite_diario = limite_total_variavel / 30
    tabela2 = [
        ("Meta de Economia", meta_economia),
        ("Gastos Fixos", total_fixos),
        ("Limite para Variáveis", limite_total_variavel),
        ("Limite Diário Ideal", limite_diario)
    ]
    imprimir_tabela("TABELA 2: PLANEJAMENTO PARA ECONOMIZAR R$ 400", tabela2)

def imprimir_tabela_semanal():
    total = sum(gastos_semanais)
    total_fixos = sum(gastos_fixos.values())
    limite_total_variavel = renda - total_fixos - meta_economia
    limite_diario = limite_total_variavel / 30

    print("\nTABELA 3: GASTOS SEMANAIS ATUALIZADA")
    print("=" * 32)
    for i, v in enumerate(gastos_semanais, start=1):
        print(f"Semana {i:<2} {'':5} R$ {v:10.2f}")
    print(f"{'-'*30}\nTOTAL GASTO {'':11} R$ {total:10.2f}\n")

    # 🔔 ALERTAS
    if total > limite_total_variavel:
        print(f"⚠️ ATENÇÃO: Você já ultrapassou o limite de gastos variáveis!\n"
              f"Limite: R$ {limite_total_variavel:.2f} | Gasto atual: R$ {total:.2f}")
    else:
        restante = limite_total_variavel - total
        print(f"✅ Você ainda pode gastar R$ {restante:.2f} em variáveis este mês.")

    dias_passados = len(gastos_semanais) * 7
    if dias_passados > 0:
        gasto_diario_medio = total / dias_passados
        if gasto_diario_medio > limite_diario:
            print(f"⚠️ Gasto diário médio: R$ {gasto_diario_medio:.2f} (acima do ideal de R$ {limite_diario:.2f}/dia)")
        else:
            print(f"✅ Gasto diário médio: R$ {gasto_diario_medio:.2f} (dentro do ideal de R$ {limite_diario:.2f}/dia)")

# ====== FUNÇÕES DE REGISTRO E EDIÇÃO ======

def registrar_gasto_semanal():
    print("\nREGISTRO DE GASTOS SEMANAIS")
    while True:
        try:
            semana = len(gastos_semanais) + 1
            valor = input(f"Gastos da semana {semana} (ou ENTER para parar): ").strip()
            if valor == "":
                break
            valor = float(valor)
            gastos_semanais.append(valor)
            salvar_gastos_csv(gastos_semanais)
            imprimir_tabela_semanal()
        except ValueError:
            print("Digite um número válido!")

def editar_tabela_1():
    global renda, gastos_variaveis_estimados
    print("\nEDITAR TABELA 1: GASTOS ATUAIS")
    print("1. Alterar Renda Mensal")
    print("2. Alterar Gastos Fixos")
    print("3. Alterar Gastos Variáveis Estimados")
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        renda = float(input("Nova renda mensal: R$ "))
    elif opcao == "2":
        print("Gastos fixos atuais:")
        for i, (nome, valor) in enumerate(gastos_fixos.items(), start=1):
            print(f"{i}. {nome}: R$ {valor:.2f}")
        idx = int(input("Digite o número do item que deseja alterar: "))
        novo_valor = float(input("Novo valor: R$ "))
        chave = list(gastos_fixos.keys())[idx - 1]
        gastos_fixos[chave] = novo_valor
    elif opcao == "3":
        gastos_variaveis_estimados = float(input("Novo valor de gastos variáveis estimados: R$ "))
    else:
        print("Opção inválida.")
    
    mostrar_tabela_1()
    mostrar_tabela_2()

def editar_tabela_2():
    global meta_economia
    print("\nEDITAR TABELA 2: PLANEJAMENTO DE ECONOMIA")
    meta_economia = float(input("Nova meta de economia mensal: R$ "))
    mostrar_tabela_2()

def editar_tabela_3():
    print("\nEDITAR TABELA 3: GASTOS SEMANAIS")
    imprimir_tabela_semanal()
    try:
        semana = int(input("Número da semana que deseja editar: "))
        if 1 <= semana <= len(gastos_semanais):
            novo_valor = float(input(f"Novo valor para semana {semana}: R$ "))
            gastos_semanais[semana - 1] = novo_valor
            salvar_gastos_csv(gastos_semanais)
            imprimir_tabela_semanal()
        else:
            print("Semana inválida.")
    except:
        print("Erro na edição. Tente novamente.")

# ====== MENU PRINCIPAL ======

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Ver Tabela 1 - Resumo dos Gastos Atuais")
        print("2. Ver Tabela 2 - Planejamento para Economizar")
        print("3. Ver Tabela 3 - Gastos Semanais")
        print("4. Registrar Novo Gasto Semanal")
        print("5. Editar Tabela 1")
        print("6. Editar Tabela 2")
        print("7. Editar Tabela 3")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            mostrar_tabela_1()
        elif escolha == "2":
            mostrar_tabela_2()
        elif escolha == "3":
            imprimir_tabela_semanal()
        elif escolha == "4":
            registrar_gasto_semanal()
        elif escolha == "5":
            editar_tabela_1()
        elif escolha == "6":
            editar_tabela_2()
        elif escolha == "7":
            editar_tabela_3()
        elif escolha == "0":
            print("Saindo... Seus dados foram salvos.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# ====== INÍCIO DO PROGRAMA ======

gastos_semanais = carregar_gastos_csv()
menu_principal()
