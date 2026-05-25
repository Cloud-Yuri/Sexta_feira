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

def detectar_joinha(mao):
    pontos = mao.landmark

    polegar_para_cima = pontos[4].y < pontos[3].y < pontos[2].y

    indicador_fechado = pontos[8].y > pontos[6].y
    medio_fechado = pontos[12].y > pontos[10].y
    anelar_fechado = pontos[16].y > pontos[14].y
    mindinho_fechado = pontos[20].y > pontos[18].y

    return (
        polegar_para_cima
        and indicador_fechado
        and medio_fechado
        and anelar_fechado
        and mindinho_fechado
    )

def detectar_mao_fechada(mao):
    pontos = mao.landmark

    indicador_fechado = pontos[8].y > pontos[6].y
    medio_fechado = pontos[12].y > pontos[10].y
    anelar_fechado = pontos[16].y > pontos[14].y
    mindinho_fechado = pontos[20].y > pontos[18].y

    return (
        indicador_fechado
        and medio_fechado
        and anelar_fechado
        and mindinho_fechado
    )