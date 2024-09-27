import xml.etree.ElementTree as ET


# Читаем xml из файла
tree = ET.parse("books.xml")

root = tree.getroot()

# Вычислить и распечатать суммарную цену книг
prices = root.iter("price")
sum_price = 0

for price in prices:
    sum_price += float(price.text)

print("Суммарная цена книг: ", round(sum_price, 2))
print()

# Распечатать название всех книг
print("Распечатать название всех книг:")
titles = root.iter("title")

for title in titles:
    print(title.text)

print()

# Изменить цену второй книги на 10,
root[1][3].text = "10"

# удалить третью книгу,
root.remove(root[2])

# добавить в конец некоторую свою книгу,
new_element = ET.Element("book")
new_element.set("id", "bk113")


new_book_author = ET.Element("author")
new_book_author.text = "Salinger, Jerome David"
new_element.append(new_book_author)

new_book_title = ET.Element("title")
new_book_title.text = "The catcher in the rye"
new_element.append(new_book_title)

new_book_genre = ET.Element("genre")
new_book_genre.text = "Romance"
new_element.append(new_book_genre)

new_book_price = ET.Element("price")
new_book_price.text = "13536"
new_element.append(new_book_price)

new_book_publish_date = ET.Element("publish_date")
new_book_publish_date.text = "2023-09-13"
new_element.append(new_book_publish_date)

new_book_description = ET.Element("description")
new_book_description.text = ("Holden Caulfield recalls the events of a long weekend,\n"
                             "Holden checks into the Edmont Hotel.")
new_element.append(new_book_description)

root.append(new_element)

# сохранить результат в файл
tree.write("out.xml")
