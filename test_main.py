from main import *


def test_deve_retornar_impressao():
    impressao = print_hi('rafa')
    print('rodando')
    assert impressao == 'meu nome é rafa'


def test_deve_ler_arquivos_dos_tweets():
    conteudo = ler_arquivo('project_twitter_data.csv')
    assert len(conteudo) == 20
    for c in conteudo:
        print(c)
        assert c != ''
