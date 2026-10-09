---
title_meta: 챕터 1
title: Python 기초
description: >-
  Python의 기본 개념을 소개합니다. Python을 대화형으로 사용하는 방법과 스크립트로 실행하는 방법을 배웁니다. 첫 번째 변수를 만들어
  보고, Python의 기본 데이터 타입을 익혀 보세요.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Python 시작하기!
  - nb_of_exercises: 5
    title: 변수와 타입
---

## Python 시작하기!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## 첫 번째 Python 코드

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

이제 첫 번째 Python 코드를 실행해볼 시간입니다!

코드 창으로 이동한 후 코드 실행 버튼을 클릭해 결과물을 확인해보세요.

`@instructions`
- 코드 실행 버튼을 클릭해 `print(5 / 8)`의 결과물을 확인해보세요.

`@hint`
- 답안을 제출하기 전에 먼저 코드를 실행해 결과물을 확인해보세요.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}`을(를) 사용하여 `5 / 8`을(를) 출력하셨습니까?")
success_msg("훌륭합니다! 다음 문제로 넘어가겠습니다!")
```

---

## Python으로 계산하기

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python은 기본적인 계산에 매우 적합합니다. 덧셈, 뺄셈, 곱셈, 나눗셈 모두 가능합니다.

스크립트의 코드에서 몇 가지 예시를 확인할 수 있습니다.

이제 직접 코드를 작성하며 연습해 보세요.

`@instructions`
- `# Subtraction` 하단에 `5`에서 `5`를 뺀 결괏값을 `print()`를 이용하여 출력하세요.
- `# Multiplication` 하단에 `3`과 `5`를 곱한 결괏값을 출력하세요.

`@hint`
- 출력 결과를 표시하려면 `print()`를 사용해야 합니다.
- 빼기는 `-`, 곱하기는 `*`을 사용하세요.

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
Ex().has_printout(0, not_printed_msg = "`print(4 + 5)`를 사용하여 합계의 결과를 출력하셨나요?")

Ex().has_printout(1, not_printed_msg = "`print(5 - 5)`를 사용하여 뺄셈의 결과를 출력하셨나요?")

Ex().has_printout(2, not_printed_msg = "`print(3 * 5)`를 사용하여 곱셈의 결과를 출력하셨나요?")

Ex().has_printout(3, not_printed_msg = "`print(10 / 2)`를 사용하여 나눗셈의 결과를 출력하셨나요?")

success_msg("정답입니다! Python은 수학을 도와줄 수 있으며, 이는 데이터 기술을 키우면서 분석에 유용할 것입니다.")
```

---

## 변수와 타입

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## 변수 할당하기

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Python에서는 변수를 사용해 값에 이름을 붙일 수 있습니다. `5`라는 값을 가진 변수 `x`를 만들기 위해서 아래의 예시와 같이 `=`를 사용합니다.

```
x = 5
```

이제 실제 값 `5` 대신 변수 이름 `x`를 사용할 수 있습니다.

Python에서 `=`는 _할당_을 의미합니다. 같음을 확인하는 연산자가 아니라는 점에 유의하세요. 아래 연습 문제에서 `____`을 직접 코드로 바꿔 보세요.

`@instructions`
- 값이 `100`인 변수 `savings`를 만드세요.
- 스크립트에 `print(savings)`를 입력하여 변수를 확인해 보세요.

`@hint`
- `savings = 100`을 입력하여 변수 `savings`를 만드세요.
- 변수 `savings`를 생성한 후에는 `print(savings)`를 입력할 수 있습니다.
- 최종 코드에는 `____`이 남아 있지 않아야합니다.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="변수 `savings`에 `100`을 할당하십시오.")
Ex().has_printout(0, not_printed_msg = "생성한 변수 `savings`를 `print(savings)`로 출력하십시오.")
success_msg("잘하셨습니다! 이제 이 변수를 사용하여 몇 가지 계산을 해보겠습니다!")
```

---

## 변수를 활용해 계산하기

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

이제 저축 변수를 만들었으니, 본격적으로 저축을 시작해보겠습니다!

실제 값 대신 변수를 이용해 계산할 수 있습니다.

매달 $10씩 저축한다면, 4개월 후에는 얼마를 모을 수 있을까요?

`@instructions`
- 값이 `10`인 `monthly_savings` 변수와 값이 `4`인 `num_months` 변수를 생성하세요.
- `monthly_savings`와 `num_months`를 곱한 값을 `new_savings`에 할당하세요.
- `new_savings` 값을 출력하세요.

`@hint`
- 변수를 이용한 계산은 숫자를 이용한 계산과 동일합니다. `10 * 4`를 입력하는 대신 숫자 자리에 변수를 넣어보세요!
- `print()`를 사용해 `new_savings`의 값을 확인해보세요.
- 변수 이름을 정확하게 입력했는지 확인하세요!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "`monthly_savings`에 `10`을 `monthly_savings = 10`을 사용하여 저장하셨습니까?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "`num_months`에 `4`를 `num_months = 4`를 사용하여 저장하셨습니까?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "올바른 변수와 기호를 사용하여 곱셈을 하셨습니까? `monthly_savings * num_months`가 예상되었으나 다른 것이 입력되었습니다.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "올바른 변수와 기호를 사용하여 덧셈을 하셨습니까? `savings + new_savings`가 예상되었으나 다른 것이 입력되었습니다.")

Ex().has_printout(0, not_printed_msg="스크립트의 끝에서 `new_savings`를 출력하는 것을 잊지 마십시오.")

success_msg("새로운 저축액이 $40입니다!")
```

---

## 다른 변수 타입

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

이전 연습 문제에서는 Python의 정수형 데이터 타입을 다뤘습니다.

- `int` 또는 정수(integer): 소수점 이하가 존재하지 않는 숫자입니다. `100`의 값을 갖는 `savings`를 정수의 예시로 들 수 있습니다.

숫자형 데이터 타입 외에도, 자주 사용되는 세 가지 데이터 타입이 있습니다.

- `float` 또는 부동 소수점(floating point): 정수 부분과 소수 부분을 점으로 구분한 숫자로, `1.1`과 같이 표현할 수 있습니다.
- `str` 또는 문자열(string): 텍스트를 나타내는 타입입니다. 작은따옴표나 큰따옴표를 사용해 문자열을 만들 수 있습니다.
- `bool` 또는 불리언(boolean): 논리값을 나타내는 타입입니다. `True` 또는 `False`(대소문자 구분 필요)만 가질 수 있습니다.

`@instructions`
- 값이 `0.5`인 새 부동 소수점 `half`를 만드세요.
- 값이 `"Hello! How are you?"`인 새 문자열 `intro`를 만드세요.
- 값이 `True`인 새 불리언 `is_good`을 만드세요.

`@hint`
- Python에서 변수를 만들려면 `=`를 사용하세요. 문자열은 작은따옴표나 큰따옴표 안에 넣어야 합니다.
- Python의 불리언 값은 `True`와 `False` 두 가지뿐입니다. `TRUE`, `true`, `FALSE`, `false` 등 다른 형태는 허용되지 않습니다.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "부동 소수점 `0.5`를 `half`에 저장하셨나요?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "음, `intro` 변수에 뭔가 잘못된 것이 있습니다. 철자를 다시 확인하고 따옴표를 사용했는지 확인하세요.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "불리언 값을 대문자로 시작하셨나요? 여기서는 따옴표를 사용할 필요가 없습니다.")

success_msg("좋습니다!")
```

---

## 다른 타입과의 연산

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Python에는 다양한 타입의 변수가 있습니다. `type()`을 사용하여 변수의 타입을 확인할 수 있습니다. 예를 들어, `type(a)`를 실행해서 `a`의 타입을 확인할 수 있습니다.

Python에서는 타입에 따라 동작 방식이 달라집니다. 예를 들어, 문자열 두 개를 더하면 정수 두 개나 불리언 두 개를 더할 때와는 다른 결과가 나옵니다.

직접 확인해 볼까요?

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
- `savings`와 `new_savings`를 더한 결과를 `total_savings`에 할당하세요.
- `type()`을 사용하여 `total_savings`의 타입을 출력하세요.

`@hint`
- `savings + new_savings`를 새 변수 `total_savings`에 할당하세요.
- `print(type(x))`를 사용하여 변수 `x`의 타입을 출력하세요.

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
msg = "미리 정의된 변수를 변경하거나 제거할 필요가 없습니다."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="`savings`와 `new_savings`를 더하여 `total_savings` 변수를 만드십시오."),
    has_printout(1, not_printed_msg = "__JINJA__:`{{sol_call}}`을(를) 사용하여 `total_savings`의 유형을 출력하십시오.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- `intro`와 `intro`를 더한 결과를 `doubleintro`에 할당하세요.
- `doubleintro`를 출력해 보세요. 예상한 결과와 같은 지 확인해보세요.

`@hint`
- `intro + intro`를 새 변수 `doubleintro`에 할당하세요.
- 스크립트에 `print(x)`를 입력하여 변수 `x`를 출력하세요.

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
msg = "미리 정의된 변수를 변경하거나 제거할 필요는 없습니다."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "`intro + intro`의 결과를 `doubleintro`에 저장했는지 확인하세요."),
    has_printout(0, not_printed_msg = "`doubleintro`를 출력하는 것을 잊지 마세요.")
)

success_msg("좋습니다. `intro + intro`가 `\"Hello! How are you?\"`와 `\"Hello! How are you?\"`를 함께 붙이는 방식을 주목하세요.")
```
