from playwright.sync_api import sync_playwright
from config import BASE_URL
# from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"{BASE_URL}/population", wait_until="networkidle")

    bacterias_population = None

    while not bacterias_population:
        bacterias_population = page.evaluate("""() => {
            const list = document.getElementById("infinite-list")

            list.scrollTop = list.scrollHeight
            
            if(list.children.length < 365) return null
            
            const bacterias = Array.from(list.children).slice(0, 365)

            return bacterias.map((item, index) => {
                const words = item.textContent.split(" ")

                return {
                    day: index + 1,
                    population: words[words.length - 1]
                }
            })
        }""")

    # infinite_list = page.query_selector("#infinite-list")
    #
    # js_function = """(element) => {
    #         element.scrollTop = element.scrollHeight
    #         return element.children.length >= 365
    # }"""
    #
    # while True:
    #     if page.evaluate(js_function, infinite_list): break
    #
    # html = page.content()
    # soup = BeautifulSoup(html, "html.parser")
    #
    # bacterias_population = []
    # items = soup.find_all("li")
    #
    # for i in range(365):
    #     bacterias_population.append(
    #         {
    #             "day": i + 1,
    #             "population": items[i].text.split(" ")[-1]
    #         }
    #     )

    browser.close()

    print(bacterias_population)
