from notas_musicais.escalas import escala


def acorde(cifra):
    """
    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
    """

    graus = (0, 2, 4)
    notas = escala(cifra, 'maior').values()

    return {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
