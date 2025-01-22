import sys
import time
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt, QTimer


class PaymentPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Payment Entry")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self.card_number_input = QLineEdit(self)
        self.card_number_input.setPlaceholderText("Enter Card Number")
        self.card_number_input.setMaxLength(16) 

        self.card_expiry_input = QLineEdit(self)
        self.card_expiry_input.setPlaceholderText("Enter Expiration Date (MM/YY)")

        self.card_cvc_input = QLineEdit(self)
        self.card_cvc_input.setPlaceholderText("Enter CVC")
        self.card_cvc_input.setMaxLength(4) 

        self.form_layout.addRow("Card Number:", self.card_number_input)
        self.form_layout.addRow("Expiration Date:", self.card_expiry_input)
        self.form_layout.addRow("CVC:", self.card_cvc_input)

        self.submit_button = QPushButton("Submit Payment", self)
        self.submit_button.clicked.connect(self.simulate_payment)

        self.loading_label = QLabel(self)
        self.loading_label.setText("")
        self.loading_label.setAlignment(Qt.AlignCenter)

        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.loading_label)
        self.setLayout(self.layout)

        self.payment_successful = False

    def simulate_payment(self):
        card_number = self.card_number_input.text()
        card_expiry = self.card_expiry_input.text()
        card_cvc = self.card_cvc_input.text()

        
        if not card_number or not card_expiry or not card_cvc:
            QMessageBox.warning(self, "Validation Error", "All fields are required!")
            return

        self.loading_label.setText("Processing payment... Please wait.")
        self.submit_button.setEnabled(False) 

        QTimer.singleShot(3000, self.show_payment_result)

    def show_payment_result(self):
        self.accept()

