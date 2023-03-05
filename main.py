auditions = {
    "proviseur": {
        },
    "professeur": {
        },
    "perturbateur": {
        },
    "eleve": {
        }
    }

sinscrire: str
sinscrire = sNom = input('votre nom, SVP : ').capitalize()
sClasse = input('votre classe ? (deux lettre un chiffre)')
sRole = int(input('''role prefere (chiffre entre 1 et 4) :
[1] proviseur
[2] professeur
[3] pertubateur
[4] eleve
'''))

if sRole == 1:
    auditions['proviseur'][sNom] = sClasse
elif sRole == 2:
    auditions['professeur'][sNom] = sClasse
elif sRole == 3:
    auditions['perturbateur'][sNom] = sClasse
else:
    auditions['eleve'][sNom] = sClasse

print("*** Auditions de un jour sans proviseur")
for i in range(5):
    sinscrire

print("*** Inscription pour cette audition closes ! ***")

print("role de proviseur :")
for sEleve, sClasse in auditions['proviseur'].items():
    print(sEleve, sClasse)

print("role de professeur :")
for sEleve, sClasse in auditions['professeur'].items():
    print(sEleve, sClasse)

print("role de pertubateur")
for sEleve, sClasse in auditions['pertubateur'].items():
    print(sEleve, sClasse)

print("role d'eleve :")
for sEleve, sClasse in auditions['eleve'].items():
    print(sEleve, sClasse)