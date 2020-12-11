tweets = []
positive_words = []
negative_words = []

def print_hi(name):
    impressao = 'meu nome é {}'.format(name)
    print(impressao)
    return impressao


def ler_arquivo(arquivo):
    f = open(arquivo, 'r')
    conteudo_arquivo_tweets_por_linha = []
    for x in f:
        if x.strip() != '':
            conteudo_arquivo_tweets_por_linha.append(x)

    f.close()
    return conteudo_arquivo_tweets_por_linha


def gerar_arquivo_com_resultado():
    f = open('resultado.csv', 'w')
    f.write('number of RTs,number of Replies,positive score,negative score,net score')
    f.close()

if __name__ == '__main__':
    tweets = ler_arquivo('project_twitter_data.csv')
    positive_words = ler_arquivo('negative_words.txt')
    negative_words = ler_arquivo('positive_words.txt')
    resultado = []

    gerar_arquivo_com_resultado(resultado)
