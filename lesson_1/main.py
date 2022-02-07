from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

h1_tags = soup.find_all("h1")

for h1 in h1_tags:
    print(h1.text)

# username = soup.find("div", class_="user__name").find("span")

# username = soup.find("div", {"class": "user__name"}).find("span").text
#
# print(username)

# user_info = soup.find(class_="user__info").find_all("span")
# print(user_info)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# for link in social_links:
#     url = link.get("href")
#     print(url)

# post_div = soup.find("div", class_="post__text").find_parents("div", "user__post")
# print(post_div)

# next_el = soup.find("div", class_="post__title").find_next().text
# print(next_el)

# next_sib = soup.find("div", class_="post__title").find_next_sibling()
# print(next_sib)
