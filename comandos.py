import os
import subprocess
import pyautogui
import webbrowser

def mostrar_help():
    print("""
========== AJUDA - SEXTA-FEIRA ==========

GESTOS:
- Paz por 3s: ativa a Sexta-feira
- 1 dedo: abre comando por texto
- Mão fechada: fecha a janela atual
- Mão aberta: abre o Explorador de Arquivos
- Joinha: abre a pesquisa do Windows
- 4 dedos: abre o menu Iniciar
- 3 dedos por 3s: encerra a Sexta-feira

COMANDOS DE TEXTO:
- help
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
- pesquisar <termo>
- abrir site <nome ou url>
- fechar janela
- cancelar desligamento

COMANDOS SENSÍVEIS:
- desligar pc
- reiniciar pc
- suspender pc

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


def executar_comando_texto(comando):
    if executar_comando_sensivel(comando):
        return

def executar_comando_sensivel(comando):
    comando = comando.lower().strip()
    if comando == "":
        return

    if comando in ["help", "ajuda", "comandos"]:
        mostrar_help()

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
    
    elif comando in ["desligar pc", "desligar computador"]:
        if confirmar_acao("[CONFIRMAÇÃO] Tem certeza que quer desligar o PC?"):
            os.system("shutdown /s /t 0")
        else:
            print("[CANCELADO] Desligamento cancelado.")

    elif comando in ["reiniciar pc", "reiniciar computador"]:
        if confirmar_acao("[CONFIRMAÇÃO] Tem certeza que quer reiniciar o PC?"):
            os.system("shutdown /r /t 0")
        else:
            print("[CANCELADO] Reinicialização cancelada.")

    elif comando in ["suspender pc", "suspender computador"]:
        if confirmar_acao("[CONFIRMAÇÃO] Tem certeza que quer suspender o PC?"):
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            print("[CANCELADO] Suspensão cancelada.")

    elif comando.startswith("abrir "):
        alvo = comando.replace("abrir ", "", 1).strip()

        if alvo == "downloads":
            os.startfile(os.path.expanduser("~/Downloads"))

        elif alvo in ["desktop", "area de trabalho"]:
            os.startfile(os.path.expanduser("~/Desktop"))

        elif alvo == "documentos":
            os.startfile(os.path.expanduser("~/Documents"))

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

        elif alvo in ["vscode", "vs code", "visual studio code"]:
            subprocess.Popen("code", shell=True)

        else:
            print(f"[COMANDO] Não sei abrir: {alvo}")

    elif comando in ["fechar janela", "fechar"]:
        pyautogui.hotkey("alt", "f4")

    else:
        print(f"[COMANDO] Não entendi: {comando}")