---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/cs-CZ/8bb76fa4-db1c-4c09-a9e8-268ade96e4da-17580333180c2830db51bd4dcd72a710.mp3
---

## Ahoj, Pythone!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Ahoj, jmenuji se Hugo a provedu tě kurzem Úvod do Pythonu pro datovou vědu.

Jsem datový vědec a lektor ve DataCampu.

---

## Jak se budete učit

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Rozhraní DataCampu](https://assets.datacamp.com/img/translations/cs-CZ/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
V tomto kurzu se naučíš Python pro datovou vědu prostřednictvím videolekcí, jako je tato, a interaktivních cvičení. Budeš mít vlastní Python session, kde můžeš experimentovat a hledat správný kód pro splnění zadání. Učíš se praxí a zároveň dostáváš okamžitou a přizpůsobenou zpětnou vazbu na svou práci.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/cs-CZ/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Obecný jazyk: vhodný pro libovolné projekty{{2}}

- Open source! Zdarma!{{3}}

- Balíčky Pythonu, i pro datovou vědu{{4}}

	- Mnoho aplikací a oblastí{{5}}

`@script`
Python vznikl z iniciativy Guida Van Rossuma. Tady vidíš mou fotografii s Guidem. Co začalo jako hobby projekt, se brzy proměnilo v univerzální programovací jazyk: dnes v Pythonu napíšeš prakticky jakýkoli software. Jak k tomu došlo? Python je open source — je zdarma. A navíc je v něm velmi snadné vytvářet balíčky, tedy kód, který můžeš sdílet s ostatními a řešit konkrétní problémy. Postupem času vzniklo stále více balíčků přímo určených pro datovou vědu. Chceš vytvořit působivé vizualizace prodejů své firmy? Na to existuje balíček. Nebo se potřebuješ připojit k databázi a analyzovat data ze senzorů? Na to taky balíček najdeš.
Lidé často přirovnávají Python k švýcarskému armádnímu nožíku programovacích jazyků, protože s ním dokážeš skoro cokoliv.
V tomto kurzu budeme postupně rozvíjet tvé dovednosti v oblasti datové vědy, takže rozhodně zůstaň — uvidíš, jak mocný tento jazyk je.

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Spouštění příkazů Pythonu**

![ipython_shell.png](https://assets.datacamp.com/img/translations/cs-CZ/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Teď, když máš chuť se do Pythonu pustit, začneme experimentovat. Začnu s

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Spouštění příkazů Pythonu**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/cs-CZ/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python shellem — místem, kde zadáváš kód v Pythonu a okamžitě vidíš výsledky. V prostředí cvičení na DataCampu je tento shell umístěn zde. Začneme jednoduše a použijeme Python jako kalkulačku.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Výpočty v IPython Shellu DataCampu](https://assets.datacamp.com/img/translations/cs-CZ/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Napíšu 4 + 5 a stisknu Enter. Python zadání vyhodnotí a zobrazí výsledek výpočtu: 9. Shell, který zde používáme, ale není ten původní — pracujeme s IPythonem, zkráceně z Interactive Python, což je vylepšená verze klasického Pythonu, která se nám bude hodit později.

IPython vytvořil Fernando Pérez a je součástí širšího ekosystému Jupyter. Kromě interaktivní práce v Pythonu můžeš také spouštět takzvané

---

## Skript v Pythonu

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Textové soubory - `.py`{{1}}

- Seznam příkazů Pythonu{{2}}

- Podobné jako psaní v IPython Shellu{{3}}

![Skript v Pythonu v DataCampu](https://assets.datacamp.com/img/translations/cs-CZ/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
Python skripty. Python skripty jsou jednoduše textové soubory s příponou .py. Jde v podstatě o seznam příkazů v Pythonu, které se spustí postupně — skoro jako bys je zadával v shellu řádek po řádku.

---

## Skript v Pythonu

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: zadání 4 + 5 ve skriptu a odeslání odpovědi. Žádný výstup se nezobrazí.](https://assets.datacamp.com/img/translations/cs-CZ/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Předchozí příkaz teď vložíme do skriptu, který najdeš zde v rozhraní DataCampu. Dalším krokem je spuštění skriptu kliknutím na „Submit Answer". Pokud skript spustíš, v panelu výstupu se nic nezobrazí. Je to proto, že ve skriptech musíš výstup explicitně vypsat pomocí funkce print.

---

## Skript v Pythonu

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/cs-CZ/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Pomocí `print()` zobrazíte výstup skriptu

`@script`
Předchozí výpočet zabalíme do volání print a skript spustíme znovu. Tentokrát se zobrazí stejný výstup jako předtím — výborně! Ukládání kódu do skriptů místo ručního zadávání každého kroku ti pomůže udržet přehled a ušetří opakované přepisování, kdykoli chceš něco změnit — stačí upravit skript a znovu ho spustit.

---

## Rozhraní DataCampu

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Snímek rozhraní DataCampu](https://assets.datacamp.com/img/translations/cs-CZ/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Teď, když víš, jak různými způsoby pracovat s Pythonem, doporučuji přejít ke cvičením. Používej IPython Shell pro experimentování a editor Python skriptů pro psaní samotného řešení. Po kliknutí na „Submit Answer" se tvůj skript spustí a zkontroluje jeho správnost.

---

## Pojďme procvičovat!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Pusť se do kódování a hlavně si to užij!
