NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica:str, tonalidade:str) -> dic[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala

    Examples:
        
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VII', 'VII']}

        >>> escalas('A', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I','II', 'III', 'IV', 'V', 'VII', 'VII']}

    Returns:
        Um dicionário com as notas da escala e os graus.
    """
    intervalos = ESCALAS[tonalidade]
    tonica_pos = NOTAS.index(tonica)

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

        return {
            'notas': temp,
            'graus': ['I', 'II', 'III', 'IV', 'V', 'VII', 'VII'],
        }
