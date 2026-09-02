---
title_meta: 챕터 2
title: Python 리스트
description: '리스트에서 데이터를 저장하고, 접근하고, 조작하는 방법을 배웁니다. 대량의 데이터를 효율적으로 다루기 위한 첫걸음을 떼보세요.'
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python 리스트
  - nb_of_exercises: 4
    title: 리스트 부분 추출하기
  - nb_of_exercises: 5
    title: 리스트 조작하기
---

## Python 리스트

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## 리스트 만들기

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

리스트는 **복합 데이터 타입**으로, 다음과 같이 다양한 값을 하나로 묶을 수 있습니다:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

가족의 키를 측정한 후, 이번에는 여러분이 살고 있는 집에 대한 정보를 수집하기로 했습니다. 집 안 각 공간의 면적은 연습 문제에서 각기 다른 변수에 저장되었습니다.

`@instructions`
- 리스트 `areas`를 만들어 복도(`hall`), 주방(`kit`), 거실(`liv`), 침실(`bed`), 욕실(`bath`)의 면적을 순서대로 포함하세요. 미리 정의된 변수를 사용하세요.
- `print()` 함수를 사용해 `areas`를 출력하세요.

`@hint`
- 이미 생성된 변수들을 사용해 다음과 같이 리스트를 만들 수 있습니다. `areas = [hall, kit, ...]`
- 소괄호 `()` 대신 대괄호 `[]`를 사용해야 합니다.
- 리스트에 변수를 포함할 때는 따옴표를 사용할 필요가 없습니다.
- `print(areas)`를 입력하여 제출 전에 리스트를 출력하세요.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "미리 정의된 변수를 제거하거나 수정하지 마십시오!"
areas_msg = "`areas`를 모든 면적 변수를 포함하는 리스트로 정의하십시오. 올바른 순서로: `[hall, kit, liv, bed, bath]`. 오타에 주의하십시오. 리스트에는 다른 것이 포함되어서는 안 됩니다!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}`을 사용하여 스크립트의 끝에서 `areas` 리스트를 출력했는지 확인하십시오."),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("좋습니다! 여기서는 리스트가 훨씬 낫지 않습니까?")
```

---

## 다양한 타입이 포함된 리스트 만들기

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

흔한 경우는 아니지만, 리스트에는 문자열, 실수, 불리언 등 다양한 Python 타입을 함께 담을 수 있습니다.

이번에는 리스트에 방 이름을 추가해서 방 이름과 넓이를 한눈에 확인할 수 있도록 만들어 보겠습니다.

시작을 돕기 위해 일부 코드가 미리 작성되어 있습니다. 이 부분을 주의하세요! `"bathroom"`은 문자열이고, `bath`는 앞서 지정한 실수 값 `9.50`을 나타내는 변수입니다.

`@instructions`
- `areas` 리스트를 완성하는 코드를 작성하세요. 각 방의 이름을 문자열로 먼저 넣고, 그 다음에 해당 방의 넓이가 오도록 리스트를 구성하세요. 적절한 위치에 `"hallway"`, `"kitchen"`, `"bedroom"` 문자열을 추가하면 됩니다.
- `areas`를 다시 출력해 보세요. 출력 결과가 더 이해하기 쉬워졌나요?

`@hint`
- `areas` 리스트의 첫 요소 네 개는 `["hallway", hall, "kitchen", kit, ...`와 같이 작성됩니다.
- 문자열은 반드시 따옴표 `""`로 감싸야 합니다.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "미리 정의된 변수를 제거하거나 수정하지 마십시오!"
areas_msg = "올바른 값을 `areas`에 할당하지 않았습니다. 지침을 다시 한 번 살펴보세요. 각 경우에 방 이름을 면적을 포함하는 변수 앞에 배치해야 합니다. 순서가 중요합니다! 오타에 주의하세요."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:스크립트의 끝에서 `areas` 리스트를 출력하기 위해 `{{sol_call}}`을(를) 사용했는지 확인하세요.")

success_msg("좋습니다! 이 리스트는 문자열과 부동 소수점 수를 모두 포함하고 있지만, 이는 Python에게 문제가 되지 않습니다!")
```

---

## 리스트 안의 리스트

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

데이터 과학자로서 수많은 데이터를 다루게 될 텐데, 이때 데이터를 그룹으로 묶으면 훨씬 편리하게 작업할 수 있습니다.

집 안의 모든 방 이름과 넓이를 문자열과 실수로 구성된 단순한 리스트에 담는 대신, 리스트 안에 리스트를 넣는 방식을 활용할 수 있습니다.

`"hallway"`는 문자열이고, `hall`은 앞서 지정한 실수 `11.25`를 나타내는 변수라는 것을 기억하세요.

`@instructions`
- 침실과 욕실 데이터도 포함하는 리스트 안의 리스트를 완성하세요. 순서에 맞게 입력해야합니다!
- `house`를 출력해 보세요. 이런 방식으로 데이터를 구조화하면 더 쉽게 이해할 수 있겠죠?

`@hint`
- `house` 리스트에 대괄호를 사용해 `["bedroom", bed]`와 `["bathroom", bath]`를 추가하여 _하위 리스트_를 만드세요.
- 각 하위 리스트 뒤에는 반드시 쉼표 `,`를 붙여야 합니다.
- 변수 `x`를 출력하려면 새 줄에 `print(x)`를 작성하세요.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "미리 정의된 변수를 제거하거나 수정하지 마십시오!"
house_msg = "`house`에 올바른 값을 할당하지 않았습니다. 지침을 다시 한 번 살펴보세요. 리스트의 리스트를 확장하여 각 방 이름과 방 면적 쌍에 대한 리스트를 포함하도록 하십시오. 순서와 오타에 주의하세요!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}`을 사용하여 `house`의 내용을 출력했는지 확인하십시오.")

success_msg("훌륭합니다! 리스트 서브세팅에 대해 배울 준비를 하세요!")
```

---

## 리스트 부분 추출하기

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## 부분 추출하여 처리하기

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Python 리스트에서 원하는 요소를 추출하는 건 어렵지 않습니다. 아래의 샘플 코드를 살펴보시면, 리스트 `x`를 만든 뒤 리스트에서 'b'를 선택합니다. 두 번째 요소이므로 인덱스 1에 위치한다는 것을 잊지 마세요. 음수 인덱싱을 사용해도 괜찮습니다.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

앞서 사용한 문자열과 실수가 모두 포함된 `areas` 리스트를 기억하시나요? 해당 리스트의 정의는 이미 스크립트에 포함되어 있습니다. 올바른 코드를 추가해서 Python 부분 추출을 직접 시도해보세요.

`@instructions`
- `areas` 리스트에서 두 번째 요소(`11.25`)를 출력하세요.
- `areas`의 마지막 요소인 `9.50`을 선택해 출력하세요. 음수 인덱스를 사용하면 편리합니다!
- 거실의 면적을 나타내는 숫자(`20.0`)를 선택해 출력하세요.

`@hint`
- 리스트 `x`의 두 번째 요소를 선택하려면 `x[1]`을 사용하세요.
- 리스트 `x`의 마지막 요소를 선택하려면 `x[-1]`을 사용하세요.
- 부분 추출 연산을 반드시 `print()`로 감싸서 실행해야합니다.
- 거실의 면적을 나타내는 숫자는 리스트의 6번째 요소이므로 `[5]`를 사용해야 합니다. `area[4]`를 사용하면 문자열이 출력됩니다!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "미리 정의된 `areas` 리스트를 제거하거나 수정하지 마십시오."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "코드를 다시 살펴보고 `areas`의 두 번째 요소를 출력하십시오. 이는 인덱스 `1`에 있습니다.")
Ex().has_printout(1, not_printed_msg = "코드를 다시 살펴보고 `areas`의 마지막 요소를 출력하십시오. 이는 인덱스 `-1`에 있습니다.")
Ex().has_printout(2, not_printed_msg = "코드를 다시 살펴보고 거실의 면적을 출력하십시오. 이는 인덱스 `5`에 있습니다.")
success_msg("잘하셨습니다!")
```

---

## 슬라이싱 활용하기

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

리스트에서 단일 값을 선택하는 것은 시작에 불과합니다. 리스트를 _슬라이싱_해서 여러 개의 요소를 한 번에 선택할 수도 있습니다. 다음 문법을 사용하세요:

```
my_list[start:end]
```

`start` 인덱스는 결과에 포함되지만, `end` 인덱스는 _포함되지 않습니다_. 인덱스를 생략하는 것도 가능합니다. `start` 인덱스를 지정하지 않으면 Python은 자동으로 리스트의 맨 앞부터 슬라이싱을 시작합니다.

`@instructions`
- 슬라이싱을 사용하여 `downstairs`의 첫 6개 요소를 담은 리스트 `areas`를 만드세요.
- `areas`의 마지막 `4`개 요소로 `upstairs`를 만드세요. 이번에는 `end` 인덱스를 생략하여 간단히 표현하세요.
- `print()`를 사용하여 `upstairs`와 `downstairs`를 모두 출력하세요.

`@hint`
- `[0:6]`와 같이 괄호를 사용하여 리스트의 첫 6개 요소를 가져올 수 있습니다.
- 리스트 `l`에서 첫 5개 요소를 제외한 나머지를 가져오려면 `l[5:]`를 사용하세요.
- `print()` 호출을 두 번 추가하여 `downstairs`와 `upstairs`를 출력하세요.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "미리 정의된 `areas` 리스트를 제거하거나 수정하지 마십시오."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s`이(가) 잘못되었습니다. `areas[%s]`와 슬라이싱을 사용하여 원하는 요소를 선택하거나 이에 상응하는 것을 사용하십시오."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="계산 후 `downstairs`를 출력하셨습니까?")
Ex().has_printout(1, not_printed_msg="계산 후 `upstairs`를 출력하셨습니까?")

success_msg("훌륭합니다!")
```

---

## 리스트 안의 리스트에서 부분 추출하기

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Python 리스트는 다른 리스트를 요소로 포함할 수 있습니다.

리스트 안의 리스트에서 일부를 추출할 때도 이전과 동일한 방법인 대괄호를 사용합니다. 예를 들어 `house` 리스트는 이렇게 보일 것입니다.

 ```
house[2][0]
```

`@instructions`
- `house` 리스트에서 `9.5`를 가져오세요.

`@hint`
- 단계별로 생각해 보세요. 먼저 리스트의 마지막 요소인 `["bathroom", 9.50]`에 접근해야 합니다. 마지막 요소의 인덱스는 `-1`이라는 것을 기억하세요.
- 다음으로 `["bathroom", 9.50]`의 두 번째 요소에 접근해야 합니다. 해당 요소의 인덱스는 `1`입니다.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("정확합니다! 리스트 퍼즐의 마지막 조각은 조작입니다.")
```

---

## 리스트 조작하기

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## 리스트 요소 교체하기

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

리스트의 요소를 교체하려면 리스트의 일부를 선택한 뒤 새 값을 할당하면 됩니다. 단일 요소를 선택할 수도 있고, 전체 리스트의 슬라이스를 한 번에 변경할 수도 있습니다.

이번 연습 문제와 이후의 연습 문제에서는 집의 다양한 방 이름과 면적이 담긴 `areas` 리스트를 계속 활용합니다.

`@instructions`
- 음수 인덱싱을 사용하여 욕실 면적을 `10.50`에서 `9.50` 제곱미터로 업데이트하세요.
- `areas` 리스트를 좀 더 세련되게 바꿔볼까요? `"living room"`을 `"chill zone"`으로 변경하세요. 이번에는 음수 인덱싱을 사용하지 마세요.

`@hint`
- 욕실 면적을 업데이트하려면 욕실 면적에 해당하는 부분(리스트의 마지막 항목)을 선택하세요.
- 그리고 해당 부분에 새로운 욕실 면적 값을 할당하여 교체하세요.
- 같은 방법으로 인덱스 4에 있는 `"living room"`의 이름도 업데이트하세요.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = '욕실 면적을 업데이트하려면 `areas[-1] = 10.50`을(를) 사용할 수 있습니다.'
chillzone_msg = '거실 이름을 업데이트하려면 `areas[4] = "chill zone"`을(를) 사용할 수 있습니다.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = '귀하의 `areas` 변경 사항이 올바른 목록을 생성하지 않았습니다. 올바른 하위 집합 연산을 사용했는지 확인하십시오. 의심스러울 때는 힌트를 사용할 수 있습니다!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('좋습니다! 코드 샘플에서 보여준 것처럼, 리스트를 슬라이스하고 다른 리스트로 대체하여 한 번의 명령으로 여러 요소를 업데이트할 수도 있습니다.')
```

---

## 리스트 확장하기

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

리스트의 요소를 변경할 수 있다면, 새로운 요소도 추가할 수 있어야겠죠? `+` 연산자를 사용할 수 있습니다.

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

와우, 복권에 당첨됐습니다! 여러분은 수영장 옆 별채와 차고를 짓기로 결정했습니다. `areas` 리스트에 해당 정보를 추가해보세요.

`@instructions`
- `+` 연산자를 사용하여 `["poolhouse", 24.5]` 리스트를 `areas` 리스트의 끝에 추가하세요. 결과 리스트를 `areas_1`로 저장하세요.
- 차고 정보를 추가하여 `areas_1`을 더 확장하세요. 문자열 `"garage"`와 실수 `15.45`를 추가하고, 결과 리스트의 이름을 `areas_2`로 지정하세요.

`@hint`
- 과제의 코드 예시를 참고하세요. 여기서 `x`는 `areas`이고, `["e", "f"]`는 `["poolhouse", 24.5]`입니다.
- `areas_1`에 더 많은 요소를 추가하려면 `areas_1 + ["element", 123]`을 사용하세요.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "미리 정의된 `areas` 리스트를 제거하거나 수정하지 마십시오."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "`areas + [\"poolhouse\", 24.5]`를 사용하여 `areas_1`을 생성하십시오. 오타에 주의하세요!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "`areas_1 + [\"garage\", 15.45]`를 사용하여 `areas_2`을 생성하십시오. 오타에 주의하세요!")
success_msg("멋집니다! 리스트가 잘 형성되고 있습니다!")
```

---

## 리스트 요소 삭제하기

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

마지막으로, 리스트에서 요소를 삭제할 수도 있습니다. `del` 명령문을 사용하시면 됩니다.

```
x = ["a", "b", "c", "d"]
del x[1]
```

주의할 점은 리스트에서 요소를 삭제하면, 삭제된 요소 뒤에 있는 모든 요소의 인덱스가 바뀐다는 점입니다!

아쉽게도 복권 당첨금이 생각보다 크지 않아서 수영장 옆 별채 공사는 포기해야 할 것 같습니다. 리스트에서 해당 항목을 삭제해야 합니다. `areas` 리스트에서 해당하는 문자열과 실수를 삭제하세요.

`@instructions`
- `areas` 리스트에서 `"poolhouse"`에 해당하는 문자열과 실수를 삭제하세요.
- 업데이트된 `areas` 리스트를 출력하세요.

`@hint`
- 요소 두 개를 삭제하려면 `del`을 두 번 사용해야 합니다. 삭제 후 인덱스가 변경된다는 점에 주의하세요!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="`areas`에서 poolhouse 문자열과 float을 제거한 후 출력하셨나요?")
success_msg("정답입니다! 나중에 Python 리스트에서 특정 요소를 더 쉽게 제거하는 방법에 대해 배우게 될 것입니다.")
```

---

## 리스트의 내부 동작 방식

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

이 연습 문제에서는 `areas`라는 이름의 리스트와 `areas_copy`라는 복사본이 제공됩니다.

현재 `areas_copy` 리스트의 첫 번째 요소가 변경되었고, `areas` 리스트가 출력된 상태입니다. 코드 실행 버튼을 클릭해보면, `areas_copy`만 수정했음에도 `areas`도 동일하게 변경되었다는 것을 확인할 수 있습니다. `areas`와 `areas_copy`가 동일한 리스트를 가리키고 있기 때문입니다.

`areas_copy`를 변경하여도 `areas`에 영향을 미치지 않도록 하려면, `list()`를 사용하거나 `[:]`을 이용해 `areas` 리스트를 명시적으로 복사해야 합니다.

`@instructions`
- `areas_copy` 변수를 생성하는 두 번째 명령어를 수정하여, `areas_copy`를 `areas`의 명시적인 복사본으로 만드세요. 수정 후에는 `areas_copy`를 변경해도 `areas`가 영향을 받지 않아야 합니다. 답변 제출을 클릭해서 확인해 보세요.

`@hint`
- `areas_copy = areas` 코드를 변경하세요. `areas`를 직접 할당하는 대신 `list(areas)` 또는 `areas[:]`를 할당할 수 있습니다.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "`areas_copy`가 올바르게 업데이트되지 않은 것 같습니다."),
  check_function("list", missing_msg = "`list(areas)`를 사용하여 `areas_copy`를 생성했는지 확인하세요.")
)

mmsg = "미리 정의된 `areas` 리스트를 제거하지 마세요."
imsg = "원본 `areas` 리스트가 아닌 복사본만 편집해야 합니다. 복사본을 만드는 방법이 확실하지 않다면 연습 문제 설명을 다시 확인하세요."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "`list(areas)`를 사용하여 `areas_copy`를 생성했는지 확인하세요.")
)

success_msg("좋습니다! 명시적 복사와 참조 기반 복사의 차이는 미묘하지만 매우 중요할 수 있습니다. 리스트가 컴퓨터의 메모리에 어떻게 저장되는지 기억해 두세요.")
```
