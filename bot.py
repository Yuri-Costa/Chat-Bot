import os
from colorama import init, Fore, Back
init(convert=True, autoreset=True)
def processar_resposta(resposta,nome):
    if resposta == '1':
        print(Fore.CYAN+f'{os.linesep}{nome}, O taekwondo é uma arte marcial originalmente coreana, que teria surgido por volta do século VII d.C. A tradução que se faz do termo taekwondo é “caminho dos pés, das mãos e do espírito”, significado que revela a proposta de desenvolvimento integral do praticante, típica das artes marciais.{os.linesep}')
    elif resposta == '2':
        print(Fore.CYAN+f'{os.linesep}{nome}, Coréia Do Sul{os.linesep}')
    elif resposta == '3':
        print(Fore.CYAN+f'{os.linesep}{nome}, O Taekwondo foi trazido ao Brasil no ano de 1970, na cidade de São Paulo, através do grão mestre Sang Min Cho, enviado oficialmente pela International Taekwondo Federation.{os.linesep}')
    elif resposta == '4':
        print(Fore.CYAN+f'{os.linesep}{nome}, A palavra SABONIM na COREIA tem o significado de “PROFESSOR HONRADO”, uma pessoa que entrega um conhecimento de valor à sociedade.{os.linesep}')
    elif resposta == '5':
        print(Fore.CYAN+f'{os.linesep}{nome}, Agora o praticante atingiu a maturidade para buscar por si só conhecimento, apenas agora ele está  pronto para descobrir-se em meio aos conhecimentos adquiridos. É a fase em que ele entende que Taekwondo é muito mais que uma luta ou um esporte, pois se confunde com sua própria vida, seus princípios e atitudes.{os.linesep}')
    else:
        print(Fore.CYAN+f'opá{nome}, só temos 5 opções de pergutas!{os.linesep}Por favor digite apenas 1, 2, 3, 4 ou 5')

def start():

    #apresentar o chat bot
    print(Fore.MAGENTA + 'Olá! Seja Muito Bem Vindo ao ChatBot de Taekwondo!')
    #pedir o nome
    nome = input(Fore.YELLOW+'digite seu nome: ')
    #pedir Email
    email = input(Fore.YELLOW+'digiter seu Email: ')
    while True:
        #menu
        resposta = input (Fore.BLUE+ f'O que gostaria de saber?{os.linesep}[1] - O que é o Taekwondo?{os.linesep}[2] - Qual País de origem do Taekwondo{os.linesep}[3] - Quando o Taekwondo chegou ao Brasil?{os.linesep}[4] - Qual o significado de sabonim?{os.linesep}[5] - Qual o significado da Faixa preta no Taekwondo?{os.linesep}')
        ##resposta
        processar_resposta(resposta,nome)

if __name__ == '__main__':
        start()
         ##resposta = input(
            ##f'O que gostaria de saber?{os.linesep}[1] - O que é o Taekwondo?{os.linesep}[2]
          ##  - Qual País de origem do taekwondo?{os.linesep}[3] -  Quando o Taekwondo veio 
           ## aoBrasil{os.linesep}[4] - Qual o significado de sabonim?{os.linesep}[5] - Qual
           ## o significado da Faixa preta no Taekwondo?{os.linesep}')
