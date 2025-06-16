from pytest import mark, raises

from src.notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():

    # ARRANGE
    tonica = 'c'
    tonalidade = 'maior'

    # ACT
    result = escala(tonica, tonalidade)

    # ASSERT
    assert result


def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    # ARRANGE
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'Essa nota não existe. Tente uma dessas: {NOTAS}'

    # ACT - FAZER O PROGRAMA FUNCIONAR
    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    assert mensagem_de_erro == error.value.args[0]


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'
    mensagem_de_erro = (
        f'Essa escala não existe ou não foi implementada. '
        f'Tente uma dessas: {list(ESCALAS.keys())}'
    )
    with raises(KeyError) as error:
        escala(tonica, tonalidade)
    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(  # ARRANGE
    'tonica,esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, esperado):   # ACT
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado   # ASSERT


def teste_deve_retornar_os_sete_graus():
    tonica = 'c'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)
    assert resultado['graus'] == esperado
