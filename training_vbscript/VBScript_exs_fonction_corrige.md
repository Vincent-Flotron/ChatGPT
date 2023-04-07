Consigne : Créez une fonction qui prend en entrée un nombre entier et retourne "true" si ce nombre est pair et "false" sinon. Ensuite, utilisez cette fonction pour afficher un message indiquant si un nombre donné est pair ou impair.

Exemple de résolution :

```vb
Function estPair(n)
    If n Mod 2 = 0 Then
        estPair = True
    Else
        estPair = False
    End If
End Function

' Demander à l'utilisateur de saisir un nombre entier
Dim nombre
nombre = InputBox("Entrez un nombre entier :")

' Vérifier si le nombre est pair ou impair en utilisant la fonction estPair
If estPair(nombre) Then
    MsgBox nombre & " est pair."
Else
    MsgBox nombre & " est impair."
End If
```

La fonction estPair prend en entrée un nombre entier et utilise une instruction If-Then pour vérifier si le nombre est pair ou impair. Si le nombre est pair, la fonction retourne "true", sinon elle retourne "false".

Ensuite, nous demandons à l'utilisateur de saisir un nombre entier avec l'instruction InputBox, puis nous utilisons la fonction estPair pour vérifier si le nombre est pair ou impair. Enfin, nous affichons un message dans une boîte de dialogue pour indiquer si le nombre est pair ou impair.