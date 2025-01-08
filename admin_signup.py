from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from database import *
from functions import *

class Admin_SignUpPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart City Management - Admin Sign Up")
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
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Title Label
        title_label = QLabel("Admin Sign Up")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        main_layout.addWidget(title_label)

        # Create form layout for input fields
        form_layout = QVBoxLayout()

        # Name field
        name_label = QLabel("Name:")
        name_label.setStyleSheet("color: white; font-size: 14px;")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        self.name_input.setStyleSheet(self.input_style())

        # Email field
        email_label = QLabel("Email:")
        email_label.setStyleSheet("color: white; font-size: 14px;")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setStyleSheet(self.input_style())

        # Password field
        password_label = QLabel("Password:")
        password_label.setStyleSheet("color: white; font-size: 14px;")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setStyleSheet(self.input_style())

        # Phone field
        phone_label = QLabel("Phone:")
        phone_label.setStyleSheet("color: white; font-size: 14px;")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter your phone number")
        self.phone_input.setStyleSheet(self.input_style())

        # Address field
        address_label = QLabel("Address:")
        address_label.setStyleSheet("color: white; font-size: 14px;")
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter your address")
        self.address_input.setStyleSheet(self.input_style())

        # Button to submit the form
        submit_button = QPushButton("Sign Up")
        submit_button.setStyleSheet(self.button_style())
        submit_button.clicked.connect(self.sign_up)

        # Add form fields to the layout
        form_layout.addWidget(name_label)
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(phone_label)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(address_label)
        form_layout.addWidget(self.address_input)
        form_layout.addWidget(submit_button)

        # Add form layout to main layout
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
            margin-top: 30px;
            transition: background-color 0.3s ease;
        """
    
    def sign_up(self):
        pass
    