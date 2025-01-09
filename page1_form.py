from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from functions import majorProblem_to_subProblem

class AddComplaintDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Complaint")
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Form layout for inputs
        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        # Title label for form
        title_label = QLabel("<b>Add New Complaint</b>")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Main category dropdown
        self.main_category_combo = QComboBox()
        self.main_category_combo.addItems(["Electrical", "Plumbing", "Potholes", "Street Lighting", "Garbage", "Other"])
        self.style_combo(self.main_category_combo)
        self.main_category_combo.currentIndexChanged.connect(self.update_subcategories)
        form_layout.addRow("Main Category:", self.main_category_combo)

        # Subcategory dropdown
        self.sub_category_combo = QComboBox()
        self.style_combo(self.sub_category_combo)
        form_layout.addRow("Sub Category:", self.sub_category_combo)
        self.update_subcategories()

        # Description input field
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter the complaint description...")
        self.style_input(self.description_input)
        form_layout.addRow("Description:", self.description_input)

        # Address input field
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter the address where issue occurred...")
        self.style_input(self.address_input)
        form_layout.addRow("Address:", self.address_input)

        # Add form layout to main layout
        layout.addLayout(form_layout)

        # Buttons
        button_layout = QVBoxLayout()
        submit_btn = QPushButton("Submit")
        submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        submit_btn.clicked.connect(self.accept)
        button_layout.addWidget(submit_btn)

        cancel_btn = QPushButton("Cancel")
        
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def style_input(self, input_field):
        input_field.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 2px solid #BDC3C7;
                border-radius: 8px;
                font-size: 14px;
                background-color: #ECF0F1;
            }
            QLineEdit:focus {
                border-color: #3498DB;
                background-color: white;
            }
        """)

    def style_combo(self, combo_box):
        combo_box.setStyleSheet("""
            QComboBox {
                padding: 10px;
                border: 2px solid #BDC3C7;
                border-radius: 8px;
                font-size: 14px;
                background-color: #ECF0F1;
            }
            QComboBox:focus {
                border-color: #3498DB;
            }
        """)

    def update_subcategories(self):
        self.sub_category_combo.clear()
        main_category = self.main_category_combo.currentText()
        self.sub_category_combo.addItems(majorProblem_to_subProblem(main_category))

    def get_data(self):
        main_category = self.main_category_combo.currentText()
        sub_category = self.sub_category_combo.currentText()
        description = self.description_input.text()
        address = self.address_input.text()
        return main_category, sub_category, description, address
        

if __name__ == "__main__":
    app = QApplication([])
    AddComplaintDialog().exec_()
