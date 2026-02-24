---
title_meta: Chương 1
title: Các khái niệm cơ bản về Python
description: >-
  Giới thiệu các khái niệm cơ bản của Python. Học cách dùng Python qua bài tập
  tương tác và qua script. Tạo biến đầu tiên và làm quen với các kiểu dữ liệu cơ
  bản của Python.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Xin chào Python!
  - nb_of_exercises: 5
    title: Biến và Kiểu dữ liệu
---

## Xin chào Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Đoạn code Python đầu tiên của bạn

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Đã đến lúc chạy đoạn code Python đầu tiên của bạn!

Chuyển sang khung code và nhấn nút **Run Code** để xem kết quả.

`@instructions`
- Nhấn nút **Run Code** để xem kết quả của `print(5 / 8)`.

`@hint`
- Chạy code trước khi gửi câu trả lời để có thời gian xem kết quả.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Bạn đã sử dụng `{{sol_call}}` để in ra `5 / 8` chưa?")
success_msg("Tuyệt vời! Chuyển sang câu tiếp theo!")
```

---

## Python như một máy tính

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python rất phù hợp để thực hiện các phép tính cơ bản. Nó có thể cộng, trừ, nhân và chia.

Đoạn code trong script đưa ra một vài ví dụ.

Giờ đến lượt bạn luyện tập bằng cách tự viết code một chút.

`@instructions`
- Hiển thị kết quả của phép trừ `5` cho `5` bên dưới `# Subtraction` bằng hàm `print()`.
- Hiển thị kết quả của phép nhân `3` với `5` bên dưới `# Multiplication`.

`@hint`
- Bạn sẽ cần dùng hàm `print()` để tạo đầu ra.
- Bạn có thể trừ với dấu `-` và nhân với dấu `*`.

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
Ex().has_printout(0, not_printed_msg = "Bạn đã sử dụng `print(4 + 5)` để in ra kết quả của phép cộng chưa?")

Ex().has_printout(1, not_printed_msg = "Bạn đã sử dụng `print(5 - 5)` để in ra kết quả của phép trừ chưa?")

Ex().has_printout(2, not_printed_msg = "Bạn đã sử dụng `print(3 * 5)` để in ra kết quả của phép nhân chưa?")

Ex().has_printout(3, not_printed_msg = "Bạn đã sử dụng `print(10 / 2)` để in ra kết quả của phép chia chưa?")

success_msg("Đúng rồi! Python có thể giúp bạn thực hiện các phép toán, một đặc điểm sẽ hữu ích cho việc phân tích khi chúng ta phát triển kỹ năng dữ liệu của mình.")
```

---

## Biến và Kiểu dữ liệu

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Gán giá trị cho biến

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Trong Python, một biến cho phép bạn tham chiếu đến một giá trị bằng một tên. Để tạo biến `x` với giá trị `5`, bạn dùng dấu `=`, như ví dụ sau:

```
x = 5
```

Giờ bạn có thể dùng tên biến này, `x`, thay cho giá trị thực tế là `5`.

Hãy nhớ, `=` trong Python có nghĩa là gán giá trị (_assignment_), không phải để kiểm tra bằng nhau! Hãy thử trong bài tập bằng cách thay `____` bằng mã lệnh của bạn.

`@instructions`
- Tạo một biến `savings` với giá trị `100`.
- Kiểm tra biến này bằng cách gõ `print(savings)` trong script.

`@hint`
- Gõ `savings = 100` để tạo biến `savings`.
- Sau khi tạo biến `savings`, gõ `print(savings)`.
- Mã lệnh cuối cùng của bạn không được chứa bất kỳ `____` nào.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Gán `100` cho biến `savings`.")
Ex().has_printout(0, not_printed_msg = "In ra `savings`, biến bạn đã tạo, với `print(savings)`.")
success_msg("Tuyệt vời! Bây giờ hãy thử thực hiện một số phép tính với biến này!")
```

---

## Tính toán với các biến

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Bạn đã tạo một biến số tiền tiết kiệm, hãy bắt đầu tiết kiệm thôi!

Thay vì tính trực tiếp với các giá trị cụ thể, bạn có thể dùng các biến.

Bốn tháng nữa bạn sẽ tiết kiệm được bao nhiêu tiền nếu mỗi tháng bạn tiết kiệm $10?

`@instructions`
- Tạo biến `monthly_savings` bằng `10` và `num_months` bằng `4`.
- Nhân `monthly_savings` với `num_months` và gán cho `new_savings`.
- Hiển thị kết quả của `new_savings`.

`@hint`
- Bạn có thể tính toán với các biến giống như với số, thay vì `10 * 4`, hãy thay số bằng các biến!
- Dùng `print()` để xem giá trị trong `new_savings`.
- Lưu ý ý viết đúng tên biến!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Bạn đã lưu `10` vào `monthly_savings` bằng cách sử dụng `monthly_savings = 10` chưa?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Bạn đã lưu `4` vào `num_months` bằng cách sử dụng `num_months = 4` chưa?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Bạn đã sử dụng đúng biến và ký hiệu để nhân chưa? Dự kiến `monthly_savings * num_months` nhưng đã nhận được cái gì đó khác.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Bạn đã sử dụng đúng biến và ký hiệu để cộng chưa? Dự kiến `savings + new_savings` nhưng đã nhận được cái gì đó khác.")

Ex().has_printout(0, not_printed_msg="Hãy nhớ in ra `new_savings` ở cuối kịch bản của bạn.")

success_msg("Bạn có $40 trong khoản tiết kiệm mới!")
```

---

## Các kiểu biến khác

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

Trong bài trước, bạn đã thực hành với kiểu dữ liệu số nguyên của Python:

- `int`, hay integer: một số không có phần thập phân. Ví dụ như `savings` với giá trị `100` là số nguyên.

Ngoài các kiểu dữ liệu số, còn có ba kiểu dữ liệu rất phổ biến khác:

- `float` hay floating point: một số có cả phần nguyên và phần thập phân, ngăn cách bằng dấu chấm. Ví dụ `1.1` là float.
- `str`, hay string: kiểu dùng để biểu diễn văn bản. Bạn có thể dùng dấu nháy đơn hoặc nháy kép để tạo string.
- `bool`, hay boolean: kiểu dùng để biểu diễn giá trị logic. Nó chỉ có thể là `True` hoặc `False` (chú ý viết hoa chữ cái đầu và viết thường các chữ cái sau rất quan trọng!)

`@instructions`
- Tạo một float mới, `half`, với giá trị `0.5`.
- Tạo một string mới, `intro`, với giá trị `"Hello! How are you?"`.
- Tạo một boolean mới, `is_good`, với giá trị `True`.

`@hint`
- Để tạo một biến trong Python, dùng `=`. Nhớ đặt string trong cặp dấu nháy đơn hoặc nháy kép.
- Chỉ có hai giá trị boolean trong Python: `True` và `False`. Các biến thể như `TRUE`, `true`, `FALSE`, `false` và những kiểu viết khác sẽ không được chấp nhận.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Bạn đã lưu giá trị float, `0.5` vào `half` chưa?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, có gì đó không đúng trong biến `intro` của bạn. Kiểm tra lại chính tả và đảm bảo rằng bạn đã sử dụng dấu ngoặc kép.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Bạn đã viết hoa giá trị boolean chưa? Hãy nhớ rằng bạn không cần sử dụng dấu ngoặc kép ở đây.")

success_msg("Tuyệt vời!")
```

---

## Phép toán với các kiểu dữ liệu khác

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Biến trong Python có nhiều kiểu khác nhau. Bạn có thể xem kiểu của một biến bằng cách dùng hàm `type()`. Ví dụ, để xem kiểu của `a`, chạy hàm: `type(a)`.

Các kiểu dữ liệu khác nhau sẽ hoạt động khác nhau trong Python. Chẳng hạn khi bạn cộng hai string, Python sẽ xử lý khác so với khi cộng hai float hoặc cộng hai boolean.

Giờ bạn hãy tự kiểm chứng điều này.

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
- Cộng `savings` và `new_savings` rồi gán cho `total_savings`.
- Dùng `type()` để hiển thị ra kiểu dữ liệu của `total_savings`.

`@hint`
- Gán `savings + new_savings` cho một biến mới, `total_savings`.
- Để hiển thị kiểu dữ liệu của biến `x`, dùng `print(type(x))`.

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
msg = "Bạn không cần phải thay đổi hoặc xóa các biến được định nghĩa trước."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Cộng `savings` và `new_savings` để tạo biến `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Sử dụng `{{sol_call}}` để in ra kiểu của `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Tính tổng của `intro` và `intro` rồi gán kết quả cho `doubleintro`.
- Hiển thị ra kết quả của `doubleintro`. Bạn có đoán trước điều này không?

`@hint`
- Gán `intro + intro` cho một biến mới, `doubleintro`.
- Để hiển thị ra biến `x`, viết `print(x)` trong script.

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
msg = "Bạn không cần phải thay đổi hoặc xóa các biến được định nghĩa trước."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Bạn đã lưu kết quả của `intro + intro` vào `doubleintro` chưa?"),
    has_printout(0, not_printed_msg = "Đừng quên in ra `doubleintro`.")
)

success_msg("Tốt lắm. Lưu ý cách `intro + intro` khiến `\"Hello! How are you?\"` và `\"Hello! How are you?\"` được ghép lại với nhau.")
```
