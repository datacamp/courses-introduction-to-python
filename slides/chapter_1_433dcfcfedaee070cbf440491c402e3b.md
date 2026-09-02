---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ko-KR/bded7e0b-81c4-4f66-a382-a754bb8771dc-9ea6593b98566181746062ba7448e284.mp3
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
잘하셨어요. 다시 만났군요! 확실히 Python은 훌륭한 계산기입니다. 하지만 더 복잡한 계산을 할 때는 코딩을 하면서 값을 '저장'하고 싶어질 겁니다.

---

## 변수

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- 구체적이고 대소문자를 구분하는 이름

- 변수 이름을 통해 값을 호출{{1}}

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
대소문자를 구분해서 특정 이름을 지정하면 저장이 가능합니다. 이러한 변수를 정의하거나 선언하면, 나중에 변수 이름을 입력해 값을 불러올 수 있습니다.

본인의 키와 몸무게를 미터법으로 측정한다고 가정해 봅시다. 키가 179센티미터이고 몸무게가 68.7킬로그램이라고 해보죠. 이 값을 height와 weight라는 두 변수에 등호를 사용하여 할당할 수 있습니다.

이제 변수 이름인 height를 입력하면, Python이 변수 이름을 찾아 해당 값을 가져와서 출력합니다.

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

$$ {{1}}extBMI = racextweightextheight^2 $$

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
이제 체질량지수인 BMI를 계산해 봅시다. BMI는 킬로그램으로 표시한 체중과 미터로 표시한 키를 이용해 화면의 식처럼 계산합니다. 실제 값을 사용해도 되지만, 보시는 것처럼 height와 weight 변수를 사용할 수도 있죠. 변수의 이름을 입력할 때마다 Python에 해당 변수를 실제 값으로 바꾸라고 요청하는 겁니다. 이 경우, weight는 68.7이고, height는 1.79입니다.

마지막으로, 이 버전에서는 Python이 결과를 새로운 변수인 bmi로 저장합니다. 이제 bmi에 방금 계산한 값이 들어갑니다.

Python에서는 항상 다양한 변수를 사용합니다. 변수를 통해 코드의 재현성을 높일 수 있습니다.

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
예를 들어, 이렇게 height, weight, bmi 변수를 생성하는 코드가 스크립트에 있다고 가정해 봅시다. 다른 체중을 사용해 bmi를 다시 계산하고 싶다면,

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
weight 변수의 선언만 변경하고 스크립트를 다시 실행하면 됩니다. 그러면 이에 맞춰 bmi도 변경됩니다. 변수 weight의 값이 변경되었기 때문이죠.

지금까지는 키나 몸무게처럼 숫자로 된 값만 다뤘는데요.

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
Python에서는 각 숫자에 특정한 타입이 있습니다. 각 값의 타입은 type 함수를 이용해 확인할 수 있습니다. bmi 값의 타입을 확인하려면, type을 입력하고 괄호 안에 bmi라고 입력하면 됩니다. 그럼 이 값이 float 값임을 알 수 있습니다. 이건 Python에서 실수를 나타내는 방식으로, 정수 부분과 소수 부분을 모두 가질 수 있습니다. Python에는 예시와 같이 int라는 정수 타입도 있습니다.

데이터 과학은 정수와 실수만으로는 충분하지 않죠.

---

## Python 타입(2)

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
Python에는 이외에도 수많은 타입이 있습니다. 가장 일반적인 것은 문자열과 불리언입니다.

문자열은 Python에서 텍스트를 나타내는 방법인데요. 예시에서 보이는 것처럼 문자열을 만들 때 큰따옴표와 작은따옴표를 모두 사용할 수 있습니다. 마지막 변수의 타입을 출력해 보면, str임을 알 수 있습니다. str은 문자열의 영문 약어입니다.

불리언은 True나 False 중 하나의 값만 가지는 타입입니다. 일상적인 대답인 '네', '아니오'와 비슷한 개념입니다. 불리언은 앞으로 데이터에서 필터링 작업을 수행할 때와 같은 경우에 매우 유용하게 사용될 것입니다.

Python 데이터 타입에는 특별한 점이 있습니다.

---

## Python 타입(3)

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

- 다른 타입 = 다른 동작!{{3}}

`@script`
두 정수를 더할 때 사용하는 코드와 두 문자열을 더할 때 사용하는 코드를 살펴보면,

정수는 값이 더해졌고, 문자열은 서로 이어 붙여졌습니다. 덧셈 연산자가 데이터 타입에 따라 다르게 동작한 거죠. 이건 일반적인 원칙인데요. 코드의 동작 방식이 다루는 타입에 따라 달라지게 됩니다.

다음 연습 문제에서는 첫 변수를 만들어보고, Python의 데이터 타입 몇 가지를 가지고 실험해볼 것입니다. 다음 영상에서 리스트에 대해 자세히 설명해 드리겠습니다.

---

## 연습해봅시다!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
이제 코딩을 시작해볼까요? 다음 챕터에서 여러분이 더욱 멋진 Python 차트를 만드는 모습을 기대하고 있겠습니다.
