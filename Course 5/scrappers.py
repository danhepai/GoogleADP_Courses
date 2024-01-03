from bs4 import BeautifulSoup
import requests


def ingredients_scrapper(url):
    """
    Scrapper to get the ingredients for a recipe from a particular recipe page
    """
    # These first three lines are getting the data for the ingredients from the div
    # contained by the particular site given by the 'url' parameter.
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    ingredients_box = soup.find("div", {"class": "oIngredientBox-listContainer"})
    ingredients_pair = ingredients_box.find_all("tr", {"class": "oIngredientBox-ingredient js_oIngredientBox-ingredient"})

    # The loop is the actual scrape of the particular page.
    ingredients = []
    for el in ingredients_pair:
        # This part of the code gets the name of the ingredient
        ingredient_name = el.find("td", {"class": "oIngredientBox-ingNameCol"}).text.strip()
        ingredient_name = ingredient_name.split('\n')[0]

        # This part of the code gets the quantity (number) and the type of quantity (piece, grams, kg, ...)
        quantity = el.find("td", {"class": "oIngredientBox-ingQuantityCol"}).text.strip().split(' ')
        quantity = [el for el in quantity if el != '']

        # This part of the code pretiffies the quantity data, so it can be easily accesed.
        if len(quantity) > 0:
            if len(quantity) > 2 and quantity[1] == '-':
                quantity_decimal = quantity[0] + quantity[1] + quantity[2]
            else:
                quantity_decimal = quantity[0]
        else:
            quantity_decimal = 'no_quantity'
        if len(quantity) > 1:
            for i in quantity:
                if i.endswith('\n'):
                    quantity_attribute = i.rstrip('\n')
                    break
        else:
            quantity_attribute = 'no_attribute'

        # Appends the recipe ingredients to a list
        ingredients.append([ingredient_name, quantity_decimal, quantity_attribute])

    # Returns a list of recipe's ingredients
    return ingredients


def title_scrapper(url):
    """
    Scrapper to get the name of a recipe from a particular recipe page
    """
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    recipe_title = soup.find_all('h1')[0].string
    return recipe_title


def page_scrapper(url, page_counter):
    """
    Scrapper to get all the pages with recipes from a site
    :return list with url-s
    """
    all_recipe_urls = []
    # page_count = BeautifulSoup(requests.get(url + '1').text, "html.parser")
    # page_count = page_count.find("span", {"class", "button-label"})
    # print(page_count)

    for page_number in range(1, page_counter + 1):
        page_url = url + str(page_number)

        soup = BeautifulSoup(requests.get(page_url).text, "html.parser")
        all_recipes = soup.find("div", {"class": "oRecipeSearchContainer-recipeFeed js_oRecipeSearchContainer-recipeFeed"})
        recipes_url = all_recipes.find_all("a")
        recipes_url = [el["href"] for el in recipes_url if el["href"] != "/retete-favorite"]
        for el in recipes_url:
            el = "https://www.bucataria.lidl.ro" + el
            all_recipe_urls.append(el)

    return all_recipe_urls
