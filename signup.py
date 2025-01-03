from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from database import *
from checks import validate_email
import sys

class SignUpPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart City Management - Sign Up")
        self.setGeometry(300, 100, 1400, 900)
        self.setFixedSize(1400, 900)
        self.setStyleSheet("background-color: #2C3E50;")  # Background color

        # Apply custom theme and font
        self.setTheme()
        
        # Create UI elements
        self.create_widgets()

    def setTheme(self):
        # Set palette for modern dark theme
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#2C3E50"))
        palette.setColor(QPalette.Button, QColor("#3498DB"))
        palette.setColor(QPalette.Highlight, QColor("#1ABC9C"))
        palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
        self.setPalette(palette)
        
        # Set font for the whole window
        font = QFont("Arial", 12)
        self.setFont(font)

    def create_widgets(self):
        main_layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Register as New Member")
        title_label.setStyleSheet("font-size: 45px; font-weight: bold; color: white;font-family: arial")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Create form layout for input fields
        form_layout = QGridLayout()

        # Add input fields (similar to your original code)

        
        # first row (2 fields)
        self.first_name_input = QLineEdit()
        self.first_name_input.setPlaceholderText("Enter First Name")
        self.first_name_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("First Name:"), 0, 0)
        form_layout.addWidget(self.first_name_input, 0, 1)

        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Enter Last Name")
        self.last_name_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Last Name:"), 0, 2)
        form_layout.addWidget(self.last_name_input, 0, 3)

        # Second row (2 fields)
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter Phone")
        self.phone_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Phone Number:"), 1, 0)
        form_layout.addWidget(self.phone_input, 1, 1)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter Email")
        self.email_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Email:"), 1, 2)
        form_layout.addWidget(self.email_input, 1, 3)

        # Third row (2 fields)
        self.cnic_input = QLineEdit()
        self.cnic_input.setPlaceholderText("Enter CNIC")
        self.cnic_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("CNIC:"), 2, 0)
        form_layout.addWidget(self.cnic_input, 2, 1)

        self.nationality_input = QLineEdit()
        self.nationality_input.setPlaceholderText("Enter Nationality")
        self.nationality_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Nationality:"), 2, 2)
        form_layout.addWidget(self.nationality_input, 2, 3)

        # Fourth row (2 fields)
        self.dob_input = QLineEdit()
        self.dob_input.setPlaceholderText("Enter Date of Birth (dd/mm/yyyy)")
        self.dob_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Date of Birth:"), 3, 0)
        form_layout.addWidget(self.dob_input, 3, 1)

        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Male", "Female", "Other"])
        self.gender_combo.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Gender:"), 3, 2)
        form_layout.addWidget(self.gender_combo, 3, 3)

        # Fifth row (2 fields)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Password:"), 4, 0)
        form_layout.addWidget(self.password_input, 4, 1)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm Password")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Confirm Password:"), 4, 2)
        form_layout.addWidget(self.confirm_password_input, 4, 3)

        # Picture selector (in the 3rd column, span 2 rows)
        self.create_picture_selector(form_layout)

        # Last row (Address field)
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter Address")
        self.address_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Address:"), 5, 0)
        form_layout.addWidget(self.address_input, 5, 1, 1, 3)  # Span across columns

        # For brevity, the fields are not repeated here

        # Sign Up Button
        self.sign_up_button = QPushButton("Sign Up")
        self.sign_up_button.setStyleSheet(self.button_style())
        self.sign_up_button.clicked.connect(self.submit_signup)

        form_layout.addWidget(self.sign_up_button, 6, 2, 1, 1)

        # Add login button
        self.sign_in_button = QPushButton("Already have an account? Log In")
        self.sign_in_button.setStyleSheet(self.button_style())
        self.sign_in_button.clicked.connect(self.go_to_login)

        form_layout.addWidget(self.sign_in_button, 7, 2, 2, 1)

        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)

    def input_style(self):
        return """
            background-color: #34495E;
            color: white;
            border-radius: 10px;
            font-size: 30px;
            margin-bottom: 20px;
        """

    def button_style(self):
        return """
            background-color: #3498DB;
            color: white;
            border-radius: 10px;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        """

    def submit_signup(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        cnic = self.cnic_input.text()
        nationality = self.nationality_input.text()
        dob = self.dob_input.text()
        gender = self.gender_combo.currentText()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        address = self.address_input.text()


        if not first_name or not last_name or not phone or not email or not cnic:
            QMessageBox.critical(self, "Error", "Please fill all the required fields.")
            return

        if not validate_email(email):
            QMessageBox.critical(self, "Error", "Please enter a valid email address.")
            return
        
        if check_email(email):
            QMessageBox.critical(self, "Error", "Email already exists. Please use a different email.")
            return
        
        if password != confirm_password:
            QMessageBox.critical(self, "Error", "Passwords do not match. Please re-enter.")
            return
        
        if phone and len(phone)!=11 and not phone.isdigit():
            QMessageBox.critical(self, "Error", "Please enter a valid phone number.")
            return
        
        if cnic and len(cnic)!=13 and not cnic.isdigit():
            QMessageBox.critical(self, "Error", "Please enter a valid CNIC number.")
            return
        
        if check_cnic(cnic):
            QMessageBox.critical(self, "Error", "CNIC already exists. Please use a different CNIC.")
            return

        
        # Insert the data into the database
        #insert(first_name, last_name, phone, email, cnic)


        
        # Retrieve the picture path if available
        picture_path = self.picture_label.pixmap().cacheKey() if self.picture_label.pixmap() else None
        
        pass

    def create_picture_selector(self, layout):
        # Picture Selector Layout
        picture_layout = QVBoxLayout()

        # QLabel to display the selected picture
        self.picture_label = QLabel("No Image Selected")
        self.picture_label.setStyleSheet("color: white; font-size: 16px;")
        self.picture_label.setAlignment(Qt.AlignCenter)
        self.picture_label.setFixedSize(200, 200)
        self.picture_label.setStyleSheet("border: 2px dashed #FFFFFF;")

        # QPushButton to open the file dialog
        select_button = QPushButton("Select Picture")
        select_button.setStyleSheet(self.button_style())
        select_button.clicked.connect(self.select_picture)

        picture_layout.addWidget(self.picture_label, alignment=Qt.AlignCenter)
        picture_layout.addWidget(select_button, alignment=Qt.AlignCenter)

        # Add the picture layout to the 3rd column (cell 0, 4)
        layout.addLayout(picture_layout, 0, 4, 5, 1)  # Span across 5 rows in 3rd column

    def select_picture(self):
        # Open file dialog to select an image
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Picture", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.picture_label.setPixmap(pixmap.scaled(self.picture_label.size(), Qt.KeepAspectRatio))
            self.picture_label.setText("")  # Clear the text once an image is selected
        
    def go_to_login(self):
        self.close()
        from login import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()

