---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/vi-VN/d8343f60-9c94-4b96-b96d-e1b704ad07c9-d14281d57817cac88efe347fa06556b8.mp3
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

## Bạn sẽ học như thế nào

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Giao diện DataCamp](https://assets.datacamp.com/img/translations/vi-VN/q1/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.jpg)

`@script`
Trong khóa học này, bạn sẽ học Python cho Khoa học Dữ liệu, thông qua các bài giảng video như bài giảng này và các bài tập tương tác. Bạn sẽ có một phiên làm việc Python riêng để thử nghiệm và tự viết code đúng theo yêu cầu. Bạn học bằng cách thực hành, đồng thời nhận phản hồi tức thì cho riêng bài làm của bạn.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Mục đích chung: tạo bất cứ thứ gì{{2}}

- Mã nguồn mở! Miễn phí!{{3}}

- Package Python cũng dành cho Khoa học dữ liệu{{4}}

	- Nhiều ứng dụng, nhiều lĩnh vực{{5}}

`@script`
Python được Guido Van Rossum hình thành. Ở đây, bạn có thể thấy ảnh mình chụp cùng Guido. Điều khởi đầu như một dự án làm vì sở thích đã sớm trở thành một ngôn ngữ lập trình đa dụng. Ngày nay, bạn có thể dùng Python để xây dựng hầu như mọi loại phần mềm. Nhưng điều này đã xảy ra như thế nào? Trước hết, Python là mã nguồn mở và miễn phí sử dụng. Thứ hai, việc tạo các gói bằng Python rất dễ dàng. Đó là những đoạn mã bạn có thể chia sẻ với người khác để giải quyết các vấn đề cụ thể. Theo thời gian, ngày càng có nhiều gói được phát triển riêng cho khoa học dữ liệu. Giả sử bạn muốn tạo một số biểu đồ trực quan sinh động về doanh số của công ty. Đã có gói hỗ trợ việc đó. Hoặc nếu muốn kết nối với cơ sở dữ liệu để phân tích các phép đo từ cảm biến thì sao? Cũng có gói hỗ trợ việc đó.
Người ta thường ví Python như con dao Thụy Sĩ trong các ngôn ngữ lập trình, vì bạn có thể dùng nó để làm gần như mọi thứ.
Trong khóa học này, chúng ta sẽ từng bước rèn luyện kỹ năng lập trình khoa học dữ liệu. Hãy tiếp tục theo dõi để khám phá ngôn ngữ này mạnh mẽ đến mức nào nhé.

---

##  IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Thực thi các lệnh Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/vi-VN/q1/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg = 95)

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

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/vi-VN/q1/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python shell. Đây là nơi để bạn nhập code Python và thấy kết quả ngay lập tức. Trong giao diện bài tập của DataCamp, Python shell đã được tích hợp sẵn. Hãy bắt đầu với một ví dụ đơn giản, dùng Python để tính toán.

---

##  IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
 

![Các phép tính trong IPython shell của DataCamp](https://assets.datacamp.com/img/translations/vi-VN/q1/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.jpg = 95)

`@script`
Gõ bốn cộng năm và nhấn Enter. Python diễn giải những gì bạn gõ và hiển thị kết quả phép tính, là chín. Thực ra, Python Shell này không phải là bản Python gốc. Chúng ta đang dùng IPython, viết tắt của Interactive Python, một phiên bản nâng cấp của Python thông thường mà sau này sẽ rất hữu ích.

IPython được tạo bởi Fernando Pérez. Nó là một phần của hệ sinh thái Jupyter rộng lớn hơn. Ngoài làm việc tương tác với Python, chúng ta cũng có thể cho Python chạy các

---

##  Python script

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Tệp văn bản - `.py`{{1}}

- Danh sách lệnh Python{{2}}

- Tương tự như nhập lệnh trong IPython Shell{{3}}

![Python script trong DataCamp](https://assets.datacamp.com/img/translations/vi-VN/q1/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
tập lệnh Python hay còn gọi là script. Các Python script thực chất chỉ là những tệp văn bản có phần mở rộng chấm py. Về cơ bản, chúng là một danh sách các lệnh Python được thực thi lần lượt, gần giống như việc bạn tự nhập từng dòng lệnh vào shell.

---

##  Python script

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: nhập 4 + 5 vào script rồi nhấn gửi câu trả lời. Không có kết quả nào được hiển thị.](https://assets.datacamp.com/img/translations/vi-VN/q1/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.jpg = 95)

`@script`
Giờ hãy đưa lệnh vừa rồi vào một script trong giao diện DataCamp, như bạn thấy ở đây. Bước tiếp theo, nhấn "Submit Answer" để chạy script. Nếu chúng ta chạy script này trong giao diện của DataCamp, sẽ không có gì xuất hiện ở khung kết quả. Đó là vì chúng ta phải chủ động gọi hàm print bên trong script nếu muốn hiển thị kết quả. 
---

##  Python script

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/vi-VN/q1/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.jpg = 95)

- Sử dụng `print()` để tạo đầu ra từ script

`@script`
Hãy đưa phép tính vừa rồi vào một hàm print và chạy lại script. Lần này, kết quả giống trước đã xuất hiện, rất tốt! Việc đặt các đoạn code vào Python script thay vì gõ lại từng bước thủ công sẽ giúp các đoạn code có hệ thống và tránh phải gõ đi gõ lại mọi thứ. Mỗi lần muốn thay đổi; ta chỉ cần sửa script và chạy lại toàn bộ là xong. 

---

## Giao diện DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Ảnh chụp màn hình giao diện DataCamp](https://assets.datacamp.com/img/translations/vi-VN/q1/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg)

`@script`
Giờ bạn đã hiểu sơ qua các cách làm việc với Python, hãy chuyển sang phần bài tập. Hãy dùng IPython Shell để thử nghiệm, và dùng trình soạn thảo Python script editor để viết lời giải chính thức. Khi bạn nhấn Submit Answer, script sẽ được chạy và kiểm tra độ chính xác. 
---

## Cùng thực hành nào!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Hãy bắt tay vào viết code và đừng quên học vui, vui học nhé!
