import colorama.ansi
from colorama import Fore, Back, Style

def encadrer(name , color="white", cadre="white"):

    longueur = len(name) + 2
    name = getattr(Fore, color.upper()) + name + Style.RESET_ALL
    print('┌', '─' * longueur, '┐', sep='')
    print(f"│ {name} │")
    print('└', '─' * longueur, '┘', sep='')


if __name__ == "__main__":
    name = input('Entrez votre nom :')
    encadrer(name)
