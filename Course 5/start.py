from file_saver import append_to_file, create_recipe_from_page
from scrappers import page_scrapper
from bs4 import BeautifulSoup
import requests

bucatarii = {
    "Bucataria_Romaneasca": "https://www.bucataria.lidl.ro/bucataria-romaneasca?filters%5Bregion%5D=19794&page=",
    "Bucataria_Italiana": "https://www.bucataria.lidl.ro/bucataria-italiana?filters%5Bregion%5D=1658&page=",
    "Bucataria_Mexicana": "https://www.bucataria.lidl.ro/bucataria-mexicana?filters%5Bregion%5D=1659&page=",
    "Bucataria_Americana": "https://www.bucataria.lidl.ro/bucataria-americana?filters%5Bregion%5D=1661&page="
}


def start():
    for bucatarie in bucatarii:
        file = bucatarie + ".txt"
        url = bucatarii[bucatarie]

        page_count = BeautifulSoup(requests.get(url + '1').text, "html.parser")
        page_count = page_count.find("div", {"class", "mPagination-mobilePages"}).text.split(' ')[1]
        pages = page_scrapper(url, int(page_count))
        for page in pages:
            append_to_file(file, create_recipe_from_page(page))


start()



