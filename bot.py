import random
import os
import tweepy
from config import CONSUMER_SECRET, CONSUMER_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def twittar(msg: str):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    api.update_status(msg)


def gerar_ameaca():
    work_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f'{work_dir}/verbos', 'r', encoding='utf-8') as vrbs:
        verbos = vrbs.read().splitlines()
    with open(f'{work_dir}/sinonimos', 'r', encoding='utf-8') as snms:
        sinonimos = snms.read().splitlines()
    with open(f'{work_dir}/resultados', 'r', encoding='utf-8') as rstds:
        resultados = rstds.read().splitlines()

    tweet_num = len(resultados) + 1

    iterations = 0
    while True:
        gerado = "Vou te {} {}".format(random.choice(verbos),
                                       random.choice(sinonimos))

        if gerado not in resultados:
            print("{}. {}".format(tweet_num, gerado))
            twittar(gerado)
            with open('resultados', 'w', encoding='utf-8') as rstds:
                rstds.writelines(gerado)
            break
        elif iterations >= 500:
            print('Não foi possível encontrar uma combinação original '
                  'após 500 tentativas.')
            break
        iterations += 1


if __name__ == '__main__':
    gerar_ameaca()
