import pymysql

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="5533",
    database="project"
)

def insert():
    try:
        cursor = connection.cursor()

        # Read the image file in binary mode
        image_path = "mueez.jpg"
        with open(image_path, "rb") as file:
            binary_data = file.read()

        # Insert the image into the table
        query = "INSERT INTO user_images (user_name, image_data) VALUES (%s, %s)"
        data = ("John Doe", binary_data)
        cursor.execute(query, data)

        # Commit the transaction
        connection.commit()
        print("Image inserted successfully!")

    finally:
        # Close the connection
        connection.close()



def retrive():
    try:
        cursor = connection.cursor()

        # Retrieve the image data
        query = "SELECT user_name, image_data FROM user_images WHERE id = %s"
        cursor.execute(query, (1,))  # Replace 1 with the ID of the desired record
        result = cursor.fetchone()
        user_name, image_data = result

        # show image
        print(user_name)
        print(image_data)

    finally:
        # Close the connection
        connection.close()


if __name__ == '__main__':
    retrive()