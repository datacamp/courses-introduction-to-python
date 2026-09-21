---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/th-TH/2a79323c-4232-4fb0-b6a4-bbbb42946f65-888c5fbf0832d185fb57c3279b52917a.mp3
---

## Hello Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
สวัสดีครับ ผมชื่อ Hugo และจะเป็นผู้สอนในคอร์ส Introduction to Python for Data Science

ผมเป็น data scientist และนักการศึกษาที่ DataCamp ครับ

---

## วิธีการเรียนรู้

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp Interface](https://assets.datacamp.com/img/translations/th-TH/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
ในคอร์สนี้ คุณจะได้เรียน Python สำหรับ Data Science ผ่านวิดีโอบทเรียนอย่างที่กำลังดูอยู่ และแบบฝึกหัดเชิงโต้ตอบ คุณจะมี Python session เป็นของตัวเอง ซึ่งสามารถทดลองเขียนโค้ดและหาคำตอบที่ถูกต้องตามโจทย์ที่กำหนดได้เลย การเรียนในแบบลงมือทำ พร้อมรับ feedback ที่ตรงจุดและทันที จะช่วยให้พัฒนาทักษะได้อย่างรวดเร็ว

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/th-TH/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- ใช้งานได้ทั่วไป: สร้างได้ทุกอย่าง{{2}}

- โอเพนซอร์ส! ฟรี!{{3}}

- แพ็กเกจ Python รวมถึงด้าน Data Science{{4}}

	- ใช้ได้หลากหลายสาขาและงาน{{5}}

`@script`
Python ถูกสร้างขึ้นโดย Guido Van Rossum และในภาพนี้คือผมกับ Guido ครับ จากที่เริ่มต้นเป็นเพียงโปรเจกต์งานอดิเรก ก็ค่อย ๆ พัฒนากลายเป็นภาษาโปรแกรมที่ใช้ได้ในวงกว้าง ปัจจุบันสามารถใช้ Python สร้างซอฟต์แวร์ได้แทบทุกประเภท แล้วเหตุใดจึงเป็นเช่นนั้น? ประการแรก Python เป็น open source และใช้งานได้ฟรี ประการที่สอง การสร้างแพ็กเกจใน Python ทำได้ไม่ยาก แพ็กเกจคือโค้ดที่แชร์ให้ผู้อื่นนำไปแก้ปัญหาเฉพาะด้านได้ ตลอดหลายปีที่ผ่านมา มีแพ็กเกจสำหรับ Data Science เกิดขึ้นมากมาย อยากสร้างกราฟวิเคราะห์ยอดขายของบริษัท ก็มีแพ็กเกจรองรับ อยากเชื่อมต่อฐานข้อมูลเพื่อวิเคราะห์ข้อมูลจากเซ็นเซอร์ ก็มีแพ็กเกจสำหรับสิ่งนั้นเช่นกัน หลายคนมักบอกว่า Python คือภาษาโปรแกรมที่ทำได้เกือบทุกอย่าง ในคอร์สนี้ เราจะค่อย ๆ สร้างทักษะการเขียนโค้ดสำหรับ Data Science ไปทีละขั้น อย่าพึ่งไปไหนนะครับ เพราะภาษานี้มีพลังมากกว่าที่คิด

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**รันคำสั่ง Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/th-TH/q1/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg = 95)

`@script`
เมื่อรู้จัก Python พอสมควรแล้ว มาเริ่มทดลองกันเลย โดยจะเริ่มที่

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**รันคำสั่ง Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/th-TH/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python shell ซึ่งเป็นพื้นที่สำหรับพิมพ์โค้ด Python และดูผลลัพธ์ได้ทันที ในหน้าแบบฝึกหัดของ DataCamp shell นี้จะอยู่ตรงนี้ครับ มาเริ่มด้วยสิ่งง่าย ๆ โดยใช้ Python เป็นเครื่องคิดเลขกัน

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![การคำนวณใน IPython Shell ของ DataCamp](https://assets.datacamp.com/img/translations/th-TH/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
ลองพิมพ์ 4 + 5 แล้วกด Enter Python จะประมวลผลสิ่งที่พิมพ์และแสดงคำตอบออกมาเป็น 9 Shell ที่ใช้ในคอร์สนี้ไม่ใช่ Python shell ดั้งเดิม แต่เป็น IPython ซึ่งย่อมาจาก Interactive Python กล่าวคือเป็น Python เวอร์ชันที่ปรับปรุงให้ทรงพลังยิ่งขึ้น และจะมีประโยชน์มากในภายหลัง

IPython สร้างขึ้นโดย Fernando Pérez และเป็นส่วนหนึ่งของ Jupyter ecosystem นอกจากการทำงานแบบ interactive แล้ว ยังสามารถให้ Python รันสิ่งที่เรียกว่า

---

## Python Script

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- ไฟล์ข้อความ - `.py`{{1}}

- รายการคำสั่ง Python{{2}}

- คล้ายกับการพิมพ์ใน IPython Shell{{3}}

![Python script ใน DataCamp](https://assets.datacamp.com/img/translations/th-TH/q1/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
Python script ได้ด้วย Python script คือไฟล์ข้อความที่มีนามสกุล .py โดยพื้นฐานแล้ว มันคือรายการคำสั่ง Python ที่รันต่อเนื่องกัน คล้ายกับการพิมพ์คำสั่งลงใน shell ทีละบรรทัดนั่นเอง

---

## Python Script

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: พิมพ์ 4 + 5 ใน script แล้วกดส่งคำตอบ โดยไม่มีผลลัพธ์แสดง](https://assets.datacamp.com/img/translations/th-TH/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
มาลองนำคำสั่งเมื่อกี้ใส่ใน script กัน ซึ่งจะอยู่ตรงนี้ในหน้าแบบฝึกหัดของ DataCamp ขั้นตอนถัดไปคือการรัน script โดยคลิก "ส่งคำตอบ" ถ้ารัน script นี้แล้ว จะสังเกตว่าไม่มีอะไรแสดงในช่องผลลัพธ์ นั่นเป็นเพราะต้องใช้คำสั่ง print อย่างชัดเจนใน script หากต้องการให้แสดงผลลัพธ์ระหว่างการรัน

---

## Python Script

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/th-TH/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- ใช้ `print()` เพื่อแสดงผลลัพธ์จาก script

`@script`
มาครอบการคำนวณก่อนหน้าด้วย print แล้วรัน script อีกครั้ง คราวนี้ได้ผลลัพธ์เหมือนเดิม การเขียนโค้ดลงใน Python script แทนการพิมพ์ซ้ำทุกครั้งจะช่วยให้โค้ดเป็นระเบียบและประหยัดเวลา เมื่อต้องการแก้ไข ก็แค่แก้ใน script แล้วรันใหม่ทั้งหมดได้เลย

---

## DataCamp Interface

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![ภาพหน้าจอของ DataCamp Interface](https://assets.datacamp.com/img/translations/th-TH/q1/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg)

`@script`
ตอนนี้รู้จักวิธีทำงานกับ Python หลายแบบแล้ว ลองไปทำแบบฝึกหัดกัน ใช้ IPython Shell สำหรับทดลอง และใช้ Python script editor สำหรับเขียนคำตอบจริง เมื่อคลิก "ส่งคำตอบ" script จะถูกรันและตรวจสอบความถูกต้องทันที

---

## มาฝึกกันเถอะ!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
มาเริ่มเขียนโค้ดกัน และอย่าลืมสนุกไปกับมันด้วยนะครับ!
