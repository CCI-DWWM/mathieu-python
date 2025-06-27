nom = input('Entrez votre nom ')
prenom = input('Entrez votre prenom ')
year = input('Entrez votre année de naissance ')

if year.isdigit():
    print('Bonjour', prenom, nom, ', Vous avez', 2025 - int(year), 'ans')
else:
    print('''J'ai pas le droit de t'insulter alors, soit sage et entre une année quand on te le demande au lieu d'entrer des conneries...''')


