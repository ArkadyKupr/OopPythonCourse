from mysql.connector import connect, Error

drop_db_query = "DROP DATABASE IF EXISTS shop;"
create_db_query = "CREATE DATABASE shop;"

create_products_category_query = """CREATE TABLE products_category
(
id INT AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
PRIMARY KEY (id)
);"""

insert_products_category_query = """INSERT INTO products_category(name)
VALUES ('Варенье'), ('Хлебобулочные изделия'), ('Фрукты');"""

create_product_query = """CREATE TABLE product
(
id INT AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
price DECIMAL(65, 2) NOT NULL,
category_id INT NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (category_id) REFERENCES products_category(id)
);"""

insert_product_query = """INSERT INTO product(name, price, category_id)
VALUES('Малиновое варенье', 100, 1), ('Клубничное варенье', 123, 1), 
('Кексы', 70, 2), ('Бородинский хлеб', 40, 2), ('Яблоки', 100, 3);"""

update_product_query = """UPDATE
product
SET
price = price * 2, name = 'Груши'
WHERE
id = 5;"""

delete_product_query = """DELETE
FROM
product
WHERE
price > 100;"""

inner_join_query = """SELECT 
product.id, product.name, product.price, products_category.name 
FROM product INNER JOIN products_category
ON product.category_id = products_category.id;"""

try:
    with connect(host="localhost", user="root", password="jkoP57fg111QWEty") as connection:
        print(connection)
except Error as e:
    print(e)
else:
    with connection.cursor() as cursor:
        cursor.execute(drop_db_query)
        cursor.execute(create_db_query)
        cursor.execute("USE shop;")
        cursor.execute(create_products_category_query)
        cursor.execute(insert_products_category_query)
        # коммит транзакции
        connection.commit()
        cursor.execute(insert_product_query)
        # коммит транзакции
        connection.commit()
        cursor.execute(update_product_query)
        # коммит update
        connection.commit()
        cursor.execute(delete_product_query)
        # коммит delete
        connection.commit()
        cursor.execute("SELECT * FROM product;")
        # удаление товаров с ценою выше, чем указанное пользователем в консоли значение
        user_price = input("Введите цену, товары выше которой должны быть удалены: ")
        cursor.execute(f"DELETE FROM product WHERE price > {str(user_price)};")
        # коммит delete
        connection.commit()
        # Изменить название и цену некоторому товару. Пользователь должен ввести название некоторого товара,
        # который нужно изменить, и доложен ввести новое название товара и цену
        user_new_product_name = input("Введите новое название товара: ")
        user_new_price = input("Введите новую цену:")
        product_name_to_change = input("Введите название товара, котор нужно изменить: ")
        cursor.execute(f"UPDATE product SET price = {str(user_new_price)}, name = '{user_new_product_name}' "
                       f"WHERE name = '{product_name_to_change}';")
        # коммит update
        connection.commit()
        # Получить данные в таком виде: id товара, название товара, цена товара, название категории
        print(cursor.execute(inner_join_query))
