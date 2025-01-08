# Flask API Project

Đây là một dự án API Flask để xử lý các file PDF và chuyển đổi các trang đầu của chúng thành hình ảnh, sau đó trả về kết quả dưới dạng base64.

# Các thư viện sử dụng
- Flask: Framework web để xây dựng API.
- requests: Thư viện để tải file từ URL.
- pdf2image: Chuyển đổi file PDF thành hình ảnh.
- Pillow: Thư viện xử lý hình ảnh.
- PyPDF2: Thư viện để làm việc với file PDF.

## Yêu cầu

Trước khi bắt đầu, hãy đảm bảo rằng bạn có cài đặt các phần mềm sau:
- Python 3.x
- pip (trình quản lý gói Python)


## Cài đặt
1. **Clone dự án từ GitHub (hoặc tải xuống mã nguồn)**:
   Nếu bạn chưa có mã nguồn, bạn có thể clone từ GitHub hoặc tải xuống và giải nén file.
   ```bash
   git clone <URL của dự án>
   cd <thư mục dự án>

2. **Tạo và kích hoạt môi trường ảo**
Tạo và kích hoạt môi trường ảo (tùy chọn, nhưng khuyến khích): Để tránh xung đột với các gói hệ thống, bạn nên sử dụng môi trường ảo.
```
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate  
```

3. **Cài đặt các thư viện yêu cầu:**
Sử dụng file requirements.txt để cài đặt tất cả các thư viện cần thiết.
```
pip install -r requirements.txt
```

4. **Tạo file requirements.txt:**
Giả sử bạn đã kích hoạt môi trường ảo, bạn chỉ cần chạy lệnh sau để xuất tất cả các thư viện và phiên bản của chúng vào file `requirements.txt`:
```
pip freeze > requirements.txt
```

5. **Chạy ứng dụng Flask:**
Sau khi cài đặt xong, bạn có thể chạy ứng dụng Flask bằng cách thực thi file app.py (hoặc file chính của bạn).

```
gunicorn -w 4 -b 0.0.0.0:8000 app:app

```

6. **Truy cập API:**
API sẽ chạy trên địa chỉ mặc định http://127.0.0.1:5000/ (hoặc địa chỉ bạn đã cấu hình). Bạn có thể gửi các yêu cầu POST với tham số đường dẫn file PDF (hoặc URL file PDF) đến API để nhận kết quả.

```
curl -X POST -F "file_path=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" http://127.0.0.1:5000/process_file
```