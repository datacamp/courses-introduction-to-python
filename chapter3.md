---
title_meta: 챕터 3
title: 함수와 패키지
description: >-
  Python 개발자들이 작성한 코드를 효율적으로 활용하기 위해 함수, 메서드, 패키지를 사용하는 방법을 배웁니다. 복잡한 문제를 더 적은
  코드로 해결해보세요!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: 함수(Functions)
  - nb_of_exercises: 4
    title: 메서드
  - nb_of_exercises: 4
    title: 패키지
---

## 함수(Functions)

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## 익숙한 함수

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

기본적으로 Python에는 데이터 과학자의 작업을 더 편리하게 해주는 다양한 함수가 내장되어 있습니다. 두 가지 함수, `print()`와 `type()`은 이미 알고 계실 겁니다. 이 외에도 데이터 타입을 변환하는 `str()`, `int()`, `bool()`, `float()`와 같은 함수도 있습니다. 더 자세한 내용은 [여기](https://docs.python.org/3/library/functions.html) 에서 확인할 수 있습니다. 이 함수들도 전부 내장된 함수입니다.

함수를 호출하는 방법은 간단합니다. 예를 들어 `3.0`의 타입을 확인하고 결과를 새 변수 `result`에 저장하려고 한다면 다음과 같이 작성하면 됩니다:

```
result = type(3.0)
```

`@instructions`
- `print()`와 `type()`을 함께 사용하여 `var1`의 타입을 출력하세요.
- `len()`을 사용하여 `var1` [리스트의 길이 ](https://docs.python.org/3/library/functions.html#len)를 구하세요. `print()`로 감싸서 바로 출력할 수 있습니다..
- `int()`를 사용하여 `var2`를 [정수](https://docs.python.org/3/library/functions.html#int)로 변환하세요. 변환된 결과는 `out2`에 저장하세요.

`@hint`
- `type()` 함수는 다음과 같이 호출하세요. `type(var1)`
- `print()` 함수는 이전에 여러 번 사용했던 방법대로 호출하면 됩니다. 출력하려는 변수를 괄호 안에 넣어보세요.
- `int(x)`를 사용하면 `x`를 정수로 변환할 수 있습니다.

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
msg = "미리 정의된 변수를 변경하거나 제거할 필요가 없습니다."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__: `{{sol_call}}`을(를) 사용하여 `var1`의 %s을(를) 출력했는지 확인하세요."
Ex().has_printout(0, not_printed_msg = patt % '유형')
Ex().has_printout(1, not_printed_msg = patt % '길이')

int_miss_msg = "`int()`을(를) 사용하여 `var2`를 정수로 변환했는지 확인하세요."
int_incorr_msg = "`var2`를 `int()`에 전달했는지 확인하세요."
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="`int()`을(를) 올바르게 호출했습니다; 이제 이 호출의 결과를 `out2`에 할당했는지 확인하세요."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("잘하셨습니다! `len()` 함수는 매우 유용합니다; 문자열에서도 작동하여 문자 수를 셀 수 있습니다!")
```

---

## 도움말 활용하기

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Python 함수 이름은 알고 있지만 사용법이 헷갈릴 때가 있죠. 재미있게도, 그럴 때는 함수의 정보를 확인하기 위해 또 다른 함수인 `help()`를 사용하면 됩니다. IPython에서는 함수 이름 앞에 `?`를 붙여서 확인할 수도 있습니다.

예를 들어, `max()` 함수에 대한 도움말을 보려면 다음 중 하나를 입력하면 됩니다.

```
help(max)
?max
```

IPython Shell에서`?pow` 또는 `help(pow)`를 입력하고 **Enter**를 눌러 `pow()`의 [문서 ](https://docs.python.org/3/library/functions.html#pow)를 열어보세요. 

다음 중 올바른 설명은 무엇인가요?

`@possible_answers`
- `pow()`는 `base`, `exp`, `mod` 세 가지 인자를 받으며, `mod`가 없으면 오류가 발생합니다.
- `pow()`는 `base`, `exp`, `None` 세 가지 필수 인자를 받습니다.
- `pow()`는 `base`와 `exp` 인자를 반드시 필요로 하며, `mod`는 선택 사항입니다.
- `pow()`는 `exp`와 `mod` 두 가지 인수를 받으며, `exp`가 없으면 오류가 발생합니다.

`@hint`
- 선택적 인자는 기본값으로 `=`로 설정되어 있으며, 해당 인자를 지정하지 않으면 함수는 기본값을 사용합니다.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "아닙니다. `mod`는 값을 지정하지 않으면 사용되는 기본값이 있습니다."
msg2 = "틀렸습니다. `None`은 `mod` 인수의 기본값입니다."
msg3 = "완벽합니다! `help()`를 사용하면 함수가 어떻게 작동하는지 이해할 수 있어, 그들의 잠재력을 최대한 발휘할 수 있습니다!"
msg4 = "틀렸습니다. `pow()`는 세 개의 인수를 받으며, 그 중 하나는 기본값을 가집니다."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## 여러 개의 인자

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

이전 연습 문제에서는 `help()`를 사용해 문서를 확인하여 선택적 인자를 알아봤습니다. 이번에는 이를 적용하여 `sorted()` 함수의 동작을 직접 바꿔 보겠습니다.

IPython Shell에 `help(sorted)`를 입력해 `sorted()`의 [문서 ](https://docs.python.org/3/library/functions.html#sorted)를 살펴보세요.

`sorted()`는 `iterable`, `key`, `reverse` 세 가지 인수를 받습니다. 이번 연습 문제에서는 `key`는 사용하지 않고 `iterable`과 `reverse`만 지정하세요.

두 개의 리스트가 이미 만들어져 있습니다.

두 리스트를 합친 후 내림차순으로 정렬해 볼까요?

`@instructions`
- `+`를 사용해 `first`와 `second`의 내용을 합쳐 새로운 리스트 `full`을 만드세요.
- `full`에서 `sorted()`를 호출하고, `reverse` 인자를 `True`로 지정하세요. 정렬된 리스트를 `full_sorted`로 저장하세요.
- 마지막으로 `full_sorted`를 출력하세요.

`@hint`
- `first`와 `second`를 숫자처럼 더한 뒤, 그 결과를 `full`에 할당하세요.
- `sorted()`를 사용할 때 두 개의 입력값 `full`과 `reverse=True`를 지정하세요.
- 변수를 출력하려면 `print()`를 사용하세요.

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
msg = "이미 있는 변수 `first`와 `second`를 변경하거나 제거할 필요가 없습니다."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="`sorted()`를 호출한 결과를 `full_sorted`에 할당했는지 확인하세요."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("좋습니다! Python 메서드에 대한 비디오로 이동하세요.")
```

---

## 메서드

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## 문자열 메서드

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

문자열에는 다양한 메서드가 연결되어 있습니다. 아래 지침을 잘 따라 그 중 몇 가지를 직접 사용해 보세요. 더 자세한 내용을 확인하려면 IPython Shell에서 `help(str)`을 입력해보세요.

실습에 사용할 문자열 변수 `place`는 이미 생성되어 있습니다.

`@instructions`
- `place`에 `.upper()` [ 메서드](https://docs.python.org/3/library/stdtypes.html#str.upper)를 사용하고, 그 결과를 `place_up`에 저장하세요. 이전 영상에서 배운 메서드 호출 문법을 사용하면 됩니다.
- `place`와 `place_up`을 출력해보세요. 두 변수 모두 바뀌었나요?
- `place`에서 `.count()`를 호출하고 `'o'`를 인수로 전달해서, 변수 `place`에 'o'가 몇 개 있는지 출력하세요. `"place"`라는 단어가 아니라 변수 `place`라는 점을 유의하세요.

`@hint`
- `place`에 `.upper()` 메서드를 추가 입력 없이 호출할 수 있습니다.
- 변수 `x`를 출력하려면 `print(x)`를 사용하세요.
- `place.count(____)` 호출을 `print()` 함수로 감싸서 결과를 출력해야합니다.

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
msg = "미리 정의된 변수를 변경하거나 제거할 필요가 없습니다."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "`%s`을(를) 출력하는 것을 잊지 마세요."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="`place.upper()` 호출의 결과를 `place_up`에 할당하세요."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "`place`에서 'o'의 개수를 잘 계산하셨습니다; 이제 `place.count('o')` 호출을 `print()` 함수로 감싸서 결과를 출력하세요."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("좋습니다! 출력물에서 `upper()` 메서드가 호출된 객체를 변경하지 않는다는 것을 확인하세요. 다음 연습에서는 리스트에 대해 다르게 작동할 것입니다!")
```

---

## 리스트 메서드

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Python 타입 중 문자열에만 메서드가 연결된 것은 아닙니다. 리스트, 실수, 정수, 불리언도 유용한 메서드를 갖추고 있습니다. 이번 연습 문제에서는 다음 두 가지 메서드를 사용해 보겠습니다.

- `.index()`: 입력값과 일치하는 첫 번째 요소의 인덱스를 반환합니다.
- `.count()`: 특정 요소가 리스트에 나타나는 횟수를 반환합니다.

집의 각 구역이 담긴 리스트 `areas`를 활용해 실습해보세요.

`@instructions`
- `.index()` 메서드를 사용해 `areas`에서 값이 `20.0`인 요소의 인덱스를 구하고 출력하세요.
- `areas`에서 `.count()`를 호출해 `9.50`이 리스트에 몇 번 등장하는지 확인하고, 그 숫자를 출력하세요.

`@hint`
- 인덱스를 출력하려면 `areas.index(___)` 호출을 `print()` 함수로 감싸세요.
- 요소 `x`가 리스트에 나타나는 횟수를 출력하려면 `areas.count(___)` 호출을 `print()` 함수로 감싸세요.

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
predef_msg = "미리 정의된 목록 `areas`를 변경하거나 제거할 필요가 없습니다."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()

Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("좋습니다! 이것들은 호출된 목록을 변경하지 않는 `list` 메서드의 예시입니다.")
```

---

## 리스트 메서드(2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

대부분의 리스트 메서드는 호출된 리스트를 직접 변경합니다. 예를 들면 다음과 같습니다.

- `.append()`: 호출된 리스트에 요소를 추가합니다.
- `.remove()`: 입력값과 일치하는 리스트의 첫 번째 요소를 [제거](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)합니다.
- `.reverse()`: 호출된 리스트의 요소 순서를 [반전](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)합니다.

이번 연습 문제에서는 집의 각 공간 면적이 담긴 리스트 `areas`를 사용합니다.

`@instructions`
- `.append()`를 두 번 사용하여 수영장 옆 별채와 차고의 면적인 `24.5`와 `15.45`를 순서대로 추가하세요.
- `areas`를 출력하세요.
- `.reverse()` 메서드를 사용하여 `areas`의 요소 순서를 반전시키세요.
- `areas`를 다시 한 번 출력하세요.

`@hint`
- 첫 번째 지침에서는 `areas.append(___)` 호출을 두 번 사용하세요.
- 변수 `x`를 출력하려면 `print(x)`를 작성하면 됩니다.
- `.reverse()` 메서드는 추가 입력이 필요 없습니다. 점 표기법과 빈 괄호(`.reverse()`)를 사용하세요.
- 변수 `x`를 출력하려면 `print(x)`를 작성하면 됩니다.

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

success_msg("훌륭합니다!")
```

---

## 패키지

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## 패키지 가져오기

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

원의 둘레와 넓이을 계산하고 싶다고 가정해보겠습니다. 공식은 다음과 같습니다:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

`pi` 값을 직접 입력하는 대신, 숫자가 포함된 `math` 패키지를 활용할 수 있습니다.

참고로, `**`는 거듭제곱 기호입니다. 예를 들어 `3**4`는 `3`의 `4`제곱으로, 결과값은 `81`입니다.

`@instructions`
- `math` 패키지를 가져오세요.
- `math.pi`를 사용하여 원의 둘레를 계산하고, 결과를 `C`에 저장하세요.
- `math.pi`를 사용하여 원의 넓이를 계산하고, 결과를 `A`에 저장하세요.

`@hint`
- `import math`를 사용한 후, `math.pi`로 `pi`를 사용하세요.
- 과제 설명에서 제공한 공식을 사용하여 `C`를 구하세요. `*`를 사용하세요.
- 과제 설명에서 제공한 공식을 사용하여 `A`를 구하세요. `*`과 `**` 연산자를 사용하세요.

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
patt = "당신의 `%s` 계산이 정확하지 않습니다. `math.pi`를 사용했는지 확인하세요."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:둘레를 출력하기 위해 `{{sol_call}}`을(를) 그대로 두세요."),
  has_printout(1, not_printed_msg = "__JINJA__:면적을 출력하기 위해 `{{sol_call}}`을(를) 그대로 두세요.")
)

success_msg("좋습니다! 패키지의 함수를 다루는 방법을 알고 있다면, 많은 파이썬 프로그래머의 힘이 당신의 손끝에 있습니다!")
```

---

## 선택적 가져오기

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

`import math`와 같은 일반적인 가져오기는 `math` 패키지의 **모든** 기능을 사용할 수 있게 해줍니다. 하지만 패키지의 특정 기능만 사용하고 싶다면, 다음과 같이 더 선택적으로 가져올 수 있습니다.

```
from math import pi
```

이번에는 같은 방식으로, `pi`만 가져와서 사용해 보세요.

`@instructions`
- `math` 패키지에서 `pi` 함수만 선택적으로 가져오세요.
- `pi`를 사용해 원의 둘레를 계산하고 `C`에 저장하세요.
- `pi`를 사용해 원의 면적을 계산하고 `A`에 저장하세요.

`@hint`
- `from math import pi`를 사용해 선택적 가져오기를 수행하세요.
- 이제 `pi`를 단독으로 사용할 수 있습니다!

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
patt = "계산한 `%s` 값이 정확하지 않습니다. `pi`만 사용했는지 확인하세요."

Ex().has_import("math.pi", not_imported_msg = "`math` 패키지에서 `pi`를 가져오는 것을 잊지 마세요. `from ___ import ___` 표기법을 사용해야 합니다.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}`을(를) 그대로 두어 둘레를 출력하도록 하세요."),
  has_printout(1, not_printed_msg = "__JINJA__:`{{sol_call}}`을(를) 그대로 두어 면적을 출력하도록 하세요.")
)

success_msg("좋습니다! 다음 연습 문제로 넘어가세요.")
```

---

## 다양한 임포트 방법

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Python에 패키지와 모듈을 가져오는 방법은 여러 가지가 있습니다. 어떤 import 문을 사용하느냐에 따라 Python 코드 작성 방식도 달라집니다.

`scipy` 패키지의 `linalg` 서브패키지에 있는 `inv()` [ 함수 ] (https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) 사용하려 한다고 가정해보겠습니다. 아래와 같이 이 함수를 호출하려고 합니다.

```
my_inv([[1,2], [3,4]])
```

오류 없이 위 코드를 실행하려면 어떤 `import` 문이 필요할까요?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- IPython 셸에서 각 import 문을 직접 입력해 보고 어떤 경우에 `my_inv([[1, 2], [3, 4]])`가 오류 없이 실행되는지 확인해 보세요. 코드를 입력한 후 **enter** 키를 눌러 실행하세요.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "틀렸습니다. 다시 시도해 보세요. IPython 셸에서 다른 import 문을 시도해 보고, 어떤 것이 `my_inv([[1, 2], [3, 4]])` 줄이 오류 없이 실행되게 하는지 확인하세요."
msg4 = "정답입니다! `as` 단어를 사용하면 가져오는 함수에 대한 로컬 이름을 만들 수 있습니다: `inv()`는 이제 `my_inv()`로 사용할 수 있습니다."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```
