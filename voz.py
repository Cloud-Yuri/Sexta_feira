import speech_recognition as sr


def ouvir_comando():
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as fonte:
        print("[VOZ] Ouvindo...")
        reconhecedor.adjust_for_ambient_noise(fonte, duration=0.5)
        audio = reconhecedor.listen(fonte)

    try:
        comando = reconhecedor.recognize_google(audio, language="pt-BR")
        print(f"[VOZ] Você disse: {comando}")
        return comando

    except sr.UnknownValueError:
        print("[VOZ] Não entendi o que você falou.")
        return ""

    except sr.RequestError:
        print("[VOZ] Erro ao acessar o serviço de reconhecimento.")
        return ""