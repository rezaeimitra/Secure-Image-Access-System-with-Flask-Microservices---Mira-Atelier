from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
BASE_UPLOAD_FOLDER = os.path.abspath('images')
os.makedirs(BASE_UPLOAD_FOLDER, exist_ok=True)

# آپلود عکس - هم برای کاربر با access_code و هم برای ادمین با user_id
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('image')
    if not file:
        return jsonify({"error": "No image file provided"}), 400

    access_code = request.form.get('access_code')
    user_id = request.form.get('user_id')

    if access_code:
        folder_name = access_code
    elif user_id:
        folder_name = f"user_{user_id}"
    else:
        return jsonify({"error": "Access code or user ID is required"}), 400

    # ایجاد پوشه برای کاربر یا ادمین
    user_folder = os.path.join(BASE_UPLOAD_FOLDER, folder_name)
    os.makedirs(user_folder, exist_ok=True)

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(user_folder, file.filename)
    file.save(filepath)

    return jsonify({
        "message": "Image uploaded successfully",
        "filename": file.filename,
        "url": f"http://localhost:5001/images/{folder_name}/{file.filename}"
    }), 200

# لیست عکس‌های کاربر بر اساس access_code
@app.route('/list-images', methods=['GET'])
def list_images():
    access_code = request.args.get('access_code')
    if not access_code:
        return jsonify({"error": "Access code is required"}), 400

    user_folder = os.path.join(BASE_UPLOAD_FOLDER, access_code)
    if not os.path.exists(user_folder):
        return jsonify({"images": []})

    files = os.listdir(user_folder)
    images = [
        {"id": i+1, "name": f, "url": f"http://localhost:5001/images/{access_code}/{f}"}
        for i, f in enumerate(files)
    ]
    return jsonify({"images": images})

# سرو عکس‌ها از مسیر درست
@app.route('/images/<folder>/<path:filename>')
def serve_image(folder, filename):
    folder_path = os.path.join(BASE_UPLOAD_FOLDER, folder)
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    print("== Image Service running on port 5001 ==")
    app.run(port=5001)
