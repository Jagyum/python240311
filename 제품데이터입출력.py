import sqlite3
import random
import string

class ProductDatabase:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            price REAL
                            )''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cur.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def update_product(self, product_id, name, price):
        self.cur.execute("UPDATE products SET name=?, price=? WHERE id=?", (name, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cur.execute("DELETE FROM products WHERE id=?", (product_id,))
        self.conn.commit()

    def select_all_products(self):
        self.cur.execute("SELECT * FROM products")
        rows = self.cur.fetchall()
        return rows

# 샘플 데이터 준비
def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

sample_data = [
    (generate_random_name(), random.uniform(50, 2000)) for _ in range(100)
]

# 데이터베이스 객체 생성
product_db = ProductDatabase()

# 샘플 데이터베이스에 추가
for name, price in sample_data:
    product_db.insert_product(name, price)

# 모든 제품 출력
print("All Products:")
print(product_db.select_all_products())

# 제품 업데이트 (예시로 첫 번째 제품을 업데이트)
product_db.update_product(1, "New Laptop", 1700)

# 업데이트된 제품 출력
print("\nUpdated Product:")
print(product_db.select_all_products())

# 제품 삭제 (예시로 마지막 제품 삭제)
product_db.delete_product(100)

# 삭제된 제품을 제외한 모든 제품 출력
print("\nProducts after deletion:")
print(product_db.select_all_products())

# 데이터베이스 연결 종료
product_db.conn.close()
