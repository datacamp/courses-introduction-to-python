---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ko-KR/3bdff5dc-33ba-4fcf-9db4-4075a4e831b8.mp3
---

## 파이썬에 오신 것을 환영합니다!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
안녕하세요, 저는 휴고이고, 이번 데이터 사이언스를 위한 파이썬 입문 과정의 진행을 맡았습니다.

저는 DataCamp의 데이터 사이언티스트이자 교육자입니다.

---

## 학습 방식

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp 인터페이스](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
이 과정에서는 지금 보시는 것 같은 동영상 레슨과 대화형 실습을 통해 데이터 사이언스를 위한 파이썬을 배우게 됩니다. 각자만의 파이썬 세션이 제공되어, 직접 실험하고 지시사항을 해결하는 올바른 코드를 고민해 볼 수 있습니다. 스스로 해 보면서, 작업에 대해 맞춤형 즉시 피드백을 받게 됩니다.

---

## 파이썬

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- 범용: 무엇이든 구축{{2}}

- 오픈 소스, 무료{{3}}

- 데이터 과학용 포함 패키지 풍부{{4}}

	- 다양한 응용 분야{{5}}

`@script`
파이썬은 귀도 반 로섬이 만들었습니다. 여기 보시는 사진은 저와 귀도가 함께 찍은 사진입니다. 취미로 시작한 프로젝트가 곧 범용 프로그래밍 언어로 발전했죠. 오늘날 파이썬으로는 사실상 어떤 소프트웨어든 만들 수 있습니다. 어떻게 가능했을까요? 우선, 파이썬은 오픈 소스이기 때문에 무료로 사용할 수 있습니다. 또, 특정 문제를 해결하기 위해 다른 사람들과 공유할 수 있는 코드 묶음인 패키지를 파이썬에서 매우 쉽게 만들 수 있습니다. 시간이 지나면서, 데이터 사이언스에 특화된 패키지들이 계속 개발되어 왔습니다. 예를 들어, 회사 매출을 멋지게 시각화하고 싶으신가요? 그에 맞는 패키지가 있습니다. 센서 측정을 분석하기 위해 데이터베이스에 연결하고 싶으신가요? 그를 위한 패키지도 있습니다.
사람들은 파이썬으로 거의 모든 것을 할 수 있다는 의미에서, 종종 파이썬을 프로그래밍 언어의 스위스 아미나이프라고 부릅니다.
이 과정에서는 데이터 사이언스 코딩 실력을 조금씩 차근차근 쌓아 갈 것이니, 언어가 얼마나 강력한지 끝까지 함께해 보세요.

---

## IPython 셸

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**파이썬 명령 실행**

![ipython_shell.png](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
이제 파이썬에 집중해 주셨으니, 바로 실험을 시작해 보겠습니다. 먼저

---

## IPython 셸

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**파이썬 명령 실행**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
파이썬 셸부터 볼게요. 여기는 파이썬 코드를 입력하면 즉시 결과를 볼 수 있는 공간입니다. DataCamp의 실습 인터페이스에는 이 셸이 여기처럼 내장되어 있습니다. 간단하게 시작해서, 파이썬을 계산기처럼 써 보겠습니다.

---

## IPython 셸

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![DataCamp의 IPython 셸에서 계산](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
제가 4 + 5를 입력하고 Enter를 누르겠습니다. 파이썬이 입력을 해석해 계산 결과인 9를 출력하죠. 여기서 사용하는 파이썬 셸은 원래 셸이 아니라 IPython입니다. Interactive Python의 줄임말로, 일반 파이썬을 한층 강화한 버전이라서 앞으로 유용하게 쓰이게 됩니다.

IPython은 페르난도 페레스가 만들었고, 더 넓은 주피터 생태계의 일부입니다. 파이썬을 대화형으로 다루는 것 외에도, 이른바

---

## 파이썬 스크립트

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- 텍스트 파일 - `.py`{{1}}

- 파이썬 명령어 목록{{2}}

- IPython 셸에서 타이핑하는 것과 유사{{3}}

![DataCamp의 파이썬 스크립트](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
파이썬 스크립트를 실행할 수도 있습니다. 파이썬 스크립트는 확장자가 .py인 단순한 텍스트 파일입니다. 셸에서 한 줄씩 직접 입력하는 것처럼, 파이썬 명령을 차례대로 실행하는 목록이라고 보시면 됩니다.

---

## 파이썬 스크립트

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: 스크립트에 4 + 5를 입력하고 제출을 누름. 출력은 없음.](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
이제 아까의 명령을 스크립트로 옮겨 보겠습니다. DataCamp 인터페이스에서 여기에서 찾을 수 있어요. 다음 단계는 'Submit Answer'를 클릭해 스크립트를 실행하는 것입니다. DataCamp 인터페이스에서 이 스크립트를 실행하면, 출력 창에 아무 것도 없을 수 있습니다. 스크립트에서 실행 중에 출력을 보려면, 반드시 print를 명시적으로 사용해야 하기 때문입니다.

---

## 파이썬 스크립트

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- 스크립트에서 출력하려면 `print()` 사용

`@script`
이전 계산을 print 호출로 감싸고, 스크립트를 다시 실행해 보겠습니다. 이번에는 아까와 동일한 출력이 생성되네요. 잘됐습니다! 코드를 매번 대화형으로 다시 입력하는 대신 파이썬 스크립트에 넣어 두면, 구조를 유지하고 수정할 때마다 매번 다시 타이핑하는 일을 피할 수 있습니다. 스크립트에서 변경만 하고, 전체를 다시 실행하면 됩니다.

---

## DataCamp 인터페이스

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCamp 인터페이스 스크린샷](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
이제 파이썬을 다루는 여러 방법을 맛보셨으니, 실습으로 넘어가 보세요. 실험에는 IPython 셸을 사용하고, 실제 정답 코드는 파이썬 스크립트 편집기에 작성해 보세요. 'Submit Answer'를 클릭하면 스크립트가 실행되고, 정답 여부가 확인됩니다.

---

## 연습해 봅시다!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
이제 코딩을 시작해 보세요. 그리고 즐기는 것도 잊지 마세요!
