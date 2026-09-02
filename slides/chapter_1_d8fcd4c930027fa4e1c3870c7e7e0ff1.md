---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ko-KR/2b91589c-8b9f-420d-b865-11b89ba40824-281e836e0b043a21ee4b048844e868fb.mp3
---

## Python 시작하기!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
안녕하세요, 저는 데이터 과학을 위한 Python 입문 과정을 진행할 휴고입니다.

DataCamp에서 데이터 과학자이자 강사로 일하고 있습니다.

---

## 학습 방법

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp 인터페이스](https://assets.datacamp.com/img/translations/ko-KR/q2/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.jpg)

`@script`
이 강의에서는 지금 보시는 것과 같은 영상 강의와 대화형 연습을 통해 데이터 과학을 위한 Python을 배우게 됩니다. 각자 Python 세션을 제공받아 직접 시도해 보면서 지시사항에 맞는 올바른 코드를 작성해 볼 수 있습니다. 직접 해 보면서 배우고, 즉각적인 맞춤형 피드백도 받게 되죠.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38) {{1}}

- 범용: 무엇이든 만들 수 있음{{2}}

- 오픈 소스, 무료 이용{{3}}

- 다양한 패키지 활용 가능(데이터 과학 분야 포함){{4}}

	- 수많은 분야에 다양하게 응용{{5}}

`@script`
Python의 창시자는 귀도 반 로섬입니다. 이건 저와 귀도가 함께 찍은 사진입니다. Python은 취미 프로젝트로 시작해서 범용 프로그래밍 언어로까지 발전했죠. 요즘은 Python을 사용하여 거의 모든 종류의 소프트웨어를 만들 수 있습니다. 왜냐하면 Python은 오픈 소스라서 무료로 사용할 수 있기 때문입니다. 그리고 Python에서는 패키지를 아주 쉽게 만들 수 있기 때문이죠. 패키지는 특정 문제를 해결하기 위해 다른 사람들과 공유할 수 있는 코드입니다. 오랜 시간 동안 데이터 과학에 특화된 패키지가 점점 더 많이 개발되었죠. 여러분이 회사 매출을 멋진 시각 자료로 보여주고 싶다고 가정해 봅시다. 여기에 딱 알맞은 패키지가 있습니다. 센서 측정값을 분석하기 위해 데이터베이스에 연결하고 싶다면 어떨까요? 이때 사용할 수 있는 패키지도 여기에 있습니다.
Python은 거의 모든 것을 할 수 있기 때문에 프로그래밍 언어계의 맥가이버 칼이라고도 불립니다.
이 강의에서는 데이터 과학 코딩 실력을 차근차근 쌓아갈 수 있습니다. 마지막까지 함께하며 Python이 얼마나 강력한 언어인지 함께 알아볼까요?

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Python 명령 실행하기**

![ipython_shell.png](https://assets.datacamp.com/img/translations/ko-KR/q2/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg = 95)

`@script`
이제 Python에 완전히 빠져든 것 같으니 실습을 시작해 봅시다. 저는 Python 셸로 시작하겠습니다.

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Python 명령 실행하기**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/ko-KR/q2/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python 셸은 Python 코드를 입력하고 즉시 결과를 확인할 수 있는 공간입니다. DataCamp의 연습 인터페이스에서 셸의 위치는 이곳입니다. 가볍게 시작해 보죠. Python을 계산기로 쓰겠습니다.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
 

![DataCamp의 IPython 셸에서의 계산](https://assets.datacamp.com/img/translations/ko-KR/q2/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.jpg = 95)

`@script`
4 더하기 5를 입력하고 엔터를 누릅니다. Python은 입력한 내용을 해석해서 계산 결과인 9를 출력합니다. 여기서 사용한 Python 셸은 오리지널 버전이 아닙니다. 대화형 인터프리터인 '인터랙티브 Python'으로, 일반 Python의 업그레이드 버전인데 나중에 유용하게 쓰일 겁니다.

인터랙티브 Python은 페르난도 페레스가 만들었으며, 주피터라는 더 큰 생태계에 속해있습니다. 대화식으로 Python을 사용하는 것 외에도, Python을 통해서 소위 말하는

---

## Python 스크립트

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- 텍스트 파일 - `.py`{{1}}

- Python 명령어 리스트{{2}}

- IPython Shell에 입력하는 것과 유사함{{3}}

![DataCamp의 Python 스크립트](https://assets.datacamp.com/img/translations/ko-KR/q2/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78) {{3}}

`@script`
Python 스크립트도 실행할 수 있죠. 이 Python 스크립트는 단순히 확장자가 py인 텍스트 파일입니다. 쉽게 말하면 Python 명령어 목록인데요. 직접 셸에 한 줄씩 명령어를 입력하는 것처럼 실행됩니다

---

## Python 스크립트

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: 스크립트에 4+5를 입력하고 답안 제출을 누르는 모습. 출력이 표시되지 않습니다.](https://assets.datacamp.com/img/translations/ko-KR/q2/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.jpg = 95)

`@script`
이제 앞에서 본 명령어를 스크립트에 넣어보죠. 스크립트는 DataCamp 인터페이스에서 확인할 수 있습니다. 다음 단계로 '답안 제출하기'를 클릭해 스크립트를 실행합니다. 스크립트를 DataCamp 인터페이스에서 실행해도 출력 창에는 아무것도 나타나지 않습니다. 실행 중에 결과를 출력하려면 스크립트 내에서 명시적으로 print를 사용해야 하기 때문입니다.

---

## Python 스크립트

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/ko-KR/q2/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.jpg = 95)

- 스크립트에서 결과를 출력하려면 `print()`를 사용하세요

`@script`
앞에서 했던 계산을 print로 감싸고, 스크립트를 다시 실행해 봅시다. 이번에는 전과 동일하게 출력되었습니다. 좋았어요! 인터랙티브 방식으로 모든 단계를 직접 입력하는 대신, 코드를 Python 스크립트에 작성해서 구조를 유지할 수 있습니다. 또한, 내용을 변경할 때에도 모든 내용을 매번 다시 입력할 필요가 없습니다. 스크립트에서 변경하고 전체를 다시 실행하기만 하면 되죠.

---

## DataCamp 인터페이스

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCamp 인터페이스의 스크린 샷](https://assets.datacamp.com/img/translations/ko-KR/q2/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg)

`@script`
이제 Python으로 작업하는 다양한 방법을 알게 되었으니, 연습 문제로 넘어가 보겠습니다. 실습할 때는 IPython Shell을 사용하고, 실제 답안을 코딩할 때는 Python 스크립트 편집기를 사용하세요. '답안 제출하기'를 클릭하면 스크립트가 실행되어 정답 여부를 확인할 수 있습니다.

---

## 연습해봅시다!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
그럼 즐겁게 코딩을 배워 볼까요?
