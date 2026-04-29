# Tóm tắt nội dung buổi học: Vòng lặp và thao tác file trong Python

## 1. Tổng quan buổi học

Chào các bạn, buổi học hôm nay chúng ta sẽ chinh phục một trong những cột trụ quan trọng nhất của lập trình: cấu trúc lặp. Mục tiêu cốt lõi không chỉ là học cú pháp mà là xây dựng tư duy logic để điều khiển máy tính thực hiện các tác vụ lặp đi lặp lại một cách tự động.

Chúng ta sẽ áp dụng vòng lặp để hiện thực hóa các thuật toán toán học thực tế như tính số Pi hay tìm căn bậc hai.

> "Kỹ năng lập trình tỉ lệ thuận với thời gian bạn tự mày mò, thử nghiệm và đối mặt với lỗi. Đừng sợ sai, vì logic của bạn sẽ sắc bén nhất chính trong quá trình gỡ lỗi (debugging). Đó là một kỹ năng không thể thiếu trên con đường trở thành chuyên gia."

Làm chủ được vòng lặp chính là chìa khóa để bạn tối ưu hóa mã nguồn và xử lý dữ liệu quy mô lớn sau này.

## 2. Khám phá vòng lặp `for` và hàm `range()`

Vòng lặp `for` giúp lập trình viên tự động hóa công việc, thay vì phải viết tay hàng trăm dòng mã tương tự nhau.

### Phân tích hàm `range()`

Hàm `range()` là "cỗ máy" sinh số phổ biến nhất. Điểm mấu chốt bạn cần nhớ là giá trị kết thúc (`stop`) luôn dừng lại ở `n - 1`.

| Cách sử dụng | Cấu trúc | Kết quả ví dụ | Giải thích |
| --- | --- | --- | --- |
| Một tham số | `range(stop)` | `range(5)` -> `0, 1, 2, 3, 4` | Mặc định từ `0` và dừng trước `stop`. |
| Hai tham số | `range(start, stop)` | `range(1, 6)` -> `1, 2, 3, 4, 5` | Bắt đầu từ `start` và dừng trước `stop`. |
| Ba tham số | `range(start, stop, step)` | `range(0, 11, 2)` -> `0, 2, 4, 6, 8, 10` | Nhảy theo bước (`step`) xác định. |

**Pro-tip từ mentor:** Trong trường hợp bạn chỉ cần lặp lại một hành động mà không quan tâm đến giá trị của biến đếm, hãy sử dụng dấu gạch dưới `_` thay cho tên biến, ví dụ: `for _ in range(5):`. Cách này giúp mã nguồn gọn gàng hơn.

### Cơ chế cập nhật biến (Assignment Logic)

Một sai lầm phổ biến của người mới bắt đầu là nhìn phép gán `total = total + i` theo góc độ toán học. Trong lập trình, hãy hiểu theo cơ chế "trái - phải":

- Vế phải (`total + i`): Là các giá trị hiện tại được lấy ra để thực hiện phép tính.
- Vế trái (`total`): Là "ngăn chứa" sẽ nhận kết quả mới của phép tính đó để lưu trữ cho lần lặp sau.
- Tính tổng: Khởi tạo `total = 0`.
- Tính tích (giai thừa): Khởi tạo `result = 1`. Nếu khởi tạo bằng `0` thì mọi phép nhân đều bằng `0`.

## 3. Điều khiển luồng lặp: `break` và `continue`

Việc kiểm soát vòng lặp một cách chiến lược giúp chương trình hoạt động thông minh và tiết kiệm tài nguyên.

- `break` (dừng và thoát): Sử dụng khi đã tìm thấy mục tiêu. Ví dụ: khi tìm nhân viên trong database 1000 người, nếu tìm thấy ở vị trí thứ 10, lệnh `break` giúp thoát ngay lập tức, tiết kiệm 990 lần chạy vô ích.
- `continue` (lờ đi và tiếp tục): Bỏ qua một trường hợp đặc biệt nhưng vẫn thực hiện các lượt lặp tiếp theo. Ví dụ: khi tăng lương, nếu gặp nhân viên không đủ điều kiện, ta dùng `continue` để bỏ qua họ và xét người kế tiếp.

### Sự khác biệt về vị trí lệnh `print`

- `print` trước lệnh `break`: Giá trị thỏa mãn điều kiện vẫn sẽ được in ra trước khi vòng lặp dừng.
- `print` sau lệnh `break`: Giá trị thỏa mãn điều kiện sẽ không bao giờ xuất hiện vì vòng lặp đã thoát trước khi lệnh `print` được chạm tới.

## 4. Hiện thực hóa thuật toán và công thức toán học

Lập trình là quá trình "ánh xạ" từ công thức toán học sang mã nguồn Python.

### Thuật toán tính số Pi

Công thức:

`4 * Σ(i = 1..n) [(-1)^(i + 1) / (2i - 1)]`

- Dùng `for i in range(1, n + 1):` để đảm bảo tính đến giá trị thứ `n`.
- Cập nhật biến `pi` theo công thức trong mỗi lượt lặp và cuối cùng nhân tất cả với `4`.

### Thuật toán Newton tính căn bậc hai

Công thức lặp:

`x_(n+1) = (x_n + a / x_n) / 2`

- Khởi tạo: Theo kinh nghiệm, hãy bắt đầu với giá trị đoán `x = a / 2`.
- Cơ chế: Lấy kết quả của lượt lặp này làm đầu vào cho lượt lặp sau. Sau khoảng 10 vòng lặp, giá trị sẽ hội tụ cực sát với căn bậc hai thực tế của `a`.

### Tính giai thừa (`n!`)

- Khởi tạo `result = 1`.
- Sử dụng `range(1, n + 1)` vì nếu chỉ dùng `range(1, n)`, Python sẽ dừng lại ở `n - 1`, làm kết quả bị sai lệch.

## 5. Vòng lặp `while` và thao tác file

### Vòng lặp `while`

Khác với `for` (biết trước số lần lặp), `while` lặp dựa trên một điều kiện đúng hoặc sai.

- Infinite loop (`while True`): Ứng dụng trong các hệ thống cần chạy liên tục không ngừng như camera giám sát hoặc các cảm biến (`sensor`) thu thập dữ liệu thời gian thực.

### Thao tác file cơ bản

Tương tác với ổ cứng luôn gồm 3 bước bắt buộc:

1. Mở file (`open`): Thiết lập kết nối.
2. Đọc/ghi dữ liệu: Thao tác nội dung.
3. Đóng file (`close`): Cực kỳ quan trọng. Việc đóng file giúp giải phóng bộ nhớ RAM và đảm bảo dữ liệu được lưu xuống ổ cứng an toàn, tránh mất mát khi chương trình gặp sự cố.

## 6. Hệ thống ôn tập và tự đánh giá

### Checklist ôn tập nhanh

- [ ] Thành thục cú pháp `range(start, stop, step)`.
- [ ] Hiểu rõ tại sao `range(1, n)` không lấy giá trị `n`.
- [ ] Phân biệt được tác động của `break` và `continue`.
- [ ] Luôn có lệnh `close()` sau khi thao tác với file.

### Câu hỏi tự kiểm tra

1. Tình huống: Để tính tổng các số chẵn từ `0` đến `10` (lấy cả số `10`), bạn phải thiết lập `range` như thế nào? Gợi ý: Hãy nhớ quy tắc `n + 1`.
2. Logic: Trong phép gán `x = x + 5`, vế trái và vế phải đại diện cho điều gì trong bộ nhớ máy tính?
3. Thiết kế: Tại sao trong các bài toán tính tích, chúng ta tuyệt đối không khởi tạo biến bằng `0`?
4. Ứng dụng: Khi lập trình một hệ thống báo động hoạt động `24/7`, bạn sẽ chọn vòng lặp `for` hay `while True`? Tại sao?

> "Nói thì dễ, đưa mã nguồn chạy được ra đây mới là bằng chứng thép. Hãy luôn thực hành trên máy của mình để thực sự làm chủ kiến thức."
