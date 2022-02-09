from utils import get_soup

soup = get_soup("/titans")


titans = [link.text for link in soup.select("b > a")]

print(titans)
print(len(titans))