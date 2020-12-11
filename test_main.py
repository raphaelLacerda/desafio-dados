from main import print_hi


def test_deve_retornar_impressao():
    impressao = print_hi("rafa")
    print('rodando')
    assert impressao == "meu nome é rafa"
