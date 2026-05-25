import cv2
import mediapipe as mp
import time
import pyautogui
import subprocess

mp_maos = mp.solutions.hands
mp_desenho = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0)

def contar_dedos(mao):
    pontos = mao.landmark

    dedos = []

    # Polegar
    if pontos[4].x < pontos[3].x:
        dedos.append(1)
    else:
        dedos.append(0)

    # Indicador, médio, anelar, mindinho
    pontas = [8, 12, 16, 20]
    bases = [6, 10, 14, 18]

    for ponta, base in zip(pontas, bases):
        if pontos[ponta].y < pontos[base].y:
            dedos.append(1)
        else:
            dedos.append(0)

    return sum(dedos)

def detectar_gesto(qtd_dedos):
    if qtd_dedos == 0:
        return "mao_fechada"
    if qtd_dedos == 1:
        return "um"
    if qtd_dedos == 2:
        return "paz"
    if qtd_dedos == 3:
        return "tres"
    if qtd_dedos == 4:
        return "menu_energia"
    if qtd_dedos == 5:
        return "mao_aberta"

    return "desconhecido"

def executar_acao(gesto):
    if gesto == "paz":
        subprocess.Popen("start chrome", shell=True)

    elif gesto == "mao_fechada":
        pyautogui.hotkey("alt", "f4")

    elif gesto == "mao_aberta":
        pyautogui.hotkey("win", "e")

    elif gesto == "menu_energia":
        pyautogui.press("win")

with mp_maos.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as maos:
    
    ultimo_check = 0
    intervalo = 2

    estado = "pausado"
    gesto = ""
    gesto_anterior = None
    inicio_gesto = None
    tempo_para_confirmar = 3
    ultimo_momento_com_mao = time.time()
    tempo_sem_mao_para_pausar = 10
    ultimo_gesto_executado = None

    while True:
        texto = f"{estado} | {gesto}"
        sucesso, frame = camera.read()

        if not sucesso:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        resultado = maos.process(rgb)
        if resultado.multi_hand_landmarks:
            ultimo_momento_com_mao = time.time()
        else:
            if estado == "ativo" and time.time() - ultimo_momento_com_mao >= tempo_sem_mao_para_pausar:
                estado = "pausado"
                ultimo_gesto_executado = None
                print("Sexta-feira PAUSADA por inatividade")

        if resultado.multi_hand_landmarks:
            for mao in resultado.multi_hand_landmarks:
                mp_desenho.draw_landmarks(frame, mao, mp_maos.HAND_CONNECTIONS)

                qtd_dedos = contar_dedos(mao)
                agora = time.time()

                if agora - ultimo_check >= intervalo:
                    gesto = detectar_gesto(qtd_dedos)
                    texto = f"{estado} | {gesto}"
                    print(gesto)
                    if gesto != gesto_anterior:
                        gesto_anterior = gesto
                        inicio_gesto = time.time()
                    else:
                        tempo_seguro = time.time() - inicio_gesto

                        if estado == "pausado":
                            if gesto == "paz" and tempo_seguro >= tempo_para_confirmar:
                                estado = "ativo"
                                print("Sexta-feira ATIVA")
                                inicio_gesto = time.time()

                        elif estado == "ativo":
                            if gesto == "tres" and tempo_seguro >= tempo_para_confirmar:
                                print("Sexta-feira ENCERRADA")
                                camera.release()
                                cv2.destroyAllWindows()
                                exit()
                            else:
                                if gesto != ultimo_gesto_executado:
                                    executar_acao(gesto)
                                    ultimo_gesto_executado = gesto
                    ultimo_check = agora

        cv2.putText(frame, texto, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Sexta-feira - Gestos", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

camera.release()
cv2.destroyAllWindows()
