from utils import get_soup

soup = get_soup("/spend")


def get_total_spend(tr):
    tds = tr.select("td")

    name = tds[0].text

    total = 0

    for td in tds[1:]:
        money = td.text[1:].split(" ", 1)[0]
        total += float(money.replace(",", ""))

    return {"name": name, "total": total}


teams = [get_total_spend(tr) for tr in soup.select("#ich tbody tr")]

print(teams)
