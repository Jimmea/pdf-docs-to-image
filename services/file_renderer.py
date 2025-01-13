import fitz  # PyMuPDF
from docx import Document
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
import os

class FileRenderer:
    def render(self, file_path):
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".pdf":
            return self.render_pdf(file_path)
        elif file_extension in [".docx", ".doc"]:
            return self.render_docx(file_path)
        else:
            raise ValueError("Định dạng file không được hỗ trợ. Hãy dùng PDF, DOC, hoặc DOCX.")

    def render_pdf(self, file_path):
        pdf_document = fitz.open(file_path)
        page = pdf_document[0]
        pix = page.get_pixmap(dpi=150)
        image_data = pix.tobytes("png")
        return base64.b64encode(image_data).decode('utf-8')

    def render_docx(self, file_path):
        # Đọc nội dung văn bản từ file docx
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])

        # Đảm bảo rằng văn bản được mã hóa bằng UTF-8 (tránh lỗi 'latin-1')
        try:
            text = text.encode('utf-8').decode('utf-8')
        except UnicodeEncodeError as e:
            # Nếu có lỗi mã hóa, có thể xử lý lỗi tại đây
            print(f"Lỗi mã hóa: {e}")
            text = text.encode('utf-8', 'ignore').decode('utf-8')  # Loại bỏ các ký tự không hợp lệ

        # Tạo ảnh với kích thước nhất định
        img = Image.new("RGB", (800, 1000), color="white")
        draw = ImageDraw.Draw(img)

        # Kiểm tra xem có font mặc định nào trong PIL không để vẽ với font phù hợp
        try:
            font = ImageFont.load_default()  # Sử dụng font mặc định nếu không có font tùy chỉnh
        except IOError:
            font = None  # Nếu không thể tải font mặc định, sử dụng font None

        # Vẽ từng dòng văn bản (tránh lỗi liên quan đến ký tự đặc biệt)
        y_position = 10
        line_height = 25
        for line in text.split("\n"):
            # Kiểm tra nếu văn bản ra ngoài ảnh
            if y_position + line_height > img.height:
                break  # Dừng lại nếu đã hết không gian ảnh
            try:
                draw.text((10, y_position), line, font=font, fill="black")
            except Exception as e:
                print(f"Lỗi khi vẽ dòng văn bản: {e}")
            y_position += line_height


        # Lưu ảnh vào bộ nhớ
        try:
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
            return img_base64  # Trả về ảnh Base64
        except Exception as e:
            print(f"Lỗi khi lưu ảnh vào bộ nhớ: {e}")
            return None