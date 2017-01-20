# SQLEntertainment

An interactive command line interface program for learning SQL without installing a SQL Server.
This program creates a database on script directory and launch an interactive shell for testing and learning SQL requests. Documentation of SQL language used (SQL is a little different betweenn database management system) is available on [SQLite Documentaion](https://www.sqlite.org/docs.html).

Actually the code is ugly and doesn't have test.

## Installation

### Unix

```bash
git clone https://github.com/nogatan/SQLEntertainment.git && cd SQLEntertainment && python3 SQLEntertainment/Sql_Entertainment.py
```

## Usage

*(Only in french for moment)*


**!schema**	Affiche le schema complet de la base de donnee d'exemple

**!clear**	Retourne à la base de test par defaut (efface toute les modifications sur la base de test)

**!load** <nom de la table>	Creer ou charger une nouvelle base de donnée Ex: !load NouveauTest.bdd

**!display** <nom de la table>	Affiche le shema d'une table en particulier (ses colones, le type des colones ect.... Ex: !display Personnel

**!list**	Affiche la liste des tables

**!help**	 Affiche cette aide

**!quit**	Quitter


## License

Do What The Fuck You Want to Public License (WTFPL)
