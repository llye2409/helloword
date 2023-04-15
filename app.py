from flask import Flask

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route mặc định
@app.route('/')
def hello():
    return 'Hello, World!'

# Chạy ứng dụng
if __name__ == '__main__':
    app.run()
