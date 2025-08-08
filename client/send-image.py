import requests

# آدرس سرور
url = "http://127.0.0.1:5000/upload"

# مسیر عکس برای ارسال
file_path = "test.jpg"

with open(file_path, "rb") as f:
    files = {"image": f}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response:", response.text)
