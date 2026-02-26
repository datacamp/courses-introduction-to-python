---
title_meta: Chapter 3
title: 함수와 패키지
description: >-
  뛰어난 Python 개발자들이 작성한 코드를 효율적으로 활용할 수 있도록 함수, 메서드, 패키지 사용법을 배웁니다. 목표는 어려운 문제를
  해결하는 데 필요한 코드의 양을 줄이는 것입니다!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: 함수
  - nb_of_exercises: 4
    title: 메서드
  - nb_of_exercises: 4
    title: 패키지
---

## 함수

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## 익숙한 함수들

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python에는 데이터 사이언티스트의 작업을 더 쉽게 해 주는 다양한 내장 함수가 기본으로 제공돼요. 이미 `print()`와 `type()` 두 가지 함수는 알고 계시죠. 이 밖에도 데이터 형식을 바꿀 때 쓰는 `str()`, `int()`, `bool()`, `float()` 같은 함수들이 있어요. 자세한 내용은 [여기](https://docs.python.org/3/library/functions.html)에서 확인할 수 있어요. 이들도 모두 내장 함수입니다.

함수를 호출하는 방법은 간단해요. `3.0`의 타입을 구해 결과를 새 변수 `result`에 저장하려면 다음과 같이 하면 됩니다:

```
result = type(3.0)
```

`@instructions`
- `print()`과 `type()`을 함께 사용해 `var1`의 타입을 출력하세요.
- `len()`을 사용해 리스트 `var1`의 [길이](https://docs.python.org/3/library/functions.html#len)를 구하세요. `print()`로 감싸 바로 출력하세요.
- `int()`를 사용해 `var2`를 [정수](https://docs.python.org/3/library/functions.html#int)로 변환하고, 결과를 `out2`에 저장하세요.

`@hint`
- `type()` 함수는 이렇게 호출해 보세요: `type(var1)`.
- `print()`는 이전에 여러 번 하신 것처럼 호출하면 돼요. 출력할 변수를 괄호 안에 넣으세요.
- `int(x)`는 `x`를 정수로 변환합니다.

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

## 도와줘요!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

어떤 Python 함수의 이름은 알고 있지만, 어떻게 써야 할지 알아봐야 할 때가 있어요. 아이러니하게도, 함수에 대한 정보를 얻으려면 또 다른 함수인 `help()`를 사용해야 해요. 특히 IPython에서는 함수 이름 앞에 `?`를 붙이는 방법도 쓸 수 있어요.

예를 들어 `max()` 함수에 대한 도움말을 보려면 다음 호출 중 하나를 사용할 수 있어요:

```
help(max)
?max
```

IPython 셸에서 `pow()`의 [문서](https://docs.python.org/3/library/functions.html#pow)를 열어 보세요. `?pow` 또는 `help(pow)`를 입력하고 **Enter**를 누르면 됩니다.

다음 중 올바른 설명은 무엇인가요?

`@possible_answers`
- `pow()`는 `base`, `exp`, `mod`의 세 인자를 받습니다. `mod`를 생략하면 함수는 오류를 반환합니다.
- `pow()`는 `base`, `exp`, `None`의 세 필수 인자를 받습니다.
- `pow()`는 `base`와 `exp` 인자가 필요하며 `mod`는 선택 사항입니다.
- `pow()`는 `exp`와 `mod`의 두 인자를 받습니다. `exp`가 없으면 오류가 발생합니다.

`@hint`
- 선택적 인자는 `=` 로 기본값을 설정해 두며, 해당 인자가 지정되지 않으면 함수가 그 기본값을 사용해요.

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

## 여러 개의 인수

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

이전 연습 문제에서는 `help()`로 문서를 확인해 선택적 인수를 알아봤어요. 이제 이를 활용해 `sorted()` 함수의 동작을 바꿔 보겠습니다.

IPython 셸에서 `help(sorted)`를 입력해 `sorted()`의 [문서](https://docs.python.org/3/library/functions.html#sorted)를 확인해 보세요.

`sorted()`는 `iterable`, `key`, `reverse` 세 가지 인수를 받습니다. 이번 연습에서는 `key`는 지정하지 않고, `iterable`과 `reverse`만 지정하면 됩니다.

두 개의 리스트가 미리 준비되어 있습니다.

이 둘을 이어 붙인 뒤 내림차순으로 정렬해 볼까요?

`@instructions`
- `+`를 사용해 `first`와 `second`의 내용을 새 리스트 `full`로 합치세요.
- `full`에 대해 `sorted()`를 호출하고 `reverse` 인수를 `True`로 지정하세요. 정렬된 리스트를 `full_sorted`로 저장하세요.
- 마지막으로 `full_sorted`를 출력하세요.

`@hint`
- `first`와 `second`를 두 숫자를 더하듯이 합해서 결과를 `full`에 할당하세요.
- `sorted()`를 사용할 때 입력을 두 개 넘기세요: `full`과 `reverse=True`.
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

문자열에는 다양한 메서드가 있어요. 아래 지침을 따라가며 몇 가지를 직접 살펴보세요. 더 자세히 확인하고 싶다면 IPython 셸에서 언제든지 `help(str)`를 입력해 보세요.

실험해 볼 수 있도록 문자열 `place`가 이미 만들어져 있어요.

`@instructions`
- `place`에 `.upper()` [메서드](https://docs.python.org/3/library/stdtypes.html#str.upper)를 사용해 결과를 `place_up`에 저장하세요. 이전 영상에서 배운 메서드 호출 문법을 사용하세요.
- `place`와 `place_up`을 출력해 보세요. 둘 다 바뀌었나요?
- 변수 `place`에서 문자 `'o'`의 개수를 세기 위해 `.count()`를 `place`에 호출하고, 메서드의 입력으로 문자 `'o'`를 전달한 뒤 그 결과를 출력하세요. 여기서 말하는 것은 단어 "place"가 아니라 변수 `place`예요!

`@hint`
- `place`에 추가 입력 없이 `.upper()` 메서드를 호출할 수 있어요.
- 변수 `x`를 출력하려면 `print(x)`라고 쓰면 돼요.
- `place.count(____)` 호출 결과를 출력하려면 `print()`로 감싸는 것을 잊지 마세요.

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

메서드가 있는 Python 타입은 문자열만이 아닙니다. 리스트, 부동소수점(float), 정수(integer), 불리언(boolean)도 유용한 메서드를 여럿 제공합니다. 이 연습 문제에서는 다음을 실험해 볼 거예요:

- `.index()`: 입력값과 일치하는 리스트의 첫 번째 원소의 인덱스를 가져오고,
- `.count()`: 특정 원소가 리스트에 몇 번 나타나는지 확인합니다.

여러분은 집의 각 공간 면적을 담은 리스트 `areas`로 작업하게 됩니다.

`@instructions`
- `.index()` 메서드를 사용해 `areas`에서 `20.0`과 같은 원소의 인덱스를 가져오세요. 이 인덱스를 출력하세요.
- `areas`에 대해 `.count()`를 호출해 리스트에 `9.50`이 몇 번 나타나는지 확인하세요. 이 숫자도 출력하세요.

`@hint`
- 인덱스를 출력하려면 `areas.index(___)` 호출을 `print()` 함수로 감싸세요.
- 리스트에서 원소 `x`가 몇 번 나타나는지 출력하려면 `areas.count(___)` 호출을 `print()` 함수로 감싸세요.

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

## 리스트 메서드 (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

대부분의 리스트 메서드는 호출된 리스트 자체를 변경합니다. 예를 들면 다음과 같아요:

- `.append()`: 호출된 리스트에 원소를 하나 추가합니다.
- `.remove()`: 입력과 일치하는 리스트의 첫 번째 원소를 [삭제](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)합니다.
- `.reverse()`: 호출된 리스트의 원소 순서를 [역순으로](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) 바꿉니다.

여러분은 집의 각 공간 면적을 담은 리스트 `areas`를 가지고 작업할 거예요.

`@instructions`
- `.append()`를 두 번 사용해 풀하우스와 차고의 면적인 `24.5`와 `15.45`를 다시 추가하세요. 이 순서를 지켜서 추가하세요.
- `areas`를 출력하세요.
- `.reverse()` 메서드를 사용해 `areas`의 원소 순서를 뒤집으세요.
- `areas`를 한 번 더 출력하세요.

`@hint`
- 첫 번째 지침에서는 `areas.append(___)` 호출을 두 번 사용하세요.
- 변수 `x`를 출력하려면 `print(x)`라고만 쓰면 돼요.
- `.reverse()` 메서드는 추가 입력이 필요하지 않아요. 점 표기법과 빈 괄호만 사용하세요: `.reverse()`.
- 변수 `x`를 출력하려면 `print(x)`라고만 쓰면 돼요.

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

## 패키지 임포트

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

원의 둘레와 넓이를 계산해 보려고 한다고 가정해 볼게요. 공식은 다음과 같습니다:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

`pi` 값을 직접 입력하는 대신, 해당 값을 포함한 `math` 패키지를 사용할 수 있어요.

참고로, `**`는 거듭제곱 연산자예요. 예를 들어 `3**4`는 `3`의 `4`제곱을 의미하며 결과는 `81`입니다.

`@instructions`
- `math` 패키지를 임포트하세요.
- `math.pi`를 사용해 원의 둘레를 계산하고 `C`에 저장하세요.
- `math.pi`를 사용해 원의 넓이를 계산하고 `A`에 저장하세요.

`@hint`
- `import math`만 사용하고, `pi`는 `math.pi`로 참조하시면 돼요.
- 지문에 나온 공식을 사용해 `C`를 구하세요. 곱셈에는 `*`를 사용해요.
- 지문에 나온 공식을 사용해 `A`를 구하세요. 곱셈에는 `*`, 거듭제곱에는 `**`를 사용해요.

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

## 선택적 임포트

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

`import math`처럼 일반적으로 임포트하면 `math` 패키지의 기능 **전체**를 사용할 수 있어요. 하지만 패키지의 특정 부분만 쓰려는 경우에는 임포트를 더 선택적으로 할 수 있습니다:

```
from math import pi
```

방금 한 것과 같은 방식으로, 이번에는 `pi`만 사용해 보세요.

`@instructions`
- `math` 패키지에서 `pi`만 임포트하는 선택적 임포트를 수행하세요.
- 원의 둘레를 `pi`로 계산해서 `C`에 저장하세요.
- 원의 넓이를 `pi`로 계산해서 `A`에 저장하세요.

`@hint`
- 선택적 임포트를 하려면 `from math import pi`를 사용하세요.
- 이제 `pi`를 바로 사용할 수 있어요!

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

## 여러 가지 가져오기 방법

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Python에서 패키지와 모듈을 가져오는 방법은 여러 가지가 있어요. 어떤 방식으로 가져오느냐에 따라 사용해야 하는 코드가 달라집니다.

예를 들어 `scipy` 패키지의 `linalg` 하위 패키지에 있는 [함수](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`를 사용하려고 한다고 가정해 볼게요. 이 함수를 다음과 같이 사용하고 싶습니다:

```
my_inv([[1,2], [3,4]])
```

위 코드를 오류 없이 실행하려면 어떤 `import` 문이 필요할까요?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- IPython 셸에서 각기 다른 import 문을 시도해 보고, 어느 것이 `my_inv([[1, 2], [3, 4]])` 줄이 오류 없이 실행되게 하는지 확인해 보세요. 입력한 코드를 실행하려면 **enter** 키를 누르세요.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "틀렸습니다. 다시 시도해 보세요. IPython 셸에서 다른 import 문을 시도해 보고, 어떤 것이 `my_inv([[1, 2], [3, 4]])` 줄이 오류 없이 실행되게 하는지 확인하세요."
msg4 = "정답입니다! `as` 단어를 사용하면 가져오는 함수에 대한 로컬 이름을 만들 수 있습니다: `inv()`는 이제 `my_inv()`로 사용할 수 있습니다."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```
