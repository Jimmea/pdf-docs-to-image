from services.file_downloader import FileDownloader
from services.file_renderer import FileRenderer


import os

class FileProcessor:
    def __init__(self):
        self.downloader = FileDownloader()
        self.renderer = FileRenderer()

    def process(self, file_url):
        try:
            # Tải file từ URL
            local_file_path = self.downloader.download(file_url)

            # Render Base64 từ file
            base64_image = self.renderer.render(local_file_path)

            # Xóa file tạm sau khi xử lý
            os.remove(local_file_path)

            return base64_image

        except Exception as e:
            raise Exception(f"Xử lý file gặp lỗi: {e}")
