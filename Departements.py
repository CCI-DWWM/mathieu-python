import csv
import sqlite3

con = sqlite3.connect("departements.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Dpt(code_departement, nom_departement, code-region, nom_region)")

# Lecture CSV
with open('departements-france.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        cur.execute("INSERT INTO Dpt VALUES(?,?,?,?)")
