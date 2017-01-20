# -*- coding: utf-8 -*-
# !/usr/bin/python3
import sqlite3
import os
try:
    approot = os.path.dirname(os.path.abspath(__file__))
except NameError:
    import sys
    approot = os.path.dirname(os.path.abspath(sys.argv[0]))
finally:
    os.chdir(approot)


approot = approot + '/'
BASE_NAME = 'test.bdd'

def clear_base():
    os.remove(approot + BASE_NAME)



def load_base():
    sql =b'CREATE TABLE  Personnel(\r\nid INT PRIMARY KEY NOT NULL,\r\nprenom TEXT,\r\nanciennete INTEGER,\r\nposte INTEGER,\r\nFOREIGN KEY(poste) REFERENCES Poste(id)\r\n,\r\nCONSTRAINT personnel_unique UNIQUE (prenom)\r\n);\r\n  \r\nCREATE TABLE  Poste (\r\nid INT PRIMARY KEY NOT NULL,\r\nlibelle TEXT,\r\nCONSTRAINT libelle_unique UNIQUE (libelle)\r\n);\r\n  \r\n CREATE TABLE   TypeAnimal (\r\nid INT PRIMARY KEY NOT NULL,\r\ntype TEXT,\r\nCONSTRAINT type_unique UNIQUE (type)\r\n);\r\n CREATE TABLE  CaracteristiqueAnnimal (\r\nid INT PRIMARY KEY NOT NULL,\r\npoid INTEGER,\r\nnom TEXT,\r\nanimal INTEGER,\r\nFOREIGN KEY(animal) REFERENCES  TypeAnimal(id)\r\n);\r\n   \r\nCREATE TABLE  AnnimalAppartenantAPersonnel (\r\n id_caracteristique_animal INTEGER,\r\n id_personnel INTEGER,\r\n id_marque_de_croquettes INTEGER,\r\nFOREIGN KEY(id_caracteristique_animal) REFERENCES  CaracteristiqueAnnimal(id),\r\nFOREIGN KEY(id_personnel) REFERENCES Personnel(id),\r\nFOREIGN KEY(id_marque_de_croquettes) REFERENCES MarqueDeCroquette(id)\r\n);\r\n\r\n  CREATE TABLE  MarqueDeCroquette (\r\nid INT PRIMARY KEY NOT NULL,\r\nlibelle TEXT,\r\nid_appartient_a INTEGER,\r\nFOREIGN KEY(id_appartient_a) REFERENCES AnnimalAppartenantAPersonnel(id)\r\n);\r\n  \r\n  \r\nINSERT INTO Poste  (id, libelle) VALUES\r\n(0, "Infirmier" ),\r\n(1, "Medecin" ),\r\n(2, "Aide-soignant" ),\r\n(3, "ASH" ) ;\r\n\r\nINSERT INTO Personnel \r\n(id, prenom, anciennete, poste) VALUES \r\n( 0, "Sophie",  2, 0 ),\r\n( 1, "Arnaud",  4, 0 ),\r\n( 2, "Gilbert",  6, 0 ),\r\n( 3, "Cedric",  10, 0 ),\r\n( 4, "Virginia H.",  12, 0 ),\r\n( 5, "Greg",  2, 1 ),\r\n( 6, "Sergio",  5, 1 ),\r\n( 7, "Anne-Sophie",  1, 2 ),\r\n( 8, "Rodrigue",  3, 2 ),\r\n( 9, "Yacinne",  2, 2 ),\r\n( 10, "Mathieu",  2, 3 ),\r\n( 11, "Ollie",  9, 3 ),\r\n( 12, "Bob",  16, 3 );\r\n\r\nINSERT INTO  TypeAnimal (id, type ) VALUES \r\n(0, "Chien" ),\r\n(1, "Chat" ),\r\n(2, "Requin Blanc" ),\r\n(3, "Lezard Vert" ) ;\r\n\r\nINSERT INTO   CaracteristiqueAnnimal (id,poid, nom ,animal) VALUES \r\n( 0, 5, "Willy",  0 ),\r\n( 1,2, "Medor",  0 ),\r\n( 2,6, "Bubzy",  1 ),\r\n( 3,4, "Reanimator", 1 ),\r\n( 4,1, "Boule De Gomme",  3 ),\r\n( 5,112, "Tartiflette",  2 );\r\n\r\nINSERT INTO   AnnimalAppartenantAPersonnel (id_caracteristique_animal, id_personnel , id_marque_de_croquettes) VALUES\r\n( 0, 1,   0 ),\r\n( 1,9,   0 ),\r\n( 2,6,   1 ),\r\n( 3,5, 1 ),\r\n( 4,3,  3 ),\r\n( 5,6,  2 );\r\n\r\nINSERT INTO   MarqueDeCroquette (id,libelle ,id_appartient_a) VALUES\r\n( 0, "CanEgou",  6 ),\r\n  ( 1, "FreshHumanMeat", 1 ),\r\n( 2, "FrozenBee",  3 ),\r\n( 3, "CanEgou",  2 ),\r\n  ( 4, "FreshHumanMeat", 4 ),\r\n( 5, "FrozenBee",  5 );\r\n\r\n\r\n  \r\n\r\n\r\n'

    conn = sqlite3.connect(approot + BASE_NAME)
    c = conn.cursor()
    decoded_sql = sql.decode('utf-8')
    r =decoded_sql.split(';')

    for i in r:
        c.execute(i + ';')

    conn.commit()
    conn.close()


def connection():
    conn = sqlite3.connect(approot + BASE_NAME)
    c = conn.cursor()
    return c


def execute_req():
    c = conn.cursor()
    c.execute("SELECT * FROM Personnel JOIN Poste WHERE Personnel.Poste==Poste.id;")
    try:
        conn.commit()
    except Exception as e:
        print(e)
    try:
        c.fetchall()
    except Exception as e:
        print(e)


def affiche_aide():
    print(
        """SQLEntertainment.\nEntrez une requete, faites ENTRER pour l'executer. Les requetes SQL se terminent par un ";", ainsi vous pouvez écrire ou copier coller une requêtes sur plusieurs lignes. \n Un exemple de requete: SELECT * FROM Personnel JOIN Poste WHERE Personnel.Poste==Poste.id;\n Le moteur utilise SQLite3 sous le capot, voyez la doc si vous voulez en savoir plus ( <3 Qwant Search Engine)\nPour vous aider à vous y retrouver, la base de donnée à laquelle vous êtes connecté est entre parenthèse dans le prompt. Par defaut, le programme se connecte à la base de donnée de test au démarrage.\nAide:\n\t!schema\tAffiche le schema complet de la base de donnee d'exemple.\n\t!clear\tRetourne à la Base de test et efface toute les modifications).\n\t!load <nom de la table>\tCreer ou charger une nouvelle base de donnée Ex: !load NouveauTest.bdd\n\t!display <nom de la table>\tAffiche le shema d'une table en particulier (ses colones, le type des colones ect.... Ex: !display Personnel\n\t!list\tAffiche la liste des tables.\n\t!help\t Affiche cette aide.\n\t!quit\tQuitter. """)


def affiche_schema_relationnel():
    print("""
Personnel
---------
\tid INTEGER
\tprenom TEXT
\tanciennete INTEGER
\tposte  (Clef etrangere en reference a Poste) INTEGER
\n
Poste
------
\tid INTEGER
\tlibelle TEXT
\n
TypeAnimal
----------
\tid INTEGER
\ttype TEXT
\n
CaracteristiqueAnnimal
----------------------
\tid INTEGER
\tpoid INTEGER
\tnom TEXT
\tid_type_animal  (Clef etrangere en reference a TypeAnimal) INTEGER
\n
AnnimalAppartenantAPersonnel
----------------------------
\tid_caracteristique_animal (Clef etrangere en reference a TypeAnimal)
\tid_personnel (Clef etrangere en reference a TypeAnimal)
\tid_marque_de_croquettes (Clef etrangere en reference a MarqueDeCroquette)
\n
MarqueDeCroquette
-----------------
\tid
\tlibelle
\tid_appartient_a (Clef etrangere en reference a AnnimalAppartenantAPersonnel)
\n\n
    """)

def __schem():
    affiche_schema_relationnel()

def __display():
    pass

def priv__display(nom_table):
    c = conn.cursor()
    c.execute( "pragma table_info('"+nom_table+"')  ;")
    try:
        conn.commit()
    except Exception as e:
        print(e)
    try:

        for i in c.fetchall():
            print("Colonne numero: ",str(i[0]), "Nom de la colone: ",i[1], "Type: ",i[2])

    except Exception as e:
        print(e)

def __listtable():
    c = conn.cursor()
    c.execute("select name from sqlite_master where type = 'table'")
    try:
        conn.commit()
    except Exception as e:
        print(e)
    try:
        print(c.fetchall())
    except Exception as e:
        print(e)

def __clear():
    os.remove(approot + BASE_NAME)
    load_base()
def __quit():
    raise Exception('Bye Bye :)')
def __help():
    affiche_aide()
def __load():
    pass
COMMANDS = {

    "!schema":__schem ,
    "!display" : __display,
    "!list" : __listtable,
    "!clear":__clear,
    '!load' : __load ,
    '!help' : __help,
    '!quit' :__quit ,
}
try:
    clear_base()
except Exception as e:
    print(e)
load_base()
affiche_aide()

while True:
    try:
        name = approot + BASE_NAME
        conn = sqlite3.connect(name)
        c = conn.cursor()
        req = input("BDD_Entertainment ({})>>".format(BASE_NAME))+ ' '

        raw_data = req.split(' ')
        print(raw_data)
        argument_list =  [w for w in raw_data if w != '']
        if '!' not in argument_list[0]  and raw_data != '' and   raw_data != ' ':
            while not ';' in req:
                req = ' '+ req + input(">>")+' '
        print(argument_list)

        if argument_list[0] in COMMANDS.keys() :
            COMMANDS[argument_list[0]]()
            print(' argument_list[0] ==',argument_list[0] )
            if argument_list[0]=='!load':
                name =  raw_data[1]
                print(name)
                BASE_NAME = name
                raise Exception()
            if argument_list[0] == '!display':
                print('commande reconnue')
                priv__display(argument_list[1])
        else:
            print('req execution', req)
            c.execute(req)
            try:
                r = [print(i) for i in c.fetchall()]
                del r
            except Exception as e:
                print(e)
        conn.commit()
        conn.close()
    except IndexError:
        pass
    except Exception as e:
        print(e)



