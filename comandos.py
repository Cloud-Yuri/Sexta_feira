import os
import subprocess
import pyautogui


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
        pyautogui.hotkey("win", "s")
        pyautogui.write(termo)

    elif comando in ["abrir downloads", "downloads"]:
        caminho = os.path.expanduser("~/Downloads")
        os.startfile(caminho)

    elif comando in ["abrir desktop", "desktop", "area de trabalho"]:
        caminho = os.path.expanduser("~/Desktop")
        os.startfile(caminho)

    elif comando in ["fechar janela", "fechar"]:
        pyautogui.hotkey("alt", "f4")

    else:
        print(f"[COMANDO] Não entendi: {comando}")