from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

all_a_tag = soup.find_all(name="a")
print(all_a_tag)

for tag in all_a_tag:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)