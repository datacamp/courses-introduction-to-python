---
title_meta: Capitolul 2
title: Liste în Python
description: >-
  Învață să stochezi, să accesezi și să manipulezi date în liste – primul pas
  spre lucrul eficient cu volume mari de date.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Liste în Python
  - nb_of_exercises: 4
    title: Extragerea elementelor din liste
  - nb_of_exercises: 5
    title: Manipularea listelor
---

## Liste Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Creează o listă

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

O listă este un **tip de date compus**; poți grupa valori împreună, astfel:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

După ce ai măsurat înălțimea membrilor familiei tale, decizi să colectezi câteva informații despre casa în care locuiești. Suprafețele diferitelor încăperi din casă sunt stocate în variabile separate în cadrul exercițiului.

`@instructions`
- Creează o listă, `areas`, care să conțină suprafața holului (`hall`), bucătăriei (`kit`), sufrageriei (`liv`), dormitorului (`bed`) și băii (`bath`), în această ordine. Folosește variabilele predefinite.
- Afișează `areas` cu ajutorul funcției `print()`.

`@hint`
- Poți folosi variabilele deja create pentru a construi lista: `areas = [hall, kit, ...]`.
- Asigură-te că folosești paranteze pătrate `[]` în loc de paranteze rotunde `()`.
- Nu este nevoie să folosești ghilimele când stochezi variabile într-o listă.
- Scrie `print(areas)` pentru a afișa lista la trimiterea răspunsului.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "Nu eliminați și nu modificați variabilele predefinite!"
areas_msg = "Definiți `areas` ca lista care conține toate variabilele de suprafață, în ordinea corectă: `[hall, kit, liv, bed, bath]`. Aveți grijă la greșelile de scriere. Lista nu ar trebui să conțină altceva!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Ați folosit `{{sol_call}}` pentru a afișa lista `areas` la sfârșitul scriptului dumneavoastră?"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("Excelent! O listă este mult mai potrivită aici, nu-i așa?")
```

---

## Creează liste cu tipuri diferite

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Deși nu este foarte frecvent, o listă poate conține și o combinație de tipuri Python: șiruri de caractere, numere cu virgulă mobilă și valori booleene.

Acum vei adăuga numele camerelor în lista ta, astfel încât să poți vedea cu ușurință atât numele, cât și suprafața fiecărei camere.

O parte din cod a fost deja scrisă pentru tine. Atenție! `"bathroom"` este un șir de caractere, în timp ce `bath` este o variabilă care reprezintă valoarea `9.50` definită anterior.

`@instructions`
- Completează codul care creează lista `areas`. Construiește lista astfel încât să conțină mai întâi numele fiecărei camere ca șir de caractere, apoi suprafața acesteia. Cu alte cuvinte, adaugă șirurile `"hallway"`, `"kitchen"` și `"bedroom"` în locurile potrivite.
- Afișează din nou `areas`; de data aceasta, informațiile sunt mai clare?

`@hint`
- Primele patru elemente ale listei `areas` sunt definite ca `["hallway", hall, "kitchen", kit, ...`.
- Un șir de caractere trebuie să fie între ghilimele `""`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "Nu ștergeți și nu editați variabilele predefinite!"
areas_msg = "Nu ați atribuit valoarea corectă variabilei `areas`. Aruncați o altă privire la instrucțiuni. Asigurați-vă că plasați numele camerei înaintea variabilei care conține suprafața de fiecare dată. Ordinea contează aici! Aveți grijă la greșelile de scriere."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Ați folosit `{{sol_call}}` pentru a afișa lista `areas` la sfârșitul scriptului dumneavoastră?")

success_msg("Excelent! Această listă conține atât șiruri de caractere, cât și numere cu virgulă mobilă, dar aceasta nu reprezintă o problemă pentru Python!")
```

---

## Listă de liste

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Ca om de știință a datelor, vei lucra adesea cu cantități mari de date, iar gruparea acestora are mult sens.

În loc să creezi o listă cu șiruri de caractere și numere reale care reprezintă numele și suprafețele camerelor din casa ta, poți crea o listă de liste.

Amintește-ți: `"hallway"` este un șir de caractere, în timp ce `hall` este o variabilă ce reprezintă valoarea `11.25` pe care ai specificat-o anterior.

`@instructions`
- Completează lista de liste astfel încât să conțină și datele pentru dormitor și baie. Asigură-te că le introduci în ordine!
- Afișează `house`; această modalitate de a-ți structura datele are mai mult sens?

`@hint`
- Adaugă _subliste_ la lista `house` introducând `["bedroom", bed]` și `["bathroom", bath]` în interiorul parantezelor pătrate.
- Nu uita să incluzi o virgulă `,` după fiecare sublistă.
- Pentru a afișa o variabilă `x`, scrie `print(x)` pe o linie nouă.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "Nu ștergeți și nu modificați variabilele predefinite!"
house_msg = "Nu ați atribuit valoarea corectă variabilei `house`. Revedeți instrucțiunile. Extindeți lista de liste astfel încât să includă câte o listă pentru fiecare pereche de nume de cameră și suprafață. Aveți grijă la ordine și greșeli de scriere!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Ați folosit `{{sol_call}}` pentru a afișa conținutul variabilei `house`?")

success_msg("Excelent! Pregătiți-vă să învățați despre indexarea listelor!")
```

---

## Extragerea elementelor din liste

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Selectează și cucerește

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Indexarea listelor Python este simplă. Uită-te la exemplul de mai jos, care creează o listă `x` și selectează "b" din ea. Reține că acesta este al doilea element, deci are indexul 1. Poți folosi și indexarea negativă.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # același rezultat!
```

Îți amintești lista `areas` de mai devreme, care conținea atât șiruri de caractere, cât și numere reale? Definiția ei se află deja în script. Poți adăuga codul potrivit pentru a face câteva operații de indexare în Python?

`@instructions`
- Afișează al doilea element din lista `areas` (are valoarea `11.25`).
- Selectează și afișează ultimul element din `areas`, adică `9.50`. Folosirea unui index negativ are sens aici!
- Selectează numărul care reprezintă suprafața livingului (`20.0`) și afișează-l.

`@hint`
- Folosește `x[1]` pentru a selecta al doilea element al unei liste `x`.
- Folosește `x[-1]` pentru a selecta ultimul element al unei liste `x`.
- Asigură-te că înfășori operațiile de indexare într-un apel `print()`.
- Numărul care reprezintă suprafața livingului este al 6-lea element din listă, deci vei folosi `[5]` aici. `area[4]` ar afișa șirul de caractere!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "Nu eliminați și nu editați lista predefinită `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Aruncați o altă privire asupra codului dumneavoastră pentru a afișa al doilea element din `areas`, care se află la indexul `1`.")
Ex().has_printout(1, not_printed_msg = "Aruncați o altă privire asupra codului dumneavoastră pentru a afișa ultimul element din `areas`, care se află la indexul `-1`.")
Ex().has_printout(2, not_printed_msg = "Aruncați o altă privire asupra codului dumneavoastră pentru a afișa suprafața sufrageriei. Aceasta se află la indexul `5`.")
success_msg("Bună treabă!")
```

---

## Feliere și segmentare

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Selectarea unui singur element dintr-o listă este doar o parte din poveste. Poți, de asemenea, să _felieri_ lista, adică să selectezi mai multe elemente simultan. Folosește sintaxa de mai jos:

```
my_list[start:end]
```

Indexul `start` este inclus, în timp ce indexul `end` _nu_ este inclus. Există și posibilitatea de a nu specifica acești indecși. Dacă nu specifici indexul `start`, Python înțelege că vrei să începi felierea de la primul element al listei.

`@instructions`
- Folosește felierea pentru a crea o listă, `downstairs`, care să conțină primele 6 elemente din `areas`.
- Creează `upstairs` ca ultimele `4` elemente din `areas`. De data aceasta, simplifică felierea omițând indexul `end`.
- Afișează atât `downstairs`, cât și `upstairs` folosind `print()`.

`@hint`
- Folosește parantezele `[0:6]` pentru a obține primele șase elemente ale unei liste.
- Pentru a obține tot ce urmează după primele 5 elemente ale unei liste `l`, folosești `l[5:]`.
- Adaugă două apeluri `print()` pentru a afișa `downstairs` și `upstairs`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "Nu eliminați și nu editați lista predefinită `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` este incorect. Utilizați `areas[%s]` și feliere pentru a selecta elementele dorite sau o metodă echivalentă."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Ați afișat `downstairs` după calcularea acesteia?")
Ex().has_printout(1, not_printed_msg="Ați afișat `upstairs` după calcularea acesteia?")

success_msg("Excelent!")
```

---

## Selectarea elementelor din liste de liste

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

O listă Python poate conține și alte liste.

Pentru a selecta elemente din liste de liste, folosești aceeași tehnică: parantezele pătrate. Pentru o listă numită `house`, ar arăta astfel:

```
house[2][0]
```

`@instructions`
- Selectează din lista `house` valoarea float `9.5`.

`@hint`
- Abordează problema pas cu pas. Mai întâi, accesează ultimul element al listei, `["bathroom", 9.50]`. Reține că indexul ultimului element este `-1`.
- Apoi accesează al doilea element din `["bathroom", 9.50]`, care se află la indexul `1`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("Corect! Ultima piesă a puzzle-ului listei este manipularea.")
```

---

## Manipularea listelor

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Înlocuirea elementelor dintr-o listă

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Pentru a înlocui elementele dintr-o listă, selectezi un subset al listei și atribui noile valori acelui subset. Poți selecta elemente individuale sau poți modifica porțiuni întregi din listă dintr-o dată.

Pentru acest exercițiu și cele următoare, vei continua să lucrezi cu lista `areas`, care conține numele și suprafețele diferitelor camere dintr-o casă.

`@instructions`
- Actualizează suprafața băii la `10.50` metri pătrați în loc de `9.50`, folosind indexare negativă.
- Dă listei `areas` un aer mai modern! Schimbă `"living room"` în `"chill zone"`. De data aceasta, nu folosi indexare negativă.

`@hint`
- Pentru a actualiza suprafața băii, identifică subsetul corespunzător (este ultimul element din listă!).
- Apoi, înlocuiește valoarea cu noua suprafață a băii prin atribuire la acest subset.
- Procedează la fel pentru a actualiza numele `"living room"`, care se află la indexul 4.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = 'Puteți folosi `areas[-1] = 10.50` pentru a actualiza suprafața băii.'
chillzone_msg = 'Puteți folosi `areas[4] = "chill zone"` pentru a actualiza numele camerei de zi.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Modificările aduse listei `areas` nu au dus la lista corectă. Sunteți sigur că ați folosit operațiile corecte de subset? În caz de îndoială, puteți folosi un indiciu!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Excelent! Așa cum a arătat exemplul de cod, puteți, de asemenea, să selectați o porțiune dintr-o listă și să o înlocuiți cu o altă listă pentru a actualiza mai multe elemente într-o singură comandă.')
```

---

## Extinde o listă

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Dacă poți modifica elementele unei liste, cu siguranță vrei să poți și adăuga elemente noi, nu-i așa? Poți folosi operatorul `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Tocmai ai câștigat la loterie – felicitări! Decizi să construiești o piscină acoperită și un garaj. Poți adăuga informațiile corespunzătoare în lista `areas`?

`@instructions`
- Folosește operatorul `+` pentru a adăuga lista `["poolhouse", 24.5]` la sfârșitul listei `areas`. Stochează lista rezultată în `areas_1`.
- Extinde mai departe `areas_1` adăugând date despre garajul tău. Adaugă șirul de caractere `"garage"` și numărul cu virgulă mobilă `15.45`. Numește lista rezultată `areas_2`.

`@hint`
- Urmează modelul de cod din enunț. `x` este `areas` aici, iar `["e", "f"]` este `["poolhouse", 24.5]`.
- Pentru a adăuga mai multe elemente la `areas_1`, folosește `areas_1 + ["element", 123]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "Nu eliminați și nu editați lista predefinită `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Utilizați `areas + [\"poolhouse\", 24.5]` pentru a crea `areas_1`. Atenție la greșeli de scriere!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Utilizați `areas_1 + [\"garage\", 15.45]` pentru a crea `areas_2`. Atenție la greșeli de scriere!")
success_msg("Excelent! Lista prinde formă!")
```

---

## Ștergerea elementelor dintr-o listă

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

În final, poți și să elimini elemente din lista ta. Poți face asta cu instrucțiunea `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Fii atent: imediat ce elimini un element dintr-o listă, indecșii tuturor elementelor care urmează după cel șters se modifică!

Din păcate, suma câștigată la loterie nu este chiar atât de mare și se pare că piscina acoperită nu mai este o opțiune. Va trebui să o elimini din listă. Decizi să ștergi atât șirul de caractere, cât și numărul zecimal corespunzător din lista `areas`.

`@instructions`
- Șterge șirul de caractere și numărul zecimal corespunzătoare `"poolhouse"` din lista ta `areas`.
- Afișează lista `areas` actualizată.

`@hint`
- Va trebui să folosești `del` de două ori pentru a șterge două elemente. Fii atent la modificarea indecșilor!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="Ați afișat `areas` după eliminarea șirului și a numărului float pentru piscină?")
success_msg("Corect! Veți învăța mai târziu despre modalități mai simple de a elimina elemente specifice din listele Python.")
```

---

## Cum funcționează listele în interior

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

În acest exercițiu ai deja un cod de pornire: o listă cu numele `areas` și o copie numită `areas_copy`.

În prezent, primul element din lista `areas_copy` este modificat, iar lista `areas` este afișată. Dacă apeși butonul Rulează codul, vei observa că, deși ai modificat `areas_copy`, schimbarea se reflectă și în lista `areas`. Acest lucru se întâmplă pentru că `areas` și `areas_copy` indică spre aceeași listă.

Dacă vrei să împiedici ca modificările din `areas_copy` să se reflecte și în `areas`, trebuie să faci o copie explicită a listei `areas` folosind `list()` sau sintaxa `[:]`.

`@instructions`
- Modifică a doua comandă, cea care creează variabila `areas_copy`, astfel încât `areas_copy` să fie o copie explicită a lui `areas`. După modificare, schimbările făcute în `areas_copy` nu ar trebui să afecteze `areas`. Trimite răspunsul pentru a verifica.

`@hint`
- Modifică apelul `areas_copy = areas`. În loc să atribui `areas`, poți atribui `list(areas)` sau `areas[:]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "Se pare că `areas_copy` nu a fost actualizat corect."),
  check_function("list", missing_msg = "Asigurați-vă că utilizați `list(areas)` pentru a crea un `areas_copy`.")
)

mmsg = "Nu eliminați lista predefinită `areas`."
imsg = "Asigurați-vă că editați DOAR copia, nu lista originală `areas`. Aruncați o altă privire asupra descrierii exercițiului dacă nu sunteți sigur cum să creați o copie."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Asigurați-vă că utilizați `list(areas)` pentru a crea un `areas_copy`.")
)

success_msg("Excelent! Diferența dintre copiile explicite și cele bazate pe referințe este subtilă, dar poate fi foarte importantă. Încercați să țineți minte cum este stocată o listă în memoria calculatorului.")
```
