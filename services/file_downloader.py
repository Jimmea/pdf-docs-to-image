import requests
import os

class FileDownloader:
    def download(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Không thể tải file. Mã lỗi HTTP: {response.status_code}")

        # Lưu file tạm
        temp_file_path = f"temp_file.{url.split('.')[-1]}"
        with open(temp_file_path, "wb") as file:
            file.write(response.content)

        return temp_file_path
