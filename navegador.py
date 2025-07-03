import requests
from bs4 import BeautifulSoup
import webbrowser
import urllib.parse
import os

historico = []

def limpar_tela():
    # Limpa a tela do terminal de forma cross-platform
    os.system('cls' if os.name == 'nt' else 'clear')

def buscar_no_duckduckgo(consulta, inicio=0, quantidade=10):
    url = f"https://html.duckduckgo.com/html/?q={consulta}"
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, "html.parser")

    links = soup.find_all("a", class_="result__a")
    
    print(f"\n🔎 Mostrando resultados {inicio + 1} até {inicio + quantidade}:\n")
    links_limpinhos = []

    for i, link in enumerate(links[inicio:inicio+quantidade]):
        texto = link.text.strip()
        url_suja = link['href']
        
        if "uddg=" in url_suja:
            url_limpa = urllib.parse.unquote(url_suja.split("uddg=")[-1])
        else:
            url_limpa = url_suja

        links_limpinhos.append((texto, url_limpa))

        print(f"{inicio + i + 1}. {texto or '[sem texto]'}")
        print(f"    {url_limpa}\n")

    return links_limpinhos

def exportar_links(lista_links):
    with open("resultados.txt", "w", encoding="utf-8") as f:
        for i, (texto, url) in enumerate(lista_links, start=1):
            f.write(f"{i}. {texto}\n")
            f.write(f"    {url}\n\n")
    print("✅ Links exportados para 'resultados.txt'.")

def mostrar_historico():
    if not historico:
        print("🕘 Histórico vazio.\n")
    else:
        print("\n🕘 Histórico de buscas:")
        for i, termo in enumerate(historico, 1):
            print(f"{i}. {termo}")
        print("")

def navegador_terminal():
    while True:
        limpar_tela()
        print("\n== MENU ==")
        print("1. Fazer nova busca")
        print("2. Ver histórico")
        print("3. Sair")
        escolha_menu = input("Escolha uma opção: ")

        if escolha_menu == "3":
            print("Encerrando navegador...")
            break

        elif escolha_menu == "2":
            limpar_tela()
            mostrar_historico()
            input("Pressione ENTER para voltar ao menu...")
            continue

        elif escolha_menu == "1":
            busca = input("🔍 O que deseja pesquisar? ").strip()
            if not busca:
                print("❌ Pesquisa inválida.")
                input("Pressione ENTER para voltar ao menu...")
                continue

            try:
                qtd = int(input("📄 Quantos resultados deseja ver (ex: 5, 10, 20)? "))
            except ValueError:
                print("Número inválido. Usando 5 por padrão.")
                qtd = 5

            historico.append(busca)

            indice = 0
            todos_links = []

            while True:
                limpar_tela()
                links = buscar_no_duckduckgo(busca, inicio=indice, quantidade=qtd)
                todos_links.extend(links)

                escolha = input("Digite o número do link para abrir, ou:\n"
                                "[N] Próxima página | [E] Exportar | [V] Voltar ao menu\n> ").strip().lower()

                if escolha == "n":
                    indice += qtd
                    continue

                elif escolha == "e":
                    exportar_links(todos_links)
                    input("Pressione ENTER para continuar...")
                    continue

                elif escolha == "v":
                    break

                elif escolha.isdigit():
                    num = int(escolha) - 1
                    if 0 <= num < len(todos_links):
                        url = todos_links[num][1]
                        print(f"🌐 Abrindo: {url}")
                        webbrowser.open(url)
                        input("Pressione ENTER para continuar...")
                    else:
                        print("❌ Número fora da lista.")
                        input("Pressione ENTER para continuar...")
                else:
                    print("❌ Comando inválido.")
                    input("Pressione ENTER para continuar...")
        else:
            print("❌ Opção inválida.")
            input("Pressione ENTER para continuar...")

navegador_terminal()
