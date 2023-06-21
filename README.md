
**Modélisation comparative de la structure de l'α-amylase (AA) d'Alteromonas haloplanktis :**

**Introduction :**

Le fonctionnement d’un système biologique implique des cascades d’interactions. Les protéines en sont les principaux acteurs.

La capacité d’une protéine à interagir dépend de sa structure tridimensionnelle (3D).

Connaître cette dernière permet donc de mieux comprendre son mode d’action (activité enzymatique, transport, signalisation, liaison avec un ligand, un récepteur, une membrane, etc).

Les méthodes expérimentales de détermination de la structure 3D des protéines sont lourdes et coûteuses en temps et ressources, voire inapplicables (cas des protéines non solubles, par exemple).

Les méthodes prédictives dites in silico proposent une alternative rapide et bon marché.

Elles sont basées sur un ensemble de lois physiques, statistiques et biologiques.

Aujourd'hui, la modélisation comparative est décrite comme la technique la plus précise parmi autres méthodes de modélisation moléculaire.

Dans ce rapport, nous appliquerons une modélisation comparative sur l'exemple de l'α-amylase (AA) d'*Alteromonas haloplanktis*.

**Etape 1 : Recherche d’une protéine homologue à la séquence cible appelée Template :**

- Accéder à la base de données (<http://www.uniprot.org/>), rechercher la séquence de la protéine α-amylase (AA) d'Alteromonas haloplanktis.

Pour obtenir la séquence de la protéine mature, on élimine la séquence signal ainsi que les éventuelles séquences propeptides.

Copier au format FASTA la séquence de la protéine mature dans un nouveau fichier appelé «alpha\_amy.txt».


![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.001.png)

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.002.png)

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.003.png)

- Soumettre la séquence cible à Blast (http://blast.ncbi.nlm.nih.gov/) :

-Choisir l’outil protein Blast (blastP)

-Copier la séquence ou charger le fichier «alpha\_amy.txt» puis sélectionner la base de données PDB

-Lancer le Blast puis observer les hits retournés :

Que sont les protéines en question (fonction, poids moléculaire ?...)

Quelle est la plus grande couverture d’alignement et quel est le plus grand pourcentage d’identité obtenus ? 

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.004.png)

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.005.png)

Le Template choisi est « Chain A, ALPHA-AMYLASE [Pseudoalteromonas haloplanktis] » (1JD7). 

En général, on choisit selon des critères bien déterminés :

Eliminer les protéines synthétiques, les fragments, les protéines mutantes.

Privilégier les protéines naturelles, ou au pire recombinantes.

Plus grand pourcentage d’identité de séquence avec la protéine cible.

Structures déterminées par cristallographie de rayons X, préférentiellement.

Meilleure résolution possible (plus petit nombre en Angström).

Non redondantes entre elles (plus grande diversité possible entre les templates) o Taille similaire à celle de la protéine cible.

Fonction biologique similaire si possible.

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.006.png)

- Depuis le serveur de la PDB, télécharger le fichier de coordonnées (1jd7 .pdb) correspondant à la structure qui sera utilisée comme Template pour la modélisation.

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.007.png)

**Etape 2 : Alignement des séquences cible et Template**

- Préparation du fichier Template :

-Ouvrir le fichier « <a name="_hlk131029978"></a>1jd7.pdb » avec un logiciel de visualisation de structures de protéines tel que PyMOL ou Chimera.

-Supprimer tous les hétéroatomes et les molécules autres que la protéine elle-même, car ils ne sont pas nécessaires pour la modélisation comparative.  

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.008.png)


` `*Autre méthode :*

*On peut faire ces modifications directement avec un éditeur de texte (par exemple, Notepad, Sublime Text, Atom, pluma pour Unix..)*

\- Sauvegarder le fichier du Template en format PDB « 1jd7\_clean.pdb ».

-Convertir le fichier <a name="_hlk130959418"></a>« 1jd7\_clean.pdb » en format fasta à l'aide d'un outil en ligne tel que <https://zhanggroup.org/pdb2fasta/>.

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.009.png)

- Accéder au site http://www.ebi.ac.uk/Tools/psa/emboss\_needle/ et copier/coller les séquences de la cible et du Template dans les deux champs prévus à cet effet. Ensuite, cliquer sur "submit" pour obtenir l'alignement.

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.010.png)

- Enregistrer le résultat obtenu dans un fichier « alignement.txt ».

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.011.png)

- A partir de ce fichier <a name="_hlk131038952"></a>créer un fichier d’alignement au format PIR « ali.pir » tout en suivant la documentation de Modeller ( section « Alignment file » : <https://salilab.org/modeller/manual/node13.html#SECTION00661200000000000000>)

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.012.png)

**Etape 3 : Construction du modèle d'homologie :**

- Préparation du fichier de script Python :

À ce stade, on a le fichier d'alignement "ali.pir", le fichier de structure du Template "1jd7\_clean.pdb". Maintenant on a besoin du fichier de script Python qui informera Modeller des différentes étapes de modélisation.

Créer un fichier de script Python "modeling.py" dans le même dossier que les autres fichiers en suivant la documentation de Modeller (section « Script file » : <https://salilab.org/modeller/manual/node13.html#SECTION00661300000000000000> ).

Dans ce script nous avons choisi d'obtenir 10 modèles (plusieurs modèles pour évaluer la qualité et la cohérence des prédictions).

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.013.png)

- Exécution du script :

En utilisant le terminal de Modeller, exécuter le script à l'aide de la commande suivante :

$ mod10.4 modeling.py

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.014.png)


**Etape 4 : Evaluation de la qualité du modèle d'homologie**

<a name="_hlk131045642"></a>L'évaluation de la qualité du modèle d'homologie est une étape essentielle dans le processus de modélisation de protéines. Elle consiste à évaluer la validité stéréochimique et la qualité locale du modèle généré, afin de déterminer si celui-ci est proche de la structure native de la protéine. Cette évaluation peut être effectuée à l'aide de différents outils et logiciels en ligne, tels que le serveur SwissModel, le serveur Prosa, Verify3D, ERRAT, et la mesure du score DOPE local. L'objectif est de sélectionner le modèle présentant la meilleure qualité pour une utilisation ultérieure dans des études structurelles et fonctionnelles de la protéine.

- **Score DOPE (Discrete Optimized Protein Energy) :**

Le score DOPE évalue la qualité globale du modèle en termes d'énergie et de probabilité de structure native. En général, le modèle avec le score DOPE le plus bas est considéré comme le meilleur, car cela signifie qu'il a la plus faible énergie et la plus grande probabilité d'être proche de la structure native de la protéine.

Le score du modèle DOPE est conçu pour sélectionner la meilleure structure parmi une collection de modèles construits par MODELLER. 

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.015.png)

**Calcul du score DOPE avec la commande « selection.assess\_dope() »**

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.016.png)

**Autre méthode :** 

La commande suivante **: « Get-ChildItem \*.pdb | ForEach-Object {Select-String -Path $\_.FullName -Pattern "DOPE score"} | Out-File -FilePath scores2.txt»** recherche tous les fichiers pdb dans le dossier courant (alpha\_amy), extrait le score DOPE pour chaque fichier et les enregistre dans un fichier appelé "scores2.txt".

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.017.png)

**Calcul du score DOPE avec commande Get sur PowerShell (grep pour unix)**

Le modèle avec le score DOPE le plus bas est généralement considéré comme **le meilleur modèle** de la protéine cible. (Modèle 10 : alpha\_amy.B99990010.pdb)

- **Méthode DOPE normalisée :**

Le score DOPE n'est pas normalisé par rapport à la taille de la protéine et a une échelle arbitraire, ce qui rend difficile la comparaison de scores entre différentes protéines. Pour surmonter cette limitation, la méthode DOPE normalisée permet de calculer un score Z, qui peut être utilisé pour comparer les scores DOPE de différents modèles.

Les scores positifs sont susceptibles d'être de mauvais modèles, tandis que les scores inférieurs à -1 ou plus sont **susceptibles d'être de type natif**. (Modèle 10 : alpha\_amy.B99990010.pdb)

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.018.png)

**Calcul du Z-score avec la commande « model.assess\_normalized\_dope()»**

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.019.png)

- **Diagramme de Ramachandran**

Le diagramme de Ramachandran est un outil important pour évaluer la qualité stéréochimique d'un modèle. Il permet de visualiser la distribution des angles de torsion φ et ψ de chaque résidu dans une structure protéique. Les angles de torsion autorisés se regroupent en régions définies sur le diagramme de Ramachandran. Les régions les plus courantes sont les régions autorisées, les régions favorables et les régions défavorables.

Soumettre les modèles sélectionnés au serveur Web : https://swissmodel.expasy.org/assess et vérifie leur validité stéréochimique.

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.020.png)

En général, un modèle avec des scores Ramachandran favorisés élevés et des scores Ramachandran outliers et des scores MolProbity et Clash faibles est considéré comme de bonne qualité stéréochimique. Dans l'ensemble, tous les modèles présentent **une qualité stéréochimique acceptable** avec des scores élevés pour les régions autorisées du diagramme de Ramachandran et des pourcentages très faibles de conformations latérales inappropriées.

- **Qualité locale du modèle**

Le serveur Prosa analysera le modèle de protéine et générera un certain nombre de graphiques et de résultats pour évaluer la qualité de votre modèle.

Accéder au site Web de Prosa : https://prosa.services.came.sbg.ac.at/prosa.php

Cliquer sur "Choose File" et sélectionnez le fichier «alpha\_amy.B99990010.pdb » .

Cliquer sur "Submit Query" pour soumettre votre fichier.

Le deuxième graphique est un tracé de fréquence d'énergie potentielle normalisé. Il montre la **distribution de l'énergie potentielle** de la structure comparée à une distribution normale. Les pics dans l'histogramme indiquent des régions où l'énergie potentielle est élevée et donc la structure est moins stable. (Selon ce graphique le modèle semble **bien stable**)

Le premier graphique est le **plot Z-score**, qui représente l'énergie potentielle de la structure en fonction de la position de chaque résidu dans la séquence. Les régions en bleu foncé correspondent aux régions de la protéine où l'énergie potentielle est la plus basse et donc où la structure est la plus stable. Les régions en jaune ou rouge (absentes dans ce graphique) correspondent aux régions où l'énergie potentielle est plus élevée, indiquant une structure moins stable.

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.021.png)![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.022.png)![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.023.png)![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.024.png)![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.025.png)

- **Évaluation de la précision de la modélisation d'homologie de l'α-amylase par alignement avec la structure expérimentale**

L'alignement entre la structure modélisée et la structure cristalline est une étape importante pour évaluer la qualité du modèle. Cela permet de comparer la conformation spatiale de la structure prédite avec celle de la structure expérimentale résolue. Le logiciel PyMol permet d'effectuer cet alignement en utilisant les atomes de carbone alpha comme référence.

Ce type d'analyse permet d'obtenir des informations sur la qualité de la prédiction de la structure ainsi que sur les régions où des erreurs ont pu être introduites.

- Ouvrir les structures de modèle (alpha\_amy.B99990010.pdb ), de cristal(<a name="_hlk131106600"></a>1aqm.pdb) et de template (1jd7\_clean.pdb) dans une nouvelle session PyMol.
- Entrer les commandes suivantes :

select reference, 1aqm\_1 and name CA

mob\_model, alpha\_amy.B99990010 and name CA

align mob\_model, reference

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.026.png)

Les résultats indiquent que l'alignement des atomes CA des deux structures (notre modèle et la structure de référence) a réussi avec succès. Le RMSD est généralement exprimé en Å (angstroms) et peut être utilisé pour évaluer la qualité de l'alignement. Dans ce cas, le RMSD est de 0,355 angströms indique une très bonne correspondance entre les deux structures. Cela suggère que notre modèle de l'alpha-amylase est très proche de la structure cristalline de référence et peut être utilisé pour des analyses et des prédictions ultérieures.

De la même manière, aligner la structure du modèle (alpha\_amy.B99990010.pdb) avec le cristal (1aqm.pdb).

- Entrer les commandes suivantes :

select mob\_template, 1jd7\_clean and name CA

align mob\_template, reference

![](Aspose.Words.f7fc63ad-96a3-474b-ba4a-1ff6b42ed1cd.027.png)

Le résultat montre que l'alignement du modèle avec la structure de référence a un RMSD de 0.355 Å et l'alignement du Template avec la structure de référence a un RMSD de 0.320 Å. Cela suggère que le modèle et le Template sont bien alignés avec la structure de référence et que le modèle est de **qualité raisonnable** pour être utilisé pour des études ultérieures.

**Conclusion :** 

Après les évaluations précédentes, le modèle alpha\_amy.B99990010 peut être considéré comme une bonne approximation de la structure réelle de l'alpha-amylase d'*Alteromonas haloplanktis*.





