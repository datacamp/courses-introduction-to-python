---
title_meta: บทที่ 1
title: Python เบื้องต้น
description: >-
  แนะนำแนวคิดพื้นฐานของ Python เรียนรู้การใช้ Python แบบโต้ตอบและแบบสคริปต์
  สร้างตัวแปรแรก และทำความรู้จักกับชนิดข้อมูลพื้นฐานของ Python
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Hello Python!
  - nb_of_exercises: 5
    title: ตัวแปรและชนิดข้อมูล
---

## Hello Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## โค้ด Python แรกของคุณ

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

ถึงเวลาลองรันโค้ด Python เป็นครั้งแรกแล้ว!

ไปที่โค้ดแล้วกดปุ่มรันโค้ดเพื่อดูผลลัพธ์

`@instructions`
- กดปุ่มรันโค้ดเพื่อดูผลลัพธ์ของ `print(5 / 8)`

`@hint`
- รันโค้ดก่อนที่จะส่งคำตอบ เพื่อให้มีเวลาสำรวจผลลัพธ์

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:คุณได้ใช้ `{{sol_call}}` เพื่อพิมพ์ `5 / 8` หรือไม่?")
success_msg("ยอดเยี่ยม! ไปยังข้อถัดไปกันเลย!")
```

---

## Python ในฐานะเครื่องคิดเลข

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python เหมาะอย่างยิ่งสำหรับการคำนวณพื้นฐาน ไม่ว่าจะเป็นการบวก ลบ คูณ หรือหาร

โค้ดในสคริปต์แสดงตัวอย่างการคำนวณเหล่านี้ให้ดูแล้ว

ถึงตาลองเขียนโค้ดเองบ้าง

`@instructions`
- พิมพ์ผลลัพธ์ของการลบ `5` ออกจาก `5` ใต้ `# Subtraction` โดยใช้ `print()`
- พิมพ์ผลลัพธ์ของการคูณ `3` ด้วย `5` ใต้ `# Multiplication`

`@hint`
- ต้องใช้ `print()` เพื่อแสดงผลลัพธ์
- ใช้ `-` สำหรับการลบ และ `*` สำหรับการคูณ

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
Ex().has_printout(0, not_printed_msg = "คุณได้ใช้ `print(4 + 5)` เพื่อแสดงผลลัพธ์ของการบวกหรือไม่?")

Ex().has_printout(1, not_printed_msg = "คุณได้ใช้ `print(5 - 5)` เพื่อแสดงผลลัพธ์ของการลบหรือไม่?")

Ex().has_printout(2, not_printed_msg = "คุณได้ใช้ `print(3 * 5)` เพื่อแสดงผลลัพธ์ของการคูณหรือไม่?")

Ex().has_printout(3, not_printed_msg = "คุณได้ใช้ `print(10 / 2)` เพื่อแสดงผลลัพธ์ของการหารหรือไม่?")

success_msg("ถูกต้อง! Python สามารถช่วยในการคำนวณได้ ซึ่งเป็นคุณสมบัติที่จะเป็นประโยชน์สำหรับการวิเคราะห์ข้อมูลเมื่อเราพัฒนาทักษะด้านข้อมูลมากขึ้น")
```

---

## ตัวแปรและชนิดข้อมูล

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## การกำหนดค่าตัวแปร

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

ใน Python ตัวแปรช่วยให้อ้างอิงค่าต่าง ๆ ด้วยชื่อที่กำหนดเองได้ ตัวอย่างเช่น หากต้องการสร้างตัวแปร `x` ที่มีค่าเท่ากับ `5` ให้ใช้เครื่องหมาย `=` ดังนี้

```
x = 5
```

จากนี้ไปสามารถใช้ชื่อตัวแปร `x` แทนค่า `5` ได้โดยตรง

จำไว้ว่าเครื่องหมาย `=` ใน Python หมายถึง _การกำหนดค่า_ ไม่ใช่การตรวจสอบว่าเท่ากันหรือไม่ ลองฝึกในแบบฝึกหัดนี้โดยแทนที่ `____` ด้วยโค้ดของคุณ

`@instructions`
- สร้างตัวแปร `savings` ที่มีค่าเท่ากับ `100`
- ตรวจสอบค่าของตัวแปรนี้โดยพิมพ์ `print(savings)` ในสคริปต์

`@hint`
- พิมพ์ `savings = 100` เพื่อสร้างตัวแปร `savings`
- หลังจากสร้างตัวแปร `savings` แล้ว ให้พิมพ์ `print(savings)`
- โค้ดสุดท้ายไม่ควรมี `____` หลงเหลืออยู่

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
Ex().check_object("savings").has_equal_value(incorrect_msg="กรุณากำหนดค่า `100` ให้กับตัวแปร `savings`")
Ex().has_printout(0, not_printed_msg = "กรุณาแสดงผล `savings` ตัวแปรที่คุณสร้างขึ้น โดยใช้ `print(savings)`")
success_msg("ยอดเยี่ยม! ลองทำการคำนวณด้วยตัวแปรนี้กันดูเลย!")
```

---

## การคำนวณด้วยตัวแปร

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

ตอนนี้สร้างตัวแปร savings ไว้แล้ว มาเริ่มออมเงินกันเลย!

แทนที่จะคำนวณด้วยค่าตัวเลขโดยตรง ลองใช้ตัวแปรแทนดูสิ

ถ้าออมเงินเดือนละ $10 จะมีเงินออมเท่าไรหลังจากผ่านไป 4 เดือน?

`@instructions`
- สร้างตัวแปร `monthly_savings` กำหนดค่าเป็น `10` และตัวแปร `num_months` กำหนดค่าเป็น `4`
- คูณ `monthly_savings` ด้วย `num_months` แล้วกำหนดผลลัพธ์ให้กับ `new_savings`
- แสดงค่าของ `new_savings` ด้วย `print()`

`@hint`
- คำนวณด้วยตัวแปรได้เหมือนกับการคำนวณด้วยตัวเลขเลย แทนที่จะเขียน `10 * 4` ให้ใช้ตัวแปรแทนตัวเลขเหล่านั้น!
- ใช้ `print()` เพื่อแสดงค่าใน `new_savings`
- ระวังการสะกดชื่อตัวแปรให้ถูกต้องด้วย!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "คุณได้บันทึกค่า `10` ไว้ใน `monthly_savings` โดยใช้ `monthly_savings = 10` หรือไม่?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "คุณได้บันทึกค่า `4` ไว้ใน `num_months` โดยใช้ `num_months = 4` หรือไม่?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "คุณได้ใช้ตัวแปรและสัญลักษณ์ที่ถูกต้องในการคูณหรือไม่? คาดว่าจะได้ `monthly_savings * num_months` แต่ได้รับค่าอื่น")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "คุณได้ใช้ตัวแปรและสัญลักษณ์ที่ถูกต้องในการบวกหรือไม่? คาดว่าจะได้ `savings + new_savings` แต่ได้รับค่าอื่น")

Ex().has_printout(0, not_printed_msg="โปรดอย่าลืมพิมพ์ `new_savings` ที่ท้ายสคริปต์ของคุณ")

success_msg("คุณมีเงินออมใหม่ $40!")
```

---

## ชนิดข้อมูลอื่น ๆ ของตัวแปร

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

ในแบบฝึกหัดก่อนหน้า คุณได้ทำงานกับชนิดข้อมูล integer ใน Python:

- `int` หรือจำนวนเต็ม: ตัวเลขที่ไม่มีส่วนทศนิยม เช่น `savings` ที่มีค่าเป็น `100`

นอกจากชนิดข้อมูลตัวเลขแล้ว ยังมีชนิดข้อมูลทั่วไปอีกสามประเภท ได้แก่:

- `float` หรือทศนิยม: ตัวเลขที่มีทั้งส่วนจำนวนเต็มและส่วนทศนิยม คั่นด้วยจุด เช่น `1.1`
- `str` หรือสตริง: ชนิดข้อมูลสำหรับแทนข้อความ สามารถใช้เครื่องหมายคำพูดเดี่ยวหรือคู่ในการสร้างสตริง
- `bool` หรือบูลีน: ชนิดข้อมูลสำหรับแทนค่าตรรกะ มีได้เพียง `True` หรือ `False` เท่านั้น (ตัวพิมพ์ใหญ่-เล็กมีความสำคัญ!)

`@instructions`
- สร้างตัวแปร float ใหม่ชื่อ `half` โดยกำหนดค่าเป็น `0.5`
- สร้างตัวแปร string ใหม่ชื่อ `intro` โดยกำหนดค่าเป็น `"Hello! How are you?"`
- สร้างตัวแปร boolean ใหม่ชื่อ `is_good` โดยกำหนดค่าเป็น `True`

`@hint`
- ในการสร้างตัวแปรใน Python ให้ใช้ `=` และอย่าลืมใส่เครื่องหมายคำพูดล้อมรอบข้อความ (ใช้เครื่องหมายคำพูดเดี่ยวหรือคู่ก็ได้)
- ค่าบูลีนใน Python มีเพียงสองค่าเท่านั้น คือ `True` และ `False` รูปแบบอื่น เช่น `TRUE`, `true`, `FALSE`, `false` จะไม่ถูกรับรอง

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
Ex().check_object("half").has_equal_value(incorrect_msg = "คุณได้บันทึกทศนิยม `0.5` ไว้ใน `half` หรือไม่?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "มีบางอย่างไม่ถูกต้องในตัวแปร `intro` ของคุณ กรุณาตรวจสอบการสะกดและตรวจสอบให้แน่ใจว่าคุณได้ใช้เครื่องหมายคำพูดอย่างถูกต้อง")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "คุณได้พิมพ์ตัวอักษรแรกของค่าบูลีนเป็นตัวพิมพ์ใหญ่หรือไม่? โปรดทราบว่าคุณไม่จำเป็นต้องใช้เครื่องหมายคำพูดในที่นี้")

success_msg("ดีมาก!")
```

---

## การดำเนินการกับประเภทข้อมูลอื่น

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

ตัวแปรใน Python มีหลายประเภท สามารถตรวจสอบประเภทของตัวแปรได้โดยใช้ `type()` ตัวอย่างเช่น หากต้องการดูประเภทของ `a` ให้รัน `type(a)`

ตัวแปรแต่ละประเภทมีพฤติกรรมต่างกันใน Python เช่น การบวก string สองตัวเข้าด้วยกันจะได้ผลลัพธ์ที่แตกต่างจากการบวก integer หรือ boolean สองตัว

ลองทดสอบดูได้เลย

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
- บวก `savings` กับ `new_savings` แล้วเก็บผลลัพธ์ไว้ในตัวแปร `total_savings`
- ใช้ `type()` เพื่อพิมพ์ประเภทของ `total_savings`

`@hint`
- นำ `savings + new_savings` มาเก็บไว้ในตัวแปรใหม่ชื่อ `total_savings`
- หากต้องการพิมพ์ประเภทของตัวแปร `x` ให้ใช้ `print(type(x))`

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
msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปรที่กำหนดไว้ล่วงหน้า"

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="เพิ่ม `savings` และ `new_savings` เพื่อสร้างตัวแปร `total_savings`"),
    has_printout(1, not_printed_msg = "__JINJA__:ใช้ `{{sol_call}}` เพื่อแสดงประเภทของ `total_savings`")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- คำนวณผลรวมของ `intro` กับ `intro` แล้วเก็บผลลัพธ์ไว้ในตัวแปร `doubleintro`
- พิมพ์ค่าของ `doubleintro` ออกมา ผลลัพธ์เป็นไปตามที่คาดไว้หรือไม่?

`@hint`
- นำ `intro + intro` มาเก็บไว้ในตัวแปรใหม่ชื่อ `doubleintro`
- หากต้องการพิมพ์ค่าของตัวแปร `x` ให้เขียน `print(x)` ในสคริปต์

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
msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปรที่กำหนดไว้ล่วงหน้า"

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "คุณได้เก็บผลลัพธ์ของ `intro + intro` ไว้ใน `doubleintro` หรือไม่?"),
    has_printout(0, not_printed_msg = "อย่าลืมพิมพ์ `doubleintro` ออกมาด้วย")
)

success_msg("ดีมาก โปรดสังเกตว่า `intro + intro` ทำให้ `\"Hello! How are you?\"` และ `\"Hello! How are you?\"` ถูกนำมาต่อกัน")
```
