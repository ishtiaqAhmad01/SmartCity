# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QComboBox, QMessageBox
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QColor, QPalette, QFont
# from signup import SignUpPage

# class LoginPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Smart City Management - Login")
#         self.setGeometry(300, 100, 1400, 900)  # Adjusted window size for a laptop-like experience
#         self.setFixedSize(1400, 900)  # Fixed window size
#         self.setStyleSheet("background-color: #2C3E50;")  # Set background color

#         # Apply custom theme and font
#         self.setTheme()
        
#         # Create UI elements
#         self.create_widgets()

#     def setTheme(self):
#         # Set palette for modern dark theme
#         palette = QPalette()
#         palette.setColor(QPalette.Window, QColor("#2C3E50"))
#         palette.setColor(QPalette.Button, QColor("#3498DB"))
#         palette.setColor(QPalette.Highlight, QColor("#1ABC9C"))
#         palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
#         self.setPalette(palette)

#         # Set font for the whole window
#         font = QFont("Arial", 12)
#         self.setFont(font)
        
#     def create_widgets(self):
#         # Main layout
#         main_layout = QVBoxLayout()
#         main_layout.setAlignment(Qt.AlignCenter)

#         # Title Label
#         title_label = QLabel("Welcome to the Smart City Management System")
#         title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
#         main_layout.addWidget(title_label)

#         # Create form layout for input fields
#         form_layout = QVBoxLayout()
        
#         # Username field
#         username_label = QLabel("Username:")
#         username_label.setStyleSheet("color: white; font-size: 14px;")
#         self.username_input = QLineEdit()
#         self.username_input.setPlaceholderText("Enter your username")
#         self.username_input.setStyleSheet(self.input_style())
        
#         # Password field
#         password_label = QLabel("Password:")
#         password_label.setStyleSheet("color: white; font-size: 14px;")
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Enter your password")
#         self.password_input.setEchoMode(QLineEdit.Password)
#         self.password_input.setStyleSheet(self.input_style())
        
#         # User type selection (ComboBox)
#         user_type_label = QLabel("Select User Type:")
#         user_type_label.setStyleSheet("color: white; font-size: 14px;")
#         self.user_type_combo = QComboBox()
#         self.user_type_combo.addItems(["Citizen", "Admin", "Service Provider"])
#         self.user_type_combo.setStyleSheet(self.input_style())

#         # Login Button
#         self.login_button = QPushButton("Login")
#         self.login_button.setStyleSheet(self.button_style())
#         self.login_button.clicked.connect(self.check_credentials)

#         # Sign Up Button
#         self.signup_button = QPushButton("Sign Up")
#         self.signup_button.setStyleSheet(self.button_style())
#         self.signup_button.clicked.connect(self.go_to_signup)

#         # Add widgets to form layout
#         form_layout.addWidget(username_label)
#         form_layout.addWidget(self.username_input)
#         form_layout.addWidget(password_label)
#         form_layout.addWidget(self.password_input)
#         form_layout.addWidget(user_type_label)
#         form_layout.addWidget(self.user_type_combo)
#         form_layout.addWidget(self.login_button)
#         form_layout.addWidget(self.signup_button)

#         main_layout.addLayout(form_layout)
        
#         # Set the main layout for the window
#         self.setLayout(main_layout)

#     def input_style(self):
#         return """
#             background-color: #34495E;
#             color: white;
#             border-radius: 10px;
#             padding: 10px;
#             font-size: 14px;
#             margin-bottom: 15px;
#         """

#     def button_style(self):
#         return """
#             background-color: #3498DB;
#             color: white;
#             border-radius: 10px;
#             padding: 15px;
#             font-size: 16px;
#             font-weight: bold;
#             transition: background-color 0.3s ease;
#         """
    

#     # To be inplemented latter
#     def check_credentials(self):
#         username = self.username_input.text()
#         password = self.password_input.text()
#         user_type = self.user_type_combo.currentText()

#         # Check for empty fields
#         if not username or not password:
#             self.show_error_message("Please enter both username and password.")
#             return

#         # For simplicity, use hardcoded username/password checks
#         if user_type == "Citizen":
#             if username == "citizen1" and password == "password123":
#                 self.show_success_message("Citizen login successful!")
#             else:
#                 self.show_error_message("Invalid credentials for Citizen.")
        
#         elif user_type == "Admin":
#             if username == "admin1" and password == "adminpass":
#                 self.show_success_message("Admin login successful!")
#             else:
#                 self.show_error_message("Invalid credentials for Admin.")
        
#         elif user_type == "Service Provider":
#             if username == "provider1" and password == "providerpass":
#                 self.show_success_message("Service Provider login successful!")
#             else:
#                 self.show_error_message("Invalid credentials for Service Provider.")
        
#     def show_error_message(self, message):
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Critical)
#         msg.setText(message)
#         msg.setWindowTitle("Login Error")
#         msg.setStyleSheet("background-color: #E74C3C; color: white; font-size: 14px;")
#         msg.exec_()

#     def show_success_message(self, message):
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Information)
#         msg.setText(message)
#         msg.setWindowTitle("Login Successful")
#         msg.setStyleSheet("background-color: #2ECC71; color: white; font-size: 14px;")
#         msg.exec_()

#     def go_to_signup(self):
#         self.signup_page = SignUpPage()
#         self.signup_page.show()
#         self.close()


# if __name__ == '__main__':
#     #def create_app():
#     app = QApplication(sys.argv)
#     window = LoginPage()
#     window.show()
#     sys.exit(app.exec_())

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import *
# #from login import create_app
# import sys

# class SignUpPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Smart City Management - Sign Up")
#         self.setGeometry(300, 100, 1400, 900)
#         self.setFixedSize(1400, 900)
#         self.setStyleSheet("background-color: #2C3E50;")  # Background color

#         # Apply custom theme and font
#         self.setTheme()
        
#         # Create UI elements
#         self.create_widgets()

#     def setTheme(self):
#         # Set palette for modern dark theme
#         palette = QPalette()
#         palette.setColor(QPalette.Window, QColor("#2C3E50"))
#         palette.setColor(QPalette.Button, QColor("#3498DB"))
#         palette.setColor(QPalette.Highlight, QColor("#1ABC9C"))
#         palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
#         self.setPalette(palette)
        
#         # Set font for the whole window
#         font = QFont("Arial", 12)
#         self.setFont(font)
        
#     def create_widgets(self):
#         # Main layout
#         main_layout = QVBoxLayout()
#         # Title Label
#         title_label = QLabel("Register as New Member")
#         title_label.setStyleSheet("font-size: 45px; font-weight: bold; color: white;font-family: arial")
#         title_label.setAlignment(Qt.AlignCenter)
#         main_layout.addWidget(title_label)

#         # Remove or adjust the spacer item
#         main_layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum))

#         # Grid layout for input fields
#         grid_layout = QGridLayout()

#         # first row (2 fields)
#         self.first_name_input = QLineEdit()
#         self.first_name_input.setPlaceholderText("Enter First Name")
#         self.first_name_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("First Name:"), 0, 0)
#         grid_layout.addWidget(self.first_name_input, 0, 1)

#         self.last_name_input = QLineEdit()
#         self.last_name_input.setPlaceholderText("Enter Last Name")
#         self.last_name_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("Last Name:"), 0, 2)
#         grid_layout.addWidget(self.last_name_input, 0, 3)

#         # Second row (2 fields)
#         self.phone_input = QLineEdit()
#         self.phone_input.setPlaceholderText("Enter Phone")
#         self.phone_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("Phone Number:"), 1, 0)
#         grid_layout.addWidget(self.phone_input, 1, 1)

#         self.email_input = QLineEdit()
#         self.email_input.setPlaceholderText("Enter Email")
#         self.email_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("Email:"), 1, 2)
#         grid_layout.addWidget(self.email_input, 1, 3)

#         # Third row (2 fields)
#         self.cnic_input = QLineEdit()
#         self.cnic_input.setPlaceholderText("Enter CNIC")
#         self.cnic_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("CNIC:"), 2, 0)
#         grid_layout.addWidget(self.cnic_input, 2, 1)

#         self.nationality_input = QLineEdit()
#         self.nationality_input.setPlaceholderText("Enter Nationality")
#         self.nationality_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("Nationality:"), 2, 2)
#         grid_layout.addWidget(self.nationality_input, 2, 3)

#         # Fourth row (2 fields)
#         self.dob_input = QLineEdit()
#         self.dob_input.setPlaceholderText("Enter Date of Birth (dd/mm/yyyy)")
#         self.dob_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("Date of Birth:"), 3, 0)
#         grid_layout.addWidget(self.dob_input, 3, 1)

#         self.gender_combo = QComboBox()
#         self.gender_combo.addItems(["Male", "Female", "Other"])
#         self.gender_combo.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("Gender:"), 3, 2)
#         grid_layout.addWidget(self.gender_combo, 3, 3)

#         # Fifth row (2 fields)
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Enter Password")
#         self.password_input.setEchoMode(QLineEdit.Password)
#         self.password_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("Password:"), 4, 0)
#         grid_layout.addWidget(self.password_input, 4, 1)

#         self.confirm_password_input = QLineEdit()
#         self.confirm_password_input.setPlaceholderText("Confirm Password")
#         self.confirm_password_input.setEchoMode(QLineEdit.Password)
#         self.confirm_password_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("Confirm Password:"), 4, 2)
#         grid_layout.addWidget(self.confirm_password_input, 4, 3)

#         # Picture selector (in the 3rd column, span 2 rows)
#         self.create_picture_selector(grid_layout)

#         # Last row (Address field)
#         self.address_input = QLineEdit()
#         self.address_input.setPlaceholderText("Enter Address")
#         self.address_input.setStyleSheet(self.input_style())
#         grid_layout.addWidget(QLabel("Address:"), 5, 0)
#         grid_layout.addWidget(self.address_input, 5, 1, 1, 3)  # Span across columns

#         # Sign Up Button
#         self.sign_up_button = QPushButton("Sign Up")
#         self.sign_up_button.setStyleSheet(self.button_style())
#         self.sign_up_button.clicked.connect(self.submit_signup)
#         grid_layout.addWidget(self.sign_up_button, 6, 2, 1, 1)  # Span across columns

#         # Sign In Button
#         self.sign_in_button = QPushButton("Already have an account? Log In")
#         self.sign_in_button.setStyleSheet(self.button_style())
#         self.sign_in_button.clicked.connect(self.go_to_login)
#         grid_layout.addWidget(self.sign_in_button, 7, 2, 2, 1)  # Span across columns

#         # Set the grid layout for the window
#         main_layout.addLayout(grid_layout)
#         self.setLayout(main_layout)

#     def input_style(self):
#         return """
#             background-color: #34495E;
#             color: white;
#             border-radius: 10px;
#             font-size: 30px;
#             margin-bottom: 20px;
#         """

#     def button_style(self):
#         return """
#             background-color: #3498DB;
#             color: white;
#             border-radius: 10px;
#             padding: 15px;
#             font-size: 16px;
#             font-weight: bold;
#             transition: background-color 0.3s ease;
#         """

#     def submit_signup(self):
#         # Collect all input values
#         phone = self.phone_input.text()
#         email = self.email_input.text()
#         first_name = self.first_name_input.text()
#         last_name = self.last_name_input.text()
#         cnic = self.cnic_input.text()
#         nationality = self.nationality_input.text()
#         dob = self.dob_input.text()
#         gender = self.gender_combo.currentText()
#         password = self.password_input.text()
#         confirm_password = self.confirm_password_input.text()
#         address = self.address_input.text()

#         # Basic validation
#         if not all([phone, email, first_name, last_name, cnic, nationality, dob, password, confirm_password, address]):
#             self.show_error_message("Please fill in all required fields.")
#             return

#         if password != confirm_password:
#             self.show_error_message("Passwords do not match.")
#             return

#         # Handle sign up (For now, simply show a success message)
#         self.show_success_message("Sign Up successful! You can now log in.")

#     def show_error_message(self, message):
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Critical)
#         msg.setText(message)
#         msg.setWindowTitle("Sign Up Error")
#         msg.setStyleSheet("background-color: #E74C3C; color: white; font-size: 14px;")
#         msg.exec_()

#     def show_success_message(self, message):
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Information)
#         msg.setText(message)
#         msg.setWindowTitle("Sign Up Successful")
#         msg.setStyleSheet("background-color: #2ECC71; color: white; font-size: 14px;")
#         msg.exec_()

#     def create_picture_selector(self, layout):
#         # Picture Selector Layout
#         picture_layout = QVBoxLayout()

#         # QLabel to display the selected picture
#         self.picture_label = QLabel("No Image Selected")
#         self.picture_label.setStyleSheet("color: white; font-size: 16px;")
#         self.picture_label.setAlignment(Qt.AlignCenter)
#         self.picture_label.setFixedSize(200, 200)
#         self.picture_label.setStyleSheet("border: 2px dashed #FFFFFF;")

#         # QPushButton to open the file dialog
#         select_button = QPushButton("Select Picture")
#         select_button.setStyleSheet(self.button_style())
#         select_button.clicked.connect(self.select_picture)

#         picture_layout.addWidget(self.picture_label, alignment=Qt.AlignCenter)
#         picture_layout.addWidget(select_button, alignment=Qt.AlignCenter)

#         # Add the picture layout to the 3rd column (cell 0, 4)
#         layout.addLayout(picture_layout, 0, 4, 5, 1)  # Span across 5 rows in 3rd column

#     def select_picture(self):
#         # Open file dialog to select an image
#         file_path, _ = QFileDialog.getOpenFileName(self, "Select Picture", "", "Images (*.png *.jpg *.jpeg *.bmp)")
#         if file_path:
#             pixmap = QPixmap(file_path)
#             self.picture_label.setPixmap(pixmap.scaled(self.picture_label.size(), Qt.KeepAspectRatio))
#             self.picture_label.setText("")  # Clear the text once an image is selected

#     def go_to_login(self):
#         # Close the current signup page and open the login page
#         self.close()
#         create_app()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = SignUpPage()
#     window.show()
#     sys.exit(app.exec_())

