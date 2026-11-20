---
title_meta: Chương 3
title: Hàm và Gói (Package)
description: >-
  Bạn sẽ học cách sử dụng hàm, phương thức và gói (package) để tận dụng hiệu quả
  code có sẵn do các lập trình viên Python xuất sắc viết. Mục tiêu là giảm lượng
  code bạn cần viết để giải quyết những bài toán khó!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Các hàm
  - nb_of_exercises: 4
    title: Các phương thức
  - nb_of_exercises: 4
    title: Gói (Package)
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

Ngay từ ban đầu, Python cung cấp một loạt hàm tích hợp sẵn để giúp bạn làm khoa học dữ liệu dễ dàng hơn. Bạn đã biết hai hàm như vậy: `print()` và `type()`. Cũng có các hàm như `str()`, `int()`, `bool()` và `float()` để chuyển đổi giữa các kiểu dữ liệu. Bạn có thể tìm hiểu về chúng [tại đây.](https://docs.python.org/3/library/functions.html) Đây cũng là các hàm tích hợp sẵn.

Gọi một hàm thì rất dễ. Để lấy kiểu của `3.0` và lưu đầu ra vào một biến mới, `result`, bạn có thể dùng cú pháp sau:

```
result = type(3.0)
```

`@instructions`
- Dùng `print()` kết hợp với `type()` để hiển thị ra kiểu của `var1`.
- Dùng `len()` để lấy [độ dài của danh sách](https://docs.python.org/3/library/functions.html#len) `var1`. Đặt nó trong một lệnh `print()` để hiển thị trực tiếp.
- Dùng `int()` để chuyển `var2` thành [số nguyên](https://docs.python.org/3/library/functions.html#int). Lưu đầu ra vào `out2`.

`@hint`
- Gọi hàm `type()` như sau: `type(var1)`.
- Gọi `print()` như bạn đã làm nhiều lần trước. Chỉ cần đặt biến bạn muốn hiển thị vào trong dấu ngoặc đơn.
- `int(x)` sẽ chuyển `x` thành một số nguyên.

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

Có thể bạn đã biết tên một hàm trong Python, nhưng vẫn cần tìm cách sử dụng nó. Thật thú vị là bạn phải hỏi thông tin về một hàm bằng một hàm khác: `help()`. Riêng trong IPython, bạn cũng có thể dùng `?` trước tên hàm.

Để xem hướng dẫn về hàm `max()`, chẳng hạn, bạn có thể dùng một trong các lệnh sau:

```
help(max)
?max
```

Hãy dùng IPython Shell để mở [tài liệu](https://docs.python.org/3/library/functions.html#pow) về `pow()`. Thực hiện bằng cách gõ `?pow` hoặc `help(pow)` rồi nhấn **Enter**.

Phát biểu nào sau đây là đúng?

`@possible_answers`
- `pow()` nhận ba đối số: `base`, `exp` và `mod`. Nếu không có `mod`, hàm sẽ trả về lỗi.
- `pow()` nhận ba đối số bắt buộc: `base`, `exp` và `None`.
- `pow()` yêu cầu hai đối số `base` và `exp`; `mod` là tùy chọn.
- `pow()` nhận hai đối số: `exp` và `mod`. Thiếu `exp` sẽ gây lỗi.

`@hint`
- Các đối số tùy chọn được gán giá trị mặc định bằng `=`, hàm sẽ dùng giá trị này nếu bạn không truyền đối số đó.

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

Trong bài tập trước, bạn đã xác định các đối số tùy chọn bằng cách xem tài liệu với `help()`. Giờ bạn sẽ áp dụng điều đó để thay đổi cách hoạt động của hàm `sorted()`.

Hãy xem [tài liệu](https://docs.python.org/3/library/functions.html#sorted) của `sorted()` bằng cách gõ `help(sorted)` trong IPython Shell.

Bạn sẽ thấy `sorted()` nhận ba đối số: `iterable`, `key` và `reverse`. Trong bài này, bạn chỉ cần chỉ định `iterable` và `reverse`, không cần `key`.

Đã có sẵn hai list cho bạn.

Bạn có thể ghép chúng lại và sắp xếp theo thứ tự giảm dần không?

`@instructions`
- Dùng `+` để trộn nội dung của `first` và `second` vào một list mới: `full`.
- Gọi `sorted()` trên `full` và đặt đối số `reverse` là `True`. Lưu list đã sắp xếp thành `full_sorted`.
- Cuối cùng, hiển thị ra `full_sorted`.

`@hint`
- Cộng `first` và `second` như hai con số và gán kết quả cho `full`.
- Dùng `sorted()` với hai đối số: `full` và `reverse=True`.
- Dùng `print()` để hiển thị ra một biến

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

String có rất nhiều phương thức đi kèm. Hãy làm theo hướng dẫn để khám phá một vài phương thức. Nếu bạn muốn tìm hiểu chi tiết hơn, hãy gõ `help(str)` trong IPython Shell.

Một string `place` đã được tạo sẵn để bạn thử nghiệm.

`@instructions`
- Sử dụng `.upper()` [method](https://docs.python.org/3/library/stdtypes.html#str.upper) trên `place` và lưu kết quả vào `place_up`. Sử dụng cú pháp cho các phương thức gọi mà bạn đã học trong video trước. 
- Hiển thị ra `place` và `place_up`. Cả hai có thay đổi không? 
- Hiển thị số chữ o trên `place` biến bằng cách gọi `.count()` trên `place` và truyền chữ `'o'` làm đầu vào cho phương thức. Chúng ta đang nói về biến `place`, không phải từ place `"place"`!

`@hint`
- Bạn có thể gọi phương thức `.upper()` trên `place` mà không cần tham số bổ sung.
- Để hiển thị ra một biến `x`, bạn có thể viết `print(x)`.
- Hãy nhớ đặt lệnh `place.count(____)` bên trong hàm `print()` để hiển thị được kết quả.

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

Không chỉ riêng string mới có các phương thức đi kèm trong Python. List, float, integer và boolean cũng là những kiểu có sẵn nhiều phương thức hữu ích. Trong bài tập này, bạn sẽ thử nghiệm với:

- `.index()`, để lấy index của phần tử đầu tiên trong list khớp với đầu vào của nó và
- `.count()`, để lấy số lần một phần tử xuất hiện trong list.

Bạn sẽ làm việc với danh sách diện tích của các phần khác nhau trong một ngôi nhà: `areas`.

`@instructions`
- Dùng phương thức `.index()` để lấy index của phần tử trong `areas` có giá trị bằng `20.0`. Hiển thị index này ra.
- Gọi `.count()` trên `areas` để xem `9.50` xuất hiện bao nhiêu lần trong list. Tiếp tục chỉ hiển thị con số này ra.

`@hint`
- Để hiển thị ra index, đặt `areas.index(___)` trong hàm `print()`.
- Để hiển thị số lần phần tử `x` xuất hiện trong list, đặt `areas.count(___)` trong hàm `print()`.

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

Hầu hết các phương thức của list sẽ thay đổi chính list mà chúng được gọi. Ví dụ:

- `.append()`, thêm một phần tử vào list được gọi,
- `.remove()`, [xóa](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) phần tử đầu tiên trong list khớp với đầu vào, và
- `.reverse()`, [đảo ngược](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) thứ tự các phần tử trong list được gọi.

Bạn sẽ làm việc với list diện tích các phần của ngôi nhà: `areas`.

`@instructions`
- Dùng `.append()` hai lần để thêm diện tích của poolhouse và garage: lần lượt là `24.5` và `15.45`. Chú ý thêm đúng theo thứ tự này.
- Hiển thị ra `areas`
- Dùng phương thức `.reverse()` để đảo ngược thứ tự các phần tử trong `areas`.
- Hiển thị ra `areas` thêm một lần nữa.

`@hint`
- Với hướng dẫn đầu tiên, dùng lệnh `areas.append(___)` hai lần.
- Để hiển thị ra một biến `x`, chỉ cần viết `print(x)`.
- Phương thức `.reverse()` không cần tham số bổ sung; chỉ cần dùng cú pháp chấm và cặp dấu ngoặc đơn rỗng: `.reverse()`.
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

## Gói (Package)

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

Thay vì tự gõ giá trị cho `pi`, bạn có thể dùng package`math` có sẵn hằng số này.

Tham khảo thêm: `**` là ký hiệu lũy thừa. Ví dụ `3**4` là `3` mũ `4` và cho kết quả `81`.

`@instructions`
- Import package `math`.
- Dùng `math.pi` để tính chu vi hình tròn và lưu vào `C`.
- Dùng `math.pi` để tính diện tích hình tròn và lưu vào `A`.

`@hint`
- Bạn chỉ cần dùng `import math`, rồi tham chiếu tới `pi` bằng `math.pi`.
- Dùng công thức trong phần bài để tìm `C`. Dùng `*`.
- Dùng công thức trong phần bài để tìm `A`. Dùng `*` và `**`.

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

## Import có chọn lọc

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Import chung như `import math` sẽ giúp bạn import **tất cả** chức năng trong package `math`. Tuy nhiên, nếu bạn chỉ dùng một phần cụ thể của package, bạn có thể import có chọn lọc hơn:

```
from math import pi
```

Hãy làm lại tương tự, nhưng lần này chỉ dùng `pi`.

`@instructions`
- Thực hiện import có chọn lọc từ package `math` để chỉ nhập `pi`.
- Dùng `pi` để tính chu vi hình tròn và lưu vào `C`.
- Dùng `pi` để tính diện tích hình tròn và lưu vào `A`.

`@hint`
- Dùng `from math import pi` để import chọn lọc.
- Giờ bạn có thể dùng riêng `pi`!

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

## Các cách import khác nhau

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Có nhiều cách để import package và module vào Python. Tùy vào cách bạn import, bạn sẽ phải dùng code khác nhau.

Giả sử bạn muốn dùng [hàm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()` trong subpackage `linalg` của package `scipy`. Bạn muốn dùng được hàm này như sau:

```
my_inv([[1,2], [3,4]])
```

Bạn cần câu lệnh `import` nào để chạy đoạn code trên mà không gặp lỗi?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Hãy thử các câu lệnh import khác nhau trong IPython shell và xem câu lệnh nào cho phép dòng `my_inv([[1, 2], [3, 4]])` chạy mà không báo lỗi. Nhấn **enter** để chạy đoạn code bạn đã viết.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Không chính xác, hãy thử lại. Hãy thử các câu lệnh import khác nhau trong IPython shell và xem câu lệnh nào khiến dòng `my_inv([[1, 2], [3, 4]])` chạy mà không gặp lỗi."
msg4 = "Chính xác! Từ khóa `as` cho phép bạn tạo một tên cục bộ cho hàm bạn đang import: `inv()` hiện có sẵn dưới dạng `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```
