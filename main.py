import cv2
import mediapipe as mp
import time
import os

from gestos import contar_dedos, detectar_gesto, detectar_joinha, detectar_mao_fechada
from acoes import executar_acao
from estado import EstadoSextaFeira
from config import INTERVALO_VERIFICACAO, MOSTRAR_CAMERA, NOME_JANELA

mp_maos = mp.solutions.hands
mp_desenho = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0)
controle = EstadoSextaFeira()

ultimo_check = 0
intervalo = INTERVALO_VERIFICACAO
gesto = ""

with mp_maos.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as maos:

    while True:
        texto = f"{controle.estado} | {gesto}"
        sucesso, frame = camera.read()

        if not sucesso:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        resultado = maos.process(rgb)

        if resultado.multi_hand_landmarks:
            controle.atualizar_mao_detectada()

            for mao in resultado.multi_hand_landmarks:
                mp_desenho.draw_landmarks(frame, mao, mp_maos.HAND_CONNECTIONS)

                qtd_dedos = contar_dedos(mao)
                agora = time.time()

                if agora - ultimo_check >= intervalo:
                    if detectar_joinha(mao):
                        gesto = "joinha"
                    elif detectar_mao_fechada(mao):
                        gesto = "mao_fechada"
                    else:
                        gesto = detectar_gesto(qtd_dedos)

                    texto = f"{controle.estado} | {gesto}"
                    print(texto)

                    if controle.mudou_gesto(gesto):
                        ultimo_check = agora
                        continue

                    tempo_seguro = controle.tempo_do_mesmo_gesto()

                    if controle.estado == "pausado":
                        if gesto == "paz" and tempo_seguro >= controle.tempo_para_confirmar:
                            controle.ativar()
                            print("Sexta-feira ATIVA")

                    elif controle.estado == "ativo":
                        if gesto == "tres":
                            print(f"Tentando encerrar... {tempo_seguro:.1f}s")

                            if tempo_seguro >= controle.tempo_para_confirmar:
                                print("Sexta-feira ENCERRADA")
                                camera.release()
                                cv2.destroyAllWindows()
                                os._exit(0)

                        elif controle.pode_executar(gesto):
                            executar_acao(gesto)
                            controle.marcar_executado(gesto)
                    ultimo_check = agora

        else:
            if controle.deve_pausar_por_inatividade():
                controle.pausar()
                print("Sexta-feira PAUSADA por inatividade")

        if MOSTRAR_CAMERA:
            cv2.imshow(NOME_JANELA, frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

camera.release()
cv2.destroyAllWindows()