import sqlite3

connexion = sqlite3.connect("scores.db")
print("Base SQLite OK")
connexion.close()