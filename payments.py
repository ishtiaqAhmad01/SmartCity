import sys
import stripe
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox

# Set your secret key from the Stripe Dashboard (test key used here)
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # Replace with your actual secret key

class PaymentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stripe Payment Simulation")
        self.setGeometry(100, 100, 400, 250)

        # Create the UI elements
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        # Input fields
        self.card_number_input = QLineEdit(self)
        self.card_number_input.setPlaceholderText("Card Number")
        self.card_expiry_input = QLineEdit(self)
        self.card_expiry_input.setPlaceholderText("Expiration Date (MM/YY)")
        self.card_cvc_input = QLineEdit(self)
        self.card_cvc_input.setPlaceholderText("CVC")

        # Add form elements
        self.form_layout.addRow("Card Number:", self.card_number_input)
        self.form_layout.addRow("Expiration Date:", self.card_expiry_input)
        self.form_layout.addRow("CVC:", self.card_cvc_input)

        # Submit Button
        self.submit_button = QPushButton("Pay Now", self)
        self.submit_button.clicked.connect(self.handle_payment)

        # Result Label
        self.result_label = QLabel(self)
        self.result_label.setText("")

        # Add everything to the layout
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.result_label)
        self.setLayout(self.layout)

    def handle_payment(self):
        # Get input values
        card_number = self.card_number_input.text()
        card_expiry = self.card_expiry_input.text()
        card_cvc = self.card_cvc_input.text()

        # Basic validation
        if not card_number or not card_expiry or not card_cvc:
            self.show_message("Error", "All fields are required!")
            return

        # Here we're simulating a payment with a test card on Stripe
        try:
            # Create a PaymentIntent in the backend (simulation)
            payment_intent = stripe.PaymentIntent.create(
                amount=500,
                currency="gbp",
                payment_method_types=["card"],
                payment_method="pm_card_visa",  # Replace with actual payment method for real transactions
                confirm=True
            )

            # Simulate payment success or failure based on response
            if payment_intent.status == "succeeded":
                self.result_label.setText("Payment Successful!")
                self.show_message("Success", "Payment was successful!")
            else:
                self.result_label.setText("Payment Failed!")
                self.show_message("Failed", "Payment failed! Please try again.")
        except stripe.error.StripeError as e:
            self.result_label.setText("Payment Failed!")
            self.show_message("Error", str(e))

    def show_message(self, title, message):
        QMessageBox.information(self, title, message)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaymentWidget()
    window.show()
    sys.exit(app.exec_())