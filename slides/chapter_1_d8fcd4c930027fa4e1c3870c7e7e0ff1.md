---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/vi-VN/53597e59-4597-458f-9044-b804455d6783.mp3
---

## Xin chào Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Xin chào, mình là Hugo và mình sẽ đồng hành cùng bạn trong khóa học Nhập Môn Python Cho Khoa Học Dữ Liệu. 

Mình là nhà khoa học dữ liệu và là giảng viên tại DataCamp.
---

## Phương pháp học

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Giao diện DataCamp](https://assets.datacamp.com/img/translations/vi-VN/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
Trong khóa học này, bạn sẽ học Python cho Khoa học Dữ liệu thông qua các bài giảng video như bài giảng này và các bài tập tương tác. Bạn sẽ có một phiên làm việc Python riêng để thử nghiệm và tự viết code đúng theo yêu cầu. Bạn học bằng cách thực hành, đồng thời nhận phản hồi tức thì cho riêng bài làm của bạn.
---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/vi-VN/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Mục đích chung: xây dựng bất kỳ thứ gì{{2}}

- Mã nguồn mở! Miễn phí!{{3}}

- Các package Python, có cả cho khoa học dữ liệu{{4}}

	- Nhiều ứng dụng trong nhiều lĩnh vực{{5}}

`@script`
Python do Guido Van Rossum sáng tạo ra. Ở đây, bạn có thể thấy một bức ảnh mình chụp cùng Guido. Từ một dự án làm cho vui, Python đã nhanh chóng trở thành ngôn ngữ lập trình đa năng: ngày nay, bạn có thể dùng Python để xây dựng hầu như bất kỳ phần mềm nào. Nhưng tại sao lại như vậy? Trước hết, Python là mã nguồn mở. Hoàn toàn miễn phí. Thứ hai, việc xây dựng các thư mục trong Python rất dễ dàng bởi vì bạn có thể chia sẻ những đoạn code với người khác để giải quyết các vấn đề cụ thể. Theo thời gian, ngày càng có nhiều thư mục dành riêng cho khoa học dữ liệu. Giả sử bạn muốn vẽ những biểu đồ trực quan sinh động về doanh số công ty, đã có thư mục cho việc đó. Hoặc bạn cần kết nối cơ sở dữ liệu để phân tích các số đo cảm biến? Cũng có thư mục cho việc đó.
Python được gọi là “dao đa năng” trong các ngôn ngữ lập trình vì bạn có thể làm gần như mọi thứ với nó.
Trong khóa học này, chúng ta sẽ từng bước xây dựng cho bạn kỹ năng lập trình dùng trong khoa học dữ liệu. Vậy nên hãy theo dõi đến cuối để thấy ngôn ngữ này mạnh mẽ đến mức nào nhé!
---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Thực thi các lệnh Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/vi-VN/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Giờ bạn đã sẵn sàng, hãy bắt đầu khám phá nào. Mình sẽ bắt đầu với
---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Thực thi các lệnh Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/vi-VN/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python shell là một nơi cho phép bạn nhập code Python và thấy kết quả ngay lập tức. Trong giao diện bài tập của DataCamp, Python shell này được tích hợp sẵn tại đây. Hãy bắt đầu với một ví dụ đơn giản, sử dụng Python như một chiếc máy tính.
---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Các phép tính trong IPython của DataCamp](https://assets.datacamp.com/img/translations/vi-VN/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif =95)

`@script`
Gõ 4 + 5 và nhấn Enter. Python diễn giải những gì bạn gõ và hiển thị kết quả phép tính, là 9. Python Shell này thực ra không phải là bản Python gốc; chúng ta đang dùng IPython, viết tắt của Interactive Python, một phiên bản nâng cấp của Python thông thường mà sẽ rất hữu ích về sau.

IPython được tạo bởi Fernando Pérez và là một phần của hệ sinh thái Jupyter rộng lớn hơn. Ngoài làm việc tương tác với Python, bạn cũng có thể cho Python chạy các
---

## Python Script

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Tệp văn bản - `.py`{{1}}

- Danh sách các lệnh trong Python{{2}}

- Tương tự như khi nhập lệnh trong IPython Shell{{3}}

![Python Script trong DataCamp](https://assets.datacamp.com/img/translations/vi-VN/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
Python script. Các Python script thực chất chỉ là những tập văn bản có phần mở rộng .py. Về cơ bản, chúng là một danh sách các lệnh Python được thực thi, gần giống như việc bạn tự gõ từng dòng lệnh trong shell, từng dòng một.
---

## Python Script

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: Nhập 4 + 5 vào ô nhập liệu và nhấn nút gửi câu trả lời Không hiển thị kết quả.](https://assets.datacamp.com/img/translations/vi-VN/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Giờ hãy đưa lệnh vừa rồi vào một script, bạn có thể tìm thấy script ngay tại đây trong giao diện của DataCamp. Bước tiếp theo là chạy script bằng cách nhấn "Submit Answer". Nếu bạn chạy script này trong giao diện của DataCamp, ô kết quả sẽ không hiển thị gì. Đó là vì bạn phải dùng lệnh print bên trong script để hiển thị kết quả.
---

## Python Script

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/vi-VN/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Sử dụng `print()` để tạo ra kết quả từ script.

`@script`
Hãy bọc phép tính vừa rồi trong một lệnh print và chạy lại script. Lần này, kết quả giống trước đã xuất hiện, rất tốt! Việc đặt các đoạn code vào Python script thay vì gõ lại từng bước thủ công sẽ giúp bạn giữ nguyên cấu trúc và tránh phải gõ đi gõ lại mọi thứ. Mỗi lần muốn thay đổi; bạn chỉ cần sửa script và chạy lại toàn bộ là xong.
---

## Giao diện DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Ảnh chụp màn hình giao diện DataCamp](https://assets.datacamp.com/img/translations/vi-VN/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Giờ bạn đã hình dung được những cách làm việc khác nhau với Python, mình gợi ý bạn chuyển sang phần bài tập. Dùng IPythonPython Shell để thử nghiệm, và dùng Python script editor để viết lời giải chính thức. Khi bạn nhấn Submit Answer, script sẽ được chạy và kiểm tra độ chính xác.
---

## Hãy thực hành nào!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Hãy bắt đầu lập trình và đừng quên học vui, vui học nhé!
