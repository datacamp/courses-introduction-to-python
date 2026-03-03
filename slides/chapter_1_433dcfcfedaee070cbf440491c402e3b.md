---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ko-KR/7d66a7f0-f1e3-4950-af42-df98d4cebf7b.mp3
---

## 변수와 타입

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
잘하셨습니다, 다시 오신 걸 환영해요! 파이썬이 훌륭한 계산기라는 게 분명하죠. 하지만 더 복잡한 계산을 하려면, 코드를 작성하는 동안 값을 "저장"하는 것이 필요합니다.

---

## 변수

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- 구체적이며 대소문자 구분

- 변수 이름으로 값 호출{{1}}

- 1.79 m - 68.7 kg{{2}}

```py
height = 1.79
weight = 68.7
```{{3}}
```py
height
```{{4}}

```out
1.79
```{{4}}

`@script`
이는 대소문자를 구분하는 특정 이름으로 변수를 정의하면 됩니다. 이렇게 변수를 만들고(선언하고) 나면, 나중에 변수 이름을 입력해서 그 값을 불러올 수 있어요.

예를 들어, 키와 몸무게를 미터법으로 쟀다고 해볼게요. 키는 1.79미터, 몸무게는 68.7킬로그램입니다. 이 값을 height와 weight라는 두 변수에 등호를 사용해 할당할 수 있어요:

이제 변수 이름인 height를 입력하면,

파이썬은 해당 변수 이름을 찾아 그 값을 가져와 출력합니다.

---

## BMI 계산하기

```yaml
type: TwoColumns
key: fe1b10a93b
code_zoom: 80
```

`@part1`
```py
height = 1.79
weight = 68.7
```
```py
height
```

```out
1.79
```

$$ \text{BMI} = \frac{\text{weight}}{\text{height}^2} $${{1}}

`@part2`
```py
68.7 / 1.79 ** 2
```{{2}}

```out
21.4413
```{{2}}

```py
weight / height ** 2
```{{3}}

```out
21.4413
```{{3}}

```py
bmi = weight / height ** 2
bmi
```{{4}}

```out
21.4413
```{{4}}

`@script`
이제 체질량지수, 즉 BMI를 계산해 볼게요. BMI는 이렇게 계산합니다. 몸무게는 킬로그램, 키는 미터 단위예요. 실제 값을 넣어 계산할 수도 있지만, 이렇게 height와 weight 변수를 그대로 사용할 수도 있어요. 변수 이름을 입력할 때마다, 파이썬은 그 자리를 변수의 실제 값으로 바꿔서 계산합니다. weight는 68.7, height는 1.79에 해당하죠.

마지막으로, 이 버전에서는 결과를 새로운 변수 bmi에 저장하도록 했습니다. 이제 bmi에는 앞에서 계산한 것과 같은 값이 들어 있어요.

파이썬에서는 변수를 아주 자주 사용합니다. 덕분에 코드의 재현성이 좋아져요.

---

## 재현성

```yaml
type: FullSlide
key: 9980f47f9d
```

`@part1`
```py
height = 1.79
weight = 68.7
bmi = weight / height ** 2
print(bmi)
```

```out
21.4413
```

`@script`
height, weight, bmi 변수를 만드는 코드가 이렇게 스크립트에 들어 있다고 가정해 볼게요. 이제 다른 몸무게로 bmi를 다시 계산하고 싶다면,

---

## 재현성

```yaml
type: FullSlide
key: a4e899f00f
disable_transition: true
```

`@part1`
```py
height = 1.79
weight = 74.2 # <-
bmi = weight / height ** 2
print(bmi)
```

```out
23.1578
```

`@script`
weight 변수의 선언만 간단히 바꾼 뒤 스크립트를 다시 실행하면 됩니다. 변수 weight의 값이 바뀌었기 때문에, bmi도 그에 맞춰 변경됩니다.

지금까지는 키와 몸무게처럼 숫자 값만 다뤘죠.

---

## Python 타입

```yaml
type: FullSlide
key: 9d86084ad4
```

`@part1`
```py
type(bmi)
```{{1}}

```out
float
```{{1}}

```py
day_of_week = 5
type(day_of_week)
```{{2}}

```out
int
```{{2}}

`@script`
파이썬에서는 이런 숫자들이 각각 특정한 타입을 가집니다. type 함수로 값의 타입을 확인할 수 있어요. bmi의 타입을 보려면, type에 bmi를 괄호 안에 넣어 호출하면 됩니다. 결과는 float인데, 이는 실수를 나타내는 파이썬의 타입이에요. 정수 부분과 소수 부분을 모두 가질 수 있는 숫자죠. 파이썬에는 정수를 위한 타입 int도 있습니다. 이 예시처럼요.

하지만 데이터 사이언스를 하려면 int와 float만으로는 충분하지 않습니다.

---

## Python 타입 (2)

```yaml
type: FullSlide
key: d971d34e6a
```

`@part1`
```py
x = "body mass index"
y = 'this works too'
```{{1}}
```py
type(y)
```{{2}}

```out
str
```{{2}}

```py
z = True
type(z)
```{{3}}

```out
bool
```{{3}}

`@script`
파이썬에는 다른 데이터 타입도 정말 많습니다. 그중 가장 흔한 것이 문자열과 불리언이에요.

문자열은 텍스트를 표현하는 방식입니다. 큰따옴표와 작은따옴표를 모두 사용할 수 있다는 점을 이 예시에서 볼 수 있어요. 마지막 변수의 타입을 출력해 보면 str, 즉 문자열의 약자임을 볼 수 있습니다.

불리언은 True 또는 False 두 값만 가질 수 있는 타입입니다. 일상 언어의 '예'와 '아니오'로 생각하시면 돼요. 불리언은 나중에 데이터를 필터링하는 작업 등에서 매우 유용하게 쓰입니다.

파이썬의 데이터 타입에는 특별한 점이 하나 있어요.

---

## Python 타입 (3)

```yaml
type: FullSlide
key: 24601e2af0
```

`@part1`
```py
2 + 3
```{{1}}

```out
5
```{{1}}

```py
'ab' + 'cd'
```{{2}}

```out
'abcd'
```{{2}}

- 타입이 다르면 동작도 다릅니다!{{3}}

`@script`
정수 두 개를 더하는 이 코드와, 문자열 두 개를 더하는 이 코드를 살펴보세요.

정수의 경우에는 값이 합산되지만, 문자열의 경우에는 서로 붙여집니다. 플러스 연산자가 데이터 타입에 따라 다르게 동작한 거죠. 이것이 일반적인 원칙입니다. 코드가 어떻게 동작하는지는 사용 중인 타입에 따라 달라집니다.

이어지는 실습에서 첫 변수를 만들어 보고, 파이썬의 여러 데이터 타입을 직접 실험해 보세요. 다음 영상에서는 리스트에 대해 자세히 설명하겠습니다.

---

## Passons à la pratique !

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
이제 코딩을 시작해 볼까요? 다음 챕터에서는 더 멋진 파이썬 차트를 만들어 볼 거예요. 곧 다시 만나겠습니다.
