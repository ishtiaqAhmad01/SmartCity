from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from database import *
from functions import *
from database import add_user_to_db
import random
import time


class User_SignUpPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart City Management - User Sign Up")
        self.setGeometry(300, 100, 1400, 900)
        self.setFixedSize(1400, 900)
        self.setStyleSheet("background-color: #2C3E50;")  # Background color

        # Apply custom theme and font
        self.setTheme()

        
        self.generated_otp = None
        self.otp_timestamp = None

        # Create UI elements
        self.create_widgets()

    def setTheme(self):
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
        title_label.setStyleSheet("font-size: 45px; font-weight: bold; color: white; font-family: arial")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        form_layout = QGridLayout()

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

        
        self.dob_input = QDateEdit()
        self.dob_input.setDisplayFormat("yyyy/MM/dd") 
        self.dob_input.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Date of Birth:"), 3, 0)
        form_layout.addWidget(self.dob_input, 3, 1)

        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Male", "Female", "Other"])
        self.gender_combo.setStyleSheet(self.input_style())
        form_layout.addWidget(QLabel("Gender:"), 3, 2)
        form_layout.addWidget(self.gender_combo, 3, 3)

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

        self.create_picture_selector(form_layout)

        province_layout = QHBoxLayout()

        province_layout.addWidget(QLabel("Address:"))
        self.province_combo = QComboBox()
        self.province_combo.addItems(pakistan_provinces())
        self.province_combo.currentTextChanged.connect(self.update_districts)
        self.province_combo.setStyleSheet(self.input_style())
        province_layout.addWidget(self.province_combo)

        self.district_combo = QComboBox()
        self.district_combo.addItems(provinces_districts(self.province_combo.currentText()))
        self.district_combo.currentTextChanged.connect(self.update_tehsils)
        self.district_combo.setStyleSheet(self.input_style())
        province_layout.addWidget(self.district_combo)

        self.tehsil_combo = QComboBox()
        self.tehsil_combo.addItems(district_tehsils(self.district_combo.currentText()))
        self.tehsil_combo.setStyleSheet(self.input_style())
        province_layout.addWidget(self.tehsil_combo)

        province_layout.addWidget(QLabel(""))  # Empty label for spacing
        form_layout.addLayout(province_layout, 5, 0, 1, 6)

        self.sign_up_button = QPushButton("Sign Up")
        self.sign_up_button.setStyleSheet(self.button_style())
        self.sign_up_button.clicked.connect(self.submit_signup)

        form_layout.addWidget(self.sign_up_button, 6, 2, 1, 1)

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
            margin-top: 30px;
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
        province = self.province_combo.currentText()
        district = self.district_combo.currentText()
        tehsil = self.tehsil_combo.currentText()
        pic_path = self.selected_file_path
        binary_pic = doc_as_binary(pic_path)

        if not cnic or not first_name or not phone or not email or not cnic or not dob or not password:
            QMessageBox.critical(self, "Error", "Please fill all the required fields.")
            return
        
        if not binary_pic:
            QMessageBox.critical(self, "Error", "Please select a picture.")
            return
        
        if not validate_email(email):
            QMessageBox.critical(self, "Error", "Please enter a valid email address.")
            return
        
        if check_user_email(email):
            QMessageBox.critical(self, "Error", "Email already exists. Please use a different email.")
            return
        
        if password != confirm_password:
            QMessageBox.critical(self, "Error", "Passwords do not match. Please re-enter.")
            return
        
        if phone and len(phone) != 11 and not phone.isdigit():
            QMessageBox.critical(self, "Error", "Please enter a valid phone number.")
            return
        
        if cnic and len(cnic) != 13 and not cnic.isdigit():
            QMessageBox.critical(self, "Error", "Please enter a valid CNIC number.")
            return
        
        if check_cnic(cnic):
            QMessageBox.critical(self, "Error", "CNIC already exists. Please use a different CNIC.")
            return
        
        self.generate_and_send_otp() 
        self.show_otp_popup()  

    def generate_and_send_otp(self):
        self.generated_otp = random.randint(1000, 9999)
        self.otp_timestamp = time.time()  
        
        send_email(self.email_input.text(), self.generated_otp)
        print(f"OTP sent: {self.generated_otp}") 
    
    def show_otp_popup(self):
        otp_dialog = QDialog(self)
        otp_dialog.setWindowTitle("Enter OTP")
        otp_dialog.setFixedSize(400, 200)
        otp_dialog.setStyleSheet("background-color: #34495E; color: white;")
        
        # Layout for the dialog
        layout = QVBoxLayout(otp_dialog)

        # OTP Input Field
        otp_label = QLabel("Enter the OTP sent to your phone/email:")
        otp_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(otp_label)

        otp_input = QLineEdit()
        otp_input.setPlaceholderText("Enter OTP")
        otp_input.setStyleSheet(self.input_style())
        layout.addWidget(otp_input)

        
        button_layout = QHBoxLayout()
        
        resend_button = QPushButton("Resend OTP")
        resend_button.setStyleSheet(self.button_style())
        resend_button.clicked.connect(self.resend_otp)  
        button_layout.addWidget(resend_button)

        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet(self.button_style())
        submit_button.clicked.connect(lambda: self.verify_otp(otp_input.text(), otp_dialog))
        button_layout.addWidget(submit_button)

        layout.addLayout(button_layout)

        # Show the dialog
        otp_dialog.exec()

    def resend_otp(self):
        if time.time() - self.otp_timestamp > 60:
            self.generate_and_send_otp()
            QMessageBox.information(self, "OTP Sent", "A new OTP has been sent to your phone/email.")
        else:
            QMessageBox.warning(self, "Warning", "Please wait before requesting another OTP.")

    def verify_otp(self, otp, dialog):
        if otp == str(self.generated_otp):
            QMessageBox.information(self, "Success", "OTP verified successfully.")
            dialog.accept()  # Close OTP popup
            self.finalize_signup() 
        else:
            QMessageBox.critical(self, "Error", "Invalid OTP. Please try again.")
    
    def finalize_signup(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        cnic = self.cnic_input.text()
        nationality = self.nationality_input.text()
        dob = self.dob_input.text()
        gender = self.gender_combo.currentText()
        password = self.password_input.text()
        province = self.province_combo.currentText()
        district = self.district_combo.currentText()
        tehsil = self.tehsil_combo.currentText()
        pic_path = self.selected_file_path
        binary_pic = doc_as_binary(pic_path)

        # Print all the variables
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print(f"CNIC: {cnic}")
        print(f"Nationality: {nationality}")
        print(f"Date of Birth: {dob}")
        print(f"Gender: {gender}")
        print(f"Password: {password}")
        print(f"Province: {province}")
        print(f"District: {district}")
        print(f"Tehsil: {tehsil}")
        print(f"Picture Path: {pic_path}")

        
        # Add user to the database
        if add_user_to_db(first_name=first_name, last_name=last_name, phone=phone, email=email, cnic=cnic, gender=gender, password=password, province=province, district=district, tehsil=tehsil, pic=pic_path, dob=dob):
            QMessageBox.information(self, "Success", "User added successfully.")
            self.go_to_login()
        else:
            QMessageBox.critical(self, "Error", "An error occurred. Please try again.")
            return

    def create_picture_selector(self, layout):
        picture_layout = QVBoxLayout()

        self.picture_label = QLabel("No Image Selected")
        self.picture_label.setStyleSheet("color: white; font-size: 16px;")
        self.picture_label.setAlignment(Qt.AlignCenter)
        self.picture_label.setFixedSize(200, 200)
        self.picture_label.setStyleSheet("border: 2px dashed #FFFFFF;")

        select_button = QPushButton("Select Picture")
        select_button.setStyleSheet(self.button_style())
        select_button.clicked.connect(self.select_picture)

        picture_layout.addWidget(self.picture_label, alignment=Qt.AlignCenter)
        picture_layout.addWidget(select_button, alignment=Qt.AlignCenter)

        layout.addLayout(picture_layout, 0, 4, 5, 1)  

    def select_picture(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Picture", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)
            if pixmap.isNull():
                QMessageBox.critical(self, "Error", "The selected image is not valid.")
            else:
                self.picture_label.setPixmap(pixmap.scaled(self.picture_label.size(), Qt.KeepAspectRatio))
                self.picture_label.setText("")
        if pixmap.isNull():  
            QMessageBox.critical(self, "Error", "The selected image is not valid.")
        else:
            self.selected_file_path = file_path  # Store the file path
            self.picture_label.setPixmap(pixmap.scaled(self.picture_label.size(), Qt.KeepAspectRatio))
            self.picture_label.setText("")

    def go_to_login(self):
        self.close()
        from login import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()

    def update_tehsils(self):
        self.tehsil_combo.clear()
        self.tehsil_combo.addItems(district_tehsils(self.district_combo.currentText()))

    def update_districts(self):
        self.district_combo.clear()
        self.district_combo.addItems(provinces_districts(self.province_combo.currentText()))


if __name__ == '__main__':
    app = QApplication([])
    window = User_SignUpPage()
    window.show()
    app.exec_()
