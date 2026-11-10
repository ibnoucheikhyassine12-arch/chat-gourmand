import sqlite3
import os

DB_NAME = "chat_gourmand_v2.db"


def creer_table():
    for essai in range(2):
        connexion = None
        try:
            connexion = sqlite3.connect(DB_NAME)
            curseur = connexion.cursor()
            curseur.execute(
                "CREATE TABLE IF NOT EXISTS scores ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "score INTEGER NOT NULL, "
                "date TEXT NOT NULL)"
            )
            connexion.commit()
            connexion.close()
            return
        except sqlite3.DatabaseError as erreur:
            print(f"Erreur base de données : {erreur}")
            if connexion is not None:
                connexion.close()
            try:
                if os.path.exists(DB_NAME):
                    os.remove(DB_NAME)
            except OSError:
                pass


def ajouter_score(score):
    try:
        connexion = sqlite3.connect(DB_NAME)
        curseur = connexion.cursor()
        curseur.execute(
            "INSERT INTO scores (score, date) VALUES (?, datetime('now'))",
            (score,)
        )
        connexion.commit()
        connexion.close()
    except sqlite3.Error as erreur:
        print(f"Erreur base de données : {erreur}")


def meilleur_score():
    try:
        connexion = sqlite3.connect(DB_NAME)
        curseur = connexion.cursor()
        curseur.execute("SELECT MAX(score) FROM scores")
        resultat = curseur.fetchone()[0]
        connexion.close()
        return resultat if resultat is not None else 0
    except sqlite3.Error as erreur:
        print(f"Erreur base de données : {erreur}")
        return 0
        
                
            
            