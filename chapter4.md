---
title_meta: 4장
title: NumPy
description: >-
  NumPy는 데이터 과학을 효율적으로 실습하는 데 기본이 되는 Python 패키지입니다. NumPy 배열의 강력한 기능을 활용하는 방법을
  배우고, 데이터 탐색을 시작해보세요.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: 2D NumPy 배열
  - nb_of_exercises: 3
    title: 'NumPy: 기초 통계'
---

## NumPy

```yaml
type: VideoExercise
key: f4545baa53
xp: 50
```

`@projector_key`
a0487c26210f6b71ea98f917734cea3a

---

## 첫 번째 NumPy 배열

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

이제 야구의 세계로 뛰어들어볼까요? 그 과정에서 데이터 과학을 위한 강력한 패키지인 `numpy`의 기본 사용법에 익숙해질 것입니다.

Python 스크립트에는 야구 선수들의 키(cm)를 담은 리스트 `baseball`이 정의되어 있습니다. 이 리스트로 `numpy` 배열을 만드는 코드를 추가해 보세요.

`@instructions`
- `numpy` 패키지를 `np`로 임포트하여, `numpy`를 `np`로 사용할 수 있도록 하세요.
- `np.array()`를 사용해 `baseball`로부터 `numpy` 배열을 만드세요. 배열의 이름은 `np_baseball`로 지정하세요.
- `np_baseball`의 타입을 출력하여 올바르게 만들었는지 확인하세요.

`@hint`
- `import numpy as np`를 사용하면 됩니다. 이제 `numpy` 함수를 사용할 때마다 `np.fun_name()` 형식으로 호출하면 됩니다.
- `np.array()`의 입력값으로 `baseball`을 사용하세요. 함수 호출 결과를 `np_baseball`에 할당하세요.
- 변수 `x`의 타입을 출력하려면 `print(type(x))`를 입력하세요.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sample_code`
```{python}
# Import the numpy package as np


baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball


# Print out type of np_baseball

```

`@solution`
```{python}
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a NumPy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

`@sct`
```{python}
predef_msg = "미리 정의된 변수를 변경하거나 제거할 필요가 없습니다."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("잘하셨습니다!")
```

---

## 야구 선수의 키

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

여러분은 열렬한 야구 팬입니다. MLB(메이저리그 베이스볼)에 연락해 주요 선수들의 키에 관한 더 많은 통계 자료를 요청했습니다. 1,000명이 넘는 선수들의 데이터를 받았으며, 이 데이터는 일반 Python 리스트 `height_in`로 저장되어 있습니다. 키의 단위는 인치(inch)입니다. 이 리스트로 `numpy` 배열을 만들고, 단위를 미터(m)로 바꿔봅시다.

`height_in`은 이미 준비되어 있고, `numpy` 패키지도 로드된 상태이므로 바로 시작할 수 있습니다(출처: stat.ucla.edu).

`@instructions`
- `height_in`으로 `numpy` 배열을 만드세요. 새 배열의 이름은 `np_height_in`으로 지정하세요.
- `np_height_in`을 출력하세요.
- `np_height_in`에 `0.0254`를 곱하여 모든 측정값의 단위를 인치에서 미터로 변환하세요. 변환된 값을 새 배열 `np_height_m`에 저장하세요.
- `np_height_m`을 출력하고 결과가 타당한지 확인하세요.

`@hint`
- `np.array()`를 사용하여 `height`를 전달하세요. 결과를 `np_height_in`에 저장하세요.
- 변수 `x`를 출력하려면 Python 스크립트에서 `print(x)`를 입력하세요.
- `np_height_in`을 하나의 숫자처럼 계산에 사용하세요. `np_height_in * conversion_factor`가 정답에 포함됩니다.
- 변수 `x`를 출력하려면 Python 스크립트에서 `print(x)`를 입력하세요.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in


# Print out np_height_in


# Convert np_height_in to m: np_height_m


# Print np_height_m

```

`@solution`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
  has_printout(0),
  check_correct(
    check_object('np_height_in').has_equal_value(),
    check_function('numpy.array').check_args(0).has_equal_ast()
  )
)

Ex().check_correct(
  has_printout(1),
  check_object("np_height_m").has_equal_value(incorrect_msg = "`np_height_m`을 계산하기 위해 `np_height_in * 0.0254`를 사용하십시오.")
)

success_msg("좋습니다! 눈 깜짝할 사이에 `numpy`는 1000개 이상의 높이 측정값에 대해 곱셈을 수행합니다.")
```

---

## NumPy 사용 시 주의할 점

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy`는 벡터 연산에 매우 유용합니다. 하지만 일반 Python 리스트와 비교해보면 몇 가지 다른 점이 있습니다.

첫째, `numpy` 배열은 다른 타입의 요소를 함께 담을 수 없습니다. 불리언과 정수처럼 타입을 혼합하면 `numpy`는 자동으로 공통 타입으로 바뀝니다. `True`와 `False` 같은 불리언 값은 숫자와 결합될 때 각각 `1`과 `0`으로 처리되므로, 배열은 최종적으로 정수형이 됩니다.

둘째, `+`, `-`, `*`, `/`와 같은 일반 산술 연산자는 Python 리스트와 `numpy` 배열에서 그 의미가 다릅니다.

다음과 같은 결과가 나오도록 하는 코드를 선택하세요.

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

`numpy` 패키지는 이미 `np`로 임포트되어 있습니다. IPython Shell에서 각 코드를 실행하고 결과를 확인할 수 있습니다.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- 각 코드 조각을 복사하여 IPython Shell에 붙여넣으세요. **enter** 키를 눌러 코드를 실행한 후, `np.array([True, 1, 2]) + np.array([3, 4, False])`의 출력과 일치하는 것을 찾아보세요.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "틀렸습니다. 다른 코드 조각을 시도해 보고 어떤 것이 목표 코드 조각과 일치하는지 확인하십시오."
msg2 = "잘하셨습니다! `True`는 1로 변환되고, `False`는 0으로 변환됩니다."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## NumPy 배열 부분 추출하기

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

리스트나 배열에 대괄호를 사용하는 부분 추출 방식은 리스트와 배열 모두에서 동일하게 작동합니다.

이 연습 문제에는 MLB 선수들의 키와 몸무게를 일반 리스트처럼 담은 `height_in`과 `weight_lb`가 이미 로드되어 있습니다. 또한 `numpy` 배열인 `np_weight_lb`와 `np_height_in`도 준비되어 있습니다.

`@instructions`
- `np_weight_lb`에서 인덱스 50에 해당하는 요소를 출력하여 부분 추출하세요.
- `np_height_in`에서 **110도 포함하여** 인덱스 100부터 110까지 요소를 담은 부분 배열을 출력하세요.

`@hint`
- `print()` 함수로 부분 추출 연산을 감싸야 합니다.
- `[100:111]`을 사용하면 인덱스 100부터 110까지의 요소를 가져올 수 있습니다.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
```

`@sample_code`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50


# Print out sub-array of np_height_in: index 100 up to and including index 110

```

`@solution`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])
```

`@sct`
```{python}
Ex().has_import("numpy", same_as=False)
msg = "미리 정의된 변수를 변경하거나 제거할 필요가 없습니다."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("좋습니다! 이제 새로운 것을 배울 시간입니다: 2D NumPy 배열!")
```

---

## 2D NumPy 배열

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## 첫 번째 2D NumPy 배열

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

실제 MLB 데이터를 다루기 전에, 먼저 작은 리스트 속의 리스트로 2D `numpy` 배열을 만들어보겠습니다.

이번 연습 문제에서 `baseball`은 리스트 속의 리스트입니다. 메인 리스트에는 4개의 요소가 있으며, 각 요소는 야구 선수 4명의 키와 몸무게를 순서대로 담은 리스트입니다. `baseball`은 이미 스크립트에 작성되어 있습니다.

`@instructions`
- `np.array()`를 사용하여 `baseball`에서 2D `numpy` 배열을 만들고, 이름을 `np_baseball`로 지정하세요.
- `np_baseball`의 타입을 출력하세요.
- `np_baseball.shape`를 사용하여 `np_baseball`의 `shape` 속성을 출력하세요.

`@hint`
- `baseball`은 이미 스크립트에 작성되어 있습니다. `np.array()`를 호출하여 2D `numpy` 배열을 만들고 `np_baseball`에 저장하세요.
- 두 번째 지침에서는 `print()`와 `type()`을 함께 사용하세요.
- `np_baseball.shape`를 사용하면 `np_baseball`의 차원을 확인할 수 있습니다. 반드시 `print()`로 감싸서 출력하세요.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball


# Print out the type of np_baseball


# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
msg = "미리 정의된 변수를 변경하거나 제거할 필요가 없습니다."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().has_import("numpy", same_as=False)

Ex().check_correct(
    multi(
        has_printout(0),
        has_printout(1)
    ),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("훌륭합니다! 이제 실제 MLB 데이터를 2D `numpy` 배열로 변환할 준비가 되었습니다!")
```

---

## 야구 데이터를 2D 형태로 바꾸기

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

여러분은 모든 정보를 2D `numpy` 배열로 재구성하는 것이 더 효율적이라는 것을 알게 되었습니다.

현재 Python 리스트 속의 리스트 형태로 데이터가 준비되어 있습니다. 각 하위 리스트는 야구 선수 한 명의 키와 몸무게를 나타냅니다. 이 리스트의 이름은 `baseball`이며, 이미 로드되어 있습니다(화면에는 보이지 않지만 사용 가능합니다).

데이터를 2D 배열로 저장하여 `numpy`의 추가 기능을 활용하세요.

`@instructions`
- `np.array()`를 사용하여 `baseball`로 2D `numpy` 배열을 만들고, 이름을 `np_baseball`로 지정하세요.
- `np_baseball`의 `shape` 속성을 출력하세요.

`@hint`
- `baseball`은 이미 Python 환경에서 이용 가능합니다. 이 리스트로 `np.array()`를 호출하여 2D `numpy` 배열을 만들고, 결과를 `np_baseball`에 저장하세요.
- `np_baseball.shape`를 사용하면 `np_baseball`의 차원을 확인할 수 있습니다. `print()` 함수로 감싸서 출력하세요.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = 

# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    has_printout(0),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("멋집니다! 이제 다차원 `numpy` 배열의 멋진 기능을 자랑할 시간입니다!")
```

---

## 2D NumPy 배열 부분 추출하기

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

2D `numpy` 배열이 규칙적인 구조를 가져, 각 행과 열의 값 개수가 일정하다면, 복잡한 부분 추출 작업도 매우 간단해집니다. 아래 코드에서 리스트 속의 리스트에서 추출된 요소 `"a"`와 `"c"`를 확인하세요.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

쉼표 앞의 인덱스는 행을, 쉼표 뒤의 인덱스는 열을 나타냅니다. `:`는 슬라이싱에 사용되며, 여기서는 모든 행을 포함하라는 의미입니다.

`@instructions`
- `np_baseball`의 50번째 행을 출력하세요.
- `np_baseball`의 두 번째 열 전체를 담은 새 변수 `np_weight_lb`를 만드세요.
- `np_baseball`에서 124번째 야구 선수의 키(첫 번째 열)를 선택하여 출력하세요.

`@hint`
- 첫 번째 지침에서는 행 인덱스 49가 필요합니다! 구체적으로는 `[49, :]`를 사용하면 됩니다.
- 두 번째 열 전체를 선택하려면 `[:, 1]`을 사용하세요.
- 마지막 지침에서는 `[123, 0]`을 사용하세요. 전체를 `print()` 문으로 감싸는 것을 잊지 마세요.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball


# Select the entire second column of np_baseball: np_weight_lb


# Print out height of 124th player

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])
```

`@sct`
```{python}
msg = "미리 정의된 변수를 변경하거나 제거할 필요가 없습니다."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "`np_baseball[:,1]`을 사용하여 `np_weight_lb`를 정의할 수 있습니다. 이렇게 하면 첫 번째 열 전체가 선택됩니다.")

Ex().has_printout(1)

success_msg("잘 진행되고 있습니다!")
```

---

## 2D 산술 연산

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

2D `numpy` 배열도 일반 `numpy` 배열과 마찬가지로 요소별 계산을 수행할 수 있습니다.

키(인치), 몸무게(파운드), 나이(년)를 나타내는 3개의 열로 구성된 2D `numpy` 배열 `np_baseball`은 이미 작성되어 있습니다. `baseball`은 일반적인 리스트 속의 리스트로, `updated`는 2D numpy 배열로 제공됩니다.

`@instructions`
- 모든 야구 선수의 키, 몸무게, 나이 변화 데이터를 구했습니다. 이 데이터는 2D `numpy` 배열인 `updated`로 제공됩니다. `np_baseball`과 `updated`를 더한 후 결과를 출력하세요.
- 키와 몸무게 단위를 미터법(각각 미터와 킬로그램)으로 변환하려고 합니다. 우선, `0.0254`, `0.453592`, `1` 세 값을 담은 `numpy` 배열을 생성하고 `conversion`이라는 이름을 붙이세요.
- `np_baseball`에 `conversion`을 곱한 후 결과를 출력하세요.

`@hint`
- `np_baseball + updated`를 사용해 두 `numpy` 배열의 요소별 합을 계산할 수 있습니다.
- `np.array()`로 `numpy` 배열을 생성하세요. 입력값은 세 개의 요소로 구성된 일반 Python 리스트입니다.
- `np_baseball * conversion`은 별도의 추가 작업 없이 바로 동작합니다. 직접 시도해 보세요! `print()` 함수로 감싸는 것을 잊지 마세요.

`@pre_exercise_code`
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("https://assets.datacamp.com/course/intro_to_python/update.csv", header = None))
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated


# Create numpy array: conversion


# Print out product of np_baseball and conversion

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```

`@sct`
```{python}
Ex().has_import("numpy")

msg = "미리 정의된 변수를 변경하거나 제거할 필요가 없습니다."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("잘하셨습니다! 아주 적은 코드로 `numpy` 데이터 구조의 모든 값을 매우 구체적인 방식으로 변경할 수 있다는 점에 주목하세요. 이는 데이터 과학자로서의 미래에 매우 유용할 것입니다!")
```

---

## NumPy: 기초 통계

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## 평균값 vs 중앙값

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

`numpy` 함수를 활용해 데이터를 더 잘 파악하는 방법을 배웠습니다.

야구 데이터는 3개의 열(키, 몸무게, 나이)과 1015개의 행으로 구성된 2D `numpy` 배열로 제공됩니다. 이 `numpy` 배열의 이름은 `np_baseball`입니다. 그런데 데이터를 재구성하다 보니, 일부 키 값이 비정상적으로 높다는 것을 발견했습니다. 아래 지침을 따라, _이상치_가 있을 때 어떤 요약 통계가 가장 적합한지 알아보세요. `np_baseball`을 사용할 수 있습니다.

`@instructions`
- `np_baseball`의 첫 번째 열과 동일한  `numpy` 배열 `np_height_in`을 만드세요.
- `np_height_in`의 평균값을 출력하세요.
- `np_height_in`의 중앙값을 출력하세요.

`@hint`
- 2D `numpy` 부분 추출을 이용하세요. `[:,0]`은 정답의 일부입니다.
- `numpy`를 `np`로 가져왔다면, `np.mean()`을 사용해 NumPy 배열의 평균을 구할 수 있습니다. `print()` 호출도 잊지 마세요.
- 마지막 지침에서는 `np.median()`을 사용하세요.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create np_height_in from np_baseball


# Print out the mean of np_height_in


# Print out the median of np_height_in

```

`@solution`
```{python}
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "`np_baseball[:,0]`을 사용하여 `np_baseball`의 첫 번째 열을 선택할 수 있습니다."),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("평균 키가 1586인치라니, 그게 맞는 소리인가요? 하지만 중앙값은 이상치에 영향을 받지 않는 것 같습니다: 74인치는 완벽하게 이해가 됩니다. 전체 데이터 세트의 분포를 파악하기 위해 중앙값과 평균을 모두 확인하는 것이 항상 좋은 생각입니다.")
```

---

## 야구 데이터 탐색하기

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

평균값과 중앙값이 너무 큰 차이를 보여서 MLB에 문제를 제기했습니다. MLB는 오류를 발견하고 수정된 데이터를 보내왔습니다. 데이터는 세 개의 열을 가진 2D NumPy 배열 `np_baseball`로 다시 제공됩니다.

편집기의 Python 스크립트에는 다양한 요약 통계와 정보성 메시지를 출력하는 코드가 포함되어 있으며, `numpy`는 `np`로 불러온 상태입니다. 나머지 코드를 완성해 보세요! `np_baseball`을 사용할 수 있습니다.

`@instructions`
- 평균 키를 출력하는 코드는 이미 포함되어 있습니다. 키의 중앙값을 계산하는 코드를 완성하세요.
- `np_baseball`의 첫 번째 열에 `np.std()`를 적용해 `stddev`를 계산하세요.
- 키가 큰 선수가 더 무거운 경향이 있을까요? `np.corrcoef()`를 사용해 `np_baseball`의 첫 번째 열과 두 번째 열의 상관관계를 `corr`에 저장하세요.

`@hint`
- `np.median()`를 사용해 중앙값을 계산하세요. 먼저 올바른 열을 선택했는지 확인하세요!
- 동일한 열을 선택해 `np.std()`로 표준 편차를 계산하세요.
- `np_baseball[:, 0]`과 `np_baseball[:, 1]`을 사용해 첫 번째와 두 번째 열을 선택하세요. 이 두 열이 `np.corrcoef()`의 입력값입니다.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
import numpy as np
```

`@sample_code`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = ____
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = ____
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = ____
print("Correlation: " + str(corr))
```

`@solution`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

`@sct`
```{python}
msg = "미리 정의된 `avg` 변수를 변경하거나 제거하지 마십시오."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "`np.median()`을 사용하여 중앙값을 계산하셨습니까?"
incorrect = "`med`를 계산하려면 `np_baseball`의 첫 번째 열을 `numpy.median()`에 전달하십시오. `np.mean()`의 예시를 참고하십시오."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "`np.std()`를 사용하여 표준 편차를 계산하셨습니까?"
incorrect = "`stddev`를 계산하려면 `np_baseball`의 첫 번째 열을 `numpy.std()`에 전달하십시오. `np.mean()`의 예시를 참고하십시오."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "`np.corrcoef()`을 사용하여 상관관계를 계산하셨습니까?"
incorrect1 = "`corr`를 계산하려면 `np.corrcoef()`의 첫 번째 인수로 `np_baseball`의 첫 번째 열을 사용해야 합니다. 이전에 했던 것과 유사합니다."
incorrect2 = "`corr`를 계산하려면 `np.corrcoef()`의 두 번째 인수로 `np_baseball`의 두 번째 열을 사용해야 합니다. 이번에는 `[:,0]` 대신 `[:,1]`을 사용하십시오."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("훌륭합니다! 견고한 기초를 쌓으셨습니다 - 이제 새로운 데이터 과학 기술을 사용하여 더 많은 도전을 해결하고 영향을 미칠 때입니다.")
```
