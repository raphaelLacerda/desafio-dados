from main import *


def test_deve_retornar_impressao():
    impressao = print_hi('rafa')
    print('rodando')
    assert impressao == 'meu nome é rafa'


def test_deve_ler_arquivos_dos_tweets():
    conteudo = ler_arquivo('project_twitter_data.csv')
    assert len(conteudo) == 20
    for c in conteudo:
        assert c != ''


def test_deve_ler_arquivos_de_palavras_positivas():
    conteudo = ler_arquivo('positive_words.txt')
    assert len(conteudo) == 2006
    for c in conteudo:
        assert c != ''


def test_deve_ler_arquivos_de_palavras_negativas():
    conteudo = ler_arquivo('negative_words.txt')
    assert len(conteudo) == 4782
    for c in conteudo:
        assert c != ''


def test_deve_gerar_arquivo_de_resultado():
    gerar_arquivo_com_resultado()
    conteudo = ler_arquivo('resultado.csv')
    assert len(conteudo) == 1

