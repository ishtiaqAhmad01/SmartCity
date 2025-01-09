import pymysql
from functions import hash_password

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='5533',
    db='ucsp',
)

def check_user_cnic_password(cnic, password):
    with connection.cursor() as cursor:
        query = "SELECT cnic, password FROM USERS WHERE cnic = %s"
        cursor.execute(query, (cnic,))
        result = cursor.fetchone()
        if result and result[0] == hash_password(password):
            return True
        else:
            return False

def check_email(email):
    try:
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    finally:
        connection.close()

def check_phone(phone):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE phone = %s"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    finally:
        connection.close()

def check_cnic(cnic):
    try:
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE cnic = %s"
        cursor.execute(query, (cnic,))
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    finally:
        connection.close()

def delete_complaint_from_db():
    pass

def add_deleded_complaint():
    pass