from utils import get_soup
from config import BASE_URL
import requests

soup = get_soup("/books")

# 1
book_container = soup.select_one("div.book-filthy")

book = {
    "title": book_container.select_one("h4").text,
    "price": book_container.select_one("p").text,
    "image": book_container.select_one("img")["src"],
}

print(book)


# 2
def download(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)


video = f"{BASE_URL}{soup.select_one('video source')['src']}"
images = [f"{BASE_URL}{image['src']}" for image in soup.select("img")]
audio = f"{BASE_URL}{soup.select_one('audio source')['src']}"

download(video, "video.mp4")
download(audio, "audio.mp3")

for image in images:
    download(image, f"{image.split('/')[-1]}")


# 3
def get_book_price(book):
    return {
        "title": book.select_one("h4").text,
        "price": book.select_one("p").text,
    }


books = [get_book_price(book) for book in soup.select('div[class^="book-"]')]

print(books)
