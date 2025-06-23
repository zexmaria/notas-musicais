from notas_musicais.acordes import acorde

"""
Entrada:
Acorde "C"

Esperado:
I - III - V

{'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
"""


def test_acorde_deve_retornar_as_notas_correspondentes():
    nota = 'C'
    esperado = ['C', 'E', 'G']
    notas, _ = acorde(nota).values()
    assert esperado == notas
