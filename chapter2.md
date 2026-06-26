---
title_meta: บทที่ 2
title: Python Lists
description: >-
  เรียนรู้การจัดเก็บ เข้าถึง และจัดการข้อมูลใน List
  ซึ่งเป็นก้าวแรกสู่การทำงานกับข้อมูลจำนวนมากอย่างมีประสิทธิภาพ
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python Lists
  - nb_of_exercises: 4
    title: การ Subset List
  - nb_of_exercises: 5
    title: การจัดการ List
---

## Python Lists

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## สร้างลิสต์

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

ลิสต์คือ **ชนิดข้อมูลแบบประกอบ** ที่ใช้รวมค่าหลายค่าเข้าด้วยกัน ดังตัวอย่างนี้:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

หลังจากวัดส่วนสูงของสมาชิกในครอบครัวแล้ว คุณตัดสินใจรวบรวมข้อมูลเกี่ยวกับบ้านที่อาศัยอยู่ด้วย พื้นที่ของแต่ละส่วนในบ้านถูกเก็บไว้ในตัวแปรแยกกันในแบบฝึกหัดนี้

`@instructions`
- สร้างลิสต์ชื่อ `areas` ที่เก็บพื้นที่ของโถงทางเดิน (`hall`), ครัว (`kit`), ห้องนั่งเล่น (`liv`), ห้องนอน (`bed`) และห้องน้ำ (`bath`) ตามลำดับนี้ โดยใช้ตัวแปรที่กำหนดไว้ให้แล้ว
- แสดงผล `areas` ด้วยฟังก์ชัน `print()`

`@hint`
- ใช้ตัวแปรที่สร้างไว้แล้วเพื่อสร้างลิสต์ได้เลย เช่น `areas = [hall, kit, ...]`
- ใช้วงเล็บเหลี่ยม `[]` ไม่ใช่วงเล็บกลม `()`
- ไม่ต้องใส่เครื่องหมายคำพูดเมื่อเก็บตัวแปรไว้ในลิสต์
- พิมพ์ `print(areas)` เพื่อแสดงผลลิสต์เมื่อส่งคำตอบ

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
predef_msg = "อย่าลบหรือแก้ไขตัวแปรที่กำหนดไว้ล่วงหน้า!"
areas_msg = "กรุณากำหนด `areas` เป็นรายการที่ประกอบด้วยตัวแปรพื้นที่ทั้งหมด ตามลำดับที่ถูกต้อง: `[hall, kit, liv, bed, bath]` กรุณาตรวจสอบการพิมพ์ผิด รายการไม่ควรมีสิ่งอื่นใดนอกจากนี้!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:คุณได้ใช้ `{{sol_call}}` เพื่อพิมพ์รายการ `areas` ที่ท้ายสคริปต์ของคุณหรือไม่?"),
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

success_msg("ยอดเยี่ยม! การใช้รายการดีกว่ามากใช่ไหม?")
```

---

## สร้างลิสต์ที่มีข้อมูลหลายประเภท

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

แม้จะไม่ค่อยพบบ่อยนัก แต่ลิสต์สามารถเก็บข้อมูลได้หลายประเภทพร้อมกัน ไม่ว่าจะเป็นสตริง, float หรือ boolean

ตอนนี้จะเพิ่มชื่อห้องลงในลิสต์ เพื่อให้ดูทั้งชื่อห้องและขนาดพื้นที่ได้ในที่เดียว

โค้ดบางส่วนเตรียมไว้ให้แล้ว สังเกตให้ดี! `"bathroom"` คือสตริง ส่วน `bath` คือตัวแปรที่เก็บค่า float `9.50` ที่กำหนดไว้ก่อนหน้านี้

`@instructions`
- เติมโค้ดที่สร้างลิสต์ `areas` ให้ครบ โดยจัดเรียงให้ลิสต์มีชื่อห้องเป็นสตริงก่อน ตามด้วยขนาดพื้นที่ของห้องนั้น กล่าวคือ ให้เพิ่มสตริง `"hallway"`, `"kitchen"` และ `"bedroom"` ในตำแหน่งที่เหมาะสม
- พิมพ์ `areas` อีกครั้ง ผลลัพธ์ที่ได้ให้ข้อมูลมากขึ้นกว่าเดิมหรือไม่?

`@hint`
- สี่ธาตุแรกของลิสต์ `areas` เขียนได้ว่า `["hallway", hall, "kitchen", kit, ...`
- สตริงต้องอยู่ในเครื่องหมายคำพูด `""`

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
predef_msg = "อย่าลบหรือแก้ไขตัวแปรที่กำหนดไว้ล่วงหน้า!"
areas_msg = "คุณไม่ได้กำหนดค่าที่ถูกต้องให้กับ `areas` กรุณาอ่านคำแนะนำอีกครั้ง โปรดวางชื่อห้องไว้ก่อนตัวแปรที่มีพื้นที่ของแต่ละห้องทุกครั้ง ลำดับมีความสำคัญที่นี่! ระวังการพิมพ์ผิดด้วย"

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:คุณได้ใช้ `{{sol_call}}` เพื่อพิมพ์รายการ `areas` ที่ท้ายสคริปต์ของคุณหรือไม่?")

success_msg("ดีมาก! รายการนี้มีทั้งสตริงและจำนวนทศนิยม แต่นั่นไม่ใช่ปัญหาสำหรับ Python!")
```

---

## ลิสต์ของลิสต์

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

ในฐานะนักวิทยาศาสตร์ข้อมูล คุณจะต้องจัดการกับข้อมูลจำนวนมาก และการจัดกลุ่มข้อมูลบางส่วนเข้าด้วยกันก็เป็นเรื่องสมเหตุสมผล

แทนที่จะสร้างลิสต์ที่มีแต่ string และ float เพื่อเก็บชื่อและพื้นที่ของห้องต่าง ๆ ในบ้าน คุณสามารถสร้างลิสต์ของลิสต์ได้แทน

จำไว้ว่า `"hallway"` คือ string ในขณะที่ `hall` คือตัวแปรที่แทนค่า float `11.25` ที่กำหนดไว้ก่อนหน้านี้

`@instructions`
- เติมลิสต์ของลิสต์ให้ครบโดยเพิ่มข้อมูลของห้องนอนและห้องน้ำเข้าไปด้วย ตรวจสอบให้แน่ใจว่าเรียงลำดับถูกต้อง
- แสดงผล `house` แล้วดูว่าการจัดโครงสร้างข้อมูลแบบนี้เข้าใจง่ายขึ้นหรือไม่

`@hint`
- เพิ่ม _ลิสต์ย่อย_ ลงในลิสต์ `house` โดยใส่ `["bedroom", bed]` และ `["bathroom", bath]` ภายในวงเล็บเหลี่ยม
- อย่าลืมใส่เครื่องหมายจุลภาค `,` หลังลิสต์ย่อยแต่ละรายการ
- หากต้องการแสดงผลตัวแปร `x` ให้เขียน `print(x)` ในบรรทัดใหม่

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
predef_msg = "อย่าลบหรือแก้ไขตัวแปรที่กำหนดไว้ล่วงหน้า!"
house_msg = "คุณยังไม่ได้กำหนดค่าที่ถูกต้องให้กับ `house` กรุณาอ่านคำแนะนำอีกครั้ง ขยายรายการของรายการให้ครอบคลุมรายการสำหรับแต่ละคู่ของชื่อห้องและพื้นที่ห้อง โปรดตรวจสอบลำดับและการพิมพ์ผิด!"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:คุณได้ใช้ `{{sol_call}}` เพื่อแสดงเนื้อหาของ `house` หรือไม่?")

success_msg("ยอดเยี่ยม! เตรียมพร้อมที่จะเรียนรู้เกี่ยวกับการเลือกข้อมูลจากรายการได้เลย!")
```

---

## การดึงข้อมูลจาก List

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Subset และพิชิตลิสต์

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

การ subset ลิสต์ใน Python นั้นไม่ยากเลย ดูตัวอย่างโค้ดด้านล่าง ซึ่งสร้างลิสต์ `x` แล้วเลือกค่า "b" ออกมา จำไว้ว่า "b" เป็นสมาชิกตัวที่สอง จึงมี index เป็น 1 และยังสามารถใช้ index ติดลบได้ด้วย

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # ได้ผลลัพธ์เหมือนกัน!
```

จำลิสต์ `areas` ที่มีทั้ง string และ float ได้ไหม? โค้ดที่กำหนดลิสต์นี้อยู่ในสคริปต์แล้ว ลองเพิ่มโค้ดเพื่อ subset ลิสต์ดูสิ

`@instructions`
- แสดงผลสมาชิกตัวที่สองของลิสต์ `areas` (มีค่าเป็น `11.25`)
- Subset และแสดงผลสมาชิกตัวสุดท้ายของ `areas` ซึ่งมีค่าเป็น `9.50` การใช้ index ติดลบเหมาะมากสำหรับกรณีนี้!
- เลือกตัวเลขที่แทนพื้นที่ของห้องนั่งเล่น (`20.0`) แล้วแสดงผลออกมา

`@hint`
- ใช้ `x[1]` เพื่อเลือกสมาชิกตัวที่สองของลิสต์ `x`
- ใช้ `x[-1]` เพื่อเลือกสมาชิกตัวสุดท้ายของลิสต์ `x`
- อย่าลืมครอบการ subset ด้วย `print()`
- ตัวเลขที่แทนพื้นที่ของห้องนั่งเล่นคือสมาชิกตัวที่ 6 ในลิสต์ ดังนั้นต้องใช้ `[5]` ที่นี่ หากใช้ `area[4]` จะได้ค่าที่เป็น string แทน!

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
msg = "อย่าลบหรือแก้ไขรายการ `areas` ที่กำหนดไว้ล่วงหน้า"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "ลองตรวจสอบโค้ดของท่านอีกครั้งเพื่อแสดงผลองค์ประกอบที่สองใน `areas` ซึ่งอยู่ที่ดัชนี `1`")
Ex().has_printout(1, not_printed_msg = "ลองตรวจสอบโค้ดของท่านอีกครั้งเพื่อแสดงผลองค์ประกอบสุดท้ายใน `areas` ซึ่งอยู่ที่ดัชนี `-1`")
Ex().has_printout(2, not_printed_msg = "ลองตรวจสอบโค้ดของท่านอีกครั้งเพื่อแสดงผลพื้นที่ของห้องนั่งเล่น ซึ่งอยู่ที่ดัชนี `5`")
success_msg("ทำได้ดีมาก!")
```

---

## การ Slice ข้อมูล

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

การเลือกค่าทีละตัวจากลิสต์เป็นเพียงส่วนหนึ่งเท่านั้น ยังสามารถ _slice_ ลิสต์ได้ด้วย นั่นคือการเลือกหลายธาตุพร้อมกัน โดยใช้ syntax ดังนี้:

```
my_list[start:end]
```

ดัชนี `start` จะถูกรวมไว้ด้วย แต่ดัชนี `end` _จะไม่ถูกรวม_ อย่างไรก็ตาม สามารถละเว้นดัชนีเหล่านี้ได้ หากไม่ระบุดัชนี `start` Python จะเริ่ม slice ตั้งแต่ธาตุแรกของลิสต์โดยอัตโนมัติ

`@instructions`
- ใช้ slicing เพื่อสร้างลิสต์ `downstairs` ที่มี 6 ธาตุแรกของ `areas`
- สร้าง `upstairs` โดยดึง `4` ธาตุสุดท้ายของ `areas` คราวนี้ให้ละดัชนี `end` เพื่อให้โค้ดกระชับขึ้น
- แสดงผล `downstairs` และ `upstairs` ด้วย `print()`

`@hint`
- ใช้ `[0:6]` เพื่อดึงหกธาตุแรกของลิสต์
- หากต้องการดึงทุกธาตุยกเว้น 5 ธาตุแรกของลิสต์ `l` ให้ใช้ `l[5:]`
- เพิ่ม `print()` สองครั้งเพื่อแสดงผล `downstairs` และ `upstairs`

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
msg = "อย่าลบหรือแก้ไขรายการ `areas` ที่กำหนดไว้ล่วงหน้า"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` ไม่ถูกต้อง กรุณาใช้ `areas[%s]` และการแบ่งส่วนเพื่อเลือกองค์ประกอบที่ต้องการ หรือวิธีที่เทียบเท่า"
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="คุณได้พิมพ์ `downstairs` หลังจากคำนวณแล้วหรือไม่?")
Ex().has_printout(1, not_printed_msg="คุณได้พิมพ์ `upstairs` หลังจากคำนวณแล้วหรือไม่?")

success_msg("ยอดเยี่ยม!")
```

---

## การ Subset ลิสต์ซ้อนลิสต์

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

ลิสต์ใน Python สามารถมีลิสต์อื่นอยู่ภายในได้

ในการ subset ลิสต์ซ้อนลิสต์ ใช้เทคนิคเดิมคือวงเล็บก้ามปู ตัวอย่างเช่น สำหรับลิสต์ `house`:

```
house[2][0]
```

`@instructions`
- Subset ลิสต์ `house` เพื่อดึงค่า float `9.5` ออกมา

`@hint`
- ลองแยกเป็นขั้นตอน ขั้นแรกให้เข้าถึงองค์ประกอบสุดท้ายของลิสต์ คือ `["bathroom", 9.50]` โดยจำไว้ว่า index ขององค์ประกอบสุดท้ายคือ `-1`
- จากนั้นให้เข้าถึงองค์ประกอบที่สองของ `["bathroom", 9.50]` ซึ่งอยู่ที่ index `1`

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

success_msg("ถูกต้องมาก! ส่วนสุดท้ายของปริศนารายการคือการจัดการ")
```

---

## การจัดการ Lists

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## แทนที่ elements ในลิสต์

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

การแทนที่ elements ในลิสต์ทำได้โดยเลือก subset แล้วกำหนดค่าใหม่ให้กับ subset นั้น สามารถเลือกทีละ element หรือจะเปลี่ยนทั้ง slice ของลิสต์พร้อมกันก็ได้

ในแบบฝึกหัดนี้และแบบฝึกหัดถัดไป จะทำงานกับลิสต์ `areas` ที่เก็บชื่อและพื้นที่ของห้องต่างๆ ในบ้านต่อไป

`@instructions`
- อัปเดตพื้นที่ห้องน้ำจาก `9.50` เป็น `10.50` ตารางเมตร โดยใช้ negative indexing
- เพิ่มความทันสมัยให้ลิสต์ `areas` ด้วยการเปลี่ยน `"living room"` เป็น `"chill zone"` คราวนี้ไม่ต้องใช้ negative indexing

`@hint`
- ในการอัปเดตพื้นที่ห้องน้ำ ให้เลือก subset ของค่าพื้นที่ห้องน้ำก่อน (เป็น item สุดท้ายในลิสต์!)
- จากนั้นกำหนดค่าพื้นที่ห้องน้ำใหม่ให้กับ subset นั้น
- ทำแบบเดียวกันเพื่ออัปเดตชื่อ `"living room"` ซึ่งอยู่ที่ index 4

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
bathroom_msg = 'คุณสามารถใช้ `areas[-1] = 10.50` เพื่ออัปเดตพื้นที่ห้องน้ำได้'
chillzone_msg = 'คุณสามารถใช้ `areas[4] = "chill zone"` เพื่ออัปเดตชื่อห้องนั่งเล่นได้'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'การเปลี่ยนแปลง `areas` ของคุณไม่ได้ให้ผลลัพธ์เป็นรายการที่ถูกต้อง คุณแน่ใจหรือไม่ว่าใช้การดำเนินการกับชุดข้อมูลย่อยที่ถูกต้อง? หากไม่แน่ใจ คุณสามารถใช้คำใบ้ได้!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('ยอดเยี่ยม! ดังที่ตัวอย่างโค้ดแสดงให้เห็น คุณยังสามารถแบ่งส่วนรายการและแทนที่ด้วยรายการอื่นเพื่ออัปเดตหลายองค์ประกอบในคำสั่งเดียวได้อีกด้วย')
```

---

## ต่อขยายลิสต์

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

นอกจากจะแก้ไขสมาชิกในลิสต์ได้แล้ว ยังสามารถเพิ่มสมาชิกใหม่เข้าไปได้อีกด้วย โดยใช้ตัวดำเนินการ `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

สมมติว่าคุณถูกรางวัลลอตเตอรีและตัดสินใจสร้างสระว่ายน้ำและโรงจอดรถเพิ่ม ลองเพิ่มข้อมูลเหล่านี้ลงในลิสต์ `areas` กัน

`@instructions`
- ใช้ตัวดำเนินการ `+` เพื่อต่อลิสต์ `["poolhouse", 24.5]` ไว้ท้ายลิสต์ `areas` แล้วเก็บผลลัพธ์ไว้ในตัวแปร `areas_1`
- ต่อขยาย `areas_1` เพิ่มเติมโดยเพิ่มข้อมูลโรงจอดรถ ได้แก่ string `"garage"` และ float `15.45` แล้วตั้งชื่อลิสต์ที่ได้ว่า `areas_2`

`@hint`
- ดูตัวอย่างโค้ดในโจทย์ โดย `x` คือ `areas` และ `["e", "f"]` คือ `["poolhouse", 24.5]`
- หากต้องการเพิ่มสมาชิกใน `areas_1` ให้ใช้ `areas_1 + ["element", 123]`

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
msg = "อย่าลบหรือแก้ไขรายการ `areas` ที่กำหนดไว้ล่วงหน้า"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "ใช้ `areas + [\"poolhouse\", 24.5]` เพื่อสร้าง `areas_1` โปรดตรวจสอบการพิมพ์ให้ถูกต้อง!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "ใช้ `areas_1 + [\"garage\", 15.45]` เพื่อสร้าง `areas_2` โปรดตรวจสอบการพิมพ์ให้ถูกต้อง!")
success_msg("ยอดเยี่ยม! รายการมีรูปแบบที่ดีขึ้นเรื่อยๆ!")
```

---

## ลบสมาชิกออกจากลิสต์

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

สุดท้าย เราสามารถลบสมาชิกออกจากลิสต์ได้ด้วยคำสั่ง `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

สังเกตให้ดี: ทันทีที่ลบสมาชิกออกจากลิสต์ index ของสมาชิกที่อยู่ถัดจากตำแหน่งที่ถูกลบจะเปลี่ยนไปทั้งหมด!

น่าเสียดายที่เงินรางวัลลอตเตอรีที่ได้มานั้นไม่มากอย่างที่คิด และดูเหมือนว่าโปรเจกต์ poolhouse คงไม่เกิดขึ้นแล้ว จึงต้องลบรายการนั้นออกจากลิสต์ โดยจะลบทั้ง string และ float ที่เกี่ยวข้องออกจากลิสต์ `areas`

`@instructions`
- ลบ string และ float ของ `"poolhouse"` ออกจากลิสต์ `areas`
- แสดงผลลิสต์ `areas` ที่อัปเดตแล้ว

`@hint`
- ต้องใช้ `del` สองครั้งเพื่อลบสองสมาชิก แต่ระวังเรื่อง index ที่เปลี่ยนไปด้วย!

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

Ex().has_printout(0, not_printed_msg="คุณได้พิมพ์ `areas` หลังจากลบสตริงและตัวเลขทศนิยมของ poolhouse แล้วหรือไม่?")
success_msg("ถูกต้อง! คุณจะได้เรียนรู้วิธีที่ง่ายกว่าในการลบองค์ประกอบเฉพาะออกจากรายการ Python ในภายหลัง")
```

---

## กลไกภายในของ List

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

ในแบบฝึกหัดนี้มีโค้ดตั้งต้นให้แล้ว ได้แก่ list ชื่อ `areas` และสำเนาของมันชื่อ `areas_copy`

ปัจจุบัน โค้ดจะเปลี่ยนค่าสมาชิกตัวแรกใน `areas_copy` แล้วพิมพ์ `areas` ออกมา ถ้ากด **รันโค้ด** จะเห็นว่าแม้จะแก้ `areas_copy` แต่การเปลี่ยนแปลงนั้นส่งผลกับ `areas` ด้วย เหตุผลคือ `areas` และ `areas_copy` ชี้ไปยัง list เดียวกัน

หากต้องการให้การเปลี่ยนแปลงใน `areas_copy` ไม่กระทบกับ `areas` จะต้องสร้างสำเนาแบบชัดเจนของ `areas` โดยใช้ `list()` หรือ `[:]`

`@instructions`
- แก้ไขคำสั่งที่สอง ซึ่งเป็นส่วนที่สร้างตัวแปร `areas_copy` ให้ `areas_copy` เป็นสำเนาแบบชัดเจนของ `areas` หลังจากแก้ไขแล้ว การเปลี่ยนแปลงใน `areas_copy` จะต้องไม่ส่งผลกับ `areas` จากนั้นกด **ส่งคำตอบ** เพื่อตรวจสอบผลลัพธ์

`@hint`
- แก้ไขบรรทัด `areas_copy = areas` แทนที่จะกำหนดค่า `areas` ตรงๆ ให้ใช้ `list(areas)` หรือ `areas[:]` แทน

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "ดูเหมือนว่า `areas_copy` ยังไม่ได้รับการอัปเดตอย่างถูกต้อง"),
  check_function("list", missing_msg = "โปรดใช้ `list(areas)` เพื่อสร้าง `areas_copy`")
)

mmsg = "โปรดอย่าลบรายการ `areas` ที่กำหนดไว้ล่วงหน้า"
imsg = "โปรดแก้ไขเฉพาะสำเนาเท่านั้น ไม่ใช่รายการ `areas` ต้นฉบับ หากท่านไม่แน่ใจวิธีการสร้างสำเนา โปรดอ่านคำอธิบายแบบฝึกหัดอีกครั้ง"
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "โปรดใช้ `list(areas)` เพื่อสร้าง `areas_copy`")
)

success_msg("ยอดเยี่ยม! ความแตกต่างระหว่างการคัดลอกแบบชัดเจนและการคัดลอกแบบอ้างอิงนั้นมีความละเอียดอ่อน แต่อาจมีความสำคัญอย่างมาก โปรดจำไว้ว่ารายการถูกจัดเก็บในหน่วยความจำของคอมพิวเตอร์อย่างไร")
```
