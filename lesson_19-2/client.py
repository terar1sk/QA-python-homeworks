import requests
import os
from urllib.parse import urlparse

BASE_URL = "http://127.0.0.1:8080"


# ========================= POST upload =========================
def upload_image(path):
    with open(path, "rb") as f:
        files = {"image": f}
        response = requests.post(
            f"{BASE_URL}/upload",
            files=files
        )
    response.raise_for_status()
    data = response.json()
    return data["image_url"]


# ========================= GET =========================
def get_image_url(filename):
    headers = {"Content-Type": "text"}
    response = requests.get(
        f"{BASE_URL}/image/{filename}",
        headers=headers
    )
    response.raise_for_status()
    return response.json()


# ========================= DELETE =========================
def delete_image(filename):
    response = requests.delete(
        f"{BASE_URL}/delete/{filename}"
    )
    response.raise_for_status()
    return response.json()


# ========================= main логика =========================
if __name__ == "__main__":
    image_path = "test.jpg"

    # POST
    image_url = upload_image(image_path)
    print("Uploaded:", image_url)
    filename = os.path.basename(urlparse(image_url).path)

    # GET
    result = get_image_url(filename)
    print("GET:", result)

    # DELETE
    result = delete_image(filename)
    print("DELETE:", result)