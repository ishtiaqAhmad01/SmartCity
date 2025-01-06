# import pymysql

# # Connect to the database
# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="5533",
#     database="project"
# )

# def check_email(email):
#     try:
#         cursor = connection.cursor()

#         query = "SELECT * FROM users WHERE email = %s"
#         cursor.execute(query, (email,))
#         result = cursor.fetchone()

#         if result:
#             return True
#         else:
#             return False

#     finally:
#         connection.close()

# def check_phone(phone):
#     try:
#         cursor = connection.cursor()

#         query = "SELECT * FROM users WHERE phone = %s"
#         cursor.execute(query, (phone,))
#         result = cursor.fetchone()

#         if result:
#             return True
#         else:
#             return False

#     finally:
#         connection.close()

# def check_cnic(cnic):
#     try:
#         cursor = connection.cursor()

#         query = "SELECT * FROM users WHERE cnic = %s"
#         cursor.execute(query, (cnic,))
#         result = cursor.fetchone()

#         if result:
#             return True
#         else:
#             return False

#     finally:
#         connection.close()

# def insert_signup_info(first_name, last_name, email, phone, cnic, password, user_type):
#     pass
