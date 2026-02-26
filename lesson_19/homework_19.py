import requests

BASE_URL = "https://images-api.nasa.gov"


# ========================= Поиск Фото =========================
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
}
response = requests.get(search_url, params=search_params)
response.raise_for_status()
data = response.json()


# ========================= Получение ID =========================
items = data["collection"]["items"]
nasa_ids = []
for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)
nasa_ids = nasa_ids[:2]
print("NASA IDs:", nasa_ids)


# ========================= Получение assets =========================
def get_jpg_url(nasa_id: str):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    response = requests.get(asset_url)
    response.raise_for_status()
    asset_data = response.json()
    items = asset_data["collection"]["items"]
    for item in items:
        url = item["href"]
        if url.lower().endswith(".jpg"):
            return url
    return None


# ========================= Загрузка Фото =========================
def download_image(url: str, filename: str):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Saved: {filename}")


# ========================= main логика =========================
for i, nasa_id in enumerate(nasa_ids, start=1):
    jpg_url = get_jpg_url(nasa_id)
    if jpg_url:
        filename = f"mars_photo{i}.jpg"
        download_image(jpg_url, filename)
    else:
        print(f"No JPG found for {nasa_id}")