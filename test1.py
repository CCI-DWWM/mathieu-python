nom = input('Entrez votre nom ')
prenom = input('Entrez votre prenom ')
year = input('Entrez votre année de naissance ')

birthyear=year.isdigit()
print('Bonjour', prenom, nom, ', Vous avez', 2025 - int(year), 'ans')


