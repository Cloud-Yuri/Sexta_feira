import os
import subprocess
import pyautogui
import webbrowser


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
    comando = comando.lower().strip()

    if comando == "":
        return

    if comando in ["abrir chrome", "chrome"]:
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