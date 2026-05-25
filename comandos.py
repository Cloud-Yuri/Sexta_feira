import os
import subprocess
import pyautogui
import webbrowser

from voz import ouvir_comando, aguardar_palavra_ativacao


def mostrar_help():
    print("""
========== AJUDA - SEXTA-FEIRA ==========

GESTOS:
- Paz por 3s: ativa a Sexta-feira
- 1 dedo: escuta um comando por voz
- Mão fechada: fecha a janela atual
- Mão aberta: abre o Explorador de Arquivos
- Joinha: abre a pesquisa do Windows
- 4 dedos: abre o menu Iniciar
- 3 dedos por 3s: encerra a Sexta-feira

COMANDOS DE AJUDA:
- help
- ajuda
- comandos

COMANDOS DE VOZ:
- ouvir
- escutar
- voz
- modo voz
- ativar voz
- escuta

COMANDOS DE DITADO:
- digitar
- ditar
- modo texto
- modo escrito

COMANDOS PARA ABRIR:
- abrir chrome
- abrir explorador
- abrir pesquisa
- abrir youtube
- abrir github
- abrir google
- abrir chatgpt
- abrir gmail
- abrir drive
- abrir vscode
- abrir bloco de notas

Também aceita variações:
- abre o youtube
- abre a pesquisa
- abre o vscode
- abrir o chrome

COMANDOS DE PESQUISA:
- pesquisar <termo>
- abrir site <nome ou url>

GUIAS / ABAS:
- abrir guia
- abrir nova guia
- nova guia
- abrir aba
- nova aba
- fechar guia
- fechar aba
- fechar tab

JANELAS:
- fechar janela
- fechar

COMANDOS SENSÍVEIS:
- desligar pc
- desligar computador
- desligar tudo
- reiniciar pc
- reiniciar computador
- reinicia
- reiniciar tudo
- suspender pc
- suspender computador
- suspende
- cancelar desligamento
- cancelar shutdown

Obs: comandos sensíveis pedem confirmação com 'sim'.

=========================================
""")


def confirmar_acao(mensagem):
    resposta = input(f"{mensagem} Digite 'sim' para confirmar: ")
    return resposta.lower().strip() == "sim"


def abrir_site(nome_site):
    sites = {
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "google": "https://www.google.com",
        "chatgpt": "https://chatgpt.com",
        "gmail": "https://mail.google.com",
        "drive": "https://drive.google.com",
    }

    if nome_site in sites:
        webbrowser.open(sites[nome_site])
    else:
        webbrowser.open(f"https://www.google.com/search?q={nome_site}")

def extrair_alvo_abrir(comando):
    prefixos = [
        "abrir ",
        "abre o ",
        "abre a ",
        "abre ",
        "abre os ",
        "abre as ",
        "abrir o ",
        "abrir a ",
        "abrir os ",
        "abrir as ",
    ]

    for prefixo in prefixos:
        if comando.startswith(prefixo):
            return comando.replace(prefixo, "", 1).strip()

    return comando

def executar_comando_texto(comando):
    comando = comando.lower().strip()
    comando = comando.replace("sexta-feira", "").replace("sexta feira", "").strip()
    if comando == "":
        return

    if comando in ["help", "ajuda", "comandos"]:
        mostrar_help()

    elif comando in ["modo voz", "ativar voz", "escuta"]:
        aguardar_palavra_ativacao()
        comando_voz = ouvir_comando()
        executar_comando_texto(comando_voz)

    elif comando in ["ouvir", "escutar", "voz"]:
        comando_voz = ouvir_comando()
        executar_comando_texto(comando_voz)

    elif comando in ["digitar", "ditar", "modo texto", "modo escrito"]:
        texto = ouvir_comando()

        if texto:
            pyautogui.write(texto)

    elif comando in ["abrir chrome", "chrome"]:
        subprocess.Popen("start chrome", shell=True)

    elif comando in ["abrir explorador", "explorador", "arquivos"]:
        pyautogui.hotkey("win", "e")

    elif comando in ["abrir pesquisa", "pesquisa"]:
        pyautogui.hotkey("win", "s")

    elif comando.startswith("pesquisar "):
        termo = comando.replace("pesquisar ", "", 1)
        webbrowser.open(f"https://www.google.com/search?q={termo}")

    elif comando.startswith("abrir site "):
        site = comando.replace("abrir site ", "", 1).strip()
        abrir_site(site)

    elif comando in ["abrir guia", "nova guia", "abrir nova guia", "abrir aba", "nova aba"]:
        pyautogui.hotkey("ctrl", "t")

    elif comando in ["fechar guia", "fechar aba", "fechar tab"]:
        pyautogui.hotkey("ctrl", "w")

    elif comando in ["fechar janela", "fechar"]:
        pyautogui.hotkey("alt", "f4")

    elif comando in ["cancelar desligamento", "cancelar shutdown"]:
        os.system("shutdown /a")
        print("[SISTEMA] Desligamento cancelado.")

    elif comando in ["desligar pc", "desligar computador", "desligar tudo"]:
        if confirmar_acao("[CONFIRMAÇÃO] Tem certeza que quer desligar o PC?"):
            os.system("shutdown /s /t 0")
        else:
            print("[CANCELADO] Desligamento cancelado.")

    elif comando in ["reiniciar pc", "reiniciar computador","reinicia", "reiniciar tudo"]:
        if confirmar_acao("[CONFIRMAÇÃO] Tem certeza que quer reiniciar o PC?"):
            os.system("shutdown /r /t 0")
        else:
            print("[CANCELADO] Reinicialização cancelada.")

    elif comando in ["suspender pc", "suspender computador", "suspende"]:
        if confirmar_acao("[CONFIRMAÇÃO] Tem certeza que quer suspender o PC?"):
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            print("[CANCELADO] Suspensão cancelada.")

    elif comando.startswith(("abrir ", "abre o ", "abre a ", "abre ", "abre os ", "abre as ", "abrir o ", "abrir a ", "abrir os ", "abrir as ")):
        alvo = extrair_alvo_abrir(comando)

        if alvo == "downloads":
            os.startfile(os.path.expanduser("~/Downloads"))

        elif alvo in ["desktop", "area de trabalho"]:
            os.startfile(os.path.expanduser("~/Desktop"))

        elif alvo == "documentos":
            os.startfile(os.path.expanduser("~/Documents"))
        
        elif alvo == "chrome":
            subprocess.Popen("start chrome", shell=True)

        elif alvo == "youtube":
            abrir_site("youtube")

        elif alvo == "github":
            abrir_site("github")

        elif alvo == "google":
            abrir_site("google")

        elif alvo == "chatgpt":
            abrir_site("chatgpt")

        elif alvo == "gmail":
            abrir_site("gmail")

        elif alvo == "drive":
            abrir_site("drive")

        elif alvo in ["bloco de notas", "notepad"]:
            subprocess.Popen("notepad")

        elif alvo in ["vscode", "vs code", "visual studio code", "vs"]:
            subprocess.Popen("code", shell=True)

        else:
            print(f"[COMANDO] Não sei abrir: {alvo}")

    else:
        print(f"[COMANDO] Não entendi: {comando}")