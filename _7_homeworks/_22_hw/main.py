import psycopg2


def connect_to_db():
    try:
        connection = psycopg2.connect(
            host='localhost',
            port="5432",
            database='playground',
            user='postgres',
            password='roma0712'
        )
        return connection
    except psycopg2.Error as err:
        print('An Error occurred: ', err)
        return None


def create_cursor(connection):
    try:
        cursor = connection.cursor()
        return cursor
    except psycopg2.Error as e:
        print("Error creating a cursor:", e)
        return None


def write_data(cursor):
    try:
        cursor.execute(
            'INSERT INTO public.products (product, price, available) VALUES (%s, %s, %s)',
            ("Makaronis", "234", "true")
        )

        cursor.execute(
            'INSERT INTO public.products (product, price, available) VALUES (%s, %s, %s)',
            ("Ducks", "765", "false")
        )

        cursor.execute(
            'INSERT INTO public.products (product, price, available) VALUES (%s, %s, %s)',
            ("Anime Girls", "999", "true")
        )

        connection.commit()
        print("Data inserted into the database successfully.")
    except psycopg2.Error as err:
        connection.rollback()
        print("Error inserting data:", err)


def read_data(cursor):
    try:
        cursor.execute("SELECT * FROM public.products")
        rows = cursor.fetchall()
        print("Data retrieved from the database:")
        for row in rows:
            print(row)
    except psycopg2.Error as err:
        print("Error reading data:", err)


if __name__ == "__main__":
    connection = connect_to_db()
    if connection is None:
        exit()

    cursor = create_cursor(connection)
    if cursor is None:
        connection.close()
        exit()

    write_data(cursor)

    read_data(cursor)

    cursor.close()
    connection.close()
