Fonctions
---------
L'objectif est de créer une fonction qui prend un tableau de nombres en entrée, calcule leur somme et retourne le résultat. Ensuite, nous allons appeler cette fonction avec un tableau de nombres et afficher le résultat dans une boîte de dialogue :

```vb
Function calculerSomme(nombres)
    Dim somme
    somme = 0
    
    For i = 0 To UBound(nombres)
        somme = somme + nombres(i)
    Next
    
    calculerSomme = somme
End Function

' Appeler la fonction avec un tableau de nombres
Dim nombres(4)
nombres(0) = 2
nombres(1) = 5
nombres(2) = 8
nombres(3) = 3
nombres(4) = 1

Dim resultat
resultat = calculerSomme(nombres)

MsgBox "La somme des nombres est : " & resultat
```

La fonction calculerSomme prend un tableau de nombres en entrée, calcule leur somme à l'aide d'une boucle For et retourne le résultat avec l'instruction calculerSomme = somme. Ensuite, nous appelons la fonction avec un tableau de nombres et stockons le résultat dans la variable resultat. Enfin, nous affichons le résultat dans une boîte de dialogue.
