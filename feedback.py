from PyQt5.QtWidgets import *

class FeedbackDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Provide Feedback")
        self.setFixedSize(300, 200)

        # Create layout
        layout = QVBoxLayout()

        # Create and add widgets
        self.rating_label = QLabel("Rating (1 to 5):")
        self.rating_input = QSpinBox()
        self.rating_input.setRange(1, 5)
        self.rating_input.setValue(5)  # default to 5
        self.feedback_label = QLabel("Your Feedback:")
        self.feedback_input = QTextEdit()

        # Add widgets to layout
        layout.addWidget(self.rating_label)
        layout.addWidget(self.rating_input)
        layout.addWidget(self.feedback_label)
        layout.addWidget(self.feedback_input)

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_feedback)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_feedback(self):
        # Get the values entered by the user
        self.rating = self.rating_input.value()
        self.feedback = self.feedback_input.toPlainText()

        # Close dialog
        self.accept()

    def get_feedback(self):
        return self.feedback, self.rating
