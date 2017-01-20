CREATE TABLE  Personnel(
id INT PRIMARY KEY NOT NULL,
prenom TEXT,
anciennete INTEGER,
poste INTEGER,
FOREIGN KEY(poste) REFERENCES Poste(id)
,
CONSTRAINT personnel_unique UNIQUE (prenom)
);
  
CREATE TABLE  Poste (
id INT PRIMARY KEY NOT NULL,
libelle TEXT,
CONSTRAINT libelle_unique UNIQUE (libelle)
);
  
 CREATE TABLE   TypeAnimal (
id INT PRIMARY KEY NOT NULL,
type TEXT,
CONSTRAINT type_unique UNIQUE (type)
);
 CREATE TABLE  CaracteristiqueAnnimal (
id INT PRIMARY KEY NOT NULL,
poid INTEGER,
nom TEXT,
animal INTEGER,
FOREIGN KEY(animal) REFERENCES  TypeAnimal(id)
);
   
CREATE TABLE  AnnimalAppartenantAPersonnel (
 id_caracteristique_animal INTEGER,
 id_personnel INTEGER,
 id_marque_de_croquettes INTEGER,
FOREIGN KEY(id_caracteristique_animal) REFERENCES  CaracteristiqueAnnimal(id),
FOREIGN KEY(id_personnel) REFERENCES Personnel(id),
FOREIGN KEY(id_marque_de_croquettes) REFERENCES MarqueDeCroquette(id)
);

  CREATE TABLE  MarqueDeCroquette (
id INT PRIMARY KEY NOT NULL,
libelle TEXT,
id_appartient_a INTEGER,
FOREIGN KEY(id_appartient_a) REFERENCES AnnimalAppartenantAPersonnel(id)
);
  
  
INSERT INTO Poste  (id, libelle) VALUES
(0, "Infirmier" ),
(1, "Medecin" ),
(2, "Aide-soignant" ),
(3, "ASH" ) ;

INSERT INTO Personnel 
(id, prenom, anciennete, poste) VALUES 
( 0, "Sophie",  2, 0 ),
( 1, "Arnaud",  4, 0 ),
( 2, "Gilbert",  6, 0 ),
( 3, "Cedric",  10, 0 ),
( 4, "Virginia H.",  12, 0 ),
( 5, "Greg",  2, 1 ),
( 6, "Sergio",  5, 1 ),
( 7, "Anne-Sophie",  1, 2 ),
( 8, "Rodrigue",  3, 2 ),
( 9, "Yacinne",  2, 2 ),
( 10, "Mathieu",  2, 3 ),
( 11, "Ollie",  9, 3 ),
( 12, "Bob",  16, 3 );

INSERT INTO  TypeAnimal (id, type ) VALUES 
(0, "Chien" ),
(1, "Chat" ),
(2, "Requin Blanc" ),
(3, "Lezard Vert" ) ;

INSERT INTO   CaracteristiqueAnnimal (id,poid, nom ,animal) VALUES 
( 0, 5, "Willy",  0 ),
( 1,2, "Medor",  0 ),
( 2,6, "Bubzy",  1 ),
( 3,4, "Reanimator", 1 ),
( 4,1, "Boule De Gomme",  3 ),
( 5,112, "Tartiflette",  2 );

INSERT INTO   AnnimalAppartenantAPersonnel (id_caracteristique_animal, id_personnel , id_marque_de_croquettes) VALUES
( 0, 1,   0 ),
( 1,9,   0 ),
( 2,6,   1 ),
( 3,5, 1 ),
( 4,3,  3 ),
( 5,6,  2 );

INSERT INTO   MarqueDeCroquette (id,libelle ,id_appartient_a) VALUES
( 0, "CanEgou",  6 ),
  ( 1, "FreshHumanMeat", 1 ),
( 2, "FrozenBee",  3 ),
( 3, "CanEgou",  2 ),
  ( 4, "FreshHumanMeat", 4 ),
( 5, "FrozenBee",  5 );


  


