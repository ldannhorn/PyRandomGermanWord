import random
import colorama
from colorama import Fore, Back
colorama.init()
from os import system
system('cls')
letters = 'abcdefghijklmnopqrstuvwxyz'

def match(length,word):
    system('cls')
    print(Fore.CYAN + f'Länge des Wortes: {length}' + Fore.RESET)
    print(Fore.GREEN + word + Fore.RESET)
    input()
    search()


def search():

    with open('de.txt', 'r') as file:
        wordlist = file.read().splitlines()
        #print(wordlist)

        while True:
            length = int(input(Fore.CYAN + 'Länge des Wortes: ' + Fore.RESET))
            while True:
                word = ''.join((random.choice(letters) for x in range(length))).lower()
                print(Fore.RED + word + Fore.RESET)

                if word in wordlist:
                    match(length,word)
                else:
                    system('cls')
                    print(Fore.CYAN + f'Länge des Wortes: {length}' + Fore.RESET)

if __name__ == '__main__':
    search()
