import pymysql
from functions import hash_password, doc_as_binary

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='5533',
    db='ucsp',
)

def check_user_cnic_password(cnic, password): #Done
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        query = "SELECT password_hash FROM USERS WHERE CNIC = %s"
        cursor.execute(query, (cnic,))
        result = cursor.fetchone()
        print(result[0])
        if result and result[0] == hash_password(password).decode('utf-8'):
            print("success")
            return True
        else:
            return False
        
def check_admin_cnic_password(cnic, password): #Done
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        query = "SELECT password_hash FROM Admin WHERE CNIC = %s"
        cursor.execute(query, (cnic,))
        result = cursor.fetchone()

        if result and result[0] == hash_password(password).decode('utf-8'):
            return True
        else:
            return False

def check_user_email(email): #Done
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False

def check_user_phone(phone): #Done
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

def check_cnic(cnic):  #Done
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE cnic = %s"
    cursor.execute(query, (cnic,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False

def add_user_to_db(cnic, first_name, last_name, email, phone, pic, dob, gender, password, province, district, tehsil): 
    try:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO users (cnic, first_name, last_name, email, phone_number, pic, dob, gender, password_hash)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (cnic, first_name, last_name, email, phone, doc_as_binary(pic), dob, gender, hash_password(password)))

            query = """
                INSERT INTO address (cnic, province, district, city)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (cnic, province, district, tehsil))


            connection.commit()
            return True
    
    except Exception as e:
        print(f"Error occurred: {e}")
        connection.rollback()
        return False
        
def add_admin_to_db(CNIC, name, email, phone_number, password_hash, address):
    try:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO admin (CNIC, name, email, phone_number, password_hash, address)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (CNIC, name, email, phone_number, hash_password(password_hash), address))

            connection.commit()
            return True
    
    except Exception as e:
        print(f"Error occurred: {e}")
        connection.rollback()
        return False

def add_doc_to_database (cnic, document_name, document_ext, document_type, doc):
    try:
        with connection.cursor() as cursor:
            encytp = 0
            query = """
                INSERT INTO documents (cnic, document_name, document_ext, document_type, doc, encrypted)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (cnic, document_name, document_ext, document_type, doc_as_binary(doc), encytp))
            connection.commit()
            return True
    except Exception as e:
        print(f"Error occurred: {e}")
        connection.rollback()
        return False

def load_doc_from_database(cnic):
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT document_name, document_ext, document_type FROM documents where cnic = %s
            """
            cursor.execute(query, (cnic))
            return cursor.fetchall()
    except Exception as e:
        print(f"Error occurred: {e}")
        connection.rollback()
        return None

def get_file_from_database(cnic, file_name):
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT doc FROM documents where cnic = %s and document_name+document_ext = %s
            """
            cursor.execute(query, (cnic, file_name))
            return cursor.fetchone()
    except Exception as e:
        print(f"Error occurred: {e}")
        connection.rollback()
        return None    
    
def get_fileinfo_from_database(cnic, file_name):
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT document_id, upload_date, cnic, document_name, document_ext, document_type  FROM documents where cnic = %s and document_name+document_ext = %s
            """
            cursor.execute(query, (cnic, file_name))
            return cursor.fetchone()
    except Exception as e:
        print(f"Error occurred: {e}")
        connection.rollback()
        return None  

def insert_complain_to_db(cnic, main_category, sub_category, description, address):
        with connection.cursor() as cursor:
            try:
                query = """
                    insert into complains(cnic, main_category, sub_category, description, address)
                    values
                    (%s, %s, %s, %s, %s)
                """

                cursor.execute(query, (cnic, main_category, sub_category, description, address))
                connection.commit()
                return True
            except Exception as e:
                print(e)
                connection.rollback()
                return False

def load_complains_from_db(cnic):
    with connection.cursor() as cursor:
        try:
            query = """
                select complain_id, description, status from complains where cnic = %s
            """
            cursor.execute(query, (cnic,))
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return ()
        
def delete_complaint_from_db(complain_id):
    with connection.cursor() as cursor:
        try:
            query = """
                delete from complains where complain_id = %s
            """
            cursor.execute(query, (complain_id,))
            connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

def add_review_of_complain(complain_id, feedback, rating):
    with connection.cursor() as cursor:
        try:
            query = """
                insert into feedback(refer_id, refer_type, feedback_text, feedback_rating)
                values(%s, %s, %s, %s)
            """
            cursor.execute(query, (complain_id, "complain", feedback, rating))
            connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

def get_user_info(cnic):
    try:
        with connection.cursor() as cursor:
            query = """
                select u.first_name, u.last_name, a.province, a.district, a.city, u.email from users u
                inner join address a on u.cnic = a.cnic where u.cnic = %s
                """   
            
            cursor.execute(query, (cnic,))
            return cursor.fetchone()
        
    except Exception as e:
        print(e)
        return False

def add_user_bill(user_cnic, bill_type, issue_date, amount_before_due, amount_after_due, due_date, tax_percentage,tax_amount,late_fee):
    try:
        with connection.cursor() as cursor:
            query = """
                insert into utility_bills(user_cnic, bill_type, issue_date, amount_before_due, amount_after_due, due_date, tax_percentage,tax_amount,late_fee)
                values
                (%s, %s, %s,%s, %s, %s,%s, %s, %s)
            """
            cursor.execute(query, (user_cnic, bill_type, issue_date, amount_before_due, amount_after_due, due_date, tax_percentage,tax_amount,late_fee))

            connection.commit()
            return True
    except Exception as e:
        print(e)
        return False

def get_bill_info(cnic, bill_type):
    try:
        with connection.cursor() as cursor:
            query = """
                select u.first_name, u.last_name, u.email, a.province, a.district, a.city, u.phone_number, b.tax_percentage, b.tax_amount, b.amount_before_due
                from users  u
                join utility_bills b on u.cnic = b.user_cnic
                join address a on a.cnic = b.user_cnic
                where u.cnic = %s and b.bill_type = %s
                """
            cursor.execute(query, (cnic, bill_type))
            return cursor.fetchone()
    except Exception as e:
        return 1

def load_current_bills_data(cnic):
    try:
        with connection.cursor() as cursor:
            query = """
                select bill_type, due_date, amount_before_due from utility_bills where user_cnic = %s
            """
            cursor.execute(query, (cnic, ))
            return cursor.fetchall()
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    First_Name = 'ISHTIAQ'
    Last_Name = 'AHMAD'
    Phone = '03072928533'
    Email = "s2023065078@umt.edu.pk"
    cnic ='3660245605291'
    Nationality = 'Pakistani'
    Date_of_Birth = '2005/03/07'
    Gender = 'Male'
    Password = 'ahmad'
    Province = 'Punjab'
    District = 'Multan'
    Tehsil = 'Multan City'
    Picture = 'C:/Users/ISHTIAQ/Downloads/Ishtiaq (2).jpg'
    print(get_bill_info(cnic, "Electric"))
    




def add_deleded_complaint():
    pass