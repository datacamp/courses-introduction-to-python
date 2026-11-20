---
title_meta: अध्याय 2
title: Python लिस्ट्स
description: >-
  डेटा को लिस्ट्स में स्टोर करना, एक्सेस करना और मैनीप्युलेट करना सीखें: भारी
  मात्रा में डेटा पर प्रभावी ढंग से काम करने की पहली सीढ़ी.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python लिस्ट्स
  - nb_of_exercises: 4
    title: लिस्ट्स का सबसेट बनाना
  - nb_of_exercises: 5
    title: लिस्ट्स में बदलाव
---

## Python Lists

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## एक लिस्ट बनाएँ

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

लिस्ट एक **compound data type** है; आप इस तरह से कई वैल्यू को साथ समूहित कर सकते हैं:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

अपने परिवार की ऊँचाई मापने के बाद, आप जिस घर में रहते हैं उसकी कुछ जानकारी इकट्ठा करने का फैसला करते हैं. आपके घर के अलग-अलग हिस्सों का एरिया इस अभ्यास में अलग-अलग वैरिएबल्स में स्टोर किया गया है.

`@instructions`
- एक लिस्ट `areas` बनाएँ, जिसमें क्रम से hallway (`hall`), kitchen (`kit`), living room (`liv`), bedroom (`bed`) और bathroom (`bath`) का एरिया हो. प्री-डिफाइंड वैरिएबल्स का उपयोग करें.
- `print()` फंक्शन से `areas` प्रिंट करें.

`@hint`
- आप बनी-बनाई वैरिएबल्स का इस्तेमाल करके लिस्ट बना सकते हैं: `areas = [hall, kit, ...]`.
- पेरेंथेसिस `()` की जगह स्क्वेयर ब्रैकेट्स `[]` का उपयोग ज़रूर करें.
- लिस्ट के अंदर वैरिएबल्स स्टोर करते समय उद्धरण चिह्नों की ज़रूरत नहीं होती.
- सबमिट करते समय लिस्ट प्रिंट करने के लिए `print(areas)` टाइप करें.

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
predef_msg = "पूर्वनिर्धारित वेरिएबल्स को न हटाएँ या संपादित न करें!"
areas_msg = "`areas` को उन सभी क्षेत्र वेरिएबल्स की सूची के रूप में परिभाषित करें, सही क्रम में: `[hall, kit, liv, bed, bath]`. टाइपो से सावधान रहें। सूची में और कुछ नहीं होना चाहिए!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:क्या आपने अपने स्क्रिप्ट के अंत में `areas` सूची को प्रिंट करने के लिए `{{sol_call}}` का उपयोग किया है?"),
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

success_msg("अच्छा! यहाँ एक सूची बहुत बेहतर है, है ना?")
```

---

## अलग-अलग टाइप वाली लिस्ट बनाएँ

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

हालाँकि यह बहुत आम नहीं है, एक लिस्ट में strings, floats, और booleans जैसे Python टाइप्स का मिश्रण भी हो सकता है.

अब आप अपनी लिस्ट में कमरों के नाम जोड़ने जा रहे हैं, ताकि आप आसानी से कमरे का नाम और आकार, दोनों एक साथ देख सकें.

आपके शुरुआत करने के लिए कुछ कोड दिया गया है. यहाँ ध्यान दें! `"bathroom"` एक string है, जबकि `bath` एक वैरिएबल है जो उस float `9.50` को दर्शाता है जिसे आपने पहले निर्दिष्ट किया था.

`@instructions`
- वह कोड पूरा करें जो `areas` लिस्ट बनाता है. लिस्ट ऐसी बनाइए कि हर कमरे का नाम पहले string के रूप में आए और उसके बाद उसका area. यानी, उपयुक्त स्थानों पर strings `"hallway"`, `"kitchen"` और `"bedroom"` जोड़ें.
- `areas` को फिर से प्रिंट करें; क्या इस बार आउटपुट अधिक जानकारीपूर्ण है?

`@hint`
- लिस्ट `areas` के पहले चार एलिमेंट इस तरह कोड किए गए हैं: `["hallway", hall, "kitchen", kit, ...`.
- किसी string को डबल quotation मार्क्स `""` में होना चाहिए.

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
predef_msg = "पूर्वनिर्धारित वेरिएबल्स को न हटाएं या संपादित न करें!"
areas_msg = "आपने `areas` को सही मान नहीं सौंपा है। निर्देशों को फिर से देखें। सुनिश्चित करें कि प्रत्येक बार क्षेत्र वाले वेरिएबल से पहले कमरे का नाम रखें। यहाँ क्रम महत्वपूर्ण है! टाइपो से सावधान रहें।"

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:क्या आपने अपने स्क्रिप्ट के अंत में `areas` सूची को प्रिंट करने के लिए `{{sol_call}}` का उपयोग किया है?")

success_msg("बहुत बढ़िया! इस सूची में स्ट्रिंग्स और फ्लोट्स दोनों शामिल हैं, लेकिन यह पायथन के लिए कोई समस्या नहीं है!")
```

---

## List of lists

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

एक डेटा साइंटिस्ट के रूप में, आप अक्सर बहुत सारा डेटा संभालेंगे, और इनमें से कुछ डेटा को ग्रुप करना समझदारी होगी.

ऐसी लिस्ट बनाने के बजाय जिसमें strings और floats हों जो आपके घर के कमरों के नाम और एरिया दर्शाएँ, आप लिस्ट की लिस्ट बना सकते हैं.

याद रखें: `"hallway"` एक string है, जबकि `hall` एक वैरिएबल है जो पहले बताए गए float `11.25` को दर्शाता है.

`@instructions`
- लिस्ट की लिस्ट को पूरा करें ताकि उसमें bedroom और bathroom का डेटा भी शामिल हो. ध्यान रखें कि इन्हें सही क्रम में दर्ज करें!
- `house` को प्रिंट करें; क्या इस तरह डेटा को स्ट्रक्चर करना ज़्यादा समझ में आता है?

`@hint`
- `house` लिस्ट में _sublists_ जोड़ें: स्क्वेयर ब्रैकेट्स के अंदर `["bedroom", bed]` और `["bathroom", bath]` शामिल करें.
- हर sublist के बाद कॉमा `,` लगाना न भूलें.
- किसी वैरिएबल `x` को प्रिंट करने के लिए, नई पंक्ति में `print(x)` लिखें.

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
predef_msg = "पूर्वनिर्धारित वेरिएबल्स को न हटाएँ या संपादित न करें!"
house_msg = "आपने `house` को सही मान नहीं सौंपा है। निर्देशों को फिर से देखें। सूचियों की सूची का विस्तार करें ताकि यह प्रत्येक कमरे के नाम और कमरे के क्षेत्र के लिए एक सूची को शामिल करे। क्रम और टाइपो का ध्यान रखें!"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:क्या आपने `{{sol_call}}` का उपयोग `house` की सामग्री को प्रिंट करने के लिए किया है?")

success_msg("बहुत बढ़िया! सूची उपसेटिंग के बारे में सीखने के लिए तैयार हो जाइए!")
```

---

## Lists का Subsetting

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Subset और आगे बढ़ें

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Python लिस्ट्स को subset करना बहुत आसान है. नीचे दिए गए कोड सैंपल में एक लिस्ट `x` बनाई गई है और फिर उसमें से "b" चुना गया है. ध्यान रखें कि यह दूसरा एलिमेंट है, इसलिए इसका इंडेक्स 1 है. आप negative indexing भी इस्तेमाल कर सकते हैं.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # वही परिणाम!
```

पहले वाली `areas` लिस्ट याद है, जिसमें strings और floats दोनों हैं? उसकी परिभाषा पहले से ही स्क्रिप्ट में मौजूद है. क्या आप Python subsetting करने के लिए सही कोड जोड़ सकते हैं?

`@instructions`
- `areas` लिस्ट से दूसरा एलिमेंट प्रिंट करें (जिसका मान `11.25` है).
- `areas` का आखिरी एलिमेंट subset करके प्रिंट करें, जो `9.50` है. यहाँ negative index इस्तेमाल करना समझदारी है!
- लिविंग रूम के एरिया (`20.0`) को दर्शाने वाली संख्या चुनें और उसे प्रिंट करें.

`@hint`
- लिस्ट `x` का दूसरा एलिमेंट चुनने के लिए `x[1]` इस्तेमाल करें.
- लिस्ट `x` का आखिरी एलिमेंट चुनने के लिए `x[-1]` इस्तेमाल करें.
- अपनी subsetting ऑपरेशन्स को `print()` कॉल में ज़रूर लपेटें.
- लिविंग रूम के एरिया को दिखाने वाली संख्या लिस्ट का 6वाँ एलिमेंट है, इसलिए यहाँ `[5]` चाहिए. `area[4]` तो स्ट्रिंग दिखा देगा!

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
msg = "पूर्वनिर्धारित `areas` सूची को न हटाएँ या संपादित न करें।"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "अपने कोड को फिर से देखें ताकि आप `areas` की दूसरी तत्व को प्रिंट कर सकें, जो कि इंडेक्स `1` पर है।")
Ex().has_printout(1, not_printed_msg = "अपने कोड को फिर से देखें ताकि आप `areas` की अंतिम तत्व को प्रिंट कर सकें, जो कि इंडेक्स `-1` पर है।")
Ex().has_printout(2, not_printed_msg = "अपने कोड को फिर से देखें ताकि आप लिविंग रूम के क्षेत्रफल को प्रिंट कर सकें। यह इंडेक्स `5` पर है।")
success_msg("शानदार काम!")
```

---

## Slicing और dicing

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

किसी list से एक-एक वैल्यू चुनना पूरी कहानी नहीं है. आप अपनी list को _slice_ भी कर सकते हैं, यानी एक साथ कई एलिमेंट्स चुन सकते हैं. इसके लिए यह सिंटैक्स इस्तेमाल करें:

```
my_list[start:end]
```

`start` इंडेक्स शामिल होता है, जबकि `end` इंडेक्स _शामिल नहीं_ होता. हालाँकि, इन इंडेसेज़ को न बताना भी संभव है. अगर आप `start` इंडेक्स नहीं बताते, तो Python समझ लेता है कि आप अपनी list की शुरुआत से slice करना चाहते हैं.

`@instructions`
- slicing का उपयोग करके `downstairs` नाम की list बनाएँ, जिसमें `areas` के पहले 6 एलिमेंट्स हों.
- `upstairs` बनाएँ, जिसमें `areas` के आखिरी `4` एलिमेंट्स हों. इस बार slicing में `end` इंडेक्स छोड़ कर लिखाई को सरल करें.
- `print()` का उपयोग करके `downstairs` और `upstairs` दोनों को प्रिंट करें.

`@hint`
- कोष्ठक `[0:6]` का उपयोग करके किसी list के पहले छह एलिमेंट्स पाएँ.
- किसी list `l` के पहले 5 एलिमेंट्स को छोड़कर बाकी सब पाने के लिए `l[5:]` लिखें.
- `downstairs` और `upstairs` को प्रिंट करने के लिए दो `print()` कॉल जोड़ें.

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
msg = "पूर्वनिर्धारित `areas` सूची को न हटाएँ या संपादित न करें।"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` गलत है। उन तत्वों का चयन करने के लिए `areas[%s]` और स्लाइसिंग का उपयोग करें, या कुछ समकक्ष।"
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="क्या आपने `downstairs` को गणना करने के बाद प्रिंट किया है?")
Ex().has_printout(1, not_printed_msg="क्या आपने `upstairs` को गणना करने के बाद प्रिंट किया है?")

success_msg("बहुत बढ़िया!")
```

---

## लिस्ट-ऑफ-लिस्ट्स का सबसेटिंग

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

एक Python लिस्ट के अंदर दूसरी लिस्ट्स भी हो सकती हैं.

लिस्ट-ऑफ-लिस्ट्स का सबसेट लेने के लिए आप पहले जैसा ही तरीका अपना सकते हैं: square brackets. किसी लिस्ट `house` के लिए यह कुछ ऐसा दिखेगा:

```
house[2][0]
```

`@instructions`
- `house` लिस्ट का सबसेट लेकर float `9.5` निकालिए.

`@hint`
- इसे चरण-दर-चरण हल करें। पहले लिस्ट के आखिरी एलिमेंट तक पहुँचिए, `["bathroom", 9.50]`. याद रखें कि आखिरी एलिमेंट का इंडेक्स `-1` होता है.
- अगला, `["bathroom", 9.50]` के दूसरे एलिमेंट तक पहुँचिए, जो इंडेक्स `1` पर है.

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

success_msg("सही! सूची पहेली का अंतिम टुकड़ा हेरफेर है।")
```

---

## Lists में Manipulation

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## लिस्ट के एलिमेंट बदलें

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

लिस्ट के एलिमेंट को बदलने के लिए, आप लिस्ट का सबसेट चुनते हैं और नए मान उस सबसेट को असाइन करते हैं। आप किसी एकल एलिमेंट का चयन कर सकते हैं या एक साथ पूरी लिस्ट के स्लाइस को बदल सकते हैं।

इस और अगले अभ्यासों के लिए, आप `areas` लिस्ट पर ही काम जारी रखेंगे, जिसमें किसी घर के अलग-अलग कमरों के नाम और उनके एरिया हैं।

`@instructions`
- नेगेटिव इंडेक्सिंग का उपयोग करके बाथरूम का एरिया `9.50` की जगह `10.50` वर्ग मीटर कर दें।
- `areas` लिस्ट को और ट्रेंडी बनाएँ! `"living room"` को `"chill zone"` में बदल दें। इस बार नेगेटिव इंडेक्सिंग का उपयोग न करें।

`@hint`
- बाथरूम के एरिया को अपडेट करने के लिए, पहले बाथरूम वाले हिस्से को सबसेट करें (यह लिस्ट का आखिरी आइटम है!).
- फिर, इस सबसेट को नया बाथरूम एरिया असाइन करके वैल्यू बदल दें।
- यही तरीका `"living room"` के नाम को अपडेट करने के लिए भी अपनाएँ, जो इंडेक्स 4 पर है।

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
bathroom_msg = 'आप `areas[-1] = 10.50` का उपयोग बाथरूम क्षेत्र को अपडेट करने के लिए कर सकते हैं।'
chillzone_msg = 'आप `areas[4] = "chill zone"` का उपयोग लिविंग रूम का नाम अपडेट करने के लिए कर सकते हैं।'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'आपके द्वारा `areas` में किए गए परिवर्तन सही सूची का परिणाम नहीं देते हैं। क्या आप सुनिश्चित हैं कि आपने सही उपसमुच्चय संचालन का उपयोग किया है? संदेह होने पर, आप एक संकेत का उपयोग कर सकते हैं!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('शानदार! जैसा कि कोड नमूने ने दिखाया, आप एक सूची को स्लाइस कर सकते हैं और इसे दूसरी सूची के साथ बदल सकते हैं ताकि एक ही कमांड में कई तत्वों को अपडेट किया जा सके।')
```

---

## सूची को बढ़ाएँ

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

अगर आप किसी list के एलिमेंट बदल सकते हैं, तो आप उनमें नए एलिमेंट जोड़ना भी चाहेंगे, है ना? इसके लिए आप `+` ऑपरेटर का उपयोग कर सकते हैं:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

आपने लॉटरी जीत ली—कमाल है! आपने एक पूलहाउस और एक गैराज बनाने का फैसला किया है. क्या आप यह जानकारी `areas` list में जोड़ सकते हैं?

`@instructions`
- `+` ऑपरेटर का उपयोग करके list `["poolhouse", 24.5]` को `areas` list के अंत में जोड़ें. परिणामस्वरूप list को `areas_1` नाम से स्टोर करें.
- `areas_1` को आगे बढ़ाते हुए अपने गैराज का डेटा जोड़ें. स्ट्रिंग `"garage"` और float `15.45` जोड़ें. परिणामस्वरूप list का नाम `areas_2` रखें.

`@hint`
- असाइनमेंट में दिए गए कोड सैंपल का अनुसरण करें. यहाँ `x` `areas` है, और `["e", "f"]` `["poolhouse", 24.5]` है.
- `areas_1` में और एलिमेंट जोड़ने के लिए `areas_1 + ["element", 123]` का उपयोग करें.

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
msg = "पूर्वनिर्धारित `areas` सूची को न हटाएँ या संपादित न करें।"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "`areas + [\"poolhouse\", 24.5]` का उपयोग करके `areas_1` बनाएँ। टाइपो से सावधान रहें!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "`areas_1 + [\"garage\", 15.45]` का उपयोग करके `areas_2` बनाएँ। टाइपो से सावधान रहें!")
success_msg("बहुत बढ़िया! सूची अच्छी तरह से आकार ले रही है!")
```

---

## लिस्ट के एलिमेंट्स हटाएँ

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

आखिर में, आप अपनी लिस्ट से एलिमेंट्स हट भी सकते हैं. यह काम आप `del` स्टेटमेंट से कर सकते हैं:

```
x = ["a", "b", "c", "d"]
del x[1]
```

यहाँ ध्यान दीजिए: जैसे ही आप लिस्ट से कोई एलिमेंट हटाते हैं, हटाए गए एलिमेंट के बाद आने वाले सभी एलिमेंट्स के इंडेक्स बदल जाते हैं!

दुर्भाग्य से, लॉटरी में जीती गई रकम उतनी बड़ी नहीं निकली, और लगता है कि पूलहाउस अब संभव नहीं है. आपको इसे लिस्ट से हटाना होगा. आप `areas` लिस्ट से उससे जुड़ी string और float को हटाने का फ़ैसला करते हैं.

`@instructions`
- अपनी `areas` लिस्ट से `"poolhouse"` के लिए दी गई string और float हटा दें.
- अपडेटेड `areas` लिस्ट को प्रिंट करें.

`@hint`
- दो एलिमेंट हटाने के लिए आपको `del` का इस्तेमाल दो बार करना होगा. लेकिन ध्यान रखें: ऐसा करने पर इंडेक्स बदलते हैं!

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

Ex().has_printout(0, not_printed_msg="क्या आपने पूलहाउस स्ट्रिंग और फ्लोट को हटाने के बाद `areas` को प्रिंट किया है?")
success_msg("सही! आप बाद में Python सूचियों से विशिष्ट तत्वों को हटाने के आसान तरीकों के बारे में जानेंगे।")
```

---

## लिस्ट का अंदरूनी कामकाज

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

इस अभ्यास में आपके लिए कुछ कोड दिया गया है: `areas` नाम की एक लिस्ट और उसकी एक कॉपी `areas_copy`.

फिलहाल, `areas_copy` लिस्ट के पहले तत्व को बदला जाता है और `areas` लिस्ट प्रिंट की जाती है। अगर आप रन कोड बटन दबाते हैं तो आप देखेंगे कि भले ही आपने `areas_copy` बदली है, वही बदलाव `areas` लिस्ट में भी दिख रहा है। ऐसा इसलिए है क्योंकि `areas` और `areas_copy` एक ही लिस्ट की ओर इशारा करते हैं.

अगर आप चाहते हैं कि `areas_copy` में किए गए बदलाव `areas` पर असर न करें, तो आपको `areas` लिस्ट की एक स्पष्ट कॉपी `list()` से या `[:]` का उपयोग करके बनानी होगी.

`@instructions`
- दूसरे कमांड को बदलें, जो वैरिएबल `areas_copy` बनाता है, ताकि `areas_copy`, `areas` की एक स्पष्ट कॉपी हो। आपके बदलाव के बाद, `areas_copy` में किए गए परिवर्तन `areas` को प्रभावित नहीं करने चाहिए। यह जाँचने के लिए उत्तर सबमिट करें.

`@hint`
- `areas_copy = areas` वाली कॉल बदलें। `areas` असाइन करने के बजाय, आप `list(areas)` या `areas[:]` असाइन कर सकते हैं.

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "`areas_copy` को सही ढंग से अपडेट नहीं किया गया है ऐसा प्रतीत होता है।"),
  check_function("list", missing_msg = "`areas_copy` बनाने के लिए `list(areas)` का उपयोग करना सुनिश्चित करें।")
)

mmsg = "पूर्वनिर्धारित `areas` सूची को न हटाएँ।"
imsg = "सुनिश्चित करें कि केवल प्रतिलिपि को ही संपादित करें, मूल `areas` सूची को नहीं। यदि आपको प्रतिलिपि बनाने का तरीका समझ में नहीं आ रहा है, तो व्यायाम विवरण को फिर से देखें।"
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "`areas_copy` बनाने के लिए `list(areas)` का उपयोग करना सुनिश्चित करें।")
)

success_msg("अच्छा! स्पष्ट और संदर्भ-आधारित प्रतियों के बीच का अंतर सूक्ष्म है, लेकिन वास्तव में महत्वपूर्ण हो सकता है। यह ध्यान में रखने की कोशिश करें कि कंप्यूटर की मेमोरी में सूची कैसे संग्रहीत होती है।")
```
