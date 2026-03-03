---
title_meta: Chapter 2
title: Python 리스트
description: '리스트에 데이터를 저장하고, 접근하며, 조작하는 방법을 배워요. 방대한 데이터를 효율적으로 다루기 위한 첫 단계입니다.'
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python 리스트
  - nb_of_exercises: 4
    title: 리스트 서브셋팅
  - nb_of_exercises: 5
    title: 리스트 조작
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

리스트는 값을 묶을 수 있는 **복합 자료형**이에요. 예를 들어 다음과 같아요:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

가족의 키를 측정한 뒤, 이번에는 집에 대한 정보를 모으려고 해요. 집의 각 공간 넓이는 이 연습 문제에 미리 정의된 변수에 각각 저장되어 있어요.

`@instructions`
- 복도(`hall`), 주방(`kit`), 거실(`liv`), 침실(`bed`), 욕실(`bath`)의 넓이를 이 순서로 담은 리스트 `areas`를 만드세요. 미리 정의된 변수를 사용하세요.
- `print()` 함수로 `areas`를 출력하세요.

`@hint`
- 이미 만들어진 변수를 사용해 리스트를 만들 수 있어요: `areas = [hall, kit, ...]`.
- 괄호는 둥근괄호 `()`가 아니라 대괄호 `[]`를 사용하세요.
- 리스트에 변수를 넣을 때는 큰따옴표가 필요하지 않아요.
- 제출할 때 리스트를 출력하려면 `print(areas)`를 입력하세요.

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

## 서로 다른 타입으로 리스트 만들기

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

자주 쓰이진 않지만, 리스트에는 문자열, 부동소수점 수, 불리언 등 다양한 Python 타입을 섞어서 담을 수 있어요.

이제 리스트에 방 이름을 추가해서, 방 이름과 크기를 함께 쉽게 확인할 수 있도록 해 볼게요.

일부 코드는 시작할 수 있도록 미리 제공되어 있어요. 여기서 주의하세요! `"bathroom"`은 문자열이고, `bath`는 앞에서 지정한 부동소수점 값 `9.50`을 나타내는 변수예요.

`@instructions`
- `areas` 리스트를 만드는 코드를 완성하세요. 각 방의 이름을 문자열로 먼저 넣고, 그다음 해당 면적을 넣도록 리스트를 구성하세요. 즉, 적절한 위치에 문자열 `"hallway"`, `"kitchen"`, `"bedroom"`을 추가하세요.
- `areas`를 다시 출력하세요. 이번 출력이 더 이해하기 쉬운가요?

`@hint`
- 리스트 `areas`의 처음 네 요소는 `["hallway", hall, "kitchen", kit, ...`처럼 작성되어 있어요.
- 문자열은 따옴표 `""`로 감싸야 해요.

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

## 리스트의 리스트

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

데이터 과학자는 보통 많은 데이터를 다루게 되고, 이 중 일부를 묶어서 관리하는 것이 더 효율적일 때가 많습니다.

집의 각 방 이름과 면적을 나타내기 위해 문자열과 실수로만 이뤄진 리스트를 만드는 대신, 리스트 안에 리스트를 넣는 방식으로 구성할 수 있습니다.

기억하세요: `"hallway"`는 문자열이고, `hall`은 이전에 지정한 실수 `11.25`를 담고 있는 변수입니다.

`@instructions`
- 리스트의 리스트를 완성해 침실과 욕실 데이터도 포함되도록 하세요. 입력 순서도 맞춰 주세요!
- `house`를 출력해 보세요. 이런 방식으로 데이터를 구성하는 게 더 이해가 잘 되나요?

`@hint`
- 대괄호 안에 `["bedroom", bed]`와 `["bathroom", bath]`를 추가해서 `house` 리스트에 서브리스트를 더하세요.
- 각 서브리스트 뒤에는 쉼표 `,`를 잊지 말고 넣으세요.
- 변수 `x`를 출력하려면, 새 줄에 `print(x)`를 적으세요.

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

## 리스트 부분 선택

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## 부분 선택으로 정복하기

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Python 리스트 부분 선택은 아주 쉽습니다. 아래 코드 예시는 리스트 `x`를 만들고 그중에서 "b"를 선택합니다. 두 번째 원소이므로 인덱스는 1이에요. 음수 인덱싱도 사용할 수 있습니다.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # 같은 결과!
```

앞에서 봤던, 문자열과 부동소수점이 함께 들어 있는 `areas` 리스트를 기억하시나요? 그 정의는 이미 스크립트에 들어 있습니다. 여기에 올바른 코드를 추가해서 Python 부분 선택을 해 보세요.

`@instructions`
- `areas` 리스트에서 두 번째 원소를 출력하세요(값은 `11.25`).
- `areas`의 마지막 원소 `9.50`을 부분 선택해 출력하세요. 여기서는 음수 인덱스를 사용하는 게 좋습니다!
- 거실 면적을 나타내는 숫자(`20.0`)를 선택해 출력하세요.

`@hint`
- 리스트 `x`의 두 번째 원소를 선택하려면 `x[1]`을 사용하세요.
- 리스트 `x`의 마지막 원소를 선택하려면 `x[-1]`을 사용하세요.
- 부분 선택(subsetting) 결과는 `print()`로 감싸서 출력하세요.
- 거실 면적을 나타내는 값은 리스트의 여섯 번째 원소이므로 여기서는 `[5]`를 사용해야 해요. `area[4]`는 문자열을 보여줄 거예요!

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

## 슬라이싱 해 보기

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

리스트에서 단일 값을 선택하는 것만이 전부는 아닙니다. 리스트의 여러 원소를 한꺼번에 선택하는, 즉 리스트를 _슬라이싱_ 할 수도 있어요. 다음 구문을 사용합니다:

```
my_list[start:end]
```

여기서 `start` 인덱스는 포함되지만, `end` 인덱스는 _포함되지 않습니다_. 또한 인덱스를 생략할 수도 있습니다. `start` 인덱스를 지정하지 않으면, Python은 슬라이스를 리스트의 시작부터 하려는 것으로 이해합니다.

`@instructions`
- 슬라이싱을 사용해 `areas`의 처음 6개 원소를 담는 리스트 `downstairs`를 만드세요.
- `areas`의 마지막 `4`개 원소로 `upstairs`를 만드세요. 이번에는 `end` 인덱스를 생략해 슬라이싱을 간단하게 하세요.
- `print()`를 사용해 `downstairs`와 `upstairs`를 모두 출력하세요.

`@hint`
- 리스트의 처음 여섯 개 원소를 얻으려면 대괄호 `[0:6]`을 사용하세요.
- 리스트 `l`에서 처음 5개 원소를 제외한 나머지를 얻으려면 `l[5:]`를 사용하면 됩니다.
- `downstairs`와 `upstairs`를 출력하도록 `print()` 호출을 두 번 추가하세요.

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

## 리스트의 리스트 부분 선택

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Python 리스트에는 다른 리스트가 들어갈 수도 있습니다.

리스트의 리스트를 부분 선택할 때도 이전과 같은 대괄호 표기법을 사용하면 됩니다. 예를 들어 리스트 `house`에 대해 다음과 같이 쓸 수 있어요:

```
house[2][0]
```

`@instructions`
- `house` 리스트에서 실수 `9.5`를 부분 선택하세요.

`@hint`
- 한 단계씩 진행해 봅시다. 먼저 리스트의 마지막 원소인 `["bathroom", 9.50]`에 접근하세요. 마지막 원소의 인덱스는 `-1`입니다.
- 다음으로 `["bathroom", 9.50]`의 두 번째 원소에 접근해야 하는데, 인덱스는 `1`입니다.

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

## 리스트 원소 바꾸기

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

리스트의 원소를 바꾸려면, 리스트에서 부분 집합을 선택한 뒤 그 부분 집합에 새 값을 할당하면 됩니다. 단일 원소를 선택할 수도 있고, 전체 리스트 슬라이스를 한꺼번에 바꿀 수도 있어요.

이번 연습 문제와 다음 연습 문제에서는 집 안의 서로 다른 방 이름과 면적을 담은 `areas` 리스트를 계속 사용합니다.

`@instructions`
- 음수 인덱싱을 사용해 욕실 면적을 `9.50`이 아닌 `10.50` 제곱미터로 업데이트하세요.
- `areas` 리스트를 좀 더 트렌디하게 만들어 볼까요? `"living room"`을 `"chill zone"`으로 바꾸세요. 이번에는 음수 인덱싱을 사용하지 마세요.

`@hint`
- 욕실 면적을 업데이트하려면, 욕실 면적의 부분 집합을 찾으세요(리스트의 마지막 항목입니다!).
- 그런 다음 이 부분 집합에 새 욕실 면적 값을 할당해 바꿔 주세요.
- 인덱스 4에 있는 `"living room"` 이름도 같은 방식으로 업데이트하세요.

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

리스트의 원소를 바꿀 수 있다면, 당연히 원소를 추가할 수도 있어야겠죠? `+` 연산자를 사용할 수 있어요:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

복권에 당첨되셨네요, 축하합니다! 수영장 딸린 별채와 차고를 짓기로 했어요. 이 정보를 `areas` 리스트에 추가해 보시겠어요?

`@instructions`
- `+` 연산자를 사용해 리스트 `["poolhouse", 24.5]`를 `areas` 리스트의 끝에 이어 붙이세요. 결과 리스트를 `areas_1`에 저장하세요.
- 차고 정보를 더해 `areas_1`을 더 확장하세요. 문자열 `"garage"`와 실수 `15.45`를 추가하세요. 결과 리스트의 이름은 `areas_2`로 하세요.

`@hint`
- 과제의 코드 예시를 따라 해 보세요. 여기서 `x`는 `areas`이고, `["e", "f"]`는 `["poolhouse", 24.5]`예요.
- `areas_1`에 요소를 더 추가하려면 `areas_1 + ["element", 123]`처럼 사용하세요.

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

마지막으로, 리스트에서 요소를 제거할 수도 있어요. 이는 `del` 문으로 할 수 있습니다:

```
x = ["a", "b", "c", "d"]
del x[1]
```

여기서 주의하세요: 리스트에서 요소를 하나 삭제하면, 삭제한 요소 뒤에 있는 모든 요소의 인덱스가 바뀝니다!

안타깝게도 복권 당첨 금액이 생각보다 크지 않아 `poolhouse`는 포기해야 할 것 같네요. 리스트에서 이를 제거해야 합니다. `areas` 리스트에서 해당 문자열과 실수(float)를 제거하세요.

`@instructions`
- `areas` 리스트에서 `"poolhouse"`에 해당하는 문자열과 실수(float)를 삭제하세요.
- 업데이트된 `areas` 리스트를 출력하세요.

`@hint`
- 두 요소를 삭제하려면 `del`을 두 번 사용해야 해요. 다만, 인덱스가 바뀐다는 점에 주의하세요!

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

## 리스트의 내부 작동 방식

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

이 연습 문제에는 미리 작성된 코드가 있어요. `areas`라는 리스트와 그 복사본인 `areas_copy`가 준비되어 있습니다.

현재 코드는 `areas_copy` 리스트의 첫 번째 원소를 바꾸고, 그다음 `areas` 리스트를 출력해요. **코드 실행**을 눌러 보면 `areas_copy`를 변경했는데도 그 변화가 `areas`에도 반영되는 것을 확인할 수 있어요. 이는 `areas`와 `areas_copy`가 같은 리스트를 가리키고 있기 때문이에요.

`areas_copy`에서의 변경이 `areas`에까지 영향을 주지 않게 하려면, `list()`나 `[:]`를 사용해 `areas` 리스트를 보다 명시적으로 복사해야 합니다.

`@instructions`
- 변수 `areas_copy`를 만드는 두 번째 명령을 바꿔서, `areas_copy`가 `areas`의 명시적 복사본이 되도록 하세요. 수정한 뒤에는 `areas_copy`에 가한 변경이 `areas`에 영향을 주지 않아야 합니다. 확인하려면 **답변 제출**을 해 보세요.

`@hint`
- `areas_copy = areas` 호출을 바꾸세요. `areas`를 그대로 할당하는 대신 `list(areas)` 또는 `areas[:]`를 할당할 수 있어요.

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
