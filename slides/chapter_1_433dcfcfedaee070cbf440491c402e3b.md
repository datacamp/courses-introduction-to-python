---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/vi-VN/2bcc24ee-be10-4d37-9e9f-f878532e186b.mp3
---

## Biến và Kiểu dữ liệu

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Bạn đã làm rất tốt và chào mừng bạn quay trở lại! Rõ ràng Python là một công cụ tính toán tuyệt vời. Nhưng nếu muốn thực hiện các phép tính phức tạp hơn, bạn sẽ cần phải “lưu” các giá trị khi viết code.
---

## Biến

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Tên cụ thể, phân biệt chữ hoa chữ thường

- Gọi giá trị thông qua tên biến{{1}}

- 1,79 m - 68,7 kg{{2}}

```py
height = 1.79
weight = 68.7
```{{3}}
```py
height
```{{4}}

```out
1.79
```{{4}}

`@script`
Bạn có thể làm việc đó bằng cách định nghĩa một biến, với một cái tên cụ thể, có phân biệt chữ hoa chữ thường. Khi đã tạo (hay khai báo) biến đó, về sau bạn chỉ cần gõ tên biến để lấy lại giá trị của nó.

Giả sử bạn đo chiều cao và cân nặng tính theo mét: bạn cao 1,79 mét và nặng 68,7 ki-lô-gam. Bạn có thể gán các giá trị này cho hai biến, tên là height và weight, bằng cách sử dụng dấu bằng:

Bây giờ nếu bạn gõ tên biến, height,

Python sẽ tìm tên biến, lấy giá trị của nó và hiển thị ra.
---

## Tính chỉ số BMI

```yaml
type: TwoColumns
key: fe1b10a93b
code_zoom: 80
```

`@part1`
```py
height = 1.79
weight = 68.7
```
```py
height
```

```out
1.79
```

$$ \text{BMI} = \frac{\text{weight}}{\text{height}^2} $${{1}}

`@part2`
```py
68.7 / 1.79 ** 2
```{{2}}

```out
21.4413
```{{2}}

```py
weight / height ** 2
```{{3}}

```out
21.4413
```{{3}}

```py
bmi = weight / height ** 2
bmi
```{{4}}

```out
21.4413
```{{4}}

`@script`
Giờ hãy tính chỉ số khối cơ thể, hay BMI. Công thức với cân nặng tính bằng ki-lô-gam và chiều cao tính bằng mét như sau. Bạn có thể dùng giá trị thực, nhưng cũng có thể dùng các biến height và weight như ở đây. Mỗi lần bạn gõ tên biến, bạn đang yêu cầu Python thay nó bằng giá trị hiện có của biến. weight tương ứng với 68,7, và height tương ứng với 1,79. 


Cuối cùng, phiên bản này sẽ yêu cầu Python lưu kết quả vào một biến mới là biến bmi. Giờ bmi chứa giá trị giống như kết quả phép tính trước đó.

Trong Python, biến được sử dụng mọi lúc mọi nơi. Chúng giúp ta tái sử dụng và dễ chỉnh sửa code.
---

## Có thể tái sử dụng code!

```yaml
type: FullSlide
key: 9980f47f9d
```

`@part1`
```py
height = 1.79
weight = 68.7
bmi = weight / height ** 2
print(bmi)
```

```out
21.4413
```

`@script`
Giả sử đoạn code tạo các biến height, weight và bmi nằm trong một script như thế này. Nếu giờ bạn muốn tính bmi cho một cân nặng khác,
---

## Có thể tái sử dụng code!

```yaml
type: FullSlide
key: a4e899f00f
disable_transition: true
```

`@part1`
```py
height = 1.79
weight = 74.2 # <-
bmi = weight / height ** 2
print(bmi)
```

```out
23.1578
```

`@script`
bạn chỉ cần thay đổi phần khai báo biến weight và chạy lại script. Giá trị bmi sẽ thay đổi tương ứng, vì giá trị của biến weight cũng đã thay đổi.

Cho đến lúc này, ta mới làm việc với các giá trị số, như chiều cao và cân nặng.
---

## Các kiểu dữ liệu trong Python

```yaml
type: FullSlide
key: 9d86084ad4
```

`@part1`
```py
type(bmi)
```{{1}}

```out
float
```{{1}}

```py
day_of_week = 5
type(day_of_week)
```{{2}}

```out
int
```{{2}}

`@script`
Trong Python, các con số này đều có kiểu dữ liệu cụ thể. Bạn có thể kiểm tra kiểu dữ liệu của một giá trị bằng hàm type. Để xem kiểu của giá trị bmi, chỉ cần viết type rồi sau đó viết bmi trong dấu ngoặc đơn. Bạn sẽ thấy đó là float, tức là một số thực. Đây là cách Python biểu thị số thực, tức số có cả phần nguyên và phần thập phân. Python cũng có kiểu dữ liệu cho số nguyên là int, như ví dụ này.                                  

Tuy nhiên để làm khoa học dữ liệu, bạn sẽ cần nhiều hơn là chỉ int và float.
---

## Các kiểu dữ liệu trong Python (2)

```yaml
type: FullSlide
key: d971d34e6a
```

`@part1`
```py
x = "body mass index"
y = 'this works too'
```{{1}}
```py
type(y)
```{{2}}

```out
str
```{{2}}

```py
z = True
type(z)
```{{3}}

```out
bool
```{{3}}

`@script`
Python có rất nhiều kiểu dữ liệu khác nhau. Phổ biến nhất là string và boolean.

String là kiểu dữ liệu văn bản. Bạn có thể dùng dấu ngoặc kép hoặc ngoặc đơn để tạo một string, như trong các ví dụ này. Nếu bạn cho hiển thị kiểu dữ liệu của biến cuối cùng ở đây, bạn sẽ thấy đó là str, viết tắt của string. 

Boolean là kiểu dữ liệu chỉ có thể là True hoặc False, giống như “Có” và “Không” trong ngôn ngữ hằng ngày. Boolean sẽ rất hữu ích sau này, ví dụ như để lọc dữ liệu.


Có một điều đặc biệt về các kiểu dữ liệu trong Python.
---

## Các kiểu dữ liệu trong Python (3)

```yaml
type: FullSlide
key: 24601e2af0
```

`@part1`
```py
2 + 3
```{{1}}

```out
5
```{{1}}

```py
'ab' + 'cd'
```{{2}}

```out
'abcd'
```{{2}}

- Kiểu dữ liệu khác nhau = hành vi khác nhau!{{3}}

`@script`
Hãy xem dòng code này cộng hai số nguyên, và dòng code kia cộng hai string.

Với số nguyên, các giá trị được cộng lại, còn với string, các chuỗi được ghép nối lại với nhau. Tuỳ theo kiểu dữ liệu mà toán tử cộng hoạt động khác nhau. Đây là một nguyên tắc chung: code hoạt động như thế nào phụ thuộc vào kiểu dữ liệu mà bạn đang làm. 

Trong các bài tập tiếp theo, bạn sẽ tạo những biến đầu tiên và thử nghiệm với một số kiểu dữ liệu của Python. Hẹn gặp bạn ở video tiếp theo, ở đó, mình sẽ giải thích mọi thứ về kiểu dữ liệu list.
---

## Cùng thực hành nào!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Cùng bắt tay vào code nào. Mình rất mong chờ được gặp bạn ở chương tiếp theo, ở đó bạn sẽ tạo ra những biểu đồ trong Python ấn tượng hơn nữa.
