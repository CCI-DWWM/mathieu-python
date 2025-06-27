"""
Exercice :
Demandez à l’utilisateur de saisir son PRENOM, puis son NOM, et enfin,
son année de naissance
Afficher « Bonjour PRENOM NOM, vous avez XX ans »
"""

nom = input("Votre nom : ")
prenom = input("Votre prénom : ")
year = input("Année de naissance : ")

year=int(year) # convertion en int
age=2025-year

print(f"Bonjour {prenom} {nom}, vous avez {age} ans")