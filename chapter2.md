---
title_meta: Chương 2
title: List trong Python
description: >-
  Học cách lưu trữ, truy cập và thao tác dữ liệu trong list: bước đầu để làm
  việc hiệu quả với lượng dữ liệu lớn.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: List trong Python
  - nb_of_exercises: 4
    title: Trích xuất phần tử trong List
  - nb_of_exercises: 5
    title: Thao tác với List
---

## List trong Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Tạo một list

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

List là một **kiểu dữ liệu phức hợp**; bạn có thể gom nhiều giá trị lại với nhau, như sau:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Sau khi đo chiều cao các thành viên trong gia đình, bạn quyết định thu thập thêm một số thông tin về ngôi nhà bạn đang ở. Diện tích của các phòng khác nhau được lưu ở các biến riêng trong bài tập này.

`@instructions`
- Tạo một list, `areas`, chứa diện tích của hành lang (`hall`), bếp (`kit`), phòng khách (`liv`), phòng ngủ (`bed`) và phòng tắm (`bath`), theo đúng thứ tự này. Hãy dùng các biến đã được định nghĩa sẵn.
- Hiển thị `areas` bằng hàm `print()`.

`@hint`
- Bạn có thể dùng các biến có sẵn để tạo list: `areas = [hall, kit, ...]`.
- Dùng dấu ngoặc vuông `[]` thay vì dấu ngoặc tròn `()`.
- Không cần dùng dấu ngoặc kép khi lưu biến bên trong một list.
- Gõ `print(areas)` để hiển thị list khi nộp bài.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "Đừng xóa hoặc chỉnh sửa các biến được định nghĩa trước!"
areas_msg = "Hãy định nghĩa `areas` là danh sách chứa tất cả các biến diện tích, theo thứ tự đúng: `[hall, kit, liv, bed, bath]`. Hãy cẩn thận với lỗi chính tả. Danh sách không nên chứa bất kỳ thứ gì khác!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Bạn đã sử dụng `{{sol_call}}` để in ra danh sách `areas` ở cuối tập lệnh của bạn chưa?"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("Tuyệt! Một danh sách tốt hơn nhiều ở đây, phải không?")
```

---

## Tạo list với nhiều kiểu dữ liệu khác nhau

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Tuy không quá phổ biến, một list vẫn có thể chứa nhiều kiểu dữ liệu trong Python như string, float và boolean.

Giờ bạn thêm tên các phòng vào list để có thể thấy cả tên phòng và diện tích cùng nhau.

Đã có sẵn một phần code cho bạn bắt đầu viết. Lưu ý! `"bathroom"` là một chuỗi, còn `bath` là một biến đại diện cho số thực `9.50` mà bạn đã khai báo trước đó.

`@instructions`
- Hoàn thiện đoạn code tạo list `areas`. Tạo list sao cho mỗi phòng xuất hiện theo thứ tự: trước là tên phòng dạng string, sau đó là diện tích phòng. Nói cách khác, hãy thêm các string `"hallway"`, `"kitchen"` và `"bedroom"` vào đúng vị trí.
- Hiển thị kết quả `areas` lần nữa; lần này có nhiều thông tin hơn không?

`@hint`
- Bốn phần tử đầu tiên của danh sách `areas` được viết là `["hallway", hall, "kitchen", kit, ...`.
- String phải đặt trong dấu ngoặc kép `""`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "Đừng xóa hoặc chỉnh sửa các biến được định nghĩa trước!"
areas_msg = "Bạn đã không gán giá trị đúng cho `areas`. Hãy xem lại hướng dẫn. Đảm bảo đặt tên phòng trước biến chứa diện tích mỗi lần. Thứ tự rất quan trọng ở đây! Hãy cẩn thận với lỗi chính tả."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Bạn đã sử dụng `{{sol_call}}` để in ra danh sách `areas` ở cuối tập lệnh của bạn chưa?")

success_msg("Tuyệt vời! Danh sách này chứa cả chuỗi và số thực, nhưng điều đó không phải là vấn đề đối với Python!")
```

---

## List chứa list

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Khi làm khoa học dữ liệu, bạn sẽ phải thường xuyên làm việc với rất nhiều dữ liệu, và việc nhóm các dữ liệu liên quan với nhau lại là hợp lý.

Thay vì tạo một danh sách chứa cả string và float để biểu thị tên và diện tích các phòng trong nhà, bạn có thể tạo một list gồm nhiều list con. 

Nhớ rằng: `"hallway"` là một string, còn `hall` là một biến đại diện cho float `11.25` mà bạn đã gán trước đó.

`@instructions`
- Hoàn thiện list chứa list để có cả dữ liệu về phòng ngủ và phòng tắm. Chú ý nhập theo đúng thứ tự!
- Hiển thị `house`; bạn thấy cấu trúc dữ liệu theo cách này có hợp lý hơn không?

`@hint`
- Thêm các _sublist_ vào danh sách `house` bằng cách thêm `["bedroom", bed]` và `["bathroom", bath]` bên trong dấu ngoặc vuông.
- Nhớ đặt dấu phẩy `,` sau mỗi sublist.
- Để in một biến `x`, viết `print(x)` trên một dòng mới.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "Không được xóa hoặc chỉnh sửa các biến được định nghĩa trước!"
house_msg = "Bạn đã không gán giá trị đúng cho `house`. Hãy xem lại hướng dẫn. Mở rộng danh sách các danh sách để nó bao gồm một danh sách cho mỗi cặp tên phòng và diện tích phòng. Chú ý thứ tự và lỗi chính tả!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Bạn đã sử dụng `{{sol_call}}` để in ra nội dung của `house` chưa?")

success_msg("Tuyệt vời! Hãy sẵn sàng để học về việc chia nhỏ danh sách!")
```

---

## Trích xuất phần tử từ list

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Trích xuất và xử lý dữ liệu

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Trích xuất phần tử từ list Python thì quá dễ. Xem ví dụ bên dưới: tạo list `x` rồi chọn "b" từ list đó. Hãy nhớ đây là phần tử thứ hai, nên có index 1. Bạn cũng có thể dùng index âm.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # kết quả tương tự!
```


Bạn còn nhớ list `areas` khi nãy, gồm cả string và float không? Định nghĩa của nó đã có sẵn trong script. Bạn hãy thêm đoạn code đúng để thực hành trích xuất phần tử trong Python.

`@instructions`
- Hiển thị phần tử thứ hai của danh sách `areas` (giá trị là `11.25`).
- Trích xuất và hiển thị phần tử cuối cùng của `areas`, là `9.50`. Ở đây dùng index âm sẽ hợp lý. 
- Chọn số biểu thị diện tích phòng khách (`20.0`) và hiển thị kết quả ra.

`@hint`
- Dùng `x[1]` để chọn phần tử thứ hai của list `x`.
- Dùng `x[-1]` để chọn phần tử cuối cùng của list `x`.
- Nhớ đặt phép lấy phần tử bên trong lệnh `print()`.
- Số biểu thị diện tích phòng khách là phần tử thứ 6 trong list, nên bạn cần `[5]` ở đây. Nếu là `area[4]` kết quả trả về sẽ là một string đấy!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "Đừng xóa hoặc chỉnh sửa danh sách `areas` được định nghĩa trước."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Hãy xem lại mã của bạn để in ra phần tử thứ hai trong `areas`, nằm ở chỉ số `1`.")
Ex().has_printout(1, not_printed_msg = "Hãy xem lại mã của bạn để in ra phần tử cuối cùng trong `areas`, nằm ở chỉ số `-1`.")
Ex().has_printout(2, not_printed_msg = "Hãy xem lại mã của bạn để in ra diện tích của phòng khách. Nó nằm ở chỉ số `5`.")
success_msg("Làm tốt lắm!")
```

---

## Cắt và chọn dữ liệu (Slicing and dicing)

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Không chỉ chọn từng giá trị đơn lẻ từ một list, bạn còn có thể _slice_ list của mình, tức là chọn nhiều phần tử cùng lúc. Cú pháp như sau:

```
my_list[start:end]
```

Index `start` sẽ được tính, còn index `end` thì _không_. Tuy nhiên, bạn cũng có thể bỏ qua các index này. Nếu không chỉ định index `start`, Python sẽ hiểu bạn muốn slice từ đầu list.

`@instructions`
- Dùng kĩ thuật slice để tạo list `downstairs` chứa 6 phần tử đầu tiên của `areas`.
- Tạo `upstairs` là 4 phần tử cuối của `areas`. Lần này, hãy bỏ qua index `end`để đơn giản hoá dòng code. 
- Dùng `print()` để hiển thị cả `downstairs` và `upstairs`.

`@hint`
- Dùng dấu ngoặc `[0:6]` để lấy 6 phần tử đầu tiên của một list.
- Để lấy tất cả trừ 5 phần tử đầu tiên của một list `l`, bạn dùng `l[5:]`.
- Thêm hai lệnh `print()` để in `downstairs` và `upstairs`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "Không được xóa hoặc chỉnh sửa danh sách `areas` đã được định nghĩa trước."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` không chính xác. Sử dụng `areas[%s]` và cắt chuỗi để chọn các phần tử bạn muốn, hoặc một cách tương đương."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Bạn đã in ra `downstairs` sau khi tính toán nó chưa?")
Ex().has_printout(1, not_printed_msg="Bạn đã in ra `upstairs` sau khi tính toán nó chưa?")

success_msg("Tuyệt vời!")
```

---

## Trích xuất phần tử từ list chứa list

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Một list Python cũng có thể chứa các list khác.

Để trích xuất phần tử từ list chứa list, bạn có thể dùng lại kỹ thuật giống như trước: dấu ngoặc vuông. Với list `house`, code sẽ như sau:

```
house[2][0]
```

`@instructions`
- Trích xuất từ list `house` để lấy số float `9.5`.

`@hint`
- Hãy chia nhỏ từng bước. Trước hết, bạn cần lấy phần tử cuối cùng của list, `["bathroom", 9.50]`. Nhớ rằng index của phần tử cuối cùng là `-1`.
- Tiếp theo, bạn lấy phần tử thứ hai của `["bathroom", 9.50]`, nằm ở chỉ số `1`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("Chính xác! Mảnh ghép cuối cùng của câu đố danh sách là thao tác.")
```

---

## Thao tác với List

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Thay thế phần tử trong list

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Để thay thế các phần tử trong list, bạn lấy phần con (subset) của list và gán giá trị mới cho phần con đó. Bạn có thể chọn từng phần tử hoặc thay đổi cả một lát cắt (slice) của list cùng lúc.

Trong bài này và các bài tiếp theo, bạn sẽ tiếp tục làm việc với list `areas` chứa tên và diện tích của các phòng trong một ngôi nhà.

`@instructions`
- Cập nhật diện tích phòng tắm thành `10.50` mét vuông thay vì `9.50` bằng cách dùng chỉ số âm.
- Hãy làm cho list `areas` xịn xò hơn! Đổi `"living room"` thành `"chill zone"`. Lần này bạn đừng dùng chỉ số âm.

`@hint`
- Để cập nhật diện tích phòng tắm, hãy xác định phần tử tương ứng với phòng tắm (nó là phần tử cuối cùng trong list!).
- Sau đó, thay giá trị cũ bằng diện tích phòng tắm mới bằng cách gán giá trị mới cho phần tử này
- Làm tương tự để cập nhật tên `"living room"`, nằm ở index 4.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = 'Bạn có thể sử dụng `areas[-1] = 10.50` để cập nhật diện tích phòng tắm.'
chillzone_msg = 'Bạn có thể sử dụng `areas[4] = "chill zone"` để cập nhật tên phòng khách.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Các thay đổi của bạn đối với `areas` không dẫn đến danh sách chính xác. Bạn có chắc chắn rằng bạn đã sử dụng các thao tác tập hợp con đúng không? Khi nghi ngờ, bạn có thể sử dụng gợi ý!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Tuyệt! Như ví dụ mã đã chỉ ra, bạn cũng có thể cắt một danh sách và thay thế nó bằng một danh sách khác để cập nhật nhiều phần tử trong một lệnh duy nhất.')
```

---

## Mở rộng một list

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Nếu bạn có thể thay đổi phần tử trong một list, vậy bạn cũng muốn thêm phần tử vào list, đúng không? Bạn có thể dùng toán tử `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```
Giả sử bạn vừa trúng số. Bạn quyết định xây thêm một bể bơi và một ga-ra. Bạn có thể thêm hai thông tin này vào list `areas` không?

`@instructions`
- Dùng toán tử `+` để nối list `["poolhouse", 24.5]` vào cuối list `areas`. Lưu list kết quả là `areas_1`.
- Mở rộng `areas_1` bằng cách thêm dữ liệu về garage của bạn. Thêm string `"garage"` và float `15.45`. Đặt tên list kết quả là `areas_2`.

`@hint`
- Làm theo dòng code mẫu trong bài. Ở đây `x` chính là `areas`, và `["e", "f"]` tương ứng với `["poolhouse", 24.5]`.
- Để thêm nhiều phần tử vào `areas_1`, dùng `areas_1 + ["element", 123]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "Đừng xóa hoặc chỉnh sửa danh sách `areas` được định nghĩa trước."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Sử dụng `areas + [\"poolhouse\", 24.5]` để tạo `areas_1`. Hãy cẩn thận với lỗi chính tả!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Sử dụng `areas_1 + [\"garage\", 15.45]` để tạo `areas_2`. Hãy cẩn thận với lỗi chính tả!")
success_msg("Tuyệt! Danh sách đang được định hình rất tốt!")
```

---

## Xóa phần tử trong list

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Cuối cùng, bạn có thể xóa phần tử khỏi list với câu lệnh `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```


Lưu ý: ngay khi bạn xóa một phần tử khỏi list, index của tất cả các phần tử đứng sau nó sẽ thay đổi!


Thật không may, số tiền bạn trúng xổ số không lớn như bạn đã nghĩ và có lẽ sẽ không có hồ bơi. Vì vậy bạn cần phải xóa nó khỏi list. Hãy xóa string và float tương ứng với hồ bơi khỏi list `areas `

`@instructions`
- Xóa string và float của `"poolhouse"` khỏi list `areas` của bạn.
- Hiển thị ra list `areas` đã được cập nhật.

`@hint`
- Bạn phải dùng `del` hai lần để xóa hai phần tử. Nhưng lưu ý khi xóa sẽ thì index sẽ thay đổi.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="Bạn đã in ra `areas` sau khi xóa chuỗi và số thực poolhouse chưa?")
success_msg("Chính xác! Bạn sẽ học về những cách dễ dàng hơn để xóa các phần tử cụ thể khỏi danh sách Python sau này.")
```

---

## Cách hoạt động bên trong list

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

Trong bài tập này, đã có sẵn một số đoạn code: một list tên là `areas` và một bản sao tên `areas_copy`.

Hiện tại, phần tử đầu tiên trong list `areas_copy` được thay đổi và kết quả của list `areas` được hiển thị. Nếu bạn bấm nút chạy code, bạn sẽ thấy khi bạn thay đổi `areas_copy`, thay đổi đó cũng xuất hiện trong list `areas`. Lý do là `areas` và `areas_copy` cùng chỉ đến một list.

Nếu bạn muốn ngăn việc thay đổi ở `areas_copy` ảnh hưởng đến `areas`, bạn phải tạo một bản sao riêng biệt của list `areas` bằng `list()` hoặc dùng `[:]`.

`@instructions`
- Hãy sửa lệnh thứ hai, lệnh tạo biến `areas_copy`, sao cho `areas_copy` là một bản sao riêng biệt của `areas`. Sau khi chỉnh sửa, các thay đổi với `areas_copy` sẽ không ảnh hưởng đến `areas`. Gửi đáp án để kiểm tra.

`@hint`
- Hãy thay đổi lệnh `areas_copy = areas`. Thay vì gán `areas`, bạn có thể gán `list(areas)` hoặc `areas[:]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "Có vẻ như `areas_copy` chưa được cập nhật đúng cách."),
  check_function("list", missing_msg = "Hãy chắc chắn sử dụng `list(areas)` để tạo một `areas_copy`.")
)

mmsg = "Đừng xóa danh sách `areas` được định nghĩa trước."
imsg = "Hãy chắc chắn chỉ chỉnh sửa bản sao, không phải danh sách `areas` gốc. Hãy xem lại mô tả bài tập nếu bạn không chắc chắn cách tạo một bản sao."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Hãy chắc chắn sử dụng `list(areas)` để tạo một `areas_copy`.")
)

success_msg("Tuyệt vời! Sự khác biệt giữa bản sao rõ ràng và bản sao tham chiếu là tinh tế, nhưng có thể thực sự quan trọng. Hãy cố gắng ghi nhớ cách một danh sách được lưu trữ trong bộ nhớ của máy tính.")
```
