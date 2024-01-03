from scrappers import title_scrapper, ingredients_scrapper


def append_to_file(file, recipe):
    with open(file, 'a+') as f:
        recipe_string = ""
        recipe_string += f"{recipe["title"].upper()}" + '\n' + '\n'
        for ingredient in recipe['ingredients']:
            recipe_string += f"{ingredient[0]} "
            if ingredient[1] != 'no_quantity':
                recipe_string += f"-> {ingredient[1]} "
            if ingredient[2] != 'no_attribute':
                recipe_string += f"{ingredient[2]}"
            recipe_string += '\n'
        f.write(recipe_string + '\n')


def create_recipe_from_page(url):
    recipe = {
        "title": title_scrapper(url),
        "ingredients": ingredients_scrapper(url)
    }

    return recipe
