---
title_meta: अध्याय 1
title: Python बेसिक्स
description: >-
  Python की बुनियादी अवधारणाओं का परिचय. सीखें कि Python को इंटरैक्टिव तरीके से
  और स्क्रिप्ट लिखकर कैसे उपयोग करें. अपने पहले वैरिएबल बनाएँ और Python के बेसिक
  डेटा टाइप्स से परिचित हों.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Hello Python!
  - nb_of_exercises: 5
    title: Variables and Types
---

## Hello Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## आपका पहला Python कोड

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

अब समय है कि आप अपना पहला Python कोड चलाएँ!

कोड सेक्शन में जाएँ और आउटपुट देखने के लिए "कोड चलाएँ" बटन दबाएँ.

`@instructions`
- `print(5 / 8)` का आउटपुट देखने के लिए "कोड चलाएँ" बटन दबाएँ.

`@hint`
- अपना उत्तर सबमिट करने से पहले कोड चलाएँ ताकि आपको आउटपुट देखने और उसे समझने का समय मिले.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@solution`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "__JINJA__:क्या आपने `{{sol_call}}` का उपयोग `5 / 8` को प्रिंट करने के लिए किया है?")
success_msg("बहुत बढ़िया! अगले पर चलते हैं!")
```

---

## कैलकुलेटर के रूप में Python

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

बेसिक कैलकुलेशन के लिए Python बिल्कुल उपयुक्त है. यह जोड़, घटाव, गुणा और भाग कर सकता है.

स्क्रिप्ट में दिया गया कोड कुछ उदाहरण दिखाता है.

अब आपकी बारी है—खुद कुछ कोड लिखकर अभ्यास कीजिए.

`@instructions`
- `# Subtraction` के नीचे `print()` का उपयोग करके `5` में से `5` घटाने का परिणाम प्रिंट करें.
- `# Multiplication` के नीचे `3` को `5` से गुणा करने का परिणाम प्रिंट करें.

`@hint`
- आउटपुट बनाने के लिए आपको `print()` का इस्तेमाल करना होगा.
- आप `-` से घटा सकते हैं और `*` से गुणा कर सकते हैं.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print()

# Multiplication

```

`@solution`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "क्या आपने अपने योग का परिणाम प्रिंट करने के लिए `print(4 + 5)` का उपयोग किया है?")

Ex().has_printout(1, not_printed_msg = "क्या आपने अपने घटाव का परिणाम प्रिंट करने के लिए `print(5 - 5)` का उपयोग किया है?")

Ex().has_printout(2, not_printed_msg = "क्या आपने अपने गुणा का परिणाम प्रिंट करने के लिए `print(3 * 5)` का उपयोग किया है?")

Ex().has_printout(3, not_printed_msg = "क्या आपने अपने विभाजन का परिणाम प्रिंट करने के लिए `print(10 / 2)` का उपयोग किया है?")

success_msg("यह सही है! पायथन आपकी गणना करने में मदद कर सकता है, एक विशेषता जो हमारे डेटा कौशल को बढ़ाने के साथ विश्लेषण के लिए सहायक होगी।")
```

---

## Variables और Types

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## वैरिएबल असाइनमेंट

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Python में, वैरिएबल की मदद से आप किसी वैल्यू को एक नाम से संदर्भित कर सकते हैं। वैल्यू `5` के साथ वैरिएबल `x` बनाने के लिए आप `=` का उपयोग करते हैं, जैसे इस उदाहरण में:

```
x = 5
```

अब आप वास्तविक वैल्यू `5` की जगह इस वैरिएबल का नाम `x` इस्तेमाल कर सकते हैं।

ध्यान रखें, Python में `=` का मतलब असाइनमेंट होता है, यह equality जाँचता नहीं है! अभ्यास में इसे आज़माइए और `____` को अपने कोड से बदलिए.

`@instructions`
- वैल्यू `100` के साथ एक वैरिएबल `savings` बनाएँ.
- इस वैरिएबल को जाँचने के लिए स्क्रिप्ट में `print(savings)` टाइप करें.

`@hint`
- वैरिएबल `savings` बनाने के लिए `savings = 100` टाइप करें.
- वैरिएबल `savings` बनाने के बाद, आप `print(savings)` टाइप कर सकते हैं.
- आपके अंतिम कोड में कहीं भी `____` नहीं होना चाहिए.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Create a variable savings
____

# Print out savings
____
```

`@solution`
```{python}
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```

`@sct`
```{python}
Ex().check_object("savings").has_equal_value(incorrect_msg="वेरिएबल `savings` को `100` असाइन करें।")
Ex().has_printout(0, not_printed_msg = "आपने जो वेरिएबल बनाया है, `savings`, उसे `print(savings)` के साथ प्रिंट करें।")
success_msg("बहुत बढ़िया! अब इस वेरिएबल के साथ कुछ गणनाएँ करने का प्रयास करें!")
```

---

## Variables के साथ कैलकुलेशन

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

आपने अब एक savings वैरिएबल बना लिया है, तो चलिए बचत शुरू करें!

वास्तविक मानों से कैलकुलेशन करने के बजाय, आप वैरिएबल्स का उपयोग कर सकते हैं.

यदि आप हर महीने $10 बचाते, तो अब से चार महीनों बाद आपने कितने पैसे बचाए होते?

`@instructions`
- `monthly_savings` नाम का वैरिएबल बनाएँ, जिसका मान `10` हो, और `num_months` जिसका मान `4` हो.
- `monthly_savings` को `num_months` से गुणा करें और परिणाम `new_savings` में असाइन करें.
- `new_savings` का मान प्रिंट करें.

`@hint`
- आप वैरिएबल्स के साथ वैसे ही कैलकुलेशन कर सकते हैं जैसे संख्याओं के साथ, इसलिए `10 * 4` के बजाय संख्याओं की जगह वैरिएबल्स लगाएँ!
- `new_savings` में राशि देखने के लिए `print()` का उपयोग करें.
- वैरिएबल्स की स्पेलिंग सही रखें!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the variables monthly_savings and num_months



# Multiply monthly_savings and num_months
new_savings = ____

# Print new_savings

```

`@solution`
```{python}
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)
```

`@sct`
```{python}
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "क्या आपने `monthly_savings = 10` का उपयोग करके `monthly_savings` में `10` सहेजा?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "क्या आपने `num_months = 4` का उपयोग करके `num_months` में `4` सहेजा?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "क्या आपने गुणा करने के लिए सही वेरिएबल्स और प्रतीकों का उपयोग किया? अपेक्षित था `monthly_savings * num_months` लेकिन कुछ और मिला।")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "क्या आपने जोड़ने के लिए सही वेरिएबल्स और प्रतीकों का उपयोग किया? अपेक्षित था `savings + new_savings` लेकिन कुछ और मिला।")

Ex().has_printout(0, not_printed_msg="अपने स्क्रिप्ट के अंत में `new_savings` को प्रिंट करना याद रखें।")

success_msg("आपके पास नई बचत में $40 हैं!")
```

---

## अन्य वैरिएबल टाइप्स

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

पिछले अभ्यास में, आपने Python के integer डेटा टाइप के साथ काम किया था:

- `int`, या integer: ऐसा नंबर जिसमें fractional भाग नहीं होता. `savings` जिसका मान `100` है, integer का एक उदाहरण है.

संख्यात्मक डेटा टाइप्स के अलावा, तीन और बहुत सामान्य डेटा टाइप्स हैं:

- `float`, या floating point: ऐसा नंबर जिसमें integer और fractional दोनों भाग होते हैं, जिन्हें एक डॉट से अलग किया जाता है. `1.1` एक float का उदाहरण है.
- `str`, या string: टेक्स्ट को दर्शाने का टाइप. एक string बनाने के लिए आप single या double quotes का उपयोग कर सकते हैं.
- `bool`, या boolean: तार्किक मान दर्शाने का टाइप. यह केवल `True` या `False` हो सकता है (अक्षरों का बड़ा-छोटा होना महत्वपूर्ण है!).

`@instructions`
- एक नया float `half` बनाएँ, जिसका मान `0.5` हो.
- एक नई string `intro` बनाएँ, जिसका मान `"Hello! How are you?"` हो.
- एक नया boolean `is_good` बनाएँ, जिसका मान `True` हो.

`@hint`
- Python में वैरिएबल बनाने के लिए `=` का इस्तेमाल करें. अपनी string को single या double quotes में लिखना न भूलें.
- Python में केवल दो boolean मान होते हैं: `True` और `False`. `TRUE`, `true`, `FALSE`, `false` और अन्य लिखावटें स्वीकार नहीं की जाएँगी.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create a variable half


# Create a variable intro


# Create a variable is_good

```

`@solution`
```{python}
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True
```

`@sct`
```{python}
Ex().check_object("half").has_equal_value(incorrect_msg = "क्या आपने फ्लोट, `0.5` को `half` में सहेजा है?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "हम्म, आपके `intro` वेरिएबल में कुछ गलत है। वर्तनी को दोबारा जांचें और सुनिश्चित करें कि आपने उद्धरण चिह्नों का उपयोग किया है।")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "क्या आपने बूलियन मान को कैपिटलाइज़ किया है? याद रखें कि यहाँ उद्धरण चिह्नों का उपयोग करने की आवश्यकता नहीं है।")

success_msg("बहुत बढ़िया!")
```

---

## अन्य टाइप्स के साथ ऑपरेशंस

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Python में वैरिएबल अलग-अलग टाइप्स के होते हैं. किसी वैरिएबल का टाइप देखने के लिए आप `type()` इस्तेमाल कर सकते हैं. उदाहरण के लिए, `a` का टाइप देखने के लिए चलाएँ: `type(a)`.

अलग-अलग टाइप्स Python में अलग तरह से बर्ताव करते हैं. जैसे, जब आप दो strings को जोड़ते हैं, तो उसका व्यवहार दो integers या दो booleans को जोड़ने से अलग होता है.

अब बारी आपकी है इसे आज़माने की.

`@pre_exercise_code`
```{python}

```

***

```yaml
type: NormalExercise
key: f4e91c4ae9
xp: 50
```

`@instructions`
- `savings` और `new_savings` को जोड़ें और उसे `total_savings` में असाइन करें.
- `type()` का उपयोग करके `total_savings` के टाइप को प्रिंट करें.

`@hint`
- `savings + new_savings` को एक नए वैरिएबल `total_savings` में असाइन करें.
- किसी वैरिएबल `x` का टाइप प्रिंट करने के लिए `print(type(x))` का उपयोग करें.

`@sample_code`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
____
print(total_savings)

# Print the type of total_savings
print(____)
```

`@solution`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))
```

`@sct`
```{python}
# predefined
msg = "आपको पूर्वनिर्धारित चर को बदलने या हटाने की आवश्यकता नहीं है।"

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="`total_savings` चर बनाने के लिए `savings` और `new_savings` को जोड़ें।"),
    has_printout(1, not_printed_msg = "__JINJA__:`total_savings` के प्रकार को प्रिंट करने के लिए `{{sol_call}}` का उपयोग करें।")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- `intro` और `intro` का sum निकालें और परिणाम को `doubleintro` में असाइन करें.
- `doubleintro` प्रिंट करें. क्या आपने यही अपेक्षा की थी?

`@hint`
- `intro + intro` को एक नए वैरिएबल `doubleintro` में असाइन करें.
- किसी वैरिएबल `x` को प्रिंट करने के लिए स्क्रिप्ट में `print(x)` लिखें.

`@sample_code`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
____

# Print out doubleintro
print(____)
```

`@solution`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)
```

`@sct`
```{python}
# predefined
msg = "आपको पूर्वनिर्धारित चर को बदलने या हटाने की आवश्यकता नहीं है।"

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "क्या आपने `intro + intro` का परिणाम `doubleintro` में संग्रहीत किया है?"),
    has_printout(0, not_printed_msg = "यह न भूलें कि `doubleintro` को प्रिंट करना है।")
)

success_msg("अच्छा। ध्यान दें कि कैसे `intro + intro` के कारण `\"Hello! How are you?\"` और `\"Hello! How are you?\"` एक साथ जुड़ जाते हैं।")
```
