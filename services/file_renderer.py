import fitz  # PyMuPDF
from docx import Document
from PIL import Image, ImageDraw
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
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])

        # Tạo ảnh từ nội dung văn bản
        img = Image.new("RGB", (800, 1000), color="white")
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), text, fill="black")

        # Lưu ảnh tạm trong bộ nhớ và encode Base64
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return base64.b64encode(buffer.read()).decode('utf-8')
