---
title_meta: Chapter 1
title: Python 기초
description: >-
  Python의 기본 개념을 소개합니다. 대화형 모드와 스크립트를 사용해 Python을 실행하는 방법을 배우고, 첫 변수를 만들며
  Python의 기본 자료형에 익숙해지세요.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Hello Python!
  - nb_of_exercises: 5
    title: 변수와 자료형
---

## 안녕하세요, Python!

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

이제 첫 번째 Python 코드를 실행해 볼 시간이에요!

코드로 이동한 다음 "코드 실행" 버튼을 눌러 결과를 확인하세요.

`@instructions`
- "코드 실행" 버튼을 눌러 `print(5 / 8)`의 결과를 확인하세요.

`@hint`
- 답변을 제출하기 전에 먼저 코드를 실행해 보세요. 결과를 살펴볼 시간을 가질 수 있어요.

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

## 계산기로서의 Python

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python은 기본 계산에 아주 적합해요. 덧셈, 뺄셈, 곱셈, 나눗셈을 모두 할 수 있어요.

스크립트의 코드는 몇 가지 예시를 보여줍니다.

이제 직접 코드를 써 보며 연습해 보세요.

`@instructions`
- `# Subtraction` 아래에서 `print()`를 사용해 `5`에서 `5`를 뺀 결과를 출력하세요.
- `# Multiplication` 아래에서 `3`에 `5`를 곱한 결과를 출력하세요.

`@hint`
- 결과를 보려면 `print()`를 사용해야 해요.
- 빼기는 `-`, 곱셈은 `*` 로 할 수 있어요.

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

## 변수와 자료형

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## 변수 할당

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Python에서 변수는 값에 이름을 붙여 참조할 수 있게 해 줍니다. 값이 `5`인 변수 `x`를 만들려면 다음 예시처럼 `=`를 사용해요:

```
x = 5
```

이제 실제 값 `5` 대신 변수 이름 `x`를 사용할 수 있습니다.

기억하세요. Python에서 `=`는 등식을 검사하는 것이 아니라 _할당_을 의미합니다! 연습 문제에서 `____`을(를) 여러분의 코드로 바꿔서 직접 해 보세요.

`@instructions`
- 값이 `100`인 변수 `savings`를 만드세요.
- 스크립트에서 `print(savings)`를 입력해 이 변수를 확인하세요.

`@hint`
- 변수 `savings`를 만들려면 `savings = 100`이라고 입력하세요.
- 변수 `savings`를 만든 뒤에는 `print(savings)`를 입력해 볼 수 있어요.
- 최종 코드에는 `____`이(가) 포함되면 안 됩니다.

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

## 변수를 사용한 계산

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

이제 저축을 나타내는 변수를 만들었으니, 실제로 저축해 볼까요?

실제 값을 바로 계산하는 대신, 변수로 계산할 수 있어요.

매달 $10씩 저축한다면, 4개월 뒤에는 얼마를 모으게 될까요?

`@instructions`
- 변수 `monthly_savings`를 `10`으로, `num_months`를 `4`로 만들어요.
- `monthly_savings`에 `num_months`를 곱해 `new_savings`에 할당하세요.
- `new_savings`의 값을 출력하세요.

`@hint`
- 변수로도 숫자와 똑같이 계산할 수 있어요. 그래서 `10 * 4` 대신 숫자 자리에 변수를 넣으면 됩니다!
- `new_savings`에 얼마가 들어 있는지 보려면 `print()`를 사용하세요.
- 변수 이름을 정확히 입력했는지 꼭 확인하세요!

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

이전 연습 문제에서는 Python의 정수(integer) 데이터 타입을 다뤘어요:

- `int`(integer): 소수 부분이 없는 숫자. 값이 `100`인 `savings`가 정수의 예예요.

숫자형 외에도 아주 흔히 쓰이는 데이터 타입이 세 가지 더 있어요:

- `float`(부동소수점): 정수 부분과 소수 부분을 점으로 구분해 갖는 숫자. `1.1`이 float의 예예요.
- `str`(문자열): 텍스트를 표현하는 타입. 작은따옴표나 큰따옴표로 문자열을 만들 수 있어요.
- `bool`(불리언): 논리값을 표현하는 타입. `True` 또는 `False`만 될 수 있어요(대소문자가 중요해요!).

`@instructions`
- 값이 `0.5`인 새 float 변수 `half`를 만드세요.
- 값이 `"Hello! How are you?"`인 새 문자열 변수 `intro`를 만드세요.
- 값이 `True`인 새 불리언 변수 `is_good`를 만드세요.

`@hint`
- Python에서 변수를 만들 때는 `=`를 사용해요. 문자열은 반드시 작은따옴표나 큰따옴표로 감싸세요.
- Python에는 불리언 값이 딱 두 개만 있어요: `True`와 `False`. `TRUE`, `true`, `FALSE`, `false` 같은 다른 표기는 인정되지 않아요.

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

Python에서 변수는 여러 가지 타입을 가질 수 있어요. 변수의 타입은 `type()`으로 확인할 수 있습니다. 예를 들어, `a`의 타입을 보려면 `type(a)`를 실행하세요.

타입이 다르면 동작도 달라집니다. 예를 들어 문자열 두 개를 더하는 것과 정수 두 개, 불리언 두 개를 더하는 것은 서로 다른 결과를 냅니다.

이제 직접 시험해 볼 시간이에요.

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
- `savings`와 `new_savings`를 더해 `total_savings`에 할당하세요.
- `type()`을 사용해 `total_savings`의 타입을 출력하세요.

`@hint`
- `savings + new_savings`를 새 변수 `total_savings`에 할당하세요.
- 변수 `x`의 타입을 출력하려면 `print(type(x))`를 사용하세요.

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
- `intro`와 `intro`의 합을 계산해 결과를 `doubleintro`에 할당하세요.
- `doubleintro`를 출력하세요. 예상하신 결과인가요?

`@hint`
- `intro + intro`를 새 변수 `doubleintro`에 할당하세요.
- 변수 `x`를 출력하려면 스크립트에 `print(x)`를 쓰세요.

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
