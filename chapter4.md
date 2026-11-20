---
title_meta: अध्याय 4
title: NumPy
description: >-
  NumPy डेटा साइंस का अभ्यास कुशलता से करने के लिए एक मूलभूत Python पैकेज है.
  NumPy array में मौजूद शक्तिशाली टूल्स के साथ काम करना सीखें और डेटा
  एक्सप्लोरेशन की शुरुआत करें.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: 2D NumPy Arrays
  - nb_of_exercises: 3
    title: 'NumPy: बेसिक स्टैटिस्टिक्स'
---

## NumPy

```yaml
type: VideoExercise
key: f4545baa53
xp: 50
```

`@projector_key`
a0487c26210f6b71ea98f917734cea3a

---

## आपका पहला NumPy Array

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

अब आप बेसबॉल की दुनिया में डूबने वाले हैं। इस दौरान, आप `numpy` के बेसिक्स के साथ सहज हो जाएँगे — यह डेटा साइंस करने के लिए एक पावरफुल पैकेज है.

Python स्क्रिप्ट में एक लिस्ट `baseball` पहले से दी गई है, जो कुछ बेसबॉल खिलाड़ियों की हाइट (सेंटीमीटर में) दर्शाती है। क्या आप इससे एक `numpy` array बनाने के लिए कुछ कोड जोड़ सकते हैं?

`@instructions`
- `numpy` पैकेज को `np` के रूप में इंपोर्ट करें, ताकि आप `numpy` को `np` से संदर्भित कर सकें.
- `np.array()` का उपयोग करके `baseball` से एक `numpy` array बनाएँ। इस array का नाम `np_baseball` रखें.
- यह जाँचने के लिए कि आपने सही किया है, `np_baseball` का type प्रिंट करें.

`@hint`
- `import numpy as np` काम कर देगा। अब, जब भी आप `numpy` का कोई फंक्शन इस्तेमाल करना चाहें, तो `np.fun_name()` का उपयोग करें.
- `np.array()` में इनपुट के रूप में `baseball` दें। फंक्शन कॉल के नतीजे को `np_baseball` में असाइन करें.
- किसी वैरिएबल `x` का type प्रिंट करने के लिए बस `print(type(x))` लिखिए.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sample_code`
```{python}
# Import the numpy package as np


baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball


# Print out type of np_baseball

```

`@solution`
```{python}
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a NumPy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

`@sct`
```{python}
predef_msg = "आपको पूर्वनिर्धारित चर को बदलने या हटाने की आवश्यकता नहीं है।"
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("बहुत बढ़िया काम!")
```

---

## बेसबॉल खिलाड़ियों की ऊँचाई

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

आप बेसबॉल के बहुत बड़े फ़ैन हैं. आप MLB (Major League Baseball) को कॉल करके मुख्य खिलाड़ियों की ऊँचाई से जुड़ी कुछ और स्टैटिस्टिक्स पूछते हैं. वे हज़ार से अधिक खिलाड़ियों का डेटा भेजते हैं, जो एक साधारण Python लिस्ट `height_in` के रूप में स्टोर है. ऊँचाई इंच में दी गई है. क्या आप इससे एक `numpy` array बना सकते हैं और यूनिट्स को मीटर में बदल सकते हैं?

`height_in` पहले से उपलब्ध है और `numpy` पैकेज लोड है, इसलिए आप तुरंत शुरू कर सकते हैं (स्रोत: stat.ucla.edu).

`@instructions`
- `height_in` से एक `numpy` array बनाइए. इस नए array का नाम `np_height_in` रखें.
- `np_height_in` प्रिंट करें.
- सभी ऊँचाइयों को इंच से मीटर में बदलने के लिए `np_height_in` को `0.0254` से गुणा करें. नए मानों को एक नए array `np_height_m` में स्टोर करें.
- `np_height_m` प्रिंट करें और जाँचें कि आउटपुट समझ में आ रहा है या नहीं.

`@hint`
- `np.array()` का उपयोग करें और उसे `height` पास करें. परिणाम को `np_height_in` में स्टोर करें.
- किसी वैरिएबल `x` को प्रिंट करने के लिए Python स्क्रिप्ट में `print(x)` टाइप करें.
- कैलकुलेशन ऐसे करें जैसे `np_height_in` एक सिंगल नंबर हो: `np_height_in * conversion_factor` उत्तर का हिस्सा है.
- किसी वैरिएबल `x` को प्रिंट करने के लिए Python स्क्रिप्ट में `print(x)` टाइप करें.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in


# Print out np_height_in


# Convert np_height_in to m: np_height_m


# Print np_height_m

```

`@solution`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
  has_printout(0),
  check_correct(
    check_object('np_height_in').has_equal_value(),
    check_function('numpy.array').check_args(0).has_equal_ast()
  )
)

Ex().check_correct(
  has_printout(1),
  check_object("np_height_m").has_equal_value(incorrect_msg = "`np_height_m` की गणना करने के लिए `np_height_in * 0.0254` का उपयोग करें।")
)

success_msg("बहुत बढ़िया! एक पल में, `numpy` 1000 से अधिक ऊँचाई मापों पर गुणा करता है।")
```

---

## NumPy के साइड इफेक्ट्स

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` वेक्टर अरिथमेटिक करने के लिए बेहतरीन है। लेकिन अगर आप इसकी फ़ंक्शनैलिटी की तुलना रेगुलर Python लिस्ट्स से करें, तो कुछ बातें अलग होती हैं।

पहला, `numpy` arrays में अलग-अलग टाइप के एलिमेंट्स नहीं हो सकते। अगर आप टाइप्स मिलाते हैं, जैसे booleans और integers, तो `numpy` उन्हें अपने-आप एक कॉमन टाइप में कन्वर्ट कर देता है। Booleans जैसे `True` और `False` को numbers के साथ मिलाने पर क्रमशः `1` और `0` माना जाता है, इसलिए array अंततः integers बन जाता है।

दूसरा, सामान्य अरिथमेटिक ऑपरेटर्स, जैसे `+`, `-`, `*` और `/`, का मतलब रेगुलर Python लिस्ट्स और `numpy` arrays के लिए अलग होता है।

वह कोड चुनिए जिसका आउटपुट नीचे दिए गए के बराबर हो:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

`numpy` पैकेज पहले से `np` नाम से इम्पोर्ट किया गया है। आउटपुट देखने के लिए आप हर विकल्प को IPython Shell में चला सकते हैं।

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- अलग-अलग कोड स्निपेट कॉपी करके IPython Shell में पेस्ट करें। कोड चलाने के लिए **enter** दबाएँ और देखें कि किसका आउटपुट `np.array([True, 1, 2]) + np.array([3, 4, False])` से जनरेट हुए आउटपुट से मेल खाता है।

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "गलत। विभिन्न कोड खंडों को आज़माएँ और देखें कि कौन सा लक्ष्य कोड खंड से मेल खाता है।"
msg2 = "बहुत अच्छा! `True` को 1 में परिवर्तित किया जाता है, `False` को 0 में परिवर्तित किया जाता है।"
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## NumPy Arrays का Subsetting

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Subsetting (लिस्ट या arrays पर square bracket नोटेशन का उपयोग) लिस्ट और arrays — दोनों के साथ बिल्कुल एक जैसा काम करता है.

इस अभ्यास में आपके लिए बैकग्राउंड में दो लिस्ट, `height_in` और `weight_lb`, पहले से लोड हैं. इनमें MLB खिलाड़ियों की हाइट और वेट सामान्य लिस्ट के रूप में हैं. साथ ही दो `numpy` arrays, `np_weight_lb` और `np_height_in`, भी आपके लिए तैयार हैं.

`@instructions`
- इंडेक्स 50 पर मौजूद एलिमेंट को प्रिंट करके `np_weight_lb` को subset करें.
- `np_height_in` का वह sub-array प्रिंट करें जिसमें इंडेक्स 100 से लेकर इंडेक्स 110 तक के एलिमेंट्स शामिल हों.

`@hint`
- अपनी subsetting ऑपरेशंस के चारों ओर `print()` कॉल ज़रूर लगाएँ.
- इंडेक्स 100 से लेकर, इंडेक्स 110 को शामिल करते हुए, एलिमेंट्स पाने के लिए `[100:111]` का उपयोग करें.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
```

`@sample_code`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50


# Print out sub-array of np_height_in: index 100 up to and including index 110

```

`@solution`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])
```

`@sct`
```{python}
Ex().has_import("numpy", same_as=False)
msg = "आपको पूर्वनिर्धारित चर को बदलने या हटाने की आवश्यकता नहीं है।"
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("अच्छा! कुछ नया सीखने का समय: 2D NumPy arrays!")
```

---

## 2D NumPy Arrays

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## आपका पहला 2D NumPy Array

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

वास्तविक MLB डेटा पर काम शुरू करने से पहले, एक छोटी list of lists से 2D `numpy` array बनाकर देखते हैं.

इस अभ्यास में, `baseball` एक list of lists है। मुख्य लिस्ट में 4 एलिमेंट हैं। इन प्रत्येक एलिमेंट में क्रम से 4 बेसबॉल खिलाड़ियों की height और weight वाली एक लिस्ट है। स्क्रिप्ट में `baseball` पहले से आपके लिए लिखा हुआ है.

`@instructions`
- `baseball` से 2D `numpy` array बनाने के लिए `np.array()` का उपयोग कीजिए। इसका नाम `np_baseball` रखिए.
- `np_baseball` का type प्रिंट कीजिए.
- `np_baseball` के `shape` attribute को प्रिंट कीजिए। इसके लिए `np_baseball.shape` का उपयोग करें.

`@hint`
- स्क्रिप्ट में `baseball` पहले से ही दिया गया है। इस पर `np.array()` कॉल कीजिए और प्राप्त 2D `numpy` array को `np_baseball` में स्टोर कीजिए.
- दूसरी निर्देशिका के लिए `type()` के साथ `print()` का उपयोग कीजिए.
- `np_baseball.shape` आपको `np_baseball` के dimensions देगा। इसके चारों ओर `print()` कॉल लगाना न भूलें.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball


# Print out the type of np_baseball


# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
msg = "आपको पूर्वनिर्धारित चर को बदलने या हटाने की आवश्यकता नहीं है।"
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    multi(
        has_printout(0),
        has_printout(1)
    ),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("बहुत बढ़िया! अब आप वास्तविक MLB डेटा को 2D `numpy` array में परिवर्तित करने के लिए तैयार हैं!")
```

---

## 2D रूप में Baseball डेटा

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

आप समझते हैं कि इस सारी जानकारी को 2D `numpy` array में पुनर्संरचना करना ज़्यादा समझदारी है.

आपके पास Python की एक list of lists है. इस list of lists में, हर sublist किसी एक baseball खिलाड़ी की लंबाई और वज़न को दर्शाती है. इस लिस्ट का नाम `baseball` है और यह आपके लिए पहले से लोड है (हालाँकि आप इसे देख नहीं सकते).

डेटा को 2D array के रूप में स्टोर करें ताकि `numpy` की अतिरिक्त क्षमताएँ अनलॉक हों.

`@instructions`
- `baseball` से `np.array()` का उपयोग करके एक 2D `numpy` array बनाएँ. इसका नाम `np_baseball` रखें.
- `np_baseball` के `shape` attribute को प्रिंट करें.

`@hint`
- `baseball` पहले से ही Python वातावरण में उपलब्ध है. इस पर `np.array()` कॉल करें और प्राप्त 2D `numpy` array को `np_baseball` में स्टोर करें.
- `np_baseball.shape` आपको `np_baseball` के आयाम देगा. इसके चारों ओर `print()` कॉल लगाना न भूलें.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = 

# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    has_printout(0),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("शानदार! बहु-आयामी `numpy` ऐरे की कुछ अद्भुत विशेषताएँ दिखाने का समय आ गया है!")
```

---

## 2D NumPy Arrays का Subsetting

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

अगर आपका 2D `numpy` array नियमित संरचना वाला है, यानी हर पंक्ति और कॉलम में निश्चित संख्या में मान हैं, तो जटिल subsetting बहुत आसान हो जाती है. नीचे दिए गए कोड में देखें जहाँ लिस्ट-ऑफ-लिस्ट्स से `"a"` और `"c"` निकाले गए हैं.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

कॉमा से पहले वाले इंडेक्स पंक्तियों को दर्शाते हैं, जबकि कॉमा के बाद वाले इंडेक्स कॉलम को. `:` slicing के लिए है; इस उदाहरण में, यह Python को सभी पंक्तियाँ शामिल करने के लिए कहता है.

`@instructions`
- `np_baseball` की 50वीं पंक्ति को प्रिंट करें.
- एक नया वैरिएबल `np_weight_lb` बनाएँ, जिसमें `np_baseball` की पूरी दूसरी कॉलम हो.
- `np_baseball` में 124वें बेसबॉल खिलाड़ी की ऊँचाई (पहली कॉलम) चुनें और उसे प्रिंट करें.

`@hint`
- पहली निर्देश में आपको पंक्ति इंडेक्स 49 चाहिए! खास तौर पर, आपको `[49, :]` का इस्तेमाल करना होगा.
- पूरी दूसरी कॉलम चुनने के लिए, आपको `[:, 1]` चाहिए.
- आखिरी निर्देश के लिए `[123, 0]` इस्तेमाल करें; सब कुछ `print()` स्टेटमेंट में लपेटना न भूलें.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball


# Select the entire second column of np_baseball: np_weight_lb


# Print out height of 124th player

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])
```

`@sct`
```{python}
msg = "आपको पूर्वनिर्धारित वेरिएबल्स को बदलने या हटाने की आवश्यकता नहीं है।"
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "आप `np_baseball[:,1]` का उपयोग `np_weight_lb` को परिभाषित करने के लिए कर सकते हैं। यह पूरे पहले कॉलम का चयन करेगा।")

Ex().has_printout(1)

success_msg("यह अच्छी तरह से चल रहा है!")
```

---

## 2D Arithmetic

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

2D `numpy` arrays, `numpy` arrays की तरह, एलिमेंट-वाइज़ कैलकुलेशन कर सकते हैं.

`np_baseball` आपके लिए दिया गया है; यह फिर से एक 2D `numpy` array है जिसमें 3 कॉलम हैं: कद (इंच में), वज़न (पाउंड में) और उम्र (साल में). `baseball` एक सामान्य सूची-की-सूची के रूप में उपलब्ध है और `updated` एक 2D numpy array के रूप में उपलब्ध है.

`@instructions`
- आपने सभी बेसबॉल खिलाड़ियों के कद, वज़न और उम्र में हुए बदलाव इकट्ठा कर लिए हैं. यह `updated` नाम के 2D `numpy` array के रूप में उपलब्ध है. `np_baseball` और `updated` को जोड़ें और परिणाम प्रिंट करें.
- आप कद और वज़न की इकाइयों को मैट्रिक (क्रमशः मीटर और किलोग्राम) में बदलना चाहते हैं. पहले कदम के रूप में, तीन वैल्यूज़ वाला एक `numpy` array बनाएँ: `0.0254`, `0.453592` और `1`. इस array का नाम `conversion` रखें.
- `np_baseball` को `conversion` से गुणा करें और परिणाम प्रिंट करें.

`@hint`
- `np_baseball + updated` दोनों `numpy` arrays का एलिमेंट-वाइज़ जोड़ करेगा.
- `np.array()` से एक `numpy` array बनाएँ; इनपुट एक साधारण Python सूची होगी जिसमें तीन एलिमेंट हों.
- `np_baseball * conversion` बिना किसी अतिरिक्त काम के चल जाएगा. इसे आज़माएँ! ध्यान रखें कि इसे `print()` कॉल में लपेटें.

`@pre_exercise_code`
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("https://assets.datacamp.com/course/intro_to_python/update.csv", header = None))
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated


# Create numpy array: conversion


# Print out product of np_baseball and conversion

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```

`@sct`
```{python}
Ex().has_import("numpy")

msg = "आपको पूर्वनिर्धारित चर को बदलने या हटाने की आवश्यकता नहीं है।"
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("बहुत बढ़िया काम! ध्यान दें कि बहुत कम कोड के साथ, आप अपने `numpy` डेटा संरचना में सभी मानों को बहुत विशिष्ट तरीके से बदल सकते हैं। यह आपके भविष्य में एक डेटा वैज्ञानिक के रूप में बहुत उपयोगी होगा!")
```

---

## NumPy: बुनियादी सांख्यिकी

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## औसत बनाम माध्यिका

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

अब आप जानते हैं कि अपने डेटा को बेहतर समझने के लिए `numpy` फंक्शंस का उपयोग कैसे करना है.

बेसबॉल डेटा 3 कॉलम्स (height, weight, age) और 1015 रोज़ वाला 2D `numpy` array है. इस `numpy` array का नाम `np_baseball` है. लेकिन डेटा को फिर से व्यवस्थित करने के बाद, आप देखते हैं कि कुछ height वैल्यूज़ असामान्य रूप से अधिक हैं. निर्देशों का पालन करें और पता करें कि जब आप ऐसे तथाकथित outliers से निपट रहे हों, तो कौन-सा summary statistic सबसे उपयुक्त है. `np_baseball` उपलब्ध है.

`@instructions`
- `numpy` array `np_height_in` बनाएँ जो `np_baseball` के पहले कॉलम के बराबर हो.
- `np_height_in` का mean प्रिंट करें.
- `np_height_in` की median प्रिंट करें.

`@hint`
- 2D `numpy` सबसेटिंग का उपयोग करें: समाधान का एक हिस्सा `[:,0]` है.
- अगर `numpy` को `np` के रूप में इम्पोर्ट किया गया है, तो आप किसी NumPy array का mean निकालने के लिए `np.mean()` का उपयोग कर सकते हैं. `print()` कॉल करना न भूलें.
- आखिरी निर्देश के लिए, `np.median()` का उपयोग करें.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create np_height_in from np_baseball


# Print out the mean of np_height_in


# Print out the median of np_height_in

```

`@solution`
```{python}
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "आप `np_baseball[:,0]` का उपयोग करके `np_baseball` से पहला कॉलम चुन सकते हैं"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("1586 इंच की औसत ऊँचाई, यह सही नहीं लगता, है ना? हालांकि, माध्यिका बाहरी मूल्यों से प्रभावित नहीं लगती: 74 इंच पूरी तरह से समझ में आता है। पूरे डेटासेट के समग्र वितरण के बारे में एक विचार प्राप्त करने के लिए हमेशा माध्यिका और औसत दोनों की जाँच करना एक अच्छा विचार है।")
```

---

## Baseball डेटा की जाँच करें

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

क्योंकि mean और median एक-दूसरे से काफी दूर हैं, आप MLB में शिकायत करने का निर्णय लेते हैं। वे गलती ढूँढते हैं और आपको सुधारा हुआ डेटा भेजते हैं। यह फिर से 3 कॉलम वाला 2D NumPy array `np_baseball` के रूप में उपलब्ध है.

एडिटर में Python स्क्रिप्ट में अलग-अलग summary statistics के साथ जानकारीपूर्ण संदेश प्रिंट करने का कोड पहले से मौजूद है और `numpy` पहले से `np` नाम से लोड है। क्या आप बाकी काम पूरा कर सकते हैं? `np_baseball` उपलब्ध है.

`@instructions`
- mean height प्रिंट करने का कोड पहले से दिया गया है। median height के लिए कोड पूरा करें.
- `stddev` निकालने के लिए `np_baseball` की पहली कॉलम पर `np.std()` का उपयोग करें.
- क्या लंबे खिलाड़ी आम तौर पर भारी होते हैं? सहसंबंध जाँचने के लिए `np.corrcoef()` का उपयोग करें और `np_baseball` की पहली और दूसरी कॉलम के बीच का correlation `corr` में स्टोर करें.

`@hint`
- माध्यिका निकालने के लिए `np.median()` का इस्तेमाल करें। पहले सही कॉलम चुनना न भूलें!
- मानक विचलन निकालते समय भी उसी कॉलम का सबसेट लें और `np.std()` का उपयोग करें.
- पहली और दूसरी कॉलम चुनने के लिए `np_baseball[:, 0]` और `np_baseball[:, 1]` का उपयोग करें; यही `np.corrcoef()` के इनपुट हैं.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
import numpy as np
```

`@sample_code`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = ____
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = ____
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = ____
print("Correlation: " + str(corr))
```

`@solution`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

`@sct`
```{python}
msg = "आपको पूर्वनिर्धारित `avg` चर को बदलना या हटाना नहीं चाहिए।"
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "क्या आपने माध्यिका की गणना के लिए `np.median()` का उपयोग किया है?"
incorrect = "`med` की गणना के लिए, `np_baseball` के पहले स्तंभ को `numpy.median()` में पास करें। `np.mean()` का उदाहरण दिखाता है कि यह कैसे किया जाता है।"
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "क्या आपने मानक विचलन की गणना के लिए `np.std()` का उपयोग किया है?"
incorrect = "`stddev` की गणना के लिए, `np_baseball` के पहले स्तंभ को `numpy.std()` में पास करें। `np.mean()` का उदाहरण दिखाता है कि यह कैसे किया जाता है।"
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "क्या आपने सहसंबंध की गणना के लिए `np.corrcoef()` का उपयोग किया है?"
incorrect1 = "`corr` की गणना के लिए, `np.corrcoef()` का पहला तर्क `np_baseball` का पहला स्तंभ होना चाहिए, जैसा कि आपने पहले किया था।"
incorrect2 = "`corr` की गणना के लिए, `np.corrcoef()` का दूसरा तर्क `np_baseball` का दूसरा स्तंभ होना चाहिए। इस बार `[:,0]` के बजाय `[:,1]` का उपयोग करें।"
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("बहुत अच्छा काम! आपने एक ठोस नींव बनाई है - अब समय आ गया है कि आप अपनी सभी नई डेटा विज्ञान कौशल का उपयोग करके और अधिक चुनौतियों का समाधान करें और प्रभाव डालें।")
```
