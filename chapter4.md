---
title_meta: บทที่ 4
title: NumPy
description: >-
  NumPy คือแพ็กเกจ Python พื้นฐานสำหรับ Data Science เรียนรู้การทำงานกับ NumPy
  array และเริ่มต้นสำรวจข้อมูลอย่างมีประสิทธิภาพ
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: NumPy Array 2 มิติ
  - nb_of_exercises: 3
    title: 'NumPy: สถิติเบื้องต้น'
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

## NumPy Array แรกของคุณ

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

ในบทนี้จะพาคุณเข้าสู่โลกของเบสบอล พร้อมกับทำความคุ้นเคยกับพื้นฐานของ `numpy` ซึ่งเป็นแพ็กเกจที่ทรงพลังสำหรับการทำ data science

มีการกำหนดลิสต์ `baseball` ไว้ใน Python script แล้ว โดยเก็บข้อมูลความสูงของนักเบสบอลบางคนในหน่วยเซนติเมตร ลองเพิ่มโค้ดเพื่อสร้าง `numpy` array จากลิสต์นี้ดูสิ

`@instructions`
- Import แพ็กเกจ `numpy` ในชื่อ `np` เพื่อให้อ้างอิง `numpy` ผ่าน `np` ได้
- ใช้ `np.array()` เพื่อสร้าง `numpy` array จาก `baseball` แล้วตั้งชื่อ array นี้ว่า `np_baseball`
- แสดงชนิดของ `np_baseball` เพื่อตรวจสอบว่าได้ผลลัพธ์ที่ถูกต้อง

`@hint`
- `import numpy as np` จะช่วยได้ จากนั้นใช้ `np.fun_name()` ทุกครั้งที่ต้องการเรียกใช้ฟังก์ชันของ `numpy`
- `np.array()` รับ `baseball` เป็น input แล้วกำหนดผลลัพธ์ให้กับตัวแปร `np_baseball`
- หากต้องการแสดงชนิดของตัวแปร `x` ให้พิมพ์ `print(type(x))`

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
predef_msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปรที่กำหนดไว้ล่วงหน้า"
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("ทำได้ดีมาก!")
```

---

## ความสูงของนักเบสบอล

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

สมมติว่าคุณเป็นแฟนเบสบอลตัวยง และตัดสินใจติดต่อ MLB (Major League Baseball) เพื่อขอข้อมูลสถิติเพิ่มเติมเกี่ยวกับความสูงของนักกีฬา ทาง MLB ส่งข้อมูลของนักกีฬามากกว่าหนึ่งพันคนมาให้ ซึ่งเก็บอยู่ในรูปแบบ Python list ธรรมดาชื่อ `height_in` โดยความสูงมีหน่วยเป็นนิ้ว ลองแปลงข้อมูลนี้เป็น `numpy` array แล้วเปลี่ยนหน่วยเป็นเมตรกัน

`height_in` พร้อมใช้งานแล้ว และได้โหลดแพ็กเกจ `numpy` ไว้เรียบร้อย สามารถเริ่มได้เลย (ที่มา: stat.ucla.edu)

`@instructions`
- สร้าง `numpy` array จาก `height_in` แล้วตั้งชื่อ array ใหม่นี้ว่า `np_height_in`
- แสดงผล `np_height_in`
- คูณ `np_height_in` ด้วย `0.0254` เพื่อแปลงความสูงทั้งหมดจากนิ้วเป็นเมตร แล้วเก็บค่าใหม่ไว้ใน array ชื่อ `np_height_m`
- แสดงผล `np_height_m` และตรวจสอบว่าผลลัพธ์สมเหตุสมผลหรือไม่

`@hint`
- ใช้ `np.array()` โดยส่ง `height` เข้าไป แล้วเก็บผลลัพธ์ไว้ในตัวแปร `np_height_in`
- หากต้องการแสดงผลตัวแปร `x` ให้พิมพ์ `print(x)` ในสคริปต์ Python
- คำนวณโดยใช้ `np_height_in` เหมือนกับตัวเลขธรรมดา เช่น `np_height_in * conversion_factor` เป็นส่วนหนึ่งของคำตอบ
- หากต้องการแสดงผลตัวแปร `x` ให้พิมพ์ `print(x)` ในสคริปต์ Python

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "ใช้ `np_height_in * 0.0254` เพื่อคำนวณ `np_height_m`")
)

success_msg("ยอดเยี่ยม! ในพริบตาเดียว `numpy` ทำการคูณข้อมูลความสูงมากกว่า 1,000 รายการ")
```

---

## ผลข้างเคียงของ NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` เหมาะมากสำหรับการคำนวณแบบเวกเตอร์ อย่างไรก็ตาม เมื่อเปรียบเทียบกับ list ทั่วไปของ Python จะพบว่ามีบางอย่างที่แตกต่างกัน

ประการแรก array ของ `numpy` ไม่สามารถมีองค์ประกอบที่ต่างชนิดกันได้ หากผสมชนิดข้อมูล เช่น boolean กับ integer `numpy` จะแปลงให้เป็นชนิดเดียวกันโดยอัตโนมัติ โดย boolean อย่าง `True` และ `False` จะถูกแทนด้วย `1` และ `0` เมื่อนำไปใช้ร่วมกับตัวเลข ทำให้ array กลายเป็น integer

ประการที่สอง ตัวดำเนินการทางคณิตศาสตร์ทั่วไป เช่น `+`, `-`, `*` และ `/` มีความหมายต่างกันสำหรับ list ของ Python กับ array ของ `numpy`

เลือกโค้ดที่ให้ผลลัพธ์ตรงกับข้อต่อไปนี้:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

แพ็กเกจ `numpy` ถูก import ไว้แล้วในชื่อ `np` สามารถรันแต่ละตัวเลือกใน IPython Shell เพื่อตรวจสอบผลลัพธ์ได้

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- คัดลอกโค้ดแต่ละส่วนแล้ววางใน IPython Shell จากนั้นกด **Enter** เพื่อรันโค้ดและดูว่าผลลัพธ์ใดตรงกับที่ได้จาก `np.array([True, 1, 2]) + np.array([3, 4, False])`

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "ไม่ถูกต้อง ลองดูโค้ดแต่ละส่วนและดูว่าส่วนใดตรงกับโค้ดเป้าหมาย"
msg2 = "ยอดเยี่ยมมาก! `True` จะถูกแปลงเป็น 1 และ `False` จะถูกแปลงเป็น 0"
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## การ Subset อาร์เรย์ NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

การ Subset (การใช้วงเล็บก้ามปูกับลิสต์หรืออาร์เรย์) ทำงานเหมือนกันทุกประการทั้งกับลิสต์และอาร์เรย์

ในแบบฝึกหัดนี้มีลิสต์สองรายการที่โหลดไว้ให้แล้วในเบื้องหลัง ได้แก่ `height_in` และ `weight_lb` ซึ่งเก็บข้อมูลส่วนสูงและน้ำหนักของนักเบสบอล MLB ในรูปแบบลิสต์ธรรมดา นอกจากนี้ยังมีอาร์เรย์ `numpy` สองตัวที่เตรียมไว้ให้ คือ `np_weight_lb` และ `np_height_in`

`@instructions`
- Subset `np_weight_lb` โดยพิมพ์ค่าที่ index 50 ออกมา
- พิมพ์ sub-array ของ `np_height_in` ที่ประกอบด้วยค่าตั้งแต่ index 100 จนถึง index 110 (**รวม** index 110 ด้วย)

`@hint`
- ตรวจสอบว่าครอบคำสั่ง `print()` ไว้รอบการดำเนินการ subsetting แล้ว
- ใช้ `[100:111]` เพื่อดึงข้อมูลตั้งแต่ index 100 จนถึง index 110 (รวม index 110 ด้วย)

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
msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปรที่กำหนดไว้ล่วงหน้า"
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("ยอดเยี่ยม! ถึงเวลาเรียนรู้สิ่งใหม่: NumPy arrays แบบ 2 มิติ!")
```

---

## NumPy Arrays แบบ 2 มิติ

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## NumPy Array 2 มิติแรกของคุณ

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

ก่อนจะทำงานกับข้อมูล MLB จริง มาลองสร้าง `numpy` array 2 มิติจากลิสต์ขนาดเล็กกันก่อน

ในแบบฝึกหัดนี้ `baseball` คือลิสต์ของลิสต์ โดยลิสต์หลักมี 4 สมาชิก แต่ละสมาชิกเป็นลิสต์ที่เก็บส่วนสูงและน้ำหนักของนักเบสบอล 4 คน ตามลำดับนั้น `baseball` ถูกกำหนดไว้ในสคริปต์ให้แล้ว

`@instructions`
- ใช้ `np.array()` เพื่อสร้าง `numpy` array 2 มิติจาก `baseball` แล้วตั้งชื่อว่า `np_baseball`
- แสดงประเภทของ `np_baseball` ด้วย `print()`
- แสดง attribute `shape` ของ `np_baseball` โดยใช้ `np_baseball.shape`

`@hint`
- `baseball` ถูกกำหนดไว้ในสคริปต์แล้ว ให้เรียกใช้ `np.array()` กับตัวแปรนี้ แล้วเก็บผลลัพธ์ที่เป็น `numpy` array 2 มิติไว้ในตัวแปร `np_baseball`
- ใช้ `print()` ร่วมกับ `type()` สำหรับคำสั่งที่สอง
- `np_baseball.shape` จะแสดงขนาดของ `np_baseball` อย่าลืมครอบด้วย `print()`

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
msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปรที่กำหนดไว้ล่วงหน้า"
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
Ex().has_import("numpy", same_as = False)

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

success_msg("ยอดเยี่ยม! ตอนนี้คุณพร้อมที่จะแปลงข้อมูล MLB จริงให้เป็น `numpy` array แบบ 2 มิติแล้ว!")
```

---

## ข้อมูลเบสบอลในรูปแบบ 2 มิติ

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

การจัดเก็บข้อมูลทั้งหมดใน `numpy` array แบบ 2 มิติจะทำให้จัดการข้อมูลได้สะดวกกว่า

ตอนนี้มี Python list ของ list อยู่แล้ว โดยแต่ละ sublist เก็บข้อมูลส่วนสูงและน้ำหนักของนักเบสบอลหนึ่งคน list นี้มีชื่อว่า `baseball` และถูกโหลดไว้ให้แล้ว (แม้จะมองไม่เห็นในโค้ด)

เก็บข้อมูลนี้ในรูปแบบ array 2 มิติ เพื่อใช้ฟีเจอร์เพิ่มเติมของ `numpy` ได้อย่างเต็มที่

`@instructions`
- ใช้ `np.array()` เพื่อสร้าง `numpy` array 2 มิติ จาก `baseball` แล้วตั้งชื่อว่า `np_baseball`
- แสดงค่า attribute `shape` ของ `np_baseball`

`@hint`
- `baseball` ถูกโหลดไว้ในสภาพแวดล้อม Python แล้ว ให้เรียกใช้ `np.array()` กับ `baseball` แล้วเก็บผลลัพธ์ที่ได้เป็น `numpy` array 2 มิติ ในตัวแปรชื่อ `np_baseball`
- `np_baseball.shape` จะแสดงขนาดของ `np_baseball` อย่าลืมครอบด้วย `print()`

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

success_msg("ยอดเยี่ยม! ถึงเวลาแสดงคุณสมบัติเด่นของอาร์เรย์ `numpy` แบบหลายมิติกันแล้ว!")
```

---

## การ Subset อาร์เรย์ NumPy แบบ 2 มิติ

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

หาก `numpy` array แบบ 2 มิติของคุณมีโครงสร้างที่สม่ำเสมอ กล่าวคือแต่ละแถวและคอลัมน์มีจำนวนค่าคงที่ การ subset ที่ซับซ้อนก็จะทำได้ง่ายมาก ลองดูโค้ดด้านล่างที่ดึงค่า `"a"` และ `"c"` ออกจาก list of lists

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

index ก่อนเครื่องหมายจุลภาคหมายถึงแถว ส่วน index หลังเครื่องหมายจุลภาคหมายถึงคอลัมน์ `:` ใช้สำหรับการ slice ซึ่งในตัวอย่างนี้หมายความว่าให้เลือกทุกแถว

`@instructions`
- แสดงผลแถวที่ 50 ของ `np_baseball`
- สร้างตัวแปรใหม่ชื่อ `np_weight_lb` โดยเก็บข้อมูลคอลัมน์ที่สองทั้งหมดของ `np_baseball`
- เลือกค่าความสูง (คอลัมน์แรก) ของนักเบสบอลคนที่ 124 ใน `np_baseball` แล้วแสดงผลออกมา

`@hint`
- สำหรับคำสั่งแรก ต้องใช้ index แถวที่ 49 โดยเฉพาะคือ `[49, :]`
- หากต้องการเลือกคอลัมน์ที่สองทั้งหมด ให้ใช้ `[:, 1]`
- สำหรับคำสั่งสุดท้าย ใช้ `[123, 0]` และอย่าลืมครอบด้วย `print()`

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
msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปรที่กำหนดไว้ล่วงหน้า"
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "คุณสามารถใช้ `np_baseball[:,1]` เพื่อกำหนด `np_weight_lb` ซึ่งจะเลือกคอลัมน์แรกทั้งหมด")

Ex().has_printout(1)

success_msg("สิ่งนี้ดำเนินไปได้ด้วยดี!")
```

---

## 2D Arithmetic

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

`numpy` array แบบ 2 มิติสามารถคำนวณแบบ element-wise ได้เช่นเดียวกับ `numpy` array ทั่วไป

`np_baseball` ถูกเขียนโค้ดไว้ให้แล้ว เป็น `numpy` array แบบ 2 มิติที่มี 3 คอลัมน์ ได้แก่ ส่วนสูง (หน่วยนิ้ว) น้ำหนัก (หน่วยปอนด์) และอายุ (หน่วยปี) `baseball` มีให้ในรูปแบบ list of lists ปกติ และ `updated` มีให้ในรูปแบบ 2D numpy array

`@instructions`
- คุณได้รับข้อมูลการเปลี่ยนแปลงด้านส่วนสูง น้ำหนัก และอายุของนักเบสบอลทุกคน ซึ่งเก็บอยู่ใน `numpy` array แบบ 2 มิติชื่อ `updated` ให้บวก `np_baseball` กับ `updated` แล้วแสดงผลลัพธ์
- ต้องการแปลงหน่วยของส่วนสูงและน้ำหนักเป็นหน่วยเมตริก (เมตร และกิโลกรัม ตามลำดับ) เริ่มต้นด้วยการสร้าง `numpy` array ที่มีค่าสามค่า ได้แก่ `0.0254`, `0.453592` และ `1` แล้วตั้งชื่อ array นี้ว่า `conversion`
- คูณ `np_baseball` กับ `conversion` แล้วแสดงผลลัพธ์

`@hint`
- `np_baseball + updated` จะทำการบวกแบบ element-wise ระหว่าง `numpy` array ทั้งสอง
- สร้าง `numpy` array ด้วย `np.array()` โดยใส่ Python list ธรรมดาที่มีสามสมาชิกเป็น input
- `np_baseball * conversion` ใช้งานได้เลยโดยไม่ต้องปรับแต่งเพิ่มเติม ลองดูได้เลย และอย่าลืมครอบด้วย `print()`

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

msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปรที่กำหนดไว้ล่วงหน้า"
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("ยอดเยี่ยมมาก! สังเกตว่าด้วยโค้ดเพียงเล็กน้อย คุณสามารถเปลี่ยนแปลงค่าทั้งหมดในโครงสร้างข้อมูล `numpy` ของคุณได้อย่างเฉพาะเจาะจง ซึ่งจะเป็นประโยชน์อย่างมากในอนาคตของคุณในฐานะนักวิทยาศาสตร์ข้อมูล!")
```

---

## NumPy: สถิติเบื้องต้น

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## ค่าเฉลี่ยเทียบกับมัธยฐาน

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

ตอนนี้รู้วิธีใช้ฟังก์ชันของ `numpy` เพื่อทำความเข้าใจข้อมูลได้ดียิ่งขึ้นแล้ว

ข้อมูลเบสบอลถูกเก็บไว้ในรูปแบบ `numpy` array 2 มิติ ที่มี 3 คอลัมน์ (ส่วนสูง น้ำหนัก อายุ) และ 1015 แถว โดยชื่อของ `numpy` array นี้คือ `np_baseball` อย่างไรก็ตาม หลังจากจัดโครงสร้างข้อมูลใหม่แล้ว พบว่าค่าส่วนสูงบางรายการสูงผิดปกติ ทำตามคำแนะนำด้านล่างเพื่อดูว่าสถิติสรุปแบบใดเหมาะสมที่สุดเมื่อต้องรับมือกับสิ่งที่เรียกว่า _outliers_ โดย `np_baseball` พร้อมใช้งานแล้ว

`@instructions`
- สร้าง `numpy` array ชื่อ `np_height_in` ให้มีค่าเท่ากับคอลัมน์แรกของ `np_baseball`
- แสดงค่าเฉลี่ยของ `np_height_in`
- แสดงค่ามัธยฐานของ `np_height_in`

`@hint`
- ใช้การ subset แบบ 2 มิติของ `numpy`: `[:,0]` เป็นส่วนหนึ่งของคำตอบ
- หาก `numpy` ถูก import มาในชื่อ `np` สามารถใช้ `np.mean()` เพื่อหาค่าเฉลี่ยของ NumPy array ได้ อย่าลืมใส่ `print()` ด้วย
- สำหรับคำแนะนำข้อสุดท้าย ให้ใช้ `np.median()`

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "คุณสามารถใช้ `np_baseball[:,0]` เพื่อเลือกคอลัมน์แรกจาก `np_baseball` ได้"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("ค่าเฉลี่ยของความสูงที่ 1586 นิ้วนั้นดูไม่ถูกต้องใช่ไหม? อย่างไรก็ตาม ค่ามัธยฐานดูเหมือนจะไม่ได้รับผลกระทบจากค่าผิดปกติ: 74 นิ้วนั้นสมเหตุสมผลอย่างยิ่ง การตรวจสอบทั้งค่ามัธยฐานและค่าเฉลี่ยถือเป็นแนวทางที่ดีเสมอ เพื่อให้ทราบถึงการกระจายโดยรวมของชุดข้อมูลทั้งหมด")
```

---

## สำรวจข้อมูลเบสบอล

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

เนื่องจากค่าเฉลี่ยและค่ามัธยฐานต่างกันมาก คุณจึงร้องเรียนไปยัง MLB ทาง MLB พบข้อผิดพลาดและส่งข้อมูลที่แก้ไขแล้วมาให้ ข้อมูลนี้อยู่ในรูปแบบ NumPy array 2 มิติชื่อ `np_baseball` ซึ่งมีสามคอลัมน์

สคริปต์ Python ในตัวแก้ไขมีโค้ดสำหรับแสดงข้อความสรุปสถิติต่าง ๆ อยู่แล้ว และได้โหลด `numpy` เป็น `np` ไว้เรียบร้อยแล้ว ลองเขียนโค้ดส่วนที่เหลือให้สมบูรณ์ดูสิ โดย `np_baseball` พร้อมใช้งานแล้ว

`@instructions`
- โค้ดสำหรับแสดงค่าเฉลี่ยส่วนสูงมีอยู่แล้ว เขียนโค้ดสำหรับค่ามัธยฐานของส่วนสูงให้ครบ
- ใช้ `np.std()` กับคอลัมน์แรกของ `np_baseball` เพื่อคำนวณ `stddev`
- ผู้เล่นที่ตัวใหญ่กว่ามักจะหนักกว่าด้วยหรือเปล่า ใช้ `np.corrcoef()` เพื่อเก็บค่าความสัมพันธ์ระหว่างคอลัมน์แรกและคอลัมน์ที่สองของ `np_baseball` ไว้ใน `corr`

`@hint`
- ใช้ `np.median()` เพื่อคำนวณค่ามัธยฐาน อย่าลืมเลือกคอลัมน์ที่ถูกต้องก่อน!
- เลือกคอลัมน์เดียวกันเมื่อคำนวณค่าเบี่ยงเบนมาตรฐานด้วย `np.std()`
- ใช้ `np_baseball[:, 0]` และ `np_baseball[:, 1]` เพื่อเลือกคอลัมน์แรกและคอลัมน์ที่สอง ซึ่งเป็น input ของ `np.corrcoef()`

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
msg = "คุณไม่ควรเปลี่ยนแปลงหรือลบตัวแปร `avg` ที่กำหนดไว้ล่วงหน้า"
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "คุณได้ใช้ `np.median()` เพื่อคำนวณค่ามัธยฐานหรือไม่?"
incorrect = "ในการคำนวณ `med` ให้ส่งคอลัมน์แรกของ `np_baseball` ไปยัง `numpy.median()` ตัวอย่างของ `np.mean()` แสดงให้เห็นวิธีการดำเนินการ"
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "คุณได้ใช้ `np.std()` เพื่อคำนวณส่วนเบี่ยงเบนมาตรฐานหรือไม่?"
incorrect = "ในการคำนวณ `stddev` ให้ส่งคอลัมน์แรกของ `np_baseball` ไปยัง `numpy.std()` ตัวอย่างของ `np.mean()` แสดงให้เห็นวิธีการดำเนินการ"
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "คุณได้ใช้ `np.corrcoef()` เพื่อคำนวณค่าสหสัมพันธ์หรือไม่?"
incorrect1 = "ในการคำนวณ `corr` อาร์กิวเมนต์แรกของ `np.corrcoef()` ควรเป็นคอลัมน์แรกของ `np_baseball` คล้ายกับที่ได้ดำเนินการไปก่อนหน้านี้"
incorrect2 = "ในการคำนวณ `corr` อาร์กิวเมนต์ที่สองของ `np.corrcoef()` ควรเป็นคอลัมน์ที่สองของ `np_baseball` แทนที่จะใช้ `[:,0]` ให้ใช้ `[:,1]` ในครั้งนี้"
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("ยอดเยี่ยมมาก! คุณได้สร้างรากฐานที่มั่นคงแล้ว ถึงเวลาที่จะนำทักษะด้านวิทยาศาสตร์ข้อมูลใหม่ทั้งหมดของคุณไปใช้เพื่อแก้ปัญหาที่ท้าทายยิ่งขึ้นและสร้างผลกระทบที่มีความหมาย")
```
