---
title_meta: Chương 4
title: NumPy
description: >-
  NumPy là package Python nền tảng giúp bạn thực hành khoa học dữ liệu hiệu quả.
  Học cách làm việc với các công cụ hữu ích trong array NumPy và bắt đầu khám
  phá dữ liệu.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: Numpy
  - nb_of_exercises: 5
    title: Array Numpy hai chiều
  - nb_of_exercises: 3
    title: 'Numpy: Thống kê cơ bản'
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

## Array NumPy đầu tiên của bạn

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Giờ bạn sẽ bước vào thế giới bóng chày. Ở đó, bạn sẽ làm quen với những kiến thức cơ bản của `numpy`, một package hữu ích cho khoa học dữ liệu.

Một list `baseball` đã có sẵn trong script Python, thể hiện chiều cao của một số cầu thủ bóng chày theo đơn vị cm. Bạn hãy thêm code để tạo một array `numpy` từ list này.

`@instructions`
- Import package `numpy` với tên viết tắt `np`, để gọi `numpy` bằng `np`.
- Dùng `np.array()` để tạo một array `numpy` từ `baseball`. Đặt tên array này là `np_baseball`.
- Hiển thị ra kiểu của `np_baseball` để kiểm tra kết quả.

`@hint`
- `import numpy as np` sẽ giải quyết việc này. Từ giờ, bạn dùng `np.fun_name()` mỗi khi muốn gọi một hàm của `numpy`.
- Hàm `np.array()`  có đầu vào là `baseball`. Gán kết quả của hàm cho `np_baseball`.
- Để hiển thị ra kiểu của một biến `x`, chỉ cần gõ `print(type(x))`.

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
predef_msg = "Bạn không cần phải thay đổi hoặc xóa các biến được định nghĩa trước."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Làm tốt lắm!")
```

---

## Chiều cao của các cầu thủ bóng chày

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Giả sử bạn là một fan cuồng của bóng chày. Bạn quyết định gọi cho MLB (Major League Baseball) để xin một số thống kê về chiều cao của các cầu thủ. Họ gửi cho bạn dữ liệu của hơn một nghìn cầu thủ, được lưu trong một list Python thông thường: `height_in`. Chiều cao được tính bằng inch. Từ đó, bạn hãy tạo một array `numpy` từ đó và chuyển đổi đơn vị sang mét không?

`height_in` đã có sẵn và package `numpy` cũng đã được import, nên bạn có thể bắt đầu ngay (Nguồn: stat.ucla.edu).

`@instructions`
- Tạo một array `numpy` từ `height_in`. Đặt tên array mới là `np_height_in`.
- Hiển thị kết quả của `np_height_in`.
- Nhân `np_height_in` với `0.0254` để đổi tất cả số đo chiều cao từ inch sang mét. Lưu các giá trị mới vào một array mới là `np_height_m`.
- Hiển thị kết quả của `np_height_m` và kiểm tra xem có hợp lý không.

`@hint`
- Dùng `np.array()` và đưa `height` vào. Lưu kết quả vào biến `np_height_in`.
- Để hiển thị một biến `x`, gõ `print(x)` trong script Python.
- Thực hiện phép tính như thể `np_height_in` là một số duy nhất: `np_height_in * conversion_factor` sẽ là một phần của đáp án.
- Để hiển thị ra một biến `x`, gõ `print(x)` trong script Python.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Sử dụng `np_height_in * 0.0254` để tính `np_height_m`.")
)

success_msg("Tuyệt vời! Trong nháy mắt, `numpy` thực hiện phép nhân trên hơn 1000 phép đo chiều cao.")
```

---

## Hiệu ứng phụ của NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` rất mạnh khi thực hiện số học véc-tơ. Tuy nhiên, nếu so sánh với danh sách (list) thông thường của Python, sẽ có một vài khác biệt.

Thứ nhất, mảng `numpy` không thể chứa các phần tử có kiểu khác nhau. Nếu bạn trộn kiểu, như boolean và số nguyên, `numpy` sẽ tự động chuyển chúng về một kiểu chung. Boolean như `True` và `False` được coi như `1` và `0` khi kết hợp với số, nên mảng cuối cùng sẽ thành số nguyên.

Thứ hai, các toán tử số học thường gặp như `+`, `-`, `*` và `/` có ý nghĩa khác nhau đối với list Python thông thường và mảng `numpy`.

Chọn đoạn mã tạo ra đầu ra sau:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Gói `numpy` đã được import là `np`. Bạn có thể chạy từng lựa chọn trong IPython Shell để xem đầu ra.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Sao chép từng đoạn mã và dán vào IPython Shell. Nhấn **enter** để chạy mã và xem đầu ra nào khớp với kết quả của `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Không chính xác. Hãy thử các đoạn mã khác nhau và xem đoạn nào khớp với đoạn mã mục tiêu."
msg2 = "Làm tốt lắm! `True` được chuyển đổi thành 1, `False` được chuyển đổi thành 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Trích xuất trong NumPy Array

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Phép trích xuất phần tử (dùng cú pháp ngoặc vuông trên list hoặc array) hoạt động hoàn toàn giống nhau với cả list và array.

Bài tập này đã có sẵn hai list, `height_in` và `weight_lb`. Chúng chứa chiều cao và cân nặng của các cầu thủ MLB dưới dạng list thông thường. Ngoài ra còn có sẵn hai `numpy` array, `np_weight_lb` và `np_height_in.

`@instructions`
- Trích xuất phần tử của `np_weight_lb` bằng cách hiển thị phần tử ở index 50
- Hiển thị ra một sub-array của `np_height_in` chứa các phần tử từ index 100 đến 110 bao gồm cả index 110.

`@hint`
- Hãy nhớ đặt các phép trích xuất phần tử trong hàm `print()`.
- Dùng `[100:111]` để lấy các phần tử từ index 100 đến 110, bao gồm cả index 110.

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
msg = "Bạn không cần phải thay đổi hoặc xóa các biến được định nghĩa trước."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Tuyệt vời! Đã đến lúc học điều gì đó mới: mảng NumPy 2D!")
```

---

## Array NumPy hai chiều

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Array NumPy 2D Đầu Tiên Của Bạn

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Trước khi làm việc với dữ liệu MLB thực tế, hãy thử tạo một array `numpy` 2D từ một list chứa list nhỏ.

Trong bài này, `baseball` là một list chứa list. List chính chứa 4 phần tử. Mỗi phần tử là một list gồm chiều cao và cân nặng của 4 cầu thủ bóng chày, theo đúng thứ tự đó. `baseball` đã được viết sẵn cho bạn trong script.

`@instructions`
- Dùng `np.array()` để tạo array `numpy` 2D từ `baseball`. Đặt tên là `np_baseball`.
- Hiển thị ra kiểu dữ liệu của `np_baseball`.
- Hiển thị ra thuộc tính `shape` của `np_baseball`. Dùng `np_baseball.shape`.

`@hint`
- `baseball` đã được tạo sẵn trong script. Gọi hàm `np.array()` với biến này và lưu array `numpy` 2D thu được vào `np_baseball`.
- Dùng `print()` kết hợp với `type()` cho yêu cầu thứ hai.
- `np_baseball.shape` sẽ cho bạn biết kích thước của `np_baseball`. Nhớ dùng lệnh `print()` bọc quanh nó.

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
msg = "Bạn không cần phải thay đổi hoặc xóa các biến được định nghĩa trước."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().has_import("numpy", same_as=False)

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

success_msg("Tuyệt vời! Bây giờ bạn đã sẵn sàng để chuyển đổi dữ liệu MLB thực tế thành một mảng 2D `numpy`!")
```

---

## Dữ liệu bóng chày ở dạng 2D

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Bạn nhận thấy việc cấu trúc lại toàn bộ dữ liệu này thành một array `numpy` 2D sẽ hợp lý hơn.

Bạn có một list chứa các list. Trong list này, mỗi list con hiển thị chiều cao và cân nặng của một cầu thủ bóng chày. Tên của list là `baseball`, list này đã có đủ dữ liệu (dù bạn không nhìn thấy).


Hãy lưu dữ liệu dưới dạng array 2D để tận dụng thêm các chức năng của `numpy`.

`@instructions`
- Dùng `np.array()` để tạo array `numpy` 2D từ `baseball`. Đặt tên là `np_baseball`.
- Hiển thị ra thuộc tính `shape` của `np_baseball`.

`@hint`
- `baseball` đã có sẵn trong Python. Gọi hàm `np.array()` với `baseball` và lưu array `numpy` 2D thu được vào `np_baseball`.
- `np_baseball.shape` sẽ cho bạn biết kích thước của `np_baseball`. Nhớ bọc nó bằng lệnh `print()`.

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

success_msg("Tuyệt vời! Đã đến lúc thể hiện một số tính năng nổi bật của mảng `numpy` đa chiều!")
```

---

## Trích xuất phần tử từ Array NumPy hai chiều

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Nếu array `numpy` hai chiều của bạn có cấu trúc đều đặn, tức là mỗi hàng và cột có số lượng giá trị cố định, thì những cách trích xuất phức tạp sẽ trở nên rất dễ dàng. Hãy xem đoạn code dưới đây, trong đó các phần tử `"a"` và `"c"` được trích xuất từ một list chứa list.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Các chỉ số trước dấu phẩy chỉ hàng, còn các chỉ số sau dấu phẩy chỉ cột. Ký hiệu `:` dùng để cắt (slice); trong ví dụ này, nó đang yêu cầu Python lấy tất cả các hàng.

`@instructions`
- Hiển thị hàng thứ 50 của `np_baseball`.
- Tạo biến mới, `np_weight_lb`, chứa toàn bộ cột thứ hai của `np_baseball`.
- Chọn chiều cao (cột thứ nhất) của cầu thủ bóng chày thứ 124 trong `np_baseball` và hiển thị kết quả

`@hint`
- Trong hướng dẫn đầu tiên, bạn cần dùng row có index 49.  Cụ thể hơn, hãy dùng `[49, :]`.
- Để chọn toàn bộ cột thứ hai, bạn dùng `[:, 1]`.
- Ở yêu cầu cuối, dùng `[123, 0]` và nhớ đặt tất cả trong lệnh `print()`.

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
msg = "Bạn không cần phải thay đổi hoặc xóa các biến được định nghĩa trước."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Bạn có thể sử dụng `np_baseball[:,1]` để định nghĩa `np_weight_lb`. Điều này sẽ chọn toàn bộ cột đầu tiên.")

Ex().has_printout(1)

success_msg("Mọi thứ đang diễn ra tốt đẹp!")
```

---

## Các phép toán trên array hai chiều

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

Các array `numpy` hai chiều có thể thực hiện phép tính theo từng phần tử, giống như array `numpy` một chiều. 

Đã có sẵn `np_baseball` cho bạn; đây là một array `numpy` hai chiều với 3 cột lần lượt thể hiện chiều cao (inch), cân nặng (pound) và tuổi (năm). `baseball` hiện có dưới dạng list chứa list thông thường và `updated` có sẵn dưới dạng array `numpy` hai chiều.

`@instructions`
- Bạn đã có dữ liệu được cập nhật về chiều cao, cân nặng và tuổi của tất cả các cầu thủ bóng chày. Dữ liệu này có sẵn dưới dạng array `numpy` hai chiều, `updated`. Hãy cộng `np_baseball` và `updated`, rồi hiển thị ra kết quả.
- Bạn muốn đổi đơn vị chiều cao và cân nặng sang hệ mét (lần lượt là mét và kilogram). Bước đầu tiên, tạo một array `numpy` với ba giá trị: `0.0254`, `0.453592` và `1`. Đặt tên array này là `conversion`.
- Nhân `np_baseball` với `conversion` và hiển thị ra kết quả.

`@hint`
- `np_baseball + updated` sẽ cộng phần tử-tương-ứng của hai array `numpy`.
- Tạo một array `numpy` với `np.array()`; đầu vào là một list Python thông thường có ba phần tử.
- `np_baseball * conversion` sẽ hoạt động ngay, không cần làm gì thêm. Hãy thử làm và nhớ đặt trong lệnh `print()`.

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

msg = "Bạn không cần phải thay đổi hoặc xóa các biến được định nghĩa trước."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("Làm tốt lắm! Hãy chú ý rằng với rất ít mã, bạn có thể thay đổi tất cả các giá trị trong cấu trúc dữ liệu `numpy` của mình theo một cách rất cụ thể. Điều này sẽ rất hữu ích trong tương lai của bạn với tư cách là một nhà khoa học dữ liệu!")
```

---

## NumPy: Thống kê cơ bản

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Trung bình so với trung vị

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Giờ bạn đã biết cách dùng các hàm của `numpy` để hiểu dữ liệu tốt hơn.

Bộ dữ liệu bóng chày có dạng array `numpy` hai chiều với 3 cột (chiều cao, cân nặng, tuổi) và 1015 hàng. Tên của array `numpy` này là `np_baseball`. Tuy nhiên, sau khi tái cấu trúc dữ liệu, bạn thấy một số giá trị chiều cao cao bất thường. Hãy làm theo hướng dẫn để xem thống kê tóm tắt nào phù hợp nhất khi bạn phải xử lý các _outlier_ (giá trị ngoại lai). Đã có sẵn `np_baseball`.

`@instructions`
- Tạo array `numpy` `np_height_in` bằng với cột đầu tiên của `np_baseball`.
- Hiển thị giá trị trung bình của `np_height_in`.
- Hiển thị trung vị của `np_height_in`.

`@hint`
- Dùng kỹ thuật trích xuất phần tử của array 2 chiều `numpy`: `[:,0]` là một phần của giải pháp. 
- Nếu đã import `numpy` là `np`, hãy dùng `np.mean()` để lấy giá trị trung bình của một array NumPy. Nhớ gọi hàm `print()`.
- Với yêu cầu cuối, dùng `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Bạn có thể sử dụng `np_baseball[:,0]` để chọn cột đầu tiên từ `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Chiều cao trung bình là 1586 inch, điều đó nghe có vẻ không đúng, phải không? Tuy nhiên, trung vị dường như không bị ảnh hưởng bởi các giá trị ngoại lai: 74 inch có vẻ hoàn toàn hợp lý. Luôn là một ý tưởng tốt để kiểm tra cả trung vị và trung bình, để có được ý tưởng về phân phối tổng thể của toàn bộ tập dữ liệu.")
```

---

## Khám phá dữ liệu bóng chày

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Vì mean và median cách nhau khá xa, bạn quyết định khiếu nại lên MLB. Họ tìm ra lỗi và gửi cho bạn dữ liệu đã chỉnh sửa. Dữ liệu lại được cung cấp dưới dạng mảng NumPy hai chiều `np_baseball` với ba cột.

Tệp script Python trong trình soạn thảo đã có sẵn code để hiển thị các thông báo hữu ích với những thống kê tóm tắt khác nhau và `numpy` đã được import với tên là `np`. `np_baseball` đã sẵn sàng. Hãy làm nốt phần còn lại.

`@instructions`
- Đã có sẵn code để tính mean của chiều cao. Hãy hoàn thiện code để tính ra median của chiều cao.
- Dùng `np.std()` trên cột thứ nhất của `np_baseball` để tính `stddev`.
- Người cao lớn có xu hướng nặng hơn không? Dùng `np.corrcoef()` để lưu hệ số tương quan giữa cột thứ nhất và cột thứ hai của `np_baseball` vào `corr`.

`@hint`
- Dùng `np.median()` để tính trung vị. Nhớ chọn đúng cột đã nhé!
- Cũng lấy đúng cột đó để tính độ lệch chuẩn với hàm `np.std()`.
- Dùng `np_baseball[:, 0]` và `np_baseball[:, 1]` để chọn cột thứ nhất và thứ hai; đây là đầu vào cho `np.corrcoef()`.

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
msg = "Bạn không nên thay đổi hoặc xóa biến `avg` đã được định nghĩa trước."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Bạn đã sử dụng `np.median()` để tính toán trung vị chưa?"
incorrect = "Để tính toán `med`, hãy truyền cột đầu tiên của `np_baseball` vào `numpy.median()`. Ví dụ của `np.mean()` cho thấy cách thực hiện."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Bạn đã sử dụng `np.std()` để tính toán độ lệch chuẩn chưa?"
incorrect = "Để tính toán `stddev`, hãy truyền cột đầu tiên của `np_baseball` vào `numpy.std()`. Ví dụ của `np.mean()` cho thấy cách thực hiện."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Bạn đã sử dụng `np.corrcoef()` để tính toán hệ số tương quan chưa?"
incorrect1 = "Để tính toán `corr`, đối số đầu tiên của `np.corrcoef()` nên là cột đầu tiên của `np_baseball`, tương tự như cách đã làm trước đó."
incorrect2 = "Để tính toán `corr`, đối số thứ hai của `np.corrcoef()` nên là cột thứ hai của `np_baseball`. Thay vì `[:,0]`, lần này hãy sử dụng `[:,1]`."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Làm tốt lắm! Bạn đã xây dựng được một nền tảng vững chắc - bây giờ là lúc sử dụng tất cả các kỹ năng khoa học dữ liệu mới của bạn để giải quyết nhiều thách thức hơn và tạo ra ảnh hưởng.")
```
