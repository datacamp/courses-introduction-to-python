---
title_meta: अध्याय 3
title: फंक्शंस और पैकेजेज
description: >-
  आप सीखेंगे कि बेहतरीन Python डेवलपर्स द्वारा लिखे गए कोड का कुशलतापूर्वक लाभ
  उठाने के लिए फंक्शंस, मेथड्स और पैकेजेज कैसे उपयोग करें. लक्ष्य है कि
  चुनौतीपूर्ण समस्याएँ सुलझाने के लिए आपको कम से कम कोड लिखना पड़े!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: फंक्शंस
  - nb_of_exercises: 4
    title: मेथड्स
  - nb_of_exercises: 4
    title: पैकेजेज
---

## Functions

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## पहचाने-पहचाने functions

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python शुरू से ही कई built-in functions देता है, जिनसे एक data scientist के रूप में आपका काम आसान हो जाता है। आप पहले से दो ऐसे functions जानते हैं: `print()` और `type()`। इसके अलावा `str()`, `int()`, `bool()` और `float()` जैसे functions भी हैं, जिनसे आप data types के बीच स्विच कर सकते हैं। इनके बारे में आप [यहाँ](https://docs.python.org/3/library/functions.html) पढ़ सकते हैं। ये भी built-in functions ही हैं।

किसी function को कॉल करना आसान है। `3.0` का type पाने और उसे `result` नाम के नए वैरिएबल में स्टोर करने के लिए आप यह लिखेंगे:

```
result = type(3.0)
```

`@instructions`
- `type()` के साथ `print()` का इस्तेमाल करके `var1` का type प्रिंट करें।
- `len()` का उपयोग करके लिस्ट `var1` की [length](https://docs.python.org/3/library/functions.html#len) निकालें। उसे सीधे प्रिंट करने के लिए `print()` में wrap करें।
- `int()` का उपयोग करके `var2` को [integer](https://docs.python.org/3/library/functions.html#int) में बदलें। आउटपुट को `out2` के रूप में स्टोर करें।

`@hint`
- `type()` फंक्शन को ऐसे कॉल करें: `type(var1)`.
- `print()` को वैसे ही कॉल करें जैसे आपने पहले कई बार किया है। जिस वैरिएबल को प्रिंट करना है, उसे कोष्ठकों में रखिए।
- `int(x)` से `x` को integer में बदला जा सकता है.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
____

# Print out length of var1
____

# Convert var2 to an integer: out2
out2 = ____
```

`@solution`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

`@sct`
```{python}
msg = "आपको पूर्वनिर्धारित वेरिएबल्स को बदलने या हटाने की आवश्यकता नहीं है।"
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:सुनिश्चित करें कि `var1` के %s को `{{sol_call}}` के साथ प्रिंट करें।"
Ex().has_printout(0, not_printed_msg = patt % 'प्रकार')
Ex().has_printout(1, not_printed_msg = patt % 'लंबाई')

int_miss_msg = "`int()` का उपयोग करके `var2` का पूर्णांक बनाया है?"
int_incorr_msg = "क्या आपने `var2` को `int()` में पास किया है?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="आपने `int()` को सही तरीके से कॉल किया है; अब सुनिश्चित करें कि इस कॉल के परिणाम को `out2` को असाइन करें।"),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("बहुत अच्छा काम! `len()` फ़ंक्शन अत्यंत उपयोगी है; यह स्ट्रिंग्स पर भी काम करता है ताकि वर्णों की संख्या गिनी जा सके!")
```

---

## Help!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

हो सकता है आपको किसी Python फंक्शन का नाम पता हो, लेकिन उसका उपयोग कैसे करें यह जानना हो। दिलचस्प बात यह है कि किसी फंक्शन के बारे में जानकारी पाने के लिए आपको एक और फंक्शन बुलाना पड़ता है: `help()`। खासकर IPython में, आप फंक्शन नाम से पहले `?` भी लगा सकते हैं।

उदाहरण के लिए, `max()` फंक्शन पर मदद पाने के लिए, आप इनमें से कोई एक कॉल कर सकते हैं:

```
help(max)
?max
```

IPython Shell का उपयोग करके `pow()` की [documentation](https://docs.python.org/3/library/functions.html#pow) खोलिए। ऐसा करने के लिए `?pow` या `help(pow)` टाइप करें और **Enter** दबाएँ।

निम्न में से कौन-सा कथन सही है?

`@possible_answers`
- `pow()` तीन आर्ग्युमेंट लेता है: `base`, `exp`, और `mod`। `mod` न देने पर फंक्शन error देगा।
- `pow()` तीन required आर्ग्युमेंट्स लेता है: `base`, `exp`, और `None`।
- `pow()` में `base` और `exp` आर्ग्युमेंट आवश्यक होते हैं; `mod` वैकल्पिक है।
- `pow()` दो आर्ग्युमेंट्स लेता है: `exp` और `mod`। `exp` न होने पर error आता है.

`@hint`
- वैकल्पिक आर्ग्युमेंट्स को `=` के साथ एक default मान दिया जाता है। अगर वह आर्ग्युमेंट पास नहीं किया गया, तो फंक्शन वही मान उपयोग करेगा.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "सही नहीं। `mod` का एक डिफ़ॉल्ट मान होता है जो उपयोग किया जाएगा यदि आप कोई मान निर्दिष्ट नहीं करते हैं।"
msg2 = "गलत। `mod` तर्क के लिए डिफ़ॉल्ट मान `None` है।"
msg3 = "सही! `help()` का उपयोग करने से आपको यह समझने में मदद मिल सकती है कि फ़ंक्शन कैसे काम करते हैं, उनकी पूरी क्षमता को उजागर करते हैं!"
msg4 = "गलत। `pow()` तीन तर्क लेता है, जिनमें से एक का डिफ़ॉल्ट मान होता है।"
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Multiple arguments

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

पिछले अभ्यास में, आपने `help()` से डॉक्युमेंटेशन देख कर वैकल्पिक आर्ग्युमेंट्स पहचाने थे. अब आप इसे `sorted()` फंक्शन के व्यवहार को बदलने के लिए लागू करेंगे.

IPython Shell में `help(sorted)` टाइप करके `sorted()` के [डॉक्युमेंटेशन](https://docs.python.org/3/library/functions.html#sorted) को देखें.

आप देखेंगे कि `sorted()` तीन आर्ग्युमेंट्स लेता है: `iterable`, `key`, और `reverse`. इस अभ्यास में, आपको केवल `iterable` और `reverse` बताने हैं, `key` नहीं.

आपके लिए दो लिस्ट बनाई गई हैं.

क्या आप इन्हें जोड़कर एक साथ पेस्ट कर सकते हैं और descending ऑर्डर में sort कर सकते हैं?

`@instructions`
- `+` का उपयोग करके `first` और `second` की सामग्री को मिलाकर एक नई लिस्ट `full` बनाएँ.
- `full` पर `sorted()` कॉल करें और `reverse` आर्ग्युमेंट को `True` सेट करें. सॉर्ट की हुई लिस्ट को `full_sorted` के रूप में सेव करें.
- अंत में `full_sorted` को प्रिंट करें.

`@hint`
- `first` और `second` को दो संख्याओं की तरह जोड़ें और परिणाम `full` को असाइन करें.
- `sorted()` को दो इनपुट के साथ इस्तेमाल करें: `full` और `reverse=True`.
- किसी वैरिएबल को प्रिंट करने के लिए `print()` का उपयोग करें.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = ____ + ____

# Sort full in descending order: full_sorted
full_sorted = ____

# Print out full_sorted
____
```

`@solution`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "आपको पहले से मौजूद वेरिएबल्स `first` और `second` को बदलने या हटाने की आवश्यकता नहीं है।"
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="सुनिश्चित करें कि आप `sorted()` को कॉल करने के परिणाम को `full_sorted` में असाइन कर रहे हैं।"),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("बहुत बढ़िया! Python विधियों पर वीडियो देखें।")
```

---

## Methods

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## स्ट्रिंग मेथड्स

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

स्ट्रिंग्स के साथ कई मेथड्स आते हैं. कुछ को जानने के लिए निर्देशों का ध्यान से पालन कीजिए. अगर आप उन्हें विस्तार से देखना चाहते हैं, तो IPython Shell में कभी भी `help(str)` टाइप कर सकते हैं.

आपके लिए प्रयोग करने हेतु एक स्ट्रिंग `place` पहले से बनाई गई है.

`@instructions`
- `place` पर `.upper()` [method](https://docs.python.org/3/library/stdtypes.html#str.upper) का उपयोग करें और परिणाम `place_up` में स्टोर करें. मेथड कॉल करने की वह सिंटैक्स इस्तेमाल कीजिए जो आपने पिछले वीडियो में सीखी थी.
- `place` और `place_up` को प्रिंट करें. क्या दोनों बदले?
- वैरिएबल `place` में मौजूद o की संख्या प्रिंट करें: इसके लिए `place` पर `.count()` कॉल करें और इस मेथड को इनपुट के रूप में अक्षर `'o'` पास करें. हम वैरिएबल `place` की बात कर रहे हैं, शब्द `"place"` की नहीं!

`@hint`
- आप `place` पर बिना किसी अतिरिक्त इनपुट के `.upper()` मेथड कॉल कर सकते हैं.
- किसी वैरिएबल `x` को प्रिंट करने के लिए `print(x)` लिखिए.
- यह सुनिश्चित करें कि आप `place.count(____)` कॉल को `print()` फंक्शन में रैप करें ताकि आउटपुट प्रिंट हो.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = 

# Print out place and place_up



# Print out the number of o's in place

```

`@solution`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

`@sct`
```{python}
msg = "आपको पूर्वनिर्धारित चर को बदलने या हटाने की आवश्यकता नहीं है।"
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "`%s` को प्रिंट करना न भूलें।"
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="अपने `place.upper()` कॉल के परिणाम को `place_up` को असाइन करें।"),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "आपने `place` में o's की संख्या की गणना ठीक से की है; अब सुनिश्चित करें कि `place.count('o')` कॉल को प्रिंट करने के लिए `print()` फ़ंक्शन में लपेटें।"),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("अच्छा! प्रिंटआउट से ध्यान दें कि `upper()` विधि उस वस्तु को नहीं बदलती जिस पर इसे कॉल किया जाता है। यह अगली कसरत में सूचियों के लिए अलग होगा!")
```

---

## लिस्ट मेथड्स

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

केवल strings ही ऐसे Python टाइप नहीं हैं जिनके साथ मेथड्स जुड़े होते हैं. Lists, floats, integers और booleans भी ऐसे टाइप हैं जिनके साथ कई उपयोगी मेथड्स आते हैं. इस अभ्यास में, आप इन पर प्रयोग करेंगे:

- `.index()`, जिससे किसी लिस्ट में दिए गए इनपुट से मेल खाने वाले पहले एलिमेंट का इंडेक्स मिलता है, और
- `.count()`, जिससे पता चलता है कि कोई एलिमेंट लिस्ट में कितनी बार आता है.

आप घर के अलग-अलग हिस्सों के एरिया वाली लिस्ट `areas` पर काम करेंगे.

`@instructions`
- `.index()` मेथड का उपयोग करके `areas` में उस एलिमेंट का इंडेक्स निकालिए जो `20.0` के बराबर है. इस इंडेक्स को प्रिंट करें.
- `areas` पर `.count()` कॉल करके पता लगाइए कि `9.50` लिस्ट में कितनी बार आता है. फिर, बस इस संख्या को प्रिंट करें.

`@hint`
- इंडेक्स प्रिंट करने के लिए, `areas.index(___)` कॉल को `print()` फंक्शन में लपेटें.
- यह प्रिंट करने के लिए कि किसी एलिमेंट `x` की सूची में कितनी बार उपस्थिति है, `areas.count(___)` कॉल को `print()` फंक्शन में लपेटें.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 9.50 appears in areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "आपको पूर्वनिर्धारित सूची `areas` को बदलने या हटाने की आवश्यकता नहीं है।"

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("अच्छा! ये `list` विधियों के उदाहरण थे जिन्होंने उस सूची को नहीं बदला जिस पर उन्हें बुलाया गया था।")
```

---

## लिस्ट मेथड्स (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

अधिकांश लिस्ट मेथड्स उस लिस्ट को बदल देते हैं जिस पर उन्हें कॉल किया जाता है. उदाहरण के लिए:

- `.append()`, जो उस लिस्ट में एक एलिमेंट जोड़ता है जिस पर इसे कॉल किया गया है,
- `.remove()`, जो इनपुट से मेल खाने वाले लिस्ट के पहले एलिमेंट को [हटा देता](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) है, और
- `.reverse()`, जो उस लिस्ट के एलिमेंट्स के क्रम को [उलट देता](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) है जिस पर इसे कॉल किया गया है.

आप घर के अलग-अलग हिस्सों के क्षेत्रफल वाली लिस्ट `areas` पर काम करेंगे.

`@instructions`
- `.append()` का दो बार उपयोग करके poolhouse और garage के आकार फिर से जोड़ें: क्रमशः `24.5` और `15.45`. ध्यान रखें कि इन्हें इसी क्रम में जोड़ें.
- `areas` को प्रिंट करें
- `areas` के एलिमेंट्स के क्रम को उलटने के लिए `.reverse()` मेथड का उपयोग करें.
- `areas` को एक बार फिर प्रिंट करें.

`@hint`
- पहली निर्देश के लिए, `areas.append(___)` कॉल का दो बार उपयोग करें.
- किसी वैरिएबल `x` को प्रिंट करने के लिए बस `print(x)` लिखें.
- `.reverse()` मेथड को अतिरिक्त इनपुट की ज़रूरत नहीं होती; बस डॉट नोटेशन और खाली ब्रैकेट्स का उपयोग करें: `.reverse()`.
- किसी वैरिएबल `x` को प्रिंट करने के लिए बस `print(x)` लिखें.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out areas


# Reverse the orders of the elements in areas


# Print out areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

`@sct`
```{python}
Ex().multi(
  check_function("areas.append", index=0, signature=False).check_args(0).has_equal_value(),
  check_function("areas.append", index=1, signature=False).check_args(0).has_equal_value(),
  check_function("print", index=0).check_args(0).has_equal_ast(),
  check_function("areas.reverse", index=0, signature=False),
  check_function("print", index=1).check_args(0).has_equal_ast()
)

success_msg("बहुत बढ़िया!")
```

---

## Packages

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## पैकेज इम्पोर्ट करें

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

मान लीजिए आप किसी वृत्त की परिधि और क्षेत्रफल निकालना चाहते हैं. उनके फ़ॉर्मूले इस प्रकार हैं:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

`pi` की संख्या खुद टाइप करने के बजाय, आप `math` पैकेज का उपयोग कर सकते हैं जिसमें यह संख्या उपलब्ध होती है.

जानकारी के लिए, `**` घातांक (exponentiation) का प्रतीक है. उदाहरण के लिए, `3**4` का अर्थ है `3` की घात `4`, और परिणाम `81` होगा.

`@instructions`
- `math` पैकेज इम्पोर्ट करें.
- वृत्त की परिधि निकालने के लिए `math.pi` का उपयोग करें और उसे `C` में स्टोर करें.
- वृत्त का क्षेत्रफल निकालने के लिए `math.pi` का उपयोग करें और उसे `A` में स्टोर करें.

`@hint`
- आप सरल रूप से `import math` कर सकते हैं, और फिर `pi` को `math.pi` के रूप में संदर्भित करें.
- `C` निकालने के लिए असाइनमेंट टेक्स्ट में दी हुई समीकरण का उपयोग करें. `*` का प्रयोग करें.
- `A` निकालने के लिए असाइनमेंट टेक्स्ट में दी हुई समीकरण का उपयोग करें. `*` और `**` का प्रयोग करें.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import the math package
import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "`%s` की आपकी गणना सही नहीं है। सुनिश्चित करें कि `math.pi` का उपयोग करें।"
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:व्यास को प्रिंट करने के लिए `{{sol_call}}` को वहीं रखें।"),
  has_printout(1, not_printed_msg = "__JINJA__:क्षेत्रफल को प्रिंट करने के लिए `{{sol_call}}` को वहीं रखें।")
)

success_msg("अच्छा! यदि आप पैकेजों से फ़ंक्शनों को संभालना जानते हैं, तो बहुत से Python प्रोग्रामरों की शक्ति आपके हाथों में है!")
```

---

## Selective import

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

सामान्य इंपोर्ट, जैसे `import math`, `math` पैकेज की **सारी** फ़ंक्शनैलिटी आपके लिए उपलब्ध कर देता है. लेकिन, अगर आप किसी पैकेज के केवल किसी खास हिस्से का उपयोग करना चाहते हैं, तो आप अपना इंपोर्ट और अधिक चयनात्मक बना सकते हैं:

```
from math import pi
```

अब वही काम दोबारा कीजिए, लेकिन इस बार सिर्फ `pi` का इस्तेमाल करें.

`@instructions`
- `math` पैकेज से चयनात्मक इंपोर्ट करें जहाँ आप केवल `pi` को इंपोर्ट करें.
- `pi` का उपयोग करके वृत्त की परिधि निकालें और उसे `C` में स्टोर करें.
- `pi` का उपयोग करके वृत्त का क्षेत्रफल निकालें और उसे `A` में स्टोर करें.

`@hint`
- चयनात्मक इंपोर्ट करने के लिए `from math import pi` का उपयोग करें.
- अब आप `pi` को सीधे इस्तेमाल कर सकते हैं!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import pi function of math package
from math import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "आपकी `%s` की गणना सही नहीं है। सुनिश्चित करें कि केवल `pi` का उपयोग करें।"

Ex().has_import("math.pi", not_imported_msg = "सुनिश्चित करें कि `math` पैकेज से `pi` आयात करें। आपको `from ___ import ___` नोटेशन का उपयोग करना चाहिए।",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:व्यास को प्रिंट करने के लिए `{{sol_call}}` को वहीं रखें।"),
  has_printout(1, not_printed_msg = "__JINJA__:क्षेत्रफल को प्रिंट करने के लिए `{{sol_call}}` को वहीं रखें।")
)

success_msg("अच्छा! अगले अभ्यास पर जाएं।")
```

---

## Import करने के अलग-अलग तरीके

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Python में पैकेज और मॉड्यूल import करने के कई तरीके होते हैं. आप जो import कॉल करेंगे, उसके अनुसार आपको अलग Python कोड लिखना होगा.

मान लीजिए आप `scipy` पैकेज के `linalg` सबपैकेज में मौजूद [function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()` का इस्तेमाल करना चाहते हैं. आप यह फ़ंक्शन इस तरह इस्तेमाल कर पाना चाहते हैं:

```
my_inv([[1,2], [3,4]])
```

ऊपर दिया गया कोड बिना किसी त्रुटि के चलाने के लिए आपको कौन-सा `import` स्टेटमेंट चाहिए?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- IPython शेल में अलग-अलग import स्टेटमेंट आज़माएँ और देखें कि इनमें से कौन-सा `my_inv([[1, 2], [3, 4]])` लाइन को बिना त्रुटि के चलाता है. आपने जो कोड टाइप किया है उसे चलाने के लिए **enter** दबाएँ.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "गलत है, पुनः प्रयास करें। IPython शेल में विभिन्न आयात कथनों को आज़माएँ और देखें कि कौन सा कथन `my_inv([[1, 2], [3, 4]])` को बिना त्रुटियों के चलाने की अनुमति देता है।"
msg4 = "सही! `as` शब्द आपको आयात की जा रही फ़ंक्शन के लिए एक स्थानीय नाम बनाने की अनुमति देता है: `inv()` अब `my_inv()` के रूप में उपलब्ध है।"
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```
