from pathlib import Path
import sqlite3


def init_db():
    global db, cursor
    db_path = Path(__file__).parent.parent / 'goods.db'
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

def create_categories_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT)''')
    db.commit()


def create_products_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    description TEXT,
    png TEXT,
    id_categories INTEGER,
    FOREIGN KEY (id_categories) REFERENCES categories(id))''')
    db.commit()


def fill_categories():
    cursor.execute('''INSERT INTO categories (name) VALUES 
    ('clothes'), 
    ('stickers'), 
    ('sketchbooks')''')
    db.commit()


def fill_products():
    cursor.execute('''INSERT INTO products (name, price, description, png, id_categories) VALUES
     ('Скетчбук Ханако-кун', 400, 'Хороший выбор для творческой личности!',
      'https://ae04.alicdn.com/kf/U00df8649e655407f9946988dc290338fF.jpg_640x640.jpg', 3),
      ('Тоторо Новогодний', 2000, 'Задроты тоже могут быть стильными!', 'https://storage.vsemayki.ru/images/0/3/3043/3043661/previews/people_4_womanshort_oversize_front_red_700.jpg',
      1),
      ('Аниме наклейки', 100, 'Подойдет для любой вещи!', 'https://ae04.alicdn.com/kf/H132d60b8ea364c47a2115258fe53d700q.jpg',
      2)''')
    db.commit()


def show_data_categories():
    cursor.execute('SELECT name FROM categories')
    return cursor.fetchall()[0]


if __name__ == '__main__':
    init_db()
    # create_categories_table()
    # create_products_table()
    # fill_categories()
    # # fill_products()
    # print(show_data_categories())












