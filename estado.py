import time


class EstadoSextaFeira:
    def __init__(self):
        self.estado = "pausado"
        self.gesto_anterior = None
        self.inicio_gesto = None
        self.tempo_para_confirmar = 3
        self.ultimo_momento_com_mao = time.time()
        self.tempo_sem_mao_para_pausar = 10
        self.ultimo_gesto_executado = None

    def atualizar_mao_detectada(self):
        self.ultimo_momento_com_mao = time.time()

    def deve_pausar_por_inatividade(self):
        return (
            self.estado == "ativo"
            and time.time() - self.ultimo_momento_com_mao >= self.tempo_sem_mao_para_pausar
        )

    def pausar(self):
        self.estado = "pausado"
        self.ultimo_gesto_executado = None

    def ativar(self):
        self.estado = "ativo"

    def mudou_gesto(self, gesto):
        if gesto != self.gesto_anterior:
            self.gesto_anterior = gesto
            self.inicio_gesto = time.time()
            self.ultimo_gesto_executado = None
            return True

        return False

    def tempo_do_mesmo_gesto(self):
        if self.inicio_gesto is None:
            return 0

        return time.time() - self.inicio_gesto

    def pode_executar(self, gesto):
        return gesto != self.ultimo_gesto_executado

    def marcar_executado(self, gesto):
        self.ultimo_gesto_executado = gesto