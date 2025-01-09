import pymysql

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="user",
    password="5533",
    database="ucsp"
)

def show_tables():
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    cursor.close()
    return tables

def get_users():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return users


if __name__ == "__main__":
    print(show_tables())