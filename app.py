import logging
from flask import Flask, jsonify, request
from api.file_processor import FileProcessor

# Cấu hình logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/process_file', methods=['POST'])
def process_file():
    try:
        # Lấy đường dẫn URL từ request
        file_url = request.form['file_path']

        if not file_url:
            logger.error("Không có tham số 'file_path' trong yêu cầu!")  # Log khi thiếu tham số
            return jsonify({"error": "Không có tham số 'file_path' trong yêu cầu!"}), 400

        # Sử dụng lớp FileProcessor để xử lý
        processor = FileProcessor()
        base64_image = processor.process(file_url)

        logger.info(f"Xử lý thành công file từ URL: {file_url}")  # Log khi thành công
        return jsonify({"base64_image": base64_image}), 200

    except Exception as e:
        logger.error(f"Lỗi trong quá trình xử lý file: {str(e)}")  # Log lỗi chi tiết
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
