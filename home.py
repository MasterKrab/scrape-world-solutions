from utils import get_soup

soup = get_soup("/")

# hidden_paragraph = soup.find("p", hidden=True)
hidden_paragraph = soup.select_one("p[hidden]")

print(hidden_paragraph.text)