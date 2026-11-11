---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/vi-VN/423d5444-bde9-428b-86ca-ede7dd6ef603-7bee3d51707d2f9021eafb58822bb786.mp3
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
Bạn đã làm rất tốt. Chào mừng bạn quay trở lại. Rõ ràng Python là một công cụ tính toán tuyệt vời. Nhưng nếu muốn thực hiện các phép tính phức tạp hơn, chúng ta sẽ cần phải lưu các giá trị khi viết code. 

---

## Biến

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Tên cụ thể, phân biệt chữ hoa chữ thường

- Truy xuất giá trị thông qua tên biến{{1}}

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
Chúng ta có thể làm việc đó bằng cách định nghĩa một biến, với một cái tên cụ thể, có phân biệt chữ hoa chữ thường. Khi đã tạo (hay khai báo) biến đó, về sau ta chỉ cần gõ tên biến để truy xuất giá trị của nó.

Giả sử bạn đo chiều cao và cân nặng tính theo mét: bạn cao một phẩy bảy mưới chín mét và nặng sáu mươi tám phẩy bảy ki-lô-gam. Bạn có thể gán các giá trị này cho hai biến, tên là height và weight, bằng dấu bằng:

Bây giờ nếu bạn gõ tên biến, height,

Python sẽ tìm tên biến, truy xuất giá trị của nó và hiển thị ra.

---

## Tính BMI

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
Giờ hãy tính chỉ số khối cơ thể, hay BMI. Công thức với cân nặng tính bằng ki-lô-gam và chiều cao tính bằng mét như sau. Ta có thể tính trực tiếp với các giá trị cụ thể, nhưng cũng có thể dùng các biến height và weight như ở đây. Mỗi lần ta nhập tên biến, Python sẽ thay thế tên đó bằng giá trị hiện có của biến. weight tương ứng với sáu mươi tám phẩy bảy, và height tương ứng với một phẩy bảy mươi chín. 

Cuối cùng, trong phiên bản này, Python sẽ lưu kết quả vào một biến mới là biến bmi. Giờ bmi chứa cùng giá trị với kết quả phép tính trước đó.

Trong Python, biến được sử dụng thường xuyên. Chúng giúp ta dễ dàng chạy lại code và thu được kết quả nhất quán.
---

## Khả năng tái lập

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
Giả sử đoạn code tạo các biến height, weight và bmi nằm trong một script như thế này. Nếu giờ ta muốn tính bmi cho một cân nặng khác,

---

## Khả năng tái lập

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
ta chỉ cần thay đổi phần khai báo biến weight và chạy lại script. Giá trị bmi sẽ thay đổi tương ứng, vì giá trị của biến weight cũng đã thay đổi.

Cho đến giờ, ta mới chỉ làm việc với các giá trị số, như chiều cao và cân nặng.

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
Trong Python, các con số này đều có kiểu dữ liệu cụ thể. Ta có thể kiểm tra kiểu dữ liệu của một giá trị bằng hàm type. Để xem kiểu của giá trị bmi, chỉ cần viết type rồi sau đó viết bmi trong dấu ngoặc đơn. Bạn sẽ thấy đó là float, tức là một số thực. Đây là cách Python biểu thị số thực, tức số có cả phần nguyên và phần thập phân. Python cũng có kiểu dữ liệu cho số nguyên là int, như ví dụ này.                                  

Tuy nhiên để làm khoa học dữ liệu, chúng ta cần nhiều kiểu dữ liệu hơn là chỉ int và float.

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

String là kiểu dữ liệu văn bản. Ta có thể dùng dấu ngoặc kép hoặc ngoặc đơn để tạo một string, như trong các ví dụ này. Nếu cho hiển thị kiểu dữ liệu của biến cuối cùng ở đây, ta sẽ thấy đó là str, viết tắt của string. 

Boolean là kiểu dữ liệu chỉ có thể là True hoặc False, giống như “Có” và “Không” trong ngôn ngữ hằng ngày. Boolean sẽ rất hữu ích sau này, chẳng hạn như để lọc dữ liệu.


Có một điều đặc biệt về các kiểu dữ liệu trong Python.

---

## Các kiểu biến trong Python (3)

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

- Kiểu khác = hoạt động khác{{3}}

`@script`
Hãy xem dòng code này, cộng hai số nguyên, và dòng code này, cộng hai string.

Với số nguyên, các giá trị được cộng lại, còn với string, các chuỗi được ghép nối lại với nhau. Tuỳ theo kiểu dữ liệu mà toán tử cộng hoạt động khác nhau. Đây là một nguyên tắc chung. Code hoạt động như thế nào phụ thuộc vào kiểu dữ liệu mà ta đang làm. 

Trong các bài tập tiếp theo, bạn sẽ tạo những biến đầu tiên và thử nghiệm với một số kiểu dữ liệu của Python. Hẹn gặp bạn ở video tiếp theo, ở đó, mình sẽ giải thích mọi thứ về kiểu dữ liệu list.

---

## Hãy cùng luyện tập!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Cùng bắt tay vào code nào. Mình rất mong chờ được gặp bạn ở chương tiếp theo, ở đó bạn sẽ tạo ra nhiều biểu đồ Python ấn tượng hơn nữa. 
