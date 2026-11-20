---
title_meta: บทที่ 3
title: ฟังก์ชันและแพ็กเกจ
description: >-
  เรียนรู้การใช้ฟังก์ชัน เมธอด และแพ็กเกจ เพื่อนำโค้ดที่นักพัฒนา Python
  มืออาชีพเขียนไว้มาใช้ได้อย่างเต็มประสิทธิภาพ
  เป้าหมายคือลดปริมาณโค้ดที่ต้องเขียนเพื่อแก้ปัญหาที่ซับซ้อน
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: ฟังก์ชัน
  - nb_of_exercises: 4
    title: เมธอด
  - nb_of_exercises: 4
    title: แพ็กเกจ
---

## ฟังก์ชัน

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## ฟังก์ชันที่คุ้นเคย

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python มีฟังก์ชันในตัว (built-in functions) หลายตัวที่ช่วยให้การทำงานด้านวิทยาศาสตร์ข้อมูลง่ายขึ้น คุณรู้จักฟังก์ชันสองตัวไปแล้ว ได้แก่ `print()` และ `type()` นอกจากนี้ยังมีฟังก์ชันอย่าง `str()`, `int()`, `bool()` และ `float()` สำหรับแปลงชนิดข้อมูล ดูรายละเอียดเพิ่มเติมได้ [ที่นี่](https://docs.python.org/3/library/functions.html) ซึ่งทั้งหมดนี้ก็เป็นฟังก์ชันในตัวเช่นกัน

การเรียกใช้ฟังก์ชันทำได้ง่ายมาก ตัวอย่างเช่น หากต้องการหาชนิดข้อมูลของ `3.0` และเก็บผลลัพธ์ไว้ในตัวแปรใหม่ชื่อ `result` ให้เขียนดังนี้:

```
result = type(3.0)
```

`@instructions`
- ใช้ `print()` ร่วมกับ `type()` เพื่อแสดงชนิดข้อมูลของ `var1`
- ใช้ `len()` เพื่อหา[ความยาวของลิสต์](https://docs.python.org/3/library/functions.html#len) `var1` แล้วครอบด้วย `print()` เพื่อแสดงผลออกมาทันที
- ใช้ `int()` เพื่อแปลง `var2` ให้เป็น[จำนวนเต็ม](https://docs.python.org/3/library/functions.html#int) แล้วเก็บผลลัพธ์ไว้ในตัวแปร `out2`

`@hint`
- เรียกใช้ฟังก์ชัน `type()` แบบนี้: `type(var1)`
- เรียกใช้ `print()` เหมือนที่เคยทำมาก่อน โดยใส่ตัวแปรที่ต้องการแสดงผลไว้ในวงเล็บ
- `int(x)` จะแปลงค่า `x` ให้เป็นจำนวนเต็ม

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
____

# Print out length of var1
____

# Convert var2 to an integer: out2
out2 = ____
```

`@solution`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

`@sct`
```{python}
msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปรที่กำหนดไว้ล่วงหน้า"
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:โปรดตรวจสอบให้แน่ใจว่าได้แสดงผล %s ของ `var1` ด้วย `{{sol_call}}`"
Ex().has_printout(0, not_printed_msg = patt % 'ประเภท')
Ex().has_printout(1, not_printed_msg = patt % 'ความยาว')

int_miss_msg = "คุณได้ใช้ `int()` เพื่อแปลง `var2` ให้เป็นจำนวนเต็มแล้วหรือไม่?"
int_incorr_msg = "คุณได้ส่ง `var2` ไปยัง `int()` แล้วหรือไม่?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="คุณเรียกใช้ `int()` ได้อย่างถูกต้องแล้ว โปรดตรวจสอบให้แน่ใจว่าได้กำหนดผลลัพธ์ของการเรียกใช้นี้ให้กับ `out2`"),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("ยอดเยี่ยมมาก! ฟังก์ชัน `len()` มีประโยชน์อย่างมาก และยังสามารถใช้กับสตริงเพื่อนับจำนวนอักขระได้อีกด้วย!")
```

---

## ขอความช่วยเหลือ!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

บางทีคุณอาจรู้ชื่อฟังก์ชัน Python อยู่แล้ว แต่ยังไม่แน่ใจว่าต้องใช้งานอย่างไร วิธีดูข้อมูลของฟังก์ชันก็คือเรียกใช้อีกฟังก์ชันหนึ่งนั่นเอง ได้แก่ `help()` และใน IPython ยังสามารถใช้ `?` นำหน้าชื่อฟังก์ชันได้ด้วย

ตัวอย่างเช่น หากต้องการดูข้อมูลของฟังก์ชัน `max()` ให้ใช้คำสั่งใดคำสั่งหนึ่งต่อไปนี้:

```
help(max)
?max
```

ให้ใช้ IPython Shell เปิดดู [เอกสาร](https://docs.python.org/3/library/functions.html#pow) ของฟังก์ชัน `pow()` โดยพิมพ์ `?pow` หรือ `help(pow)` แล้วกด **Enter**

ข้อใดต่อไปนี้ถูกต้อง?

`@possible_answers`
- `pow()` รับอาร์กิวเมนต์ 3 ตัว ได้แก่ `base`, `exp` และ `mod` หากไม่ระบุ `mod` ฟังก์ชันจะเกิดข้อผิดพลาด
- `pow()` ต้องการอาร์กิวเมนต์บังคับ 3 ตัว ได้แก่ `base`, `exp` และ `None`
- `pow()` ต้องการอาร์กิวเมนต์ `base` และ `exp` ส่วน `mod` เป็นอาร์กิวเมนต์ที่ไม่บังคับ
- `pow()` รับอาร์กิวเมนต์ 2 ตัว ได้แก่ `exp` และ `mod` หากไม่ระบุ `exp` จะเกิดข้อผิดพลาด

`@hint`
- อาร์กิวเมนต์ที่ไม่บังคับจะถูกกำหนดค่าเริ่มต้นด้วย `=` ซึ่งฟังก์ชันจะใช้ค่านั้นหากไม่ได้ระบุอาร์กิวเมนต์นั้นมา

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "ไม่ถูกต้องทีเดียว `mod` มีค่าเริ่มต้นที่จะถูกใช้หากท่านไม่ได้ระบุค่า"
msg2 = "ไม่ถูกต้อง `None` คือค่าเริ่มต้นสำหรับอาร์กิวเมนต์ `mod`"
msg3 = "ยอดเยี่ยม! การใช้ `help()` ช่วยให้ท่านเข้าใจวิธีการทำงานของฟังก์ชัน และปลดปล่อยศักยภาพสูงสุดของฟังก์ชันเหล่านั้นได้!"
msg4 = "ไม่ถูกต้อง `pow()` รับอาร์กิวเมนต์สามตัว โดยหนึ่งในนั้นมีค่าเริ่มต้น"
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## อาร์กิวเมนต์หลายตัว

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

ในแบบฝึกหัดก่อนหน้า เราได้ระบุอาร์กิวเมนต์ที่ไม่บังคับโดยดูจากเอกสารประกอบด้วย `help()` คราวนี้จะนำความรู้นั้นมาใช้เพื่อเปลี่ยนพฤติกรรมของฟังก์ชัน `sorted()`

ลองดู[เอกสารประกอบ](https://docs.python.org/3/library/functions.html#sorted) ของ `sorted()` โดยพิมพ์ `help(sorted)` ใน IPython Shell

จะเห็นว่า `sorted()` รับอาร์กิวเมนต์สามตัว ได้แก่ `iterable`, `key`, และ `reverse` ในแบบฝึกหัดนี้ต้องระบุเพียง `iterable` และ `reverse` เท่านั้น ไม่จำเป็นต้องระบุ `key`

มีลิสต์สองรายการเตรียมไว้ให้แล้ว

ลองนำลิสต์ทั้งสองมาต่อกัน แล้วเรียงลำดับจากมากไปน้อยดูสิ

`@instructions`
- ใช้ `+` เพื่อรวมเนื้อหาของ `first` และ `second` เข้าด้วยกันเป็นลิสต์ใหม่ชื่อ `full`
- เรียกใช้ `sorted()` กับ `full` และกำหนดอาร์กิวเมนต์ `reverse` ให้เป็น `True` จากนั้นบันทึกลิสต์ที่เรียงแล้วไว้ในชื่อ `full_sorted`
- สุดท้าย พิมพ์ `full_sorted` แสดงผลออกมา

`@hint`
- นำ `first` และ `second` มาบวกกันเหมือนกับตัวเลขสองตัว แล้วกำหนดผลลัพธ์ให้กับ `full`
- ใช้ `sorted()` โดยระบุอินพุตสองตัว ได้แก่ `full` และ `reverse=True`
- หากต้องการแสดงผลตัวแปร ให้ใช้ `print()`

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = ____ + ____

# Sort full in descending order: full_sorted
full_sorted = ____

# Print out full_sorted
____
```

`@solution`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปร `first` และ `second` ที่มีอยู่แล้ว"
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="โปรดตรวจสอบให้แน่ใจว่าคุณได้กำหนดผลลัพธ์จากการเรียกใช้ `sorted()` ให้กับ `full_sorted`"),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("ยอดเยี่ยม! ไปที่วิดีโอเกี่ยวกับเมธอดใน Python ได้เลย")
```

---

## เมธอด

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## เมธอดของ String

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

String มีเมธอดให้ใช้งานหลายตัว ทำตามคำแนะนำด้านล่างเพื่อลองใช้บางส่วนจากนั้น หากอยากศึกษาเพิ่มเติม สามารถพิมพ์ `help(str)` ใน IPython Shell ได้เลย

ตัวแปร `place` ชนิด string ถูกสร้างไว้ให้แล้วสำหรับการทดลองในแบบฝึกหัดนี้

`@instructions`
- เรียกใช้[เมธอด](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` บน `place` แล้วเก็บผลลัพธ์ไว้ในตัวแปร `place_up` โดยใช้ syntax การเรียกเมธอดที่เรียนไปในวิดีโอก่อนหน้า
- พิมพ์ `place` และ `place_up` ออกมา ทั้งสองตัวแปรเปลี่ยนแปลงไปหรือไม่?
- พิมพ์จำนวนตัวอักษร o ในตัวแปร `place` โดยเรียกใช้ `.count()` บน `place` และส่งตัวอักษร `'o'` เป็น input ของเมธอด — ที่กล่าวถึงคือตัวแปร `place` ไม่ใช่คำว่า `"place"`!

`@hint`
- สามารถเรียกใช้เมธอด `.upper()` บน `place` ได้โดยไม่ต้องใส่อาร์กิวเมนต์เพิ่มเติม
- หากต้องการพิมพ์ตัวแปร `x` ให้เขียน `print(x)`
- อย่าลืมครอบ `place.count(____)` ด้วยฟังก์ชัน `print()` เพื่อแสดงผลลัพธ์

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = 

# Print out place and place_up



# Print out the number of o's in place

```

`@solution`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

`@sct`
```{python}
msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบตัวแปรที่กำหนดไว้ล่วงหน้า"
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "อย่าลืมพิมพ์ `%s` ออกมาด้วย"
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="กรุณากำหนดผลลัพธ์ของการเรียก `place.upper()` ให้กับ `place_up`"),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "คุณคำนวณจำนวนตัวอักษร o ใน `place` ได้ถูกต้องแล้ว ขณะนี้โปรดตรวจสอบให้แน่ใจว่าได้ครอบการเรียก `place.count('o')` ด้วยฟังก์ชัน `print()` เพื่อพิมพ์ผลลัพธ์ออกมา"),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("ยอดเยี่ยม! สังเกตจากผลลัพธ์ที่พิมพ์ออกมาว่าเมธอด `upper()` ไม่ได้เปลี่ยนแปลงออบเจกต์ที่ถูกเรียกใช้ ซึ่งจะแตกต่างออกไปสำหรับรายการในแบบฝึกหัดถัดไป!")
```

---

## เมธอดของลิสต์

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

ใน Python ไม่ใช่แค่ String เท่านั้นที่มีเมธอด ลิสต์ ตัวเลขทศนิยม จำนวนเต็ม และบูลีน ก็มีเมธอดที่มีประโยชน์มากมายเช่นกัน ในแบบฝึกหัดนี้ จะได้ทดลองใช้งาน:

- `.index()` เพื่อหา index ของสมาชิกตัวแรกในลิสต์ที่ตรงกับค่าที่ระบุ และ
- `.count()` เพื่อนับจำนวนครั้งที่สมาชิกนั้นปรากฏในลิสต์

จะทำงานกับลิสต์ `areas` ซึ่งเก็บพื้นที่ของส่วนต่าง ๆ ในบ้าน

`@instructions`
- ใช้เมธอด `.index()` เพื่อหา index ของสมาชิกใน `areas` ที่มีค่าเท่ากับ `20.0` แล้วพิมพ์ค่านั้นออกมา
- เรียก `.count()` บน `areas` เพื่อตรวจสอบว่า `9.50` ปรากฏในลิสต์กี่ครั้ง แล้วพิมพ์ตัวเลขนั้นออกมา

`@hint`
- หากต้องการพิมพ์ค่า index ให้ครอบการเรียก `areas.index(___)` ด้วยฟังก์ชัน `print()`
- หากต้องการพิมพ์จำนวนครั้งที่สมาชิก `x` ปรากฏในลิสต์ ให้ครอบการเรียก `areas.count(___)` ด้วยฟังก์ชัน `print()`

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 9.50 appears in areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "คุณไม่จำเป็นต้องเปลี่ยนแปลงหรือลบรายการที่กำหนดไว้ล่วงหน้า `areas`"

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("ดีมาก! นี่คือตัวอย่างของเมธอด `list` ที่ไม่ได้เปลี่ยนแปลงรายการที่ถูกเรียกใช้")
```

---

## เมธอดของลิสต์ (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

เมธอดส่วนใหญ่ของลิสต์จะเปลี่ยนแปลงลิสต์ที่ถูกเรียกใช้โดยตรง ตัวอย่างเช่น:

- `.append()` ใช้เพิ่มสมาชิกเข้าไปในลิสต์
- `.remove()` ใช้[ลบ](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)สมาชิกตัวแรกในลิสต์ที่ตรงกับค่าที่ระบุ
- `.reverse()` ใช้[สลับ](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)ลำดับของสมาชิกในลิสต์

ในแบบฝึกหัดนี้จะทำงานกับลิสต์ `areas` ที่เก็บพื้นที่ของแต่ละส่วนในบ้าน

`@instructions`
- ใช้ `.append()` สองครั้งเพื่อเพิ่มขนาดของห้องพักริมสระน้ำและโรงรถอีกครั้ง ได้แก่ `24.5` และ `15.45` ตามลำดับ โดยเพิ่มตามลำดับนี้
- แสดงค่า `areas`
- ใช้เมธอด `.reverse()` เพื่อสลับลำดับสมาชิกใน `areas`
- แสดงค่า `areas` อีกครั้ง

`@hint`
- สำหรับคำแนะนำข้อแรก ให้ใช้คำสั่ง `areas.append(___)` สองครั้ง
- หากต้องการแสดงค่าตัวแปร `x` ให้เขียน `print(x)`
- เมธอด `.reverse()` ไม่ต้องการอาร์กิวเมนต์เพิ่มเติม ใช้เพียง dot notation กับวงเล็บเปล่า: `.reverse()`
- หากต้องการแสดงค่าตัวแปร `x` ให้เขียน `print(x)`

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out areas


# Reverse the orders of the elements in areas


# Print out areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

`@sct`
```{python}
Ex().multi(
  check_function("areas.append", index=0, signature=False).check_args(0).has_equal_value(),
  check_function("areas.append", index=1, signature=False).check_args(0).has_equal_value(),
  check_function("print", index=0).check_args(0).has_equal_ast(),
  check_function("areas.reverse", index=0, signature=False),
  check_function("print", index=1).check_args(0).has_equal_ast()
)

success_msg("ยอดเยี่ยม!")
```

---

## แพ็กเกจ

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Import แพ็กเกจ

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

สมมติว่าต้องการคำนวณเส้นรอบวงและพื้นที่ของวงกลม สูตรที่ใช้มีดังนี้:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

แทนที่จะพิมพ์ค่าตัวเลขของ `pi` เอง สามารถใช้แพ็กเกจ `math` ซึ่งมีค่าคงที่นี้อยู่แล้ว

สำหรับข้อมูลเพิ่มเติม `**` คือสัญลักษณ์สำหรับการยกกำลัง เช่น `3**4` หมายถึง `3` ยกกำลัง `4` ซึ่งได้ผลลัพธ์เป็น `81`

`@instructions`
- Import แพ็กเกจ `math`
- ใช้ `math.pi` คำนวณเส้นรอบวงของวงกลม แล้วเก็บผลลัพธ์ไว้ในตัวแปร `C`
- ใช้ `math.pi` คำนวณพื้นที่ของวงกลม แล้วเก็บผลลัพธ์ไว้ในตัวแปร `A`

`@hint`
- ใช้ `import math` จากนั้นอ้างอิงค่า `pi` ด้วย `math.pi`
- ใช้สมการในโจทย์เพื่อหาค่า `C` โดยใช้ `*`
- ใช้สมการในโจทย์เพื่อหาค่า `A` โดยใช้ `*` และ `**`

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import the math package
import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "การคำนวณ `%s` ของท่านยังไม่ถูกต้อง โปรดตรวจสอบให้แน่ใจว่าได้ใช้ `math.pi`"
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:โปรดคงคำสั่ง `{{sol_call}}` ไว้เพื่อแสดงผลเส้นรอบวง"),
  has_printout(1, not_printed_msg = "__JINJA__:โปรดคงคำสั่ง `{{sol_call}}` ไว้เพื่อแสดงผลพื้นที่")
)

success_msg("ยอดเยี่ยม! หากท่านทราบวิธีใช้งานฟังก์ชันจากแพ็กเกจต่าง ๆ ท่านก็จะสามารถใช้ประโยชน์จากพลังของนักพัฒนา Python จำนวนมากได้อย่างเต็มที่!")
```

---

## การนำเข้าแบบเจาะจง

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

การนำเข้าแบบทั่วไป เช่น `import math` จะทำให้ใช้งานฟังก์ชันทั้งหมดจากแพ็กเกจ `math` ได้ทุกอย่าง แต่ถ้าต้องการใช้เพียงบางส่วนของแพ็กเกจ สามารถนำเข้าแบบเจาะจงได้:

```
from math import pi
```

ลองทำแบบเดิมอีกครั้ง แต่คราวนี้ให้นำเข้าเฉพาะ `pi` เท่านั้น

`@instructions`
- นำเข้าแบบเจาะจงจากแพ็กเกจ `math` โดยนำเข้าเฉพาะฟังก์ชัน `pi`
- ใช้ `pi` คำนวณเส้นรอบวงของวงกลม แล้วเก็บผลลัพธ์ไว้ในตัวแปร `C`
- ใช้ `pi` คำนวณพื้นที่ของวงกลม แล้วเก็บผลลัพธ์ไว้ในตัวแปร `A`

`@hint`
- ใช้ `from math import pi` เพื่อนำเข้าแบบเจาะจง
- จากนั้นสามารถใช้ `pi` ได้โดยตรงเลย!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import pi function of math package
from math import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "การคำนวณ `%s` ของท่านยังไม่ถูกต้อง โปรดตรวจสอบให้แน่ใจว่าใช้เฉพาะ `pi` เท่านั้น"

Ex().has_import("math.pi", not_imported_msg = "โปรดนำเข้า `pi` จากแพ็กเกจ `math` ท่านควรใช้รูปแบบ `from ___ import ___`",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:โปรดคงไว้ซึ่ง `{{sol_call}}` เพื่อแสดงผลค่าเส้นรอบวง"),
  has_printout(1, not_printed_msg = "__JINJA__:โปรดคงไว้ซึ่ง `{{sol_call}}` เพื่อแสดงผลค่าพื้นที่")
)

success_msg("ยอดเยี่ยม! ดำเนินการไปยังแบบฝึกหัดถัดไปได้เลย")
```

---

## วิธีการ import ที่แตกต่างกัน

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

มีหลายวิธีในการ import แพ็กเกจและโมดูลเข้าสู่ Python โดยขึ้นอยู่กับคำสั่ง import ที่ใช้ โค้ด Python ที่ต้องเขียนก็จะแตกต่างกันออกไป

สมมติว่าต้องการใช้ [ฟังก์ชัน](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()` ซึ่งอยู่ใน subpackage `linalg` ของแพ็กเกจ `scipy` โดยต้องการเรียกใช้ฟังก์ชันนี้ในรูปแบบต่อไปนี้:

```
my_inv([[1,2], [3,4]])
```

ต้องใช้คำสั่ง `import` แบบใดจึงจะรันโค้ดข้างต้นได้โดยไม่เกิดข้อผิดพลาด?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- ลองใช้คำสั่ง import แต่ละแบบใน IPython shell แล้วดูว่าแบบไหนทำให้บรรทัด `my_inv([[1, 2], [3, 4]])` รันได้โดยไม่เกิดข้อผิดพลาด กด **enter** เพื่อรันโค้ดที่พิมพ์ไว้

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "ไม่ถูกต้อง ลองอีกครั้ง ลองใช้คำสั่ง import ที่แตกต่างกันใน IPython shell และดูว่าคำสั่งใดทำให้บรรทัด `my_inv([[1, 2], [3, 4]])` ทำงานได้โดยไม่เกิดข้อผิดพลาด"
msg4 = "ถูกต้อง! คำว่า `as` ช่วยให้คุณสามารถสร้างชื่อในเครื่องสำหรับฟังก์ชันที่คุณนำเข้า: ขณะนี้ `inv()` สามารถใช้งานได้ในชื่อ `my_inv()` แล้ว"
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```
