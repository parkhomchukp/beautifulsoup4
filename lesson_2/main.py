import requests
import json
import csv
from bs4 import BeautifulSoup

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;"
              "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
#
# req = requests.get(url, headers)
#
# src = req.text
#
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

# with open("index.html", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
#
# all_products_hrefs = soup.find_all("a", class_="mzr-tc-group-item-href")
#
# all_categories = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#     all_categories[item_text] = item_href
#
# with open("all_categories.json", "w") as file:
#     json.dump(all_categories, file, indent=4, ensure_ascii=False)

with open("all_categories.json") as file:
    all_categories = json.load(file)

iteration_counter = int(len(all_categories)) - 1

count = 0

print(f"Total iterations: {iteration_counter}")

for category_name, category_href in all_categories.items():
    rep = [" ", ",", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")

    req = requests.get(url=category_href, headers=headers)

    src = req.text

    with open(f"data/{count}_{category_name}.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # check page for data
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    # extracting titles from table
    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbs = table_head[4].text

    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbs
            )
        )

    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    product_info = []
    for product_data in products_data:
        product_tds = product_data.find_all("td")

        title = product_tds[0].find("a").text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbs = product_tds[4].text

        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbs": carbs
            }
        )

        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbs
                )
            )

        with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
            json.dump(all_categories, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"# Iteration {count}. {category_name} has been written. "
          f"{int(iteration_counter) - int(count)} iterations left")
