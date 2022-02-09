from utils import get_soup

soup = get_soup("/soup")

links = []

for link in soup.select("#bodyContent a[href]"):
    href = link.get("href")

    if href and "wikipedia.org" in href:
        links.append(href)

print(links)
