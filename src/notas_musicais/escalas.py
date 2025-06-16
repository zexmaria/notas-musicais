NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}

RELATIVAS_MENOR = {
    'C': 'A',
    'C#': 'A#',
    'D': 'B',
    'D#': 'C',
    'E': 'C#',
    'F': 'D',
    'F#': 'D#',
    'G': 'E',
    'G#': 'F',
    'A': 'F#',
    'A#': 'G',
    'B': 'G#',
}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala

    Examples:

    >>> escala('C', 'maior')
    {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    >>> escala('c', 'maior')
    {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    Returns:
        Um dicionário com as notas da escala e os graus.

    Raises:
        ValueError: Caso a nota não exista
        KeyError: Caso a tonalidade não exista ou não tenha sido implementada.
    """
    is_minuscula = tonica.islower()
    tonica = tonica.upper()

    if is_minuscula and tonalidade == 'maior':
        tonica = RELATIVAS_MENOR[tonica]

    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)

    except ValueError:
        raise ValueError(f'Essa nota não existe. Tente uma dessas: {NOTAS}')
    except KeyError:
        raise KeyError(
            f'Essa escala não existe ou não foi implementada. Tente uma dessas: {list(ESCALAS.keys())}'
        )

    notas = [(tonica_pos + intervalo) % 12 for intervalo in intervalos]
    notas_escala = [NOTAS[i] for i in notas]

    return {
        'notas': notas_escala,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
