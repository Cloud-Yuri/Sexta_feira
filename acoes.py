import pyautogui
import subprocess


def executar_acao(gesto):
    if gesto == "paz":
        subprocess.Popen("start chrome", shell=True)

    elif gesto == "mao_fechada":
        pyautogui.hotkey("alt", "f4")

    elif gesto == "mao_aberta":
        pyautogui.hotkey("win", "e")

    elif gesto == "menu_energia":
        pyautogui.press("win")
        
    elif gesto == "joinha":
        pyautogui.hotkey("win", "s")