import psycopg2


def create_product_table():
    with psycopg2.connect(dbname="playground", host="localhost", user="postgres", password="roma0712",
                          port="5432") as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                product TEXT UNIQUE,
                price DECIMAL,
                available BOOLEAN
            )
        ''')
        connection.commit()


def insert_data_to_db(filename):
    with psycopg2.connect(dbname="playground", host="localhost", user="postgres", password="roma0712",
                          port="5432") as connection:
        with open(filename, 'r', encoding='utf-8') as file:
            cursor = connection.cursor()
            for line in file:
                values = line.strip().split(',')

                query = '''
                    INSERT INTO products (product, price, available)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (product)
                    DO UPDATE SET
                        product = EXCLUDED.product,
                        price = EXCLUDED.price,
                        available = EXCLUDED.available
                '''
                data = tuple(values)

                cursor.execute(query, data)
                connection.commit()


def export_data_to_file(filename):
    with psycopg2.connect(dbname="playground", host="localhost", user="postgres", password="roma0712",
                          port="5432") as connection:
        cursor = connection.cursor()

        query = '''
            SELECT product, price, available
            FROM products
        '''

        cursor.execute(query)
        records = cursor.fetchall()

        with open(filename, 'w', encoding='utf-8') as file:
            for record in records:
                line = ','.join(str(field) for field in record)
                file.write(line + '\n')


if __name__ == '__main__':
    create_product_table()
    insert_data_to_db('./temp/data.txt')
    export_data_to_file('./temp/data2.txt')
