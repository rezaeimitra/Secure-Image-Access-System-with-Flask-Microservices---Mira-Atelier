from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import mysql.connector

app = Flask(__name__)
CORS(app)

# تنظیمات اتصال به MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # رمز عبور رو وارد کن اگه داری
    'database': 'your_database_name'  # اسم دیتابیس‌ات رو اینجا بزن
}

@app.route('/')
def home():
    return jsonify({"message": "Gateway server is running!"})

# تابع برای بررسی access_code و گرفتن user_id
def get_user_folder_by_access_code(code):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id FROM user WHERE access_code = %s", (code,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            user_id = result['id']
            return f"user_{user_id}"
        else:
            return None
    except mysql.connector.Error as err:
        print("Database error:", err)
        return None

@app.route('/get_images', methods=['GET'])
def get_images():
    access_code = request.args.get('access_code')
    if not access_code:
        return jsonify({"error": "access_code is required"}), 400

    user_folder = get_user_folder_by_access_code(access_code)
    if not user_folder:
        return jsonify({"error": "Invalid access code"}), 403

    try:
        response = requests.get("http://localhost:5001/list-images", params={"access_code": access_code})
        return jsonify(response.json()), response.status_code
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Image service unavailable"}), 503

@app.route('/upload-image', methods=['POST'])
def upload_image():
    access_code = request.form.get('access_code')
    if not access_code:
        return jsonify({"error": "access_code is required"}), 400

    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    user_folder = get_user_folder_by_access_code(access_code)
    if not user_folder:
        return jsonify({"error": "Invalid access code"}), 403

    file = request.files['image']

    try:
        response = requests.post(
            "http://localhost:5001/upload",
            files={"image": (file.filename, file.stream, file.mimetype)},
            data={"user_folder": user_folder}
        )
        return jsonify(response.json()), response.status_code
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Image service unavailable"}), 503

if __name__ == '__main__':
    print("== Gateway server running ==")
    app.run(host='0.0.0.0', port=5000)
