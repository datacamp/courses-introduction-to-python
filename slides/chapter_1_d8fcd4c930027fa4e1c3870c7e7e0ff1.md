---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/hi-IN/bac31954-fb2a-4df1-bc85-d29d141d83d9-31106f5eb8d80632dd1e1bacdf92ee0a.mp3
---

## नमस्ते Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
नमस्ते, मेरा नाम ह्यूगो है और मैं Data Science के लिए Python की भूमिका कोर्स में आपका होस्ट रहूँगा।

मैं DataCamp में डेटा साइंटिस्ट और एजुकेटर हूँ।

---

## आप कैसे सीखेंगे

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp इंटरफ़ेस](https://assets.datacamp.com/img/translations/hi-IN/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
इस कोर्स में, आप इस तरह के वीडियो लेसन और इंटरैक्टिव एक्सरसाइज़ के ज़रिए Data Science के लिए Python सीखेंगे। आपको अपना खुद का Python सेशन मिलता है जहाँ आप प्रयोग कर सकते हैं और निर्देशों को हल करने के लिए सही कोड लिखने की कोशिश कर सकते हैं। आप करके सीखेंगे, और अपने काम पर कस्टमाइज़्ड व तुरंत फीडबैक पाएँगे।

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/hi-IN/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- जनरल पर्पज़: कुछ भी बनाइए{{2}}

- ओपन सोर्स! फ्री!{{3}}

- डेटा साइंस सहित Python पैकेज{{4}}

	- कई एप्लिकेशन और क्षेत्र{{5}}

`@script`
Python की कल्पना गुइडो वैन रोसम ने की थी। यहाँ आप मेरी और गुइडो की एक फ़ोटो देख सकते हैं। जो एक शौकिया प्रोजेक्ट के रूप में शुरू हुआ था, वह जल्दी ही एक जनरल-पर्पज़ प्रोग्रामिंग लैंग्वेज बन गया। आज आप Python से लगभग किसी भी तरह का सॉफ़्टवेयर बना सकते हैं। लेकिन ऐसा कैसे हुआ? सबसे पहले, Python ओपन सोर्स है। इसे उपयोग करना मुफ़्त है। दूसरा, Python में पैकेज बनाना बहुत आसान है। यानी ऐसा कोड जिसे आप दूसरों के साथ साझा कर सकते हैं ताकि खास समस्याएँ सुलझाई जा सकें। समय के साथ, डेटा साइंस के लिए बनाए गए ऐसे और भी बहुत से पैकेज विकसित हुए हैं। मान लीजिए आप अपनी कंपनी की सेल्स की बढ़िया विज़ुअलाइज़ेशन बनाना चाहते हैं। उसके लिए पैकेज मौजूद है। या फिर किसी डेटाबेस से जुड़कर सेंसर माप का विश्लेषण करना है। उसके लिए भी पैकेज है।
लोग अक्सर Python को प्रोग्रामिंग लैंग्वेज का स्विस आर्मी नाइफ़ कहते हैं, क्योंकि इससे आप लगभग सब कुछ कर सकते हैं।
इस कोर्स में हम धीरे-धीरे आपके डेटा साइंस कोडिंग स्किल्स बनाएँगे, तो जुड़े रहिएगा और देखिए यह लैंग्वेज कितनी शक्तिशाली हो सकती है।

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Python कमांड चलाएँ**

![ipython_shell.png](https://assets.datacamp.com/img/translations/hi-IN/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
अब जबकि आप Python पर पूरा ध्यान दे रहे हैं, तो चलिए प्रयोग शुरू करते हैं। मैं शुरुआत करता हूँ

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Python कमांड चलाएँ**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/hi-IN/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python shell से। यह वह जगह है जहाँ आप Python कोड टाइप कर सकते हैं और तुरंत नतीजे देख सकते हैं। DataCamp के एक्सरसाइज़ इंटरफ़ेस में यह शेल यहीं एंबेडेड है। चलिए सबसे आसान से शुरू करते हैं और Python को कैलकुलेटर की तरह इस्तेमाल करते हैं।

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![DataCamp के IPython shell में कैलकुलेशन](https://assets.datacamp.com/img/translations/hi-IN/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
मैं 4 + 5 टाइप करता हूँ और Enter दबाता हूँ। Python आपके इनपुट को समझकर आपके कैलकुलेशन का परिणाम प्रिंट कर देता है, 9। यहाँ जो Python shell इस्तेमाल हो रहा है, वह असली वाला नहीं है। हम IPython का इस्तेमाल कर रहे हैं, यानी Interactive Python। यह रेगुलर Python का एक पावरफुल वर्ज़न है जो आगे काम आएगा।

IPython को फ़र्नान्डो पेरेज़ ने बनाया था और यह बड़े Jupyter इकोसिस्टम का हिस्सा है। इंटरएक्टिवली Python चलाने के अलावा, आप Python से所谓

---

## Python स्क्रिप्ट

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- टेक्स्ट फाइलें - `.py`{{1}}

- Python कमांड्स की सूची{{2}}

- IPython Shell जैसा ही टाइपिंग अनुभव{{3}}

![DataCamp में Python स्क्रिप्ट](https://assets.datacamp.com/img/translations/hi-IN/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
python scripts भी चला सकते हैं। ये python scripts साधारण टेक्स्ट फाइलें होती हैं जिनका एक्सटेंशन .py होता है। असल में यह Python कमांड्स की एक लिस्ट होती है जो ऐसे चलती हैं जैसे आप शेल में लाइन-बाय-लाइन खुद टाइप कर रहे हों।

---

## Python स्क्रिप्ट

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: स्क्रिप्ट में 4 + 5 टाइप करके "उत्तर सबमिट करें" दबाया गया। कोई आउटपुट नहीं दिखता।](https://assets.datacamp.com/img/translations/hi-IN/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
चलिए अब पिछले वाले कमांड को एक स्क्रिप्ट में डालते हैं, जो DataCamp के इंटरफ़ेस में यहाँ मौजूद है। अगला कदम है स्क्रिप्ट को चलाना, "Submit Answer" पर क्लिक करके। अगर आप यह स्क्रिप्ट DataCamp इंटरफ़ेस में चलाते हैं, तो आउटपुट पेन में कुछ नहीं दिखेगा। ऐसा इसलिए क्योंकि स्क्रिप्ट के अंदर आउटपुट दिखाने के लिए आपको स्पष्ट रूप से print का उपयोग करना पड़ता है।

---

## Python स्क्रिप्ट

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/hi-IN/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- स्क्रिप्ट से आउटपुट दिखाने के लिए `print()` इस्तेमाल करें

`@script`
चलिए अपनी पिछली गणना को print कॉल में लपेटते हैं और स्क्रिप्ट फिर चलाते हैं। इस बार, पहले जैसा ही आउटपुट मिल गया, बढ़िया। अपने कोड को Python स्क्रिप्ट्स में रखना, हर स्टेप को इंटरएक्टिवली बार-बार टाइप करने की बजाय, आपको स्ट्रक्चर बनाए रखने में मदद करेगा। और जब भी बदलाव करना हो, बस स्क्रिप्ट में बदलाव कीजिए और पूरी स्क्रिप्ट दोबारा चला दीजिए।

---

## DataCamp इंटरफ़ेस

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCamp इंटरफ़ेस का स्क्रीनशॉट](https://assets.datacamp.com/img/translations/hi-IN/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
अब जब आपको Python के साथ काम करने के अलग-अलग तरीकों का अंदाज़ा हो गया है, तो मेरी सलाह है कि आप एक्सरसाइज़ पर जाएँ। प्रयोग के लिए IPython Shell का इस्तेमाल कीजिए, और असली उत्तर का कोड लिखने के लिए Python script editor का। जैसे ही आप Submit Answer पर क्लिक करेंगे, आपकी स्क्रिप्ट चलेगी और उसकी शुद्धता जाँची जाएगी।

---

## अभ्यास करते हैं!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
कोड लिखना शुरू कीजिए और मज़ा लेना मत भूलिए।
