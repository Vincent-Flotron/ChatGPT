Je serais heureux de vous aider à vous entraîner en programmation avec VBScript. Voici 4 exercices avec leurs corrigés pour vous entraîner aux variables, tableaux et boucles. Ils vous aideront à vous entraîner aux variables, tableaux et boucles en VBScript.

Exercice 1 : Variable
---------------------

Écrivez un script qui demande à l'utilisateur son nom et qui affiche un message de salutation en utilisant sa réponse.

**Solution :**


```vb
Dim nom
nom = InputBox("Quel est votre nom ?")
MsgBox "Bonjour " & nom & " !"
```

Exercice 2 : Tableaux
---------------------

Écrivez un script qui crée un tableau contenant les noms de 5 fruits, puis qui parcourt le tableau et affiche chaque élément.

**Solution :**


```vb
Dim fruits(4)
fruits(0) = "pomme"
fruits(1) = "banane"
fruits(2) = "orange"
fruits(3) = "kiwi"
fruits(4) = "fraise"

For i = 0 To 4
    MsgBox fruits(i)
Next
```

Exercice 3 : Boucles
--------------------

Écrivez un script qui demande à l'utilisateur de saisir un nombre entier et qui affiche tous les nombres de 1 jusqu'à ce nombre.

**Solution :**


```vb
Dim n
n = InputBox("Entrez un nombre entier :")

For i = 1 To n
    MsgBox i
Next
```

Exercice 4 : Boucles et tableaux
--------------------------------

Écrivez un script qui crée un tableau contenant les noms de 5 pays, puis qui parcourt le tableau et affiche chaque élément avec son numéro d'ordre.

**Solution :**


```vb
Dim pays(4)
pays(0) = "France"
pays(1) = "Espagne"
pays(2) = "Italie"
pays(3) = "Allemagne"
pays(4) = "Royaume-Uni"

For i = 0 To 4
    MsgBox i+1 & ". " & pays(i)
Next
```
