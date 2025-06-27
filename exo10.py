import random

nombres = tuple(random.randint(0, 100) for _ in range(50))

print(nombres)

plus_petit = min(nombres)
plus_grand = max(nombres)

print("Le plus petit nombre est :", plus_petit)
print("Le plus grand nombre est :", plus_grand)
