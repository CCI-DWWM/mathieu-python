from itertools import count

Phrase = input("Entrez une phrase : ").lower()
Voyelles = [ "a", "à", "e", "é", "è", "i", "o", "ô", "u", "y"]
Consonnes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
voyelle = 0
consonne = 0

for lettre in Phrase:
    if lettre in Voyelles:
        voyelle = voyelle + 1
    if lettre in Consonnes:
        consonne = consonne + 1

print("Le nombre de voyelle est : ", voyelle)
print("Le nombre de consonne est : ", consonne)