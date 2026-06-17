---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/hi-IN/97b8ecd4-b9e6-4c9b-9056-671abe4995e7-e40b517fc7759428dc2bfae518ea2f50.mp3
---

## 2D NumPy Arrays

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
शाबाश, आप तो कमाल कर रहे हैं! अब पिछले वीडियो वाले numpy arrays को दोबारा बनाएँ.

---

## NumPy Arrays का प्रकार

```yaml
type: FullSlide
key: 1b9db47fd2
code_zoom: 100
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

```py
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`
अगर आप इन arrays का type पूछते हैं, तो Python बताएगा कि ये numpy.ndarray हैं. numpy का डॉट बताता है कि यह एक type है जो numpy पैकेज में परिभाषित है. ndarray का मतलब है n-dimensional array. np_height और np_weight एक-आयामी arrays हैं, लेकिन 2-आयामी, 3-आयामी, यहाँ तक कि 7-आयामी arrays बनाना भी पूरी तरह संभव है! इस वीडियो में फिलहाल 2 पर ही टिके रहते हैं.

---

## 2D NumPy Arrays

```yaml
type: FullSlide
key: ebb550dcba
code_zoom: 71
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```{{1}}
```py
np_2d
```{{2}}

```out
array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
```{{2}}

```py
np_2d.shape
```{{3}}

```out
(2, 5) # 2 rows, 5 columns
```{{3}}

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```{{4}}

```out
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')
```{{4}}

`@script`
आप एक साधारण Python list of lists से 2D numpy array बना सकते हैं. आइए अपनी फैमिली के सारे height और weight डेटा के लिए एक numpy array बनाने की कोशिश करें, कुछ इस तरह.

अगर आप अब np_2d को प्रिंट करते हैं, तो दिखेगा कि यह एक आयताकार डेटा स्ट्रक्चर है. लिस्ट के भीतर हर sublist, दो-आयामी numpy array में एक row के बराबर होती है. np_2d.shape से आप देख सकते हैं कि वाकई 2 rows और 5 columns हैं. shape, np_2d array का एक attribute है, जो आपको डेटा स्ट्रक्चर के बारे में और जानकारी दे सकता है.

ध्यान रखें, किसी attribute को एक्सेस करने की सिंटैक्स देखने में method कॉल जैसी लगती है, लेकिन वे अलग होती हैं. याद रखिए, methods के बाद गोल ब्रैकेट होते हैं. और, जैसा यहाँ दिख रहा है, attributes के बाद नहीं होते.

साथ ही 2D arrays के लिए भी वही NumPy नियम लागू होता है. एक array में केवल एक ही type के मान हो सकते हैं. अगर आप किसी एक float को string में बदलते हैं, तो पूरा array strings में बदल जाएगा, ताकि array समान type का बना रहे.

---

## Subsetting

```yaml
type: FullSlide
key: e71d2fc8b8
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0]
```

```out
array([1.73, 1.68, 1.71, 1.89, 1.79])
```

`@script`
2D numpy array को आप lists of lists का बेहतर रूप मान सकते हैं. आप arrays पर वैसी ही गणनाएँ कर सकते हैं जैसी पहले दिखाई गईं, और अधिक उन्नत subsetting भी कर सकते हैं.

मान लीजिए आपको पहली row चाहिए, और फिर उसी row का तीसरा element. Row चुनने के लिए आपको square brackets में index 0 लगाना होगा. zero indexing मत भूलिए.

फिर तीसरा element चुनने के लिए, उसी कॉल में एक और bracket जोड़िए. इस बार index 2 के साथ.

---

## Subsetting

```yaml
type: FullSlide
key: 57a1fb1581
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0, 2]
```{{1}}

```out
1.71
```{{1}}

`@script`
कुछ इस तरह. मूलतः, आप पहले row चुन रहे हैं, और फिर उसी row में से अगला चयन कर रहे हैं.

Subsetting का एक वैकल्पिक तरीका भी है, single square brackets के साथ comma का उपयोग. यह कॉल पहले वाली की तरह ही वही मान लौटाती है. comma से पहले का मान row बताता है, और comma के बाद का मान column. जिन rows और columns का आप चयन करते हैं, उनका intersection लौटता है. जैसे-जैसे अभ्यास होगा, यह सिंटैक्स अधिक सहज लगेगा और और भी संभावनाएँ खोलेगा.

---

## Subsetting

```yaml
type: FullSlide
key: feb75c975c
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[:, 1:3]
```{{1}}

```out
array([[ 1.68,  1.71],
       [59.2 , 63.6 ]])
```{{1}}

```py
np_2d[1, :]
```{{2}}

```out
array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{2}}

`@script`
मान लीजिए आप दूसरे और तीसरे फैमिली मेंबर की height और weight चुनना चाहते हैं. आपको दोनों rows चाहिए, तो comma से पहले colon लगाइए. आपको केवल दूसरा और तीसरा column चाहिए, तो comma के बाद indices 1 से 3 तक दीजिए. याद रखिए, तीसरा index शामिल नहीं होता. उनका intersection हमें 2 rows और 2 columns वाला एक 2D array देता है.

इसी तरह, सभी फैमिली मेंबर्स का weight इस तरह चुन सकते हैं. आपको केवल दूसरी row चाहिए, तो comma से पहले 1 दीजिए. आपको सभी columns चाहिए, तो comma के बाद colon लगाइए. Intersection पूरी दूसरी row देता है.

अंत में, 2D numpy arrays आपको element-wise गणनाएँ करने देते हैं, ठीक वैसे ही जैसे आपने 1D numpy arrays के साथ किया था. यह वही चीज़ है

---

## अभ्यास करते हैं!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
जिस पर आप exercises में प्रयोग कर सकते हैं, 2D numpy arrays बनाने और subsetting के साथ. मज़ेदार रहेगा!
