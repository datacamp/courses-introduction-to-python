---
title_meta: Chương 3
title: Hàm và Thư mục (Package)
description: >-
  Bạn sẽ học cách sử dụng hàm, phương thức và thư mục (package) để tận dụng hiệu
  quả code có sẵn do các lập trình viên Python xuất sắc viết. Mục tiêu là giảm
  lượng code bạn cần viết để giải quyết những bài toán khó!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Hàm
  - nb_of_exercises: 4
    title: Phương thức
  - nb_of_exercises: 4
    title: Thư mục (Package)
---

## Các hàm

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Các hàm quen thuộc

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python vốn đã có nhiều hàm có sẵn để giúp làm việc với dữ liệu dễ dàng hơn. Hai hàm như vậy là: `print()` và `type()`. Còn có các hàm như `str()`, `int()`, `bool()` và `float()` để chuyển đổi giữa các kiểu dữ liệu. Bạn có thể tìm hiểu về chúng [tại đây.](https://docs.python.org/3/library/functions.html) Đây cũng là các hàm đã được tạo sẵn.

Cách gọi hàm rất đơn giản. Để lấy kiểu dữ liệu của `3.0` và lưu kết quả vào một biến mới, `result`, bạn có thể dùng:

```
result = type(3.0)
```

`@instructions`
- Dùng `print()` kết hợp với `type()` để hiển thị ra kiểu của `var1`.
- Dùng `len()` để lấy [độ dài của list](https://docs.python.org/3/library/functions.html#len) `var1`. Đặt nó trong một lệnh `print()` để hiển thị kết quả trực tiếp.
- Dùng `int()` để chuyển `var2` sang [số nguyên](https://docs.python.org/3/library/functions.html#int). Lưu kết quả vào `out2`.

`@hint`
- Gọi hàm `type()` như sau: `type(var1)`.
- Gọi hàm `print()` giống như bạn vẫn làm. Chỉ cần đặt biến bạn muốn hiển thị trong dấu ngoặc đơn.
- `int(x)` sẽ chuyển `x` sang kiểu số nguyên (integer)

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
msg = "Bạn không cần phải thay đổi hoặc xóa các biến được định nghĩa trước."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Hãy chắc chắn in ra %s của `var1` với `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'kiểu')
Ex().has_printout(1, not_printed_msg = patt % 'độ dài')

int_miss_msg = "Bạn đã sử dụng `int()` để tạo một số nguyên từ `var2` chưa?"
int_incorr_msg = "Bạn đã truyền `var2` vào `int()` chưa?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Bạn đã gọi `int()` đúng cách; bây giờ hãy chắc chắn gán kết quả của lệnh gọi này cho `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Làm tốt lắm! Hàm `len()` cực kỳ hữu ích; nó cũng hoạt động trên chuỗi để đếm số ký tự!")
```

---

## Hàm help

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Giả sử bạn đã biết tên của một hàm trong Python nhưng chưa biết cách sử dụng nó. Trớ trêu là bạn phải hỏi thông tin về một hàm bằng một hàm khác, hàm help: `help()`. Riêng trong IPython, bạn cũng có thể dùng `?` trước tên hàm.


Chẳng hạn, để xem cách dùng hàm `max()`, bạn có thể dùng một trong các lệnh sau:

```
help(max)
?max
```

Hãy dùng IPython Shell để mở [tài liệu](https://docs.python.org/3/library/functions.html#pow) của `pow()`. Mở bằng cách gõ `?pow` hoặc `help(pow)` rồi nhấn **Enter**.

Câu nào sau đây đúng?

`@possible_answers`
- `pow()` có ba đối số: `base`, `exp` và `mod`. Nếu không có `mod`, hàm sẽ bị lỗi.
- `pow()` có ba đối số bắt buộc: `base`, `exp` và `None`.
- `pow()` yêu cầu hai đối số `base` và `exp`; `mod` là tùy chọn.
- `pow()` nhận hai đối số: `exp` và `mod`. Thiếu `exp` hàm sẽ bị lỗi.

`@hint`
- Đối số tùy chọn được gán bằng dấu `=` với một giá trị mặc định; hàm sẽ dùng giá trị này nếu đối số đó không được chỉ định.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Không hẳn. `mod` có một giá trị mặc định sẽ được sử dụng nếu bạn không chỉ định giá trị."
msg2 = "Không chính xác. `None` là giá trị mặc định cho đối số `mod`."
msg3 = "Hoàn hảo! Sử dụng `help()` có thể giúp bạn hiểu cách các hàm hoạt động, khai thác toàn bộ tiềm năng của chúng!"
msg4 = "Không chính xác. `pow()` nhận ba đối số, một trong số đó có giá trị mặc định."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Nhiều đối số

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

Trong bài trước, bạn đã nhận biết các đối số tùy chọn bằng cách xem tài liệu với `help()`. Giờ bạn sẽ áp dụng điều đó để thay đổi cách hoạt động của hàm `sorted()`.

Hãy xem [tài liệu](https://docs.python.org/3/library/functions.html#sorted) của `sorted()` bằng cách gõ `help(sorted)` trong IPython Shell.

Bạn sẽ thấy `sorted()` nhận ba đối số: `iterable`, `key` và `reverse`. Trong bài này, bạn chỉ cần chỉ định `iterable` và `reverse`, không cần `key`.

Đã có sẵn hai list cho bạn.

Bạn hãy ghép chúng lại và sắp xếp theo thứ tự giảm dần.

`@instructions`
- Dùng `+` để gộp nội dung của `first` và `second` vào một list mới: `full`.
- Gọi hàm `sorted()` trên list `full` và chỉ định đối số `reverse` là `True`. Lưu list đã sắp xếp vào biến `full_sorted`.
- Cuối cùng, hiển thị kết quả của `full_sorted`.

`@hint`
- Cộng `first` và `second` như cộng hai số và gán kết quả vào biến `full`.
- Dùng `sorted()` với hai đối số: `full` và `reverse=True`.
- Để hiển thị một biến, dùng `print()`.

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
msg = "Bạn không cần phải thay đổi hoặc xóa các biến `first` và `second` đã có."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Hãy chắc chắn rằng bạn gán kết quả của việc gọi `sorted()` cho `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Tuyệt! Hãy xem video về các phương thức trong Python.")
```

---

## Các phương thức

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Phương thức với string

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

String đi kèm rất nhiều phương thức. Làm theo hướng dẫn để hiểu thêm một số phương thức. Nếu muốn tìm hiểu kỹ hơn, hãy gõ `help(str)` trong IPython Shell.


Một string `place` đã được tạo sẵn để bạn thực hành.

`@instructions`
- Dùng [phương thức](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` trên `place` và lưu kết quả vào `place_up`. Hãy dùng cú pháp gọi phương thức mà bạn đã học trong video trước.
- Hiển thị kết quả của `place` và `place_up`. Cả hai có thay đổi không?
- Hiển thị số lượng ký tự 'o' trong biến `place` bằng cách gọi `.count()` trên `place` và đặt chữ `'o'` làm đầu vào cho phương thức. Lưu ý: chúng ta đang nói về biến `place`, không phải từ `"place"`!

`@hint`
- Bạn có thể gọi phương thức `.upper()` trên `place` mà không cần thêm đầu vào nào.
- Để hiển thị ra một biến `x`, hãy viết `print(x)`.
- Nhớ đặt lệnh `place.count(____)` trong hàm `print()` để hiển thị kết quả.

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
msg = "Bạn không cần phải thay đổi hoặc xóa các biến được định nghĩa trước."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Đừng quên in ra `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Gán kết quả của lệnh gọi `place.upper()` của bạn cho `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Bạn đã tính toán số lượng chữ o trong `place` đúng; bây giờ hãy đảm bảo bao bọc lệnh gọi `place.count('o')` trong một hàm `print()` để in ra kết quả."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Tốt lắm! Lưu ý từ các kết quả in ra rằng phương thức `upper()` không thay đổi đối tượng mà nó được gọi. Điều này sẽ khác đối với danh sách trong bài tập tiếp theo!")
```

---

## Các phương thức của list

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Trong Python, không chỉ string mới có các phương thức riêng. List, float, integer và boolean cũng là những kiểu dữ liệu có sẵn nhiều phương thức hữu ích riêng. Trong bài tập này, bạn sẽ thực hành với:

- `.index()`, để lấy vị trí của phần tử đầu tiên trong list khớp với đầu vào và
- `.count()`, để đếm số lần một phần tử xuất hiện trong list.

Bạn sẽ làm với list lưu diện tích các phần khác nhau của một căn nhà: `areas`.

`@instructions`
- Dùng phương thức `.index()` để biết vị trí của phần tử trong `areas` có giá trị bằng `20.0`. Hiển thị index này ra.
- Gọi lệnh `.count()` trên `areas` để tìm xem `9.50` xuất hiện bao nhiêu lần trong list. Tiếp tục, chỉ cần hiển thị kết quả ra.

`@hint`
- Để hiển thị index, đặt lệnh `areas.index(___)` trong hàm `print()`.
- Để hiển thị số lần phần tử `x` xuất hiện trong list, đặt lệnh `areas.count(___)` trong hàm `print()`.

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
predef_msg = "Bạn không cần phải thay đổi hoặc xóa danh sách được định nghĩa trước `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Tuyệt vời! Đây là những ví dụ về các phương thức của `list` không thay đổi danh sách mà chúng được gọi trên.")
```

---

## Các phương thức của list (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Hầu hết các phương thức của list sẽ thay đổi chính list được gọi. Ví dụ:

- `.append()`, thêm một phần tử vào list mà nó được gọi,
- `.remove()`, [xóa](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) xoá phần tử đầu tiên trong list khớp với giá trị đầu vào, và
- `.reverse()`, [đảo ngược](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) đảo ngược thứ tự các phần tử trong list.

Bạn sẽ thực hành với list diện tích các phần khác nhau của ngôi nhà: `areas`.

`@instructions`
- Dùng `.append()` hai lần để thêm diện tích của poolhouse và garage: lần lượt là `24.5` và `15.45`. Chú ý thêm đúng theo thứ tự này.
- Hiển thị kết quả `areas`
- Dùng phương thức `.reverse()` để đảo ngược thứ tự các phần tử trong `areas`.
- Hiển thị kết quả `areas` ra một lần nữa.

`@hint`
- Với yêu cầu đầu tiên, dùng hàm `areas.append(___)` hai lần.

- Để hiển thị ra một biến `x`, chỉ cần viết `print(x)`.
- Phương thức `.reverse()` không cần dữ liệu đầu vào; chỉ dùng cú pháp chấm và cặp ngoặc đơn để trống: `.reverse()`.
- Để hiển thị ra một biến `x`, chỉ cần viết `print(x)`.

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

success_msg("Tuyệt vời!")
```

---

## Packages

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Import package

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Giả sử bạn muốn tính chu vi và diện tích của một hình tròn. Công thức như sau:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Thay vì gõ thủ công giá trị của `pi`, bạn có thể dùng package `math` chứa hằng số này.

Lưu ý: `**` là ký hiệu lũy thừa. Ví dụ `3**4` nghĩa là `3` mũ `4` và cho kết quả `81`.

`@instructions`
- Import package `math`.
- Dùng `math.pi` để tính chu vi hình tròn và lưu vào `C`.
- Dùng `math.pi` để tính diện tích hình tròn và lưu vào `A`.

`@hint`
- Bạn chỉ cần dùng `import math`, rồi tham chiếu đến `pi` bằng `math.pi`.
- Dùng công thức trong phần mô tả bài tập để tìm `C`. Dùng `*`.
- Dùng công thức trong phần mô tả bài tập để tìm `A`. Dùng `*` và `**`.

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
patt = "Phép tính `%s` của bạn chưa hoàn toàn chính xác. Hãy chắc chắn sử dụng `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Giữ `{{sol_call}}` ở đó để in ra chu vi."),
  has_printout(1, not_printed_msg = "__JINJA__:Giữ `{{sol_call}}` ở đó để in ra diện tích.")
)

success_msg("Tuyệt vời! Nếu bạn biết cách xử lý các hàm từ các gói, sức mạnh của nhiều lập trình viên Python sẽ nằm trong tầm tay của bạn!")
```

---

## Import chọn lọc

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Cách import chung như `import math` sẽ giúp bạn truy cập **toàn bộ** chức năng của package `math`. Tuy nhiên, nếu bạn chỉ cần một phần cụ thể của package, bạn có thể import chọn lọc hơn:

```
from math import pi
```

Hãy làm lại ví dụ trước, nhưng lần này chỉ dùng `pi`.

`@instructions`
- Thực hiện import chọn lọc từ package `math` chỉ import hàm `pi`.
- Dùng `pi` để tính chu vi hình tròn và lưu kết quả vào biến `C`.
- Dùng `pi` để tính diện tích hình tròn và lưu kết quả vào biến `A`.

`@hint`
- Dùng câu lệnh `from math import pi` để import có chọn lọc.
- Giờ bạn chỉ cần dùng trực tiếp `pi`.

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
patt = "Phép tính `%s` của bạn chưa hoàn toàn chính xác. Hãy chắc chắn chỉ sử dụng `pi`."

Ex().has_import("math.pi", not_imported_msg = "Hãy chắc chắn rằng bạn đã nhập `pi` từ gói `math`. Bạn nên sử dụng ký hiệu `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Giữ `{{sol_call}}` ở đó để in ra chu vi."),
  has_printout(1, not_printed_msg = "__JINJA__:Giữ `{{sol_call}}` ở đó để in ra diện tích.")
)

success_msg("Tuyệt vời! Hãy chuyển sang bài tập tiếp theo.")
```

---

## Nhiều cách import khác nhau

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Có nhiều cách để import package và module vào Python. Tùy vào cách bạn import, bạn sẽ phải viết những đoạn code khác nhau.

Giả sử bạn muốn dùng [hàm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, nằm trong subpackage `linalg` của package `scipy`. Bạn muốn dùng được hàm này như đoạn code sau:

```
my_inv([[1,2], [3,4]])
... 


Vậy bạn phải dùng câu lệnh import nào để chạy đoạn code trên mà không bị lỗi?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Hãy thử các câu lệnh import khác nhau trong IPython shell và xem câu lệnh nào giúp dòng `my_inv([[1, 2], [3, 4]])` chạy mà không báo lỗi. Nhấn **enter** để chạy đoạn code bạn viết.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Không chính xác, hãy thử lại. Hãy thử các câu lệnh import khác nhau trong IPython shell và xem câu lệnh nào khiến dòng `my_inv([[1, 2], [3, 4]])` chạy mà không gặp lỗi."
msg4 = "Chính xác! Từ khóa `as` cho phép bạn tạo một tên cục bộ cho hàm bạn đang import: `inv()` hiện có sẵn dưới dạng `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```
