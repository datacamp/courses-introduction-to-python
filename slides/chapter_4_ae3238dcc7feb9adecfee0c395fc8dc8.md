---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/vi-VN/eb544618-d5e7-437d-a30e-e59fca1fc897.mp3
---

## Numpy Array 2 chiều

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Làm tốt lắm, bạn đúng là chuyên gia rồi đó! Giờ hãy cùng tạo lại các Numpy array từ video trước.
---

## Các loại NumPy Array

```yaml
type: FullSlide
key: 1b9db47fd2
code_zoom: 100
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

```py
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`
Nếu ta hỏi kiểu dữ liệu của các array này, Python sẽ cho ta biết rằng chúng là numpy.ndarray. Phần numpy chấm cho biết kiểu này được định nghĩa trong package numpy. Còn ndarray là viết tắt của n dimensional array tức là array đa chiều. Các array np_height và np_weight là array một chiều, nhưng bạn hoàn toàn có thể tạo array 2 chiều, 3 chiều, thậm chí 7 chiều! Tuy nhiên, trong video này, ta chỉ tập trung vào 2 chiều mà thôi.
---

## Numpy Array 2 chiều

```yaml
type: FullSlide
key: ebb550dcba
code_zoom: 71
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```{{1}}
```py
np_2d
```{{2}}

```out
array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
```{{2}}

```py
np_2d.shape
```{{3}}

```out
(2, 5) # 2 rows, 5 columns
```{{3}}

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```{{4}}

```out
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')
```{{4}}

`@script`
Ta có thể tạo một numpy array 2 chiều từ một list Python chứa các list con. Hãy thử tạo một numpy array chứa toàn bộ dữ liệu chiều cao và cân nặng của gia đình bạn, như sau.

Nếu hiển thị np_2d ra, ta sẽ thấy đây là một cấu trúc hình chữ nhật: Mỗi list con trong list ban đầu tương ứng với một hàng trong numpy array hai chiều. Từ np_2d.shape, ta sẽ thấy có hai hàng và năm cột. shape là một thuộc tính của array np_2d, cung cấp cho ta thêm thông tin về hình dáng của cấu trúc dữ liệu.

Lưu ý cú pháp truy cập thuộc tính trông hơi giống cú pháp gọi phương thức, nhưng chúng không giống nhau! Bạn hãy nhớ rằng phương thức có dấu ngoặc tròn phía sau, còn thuộc tính thì không, như bạn thấy ở đây. 

Quy tắc của NumPy vẫn áp dụng với array 2 chiều: một array chỉ có thể chứa một kiểu dữ liệu duy nhất. Nếu bạn đổi một float thành string, toàn bộ phần tử trong array sẽ bị đổi thành string để đảm bảo tính đồng nhất.
---

## Trích xuất

```yaml
type: FullSlide
key: e71d2fc8b8
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0]
```

```out
array([1.73, 1.68, 1.71, 1.89, 1.79])
```

`@script`
Ta có thể coi array numpy 2 chiều như một phiên bản nâng cấp của list chứa list: có thể thực hiện phép tính trên toàn bộ array, như mình đã lấy ví dụ minh họa trước đó, và cũng có thể trích, cắt dữ liệu linh hoạt hơn.
Giả sử bạn muốn lấy hàng đầu tiên, rồi sau đó lấy phần tử thứ ba trong hàng đó. Để chọn hàng, bạn dùng index 0 trong ngoặc vuông. Đừng quên Python bắt đầu đếm từ số 0.

Sau đó để chọn phần tử thứ ba, bạn dùng thêm một cặp ngoặc vuông nữa với index 2
---

## Trích xuất

```yaml
type: FullSlide
key: 57a1fb1581
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0, 2]
```{{1}}

```out
1.71
```{{1}}

`@script`
như thế này. Về cơ bản, bạn chọn hàng trước, rồi từ hàng đó chọn tiếp phần tử.

Cũng có một cách trích xuất dữ liệu khác, chỉ dùng một cặp ngoặc vuông và dấu phẩy. Lệnh này trả về đúng giá trị như lúc trước. Giá trị trước dấu phẩy chỉ hàng, giá trị sau dấu phẩy chỉ cột. Kết quả trả về là giao điểm của hàng và cột. Khi đã quen, cú pháp này trực quan hơn và giúp ta làm việc với dữ liệu linh hơn.
---

## Trích xuất

```yaml
type: FullSlide
key: feb75c975c
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[:, 1:3]
```{{1}}

```out
array([[ 1.68,  1.71],
       [59.2 , 63.6 ]])
```{{1}}

```py
np_2d[1, :]
```{{2}}

```out
array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{2}}

`@script`
Giả sử ta muốn chọn chiều cao và cân nặng của thành viên thứ hai và thứ ba trong gia đình. Ta cần cả hai hàng, nên ta đặt dấu hai chấm trước dấu phẩy. Ta chỉ cần cột thứ hai và thứ ba, nên ta dùng index từ 1 đến 3 sau dấu phẩy. Lưu ý là index 3 không được tính vào. Kết quả là một array hai chiều với hai hàng và hai cột:


Tương tự, ta có thể chọn cân nặng của tất cả thành viên như sau: ta chỉ cần hàng thứ hai, nên ta đặt 1 trước dấu phẩy. Ta cần tất cả các cột, nên ta dùng dấu hai chấm sau dấu phẩy. Kết quả là toàn bộ hàng thứ hai.

Cuối cùng, numpy array hai chiều cho phép ta thực hiện các phép tính theo từng phần tử, giống như ta đã làm với array một chiều. Bạn có thể
---

## Cùng thực hành nào!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
luyện tập điều đó trong phần bài tập, cùng với việc tạo và trích xuất dữ liệu từ Numpy array hai chiều! Thật thú vị phải không?
