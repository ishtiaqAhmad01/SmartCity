from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class AddDocumentPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Document")
        self.setGeometry(100, 100, 450, 450)
        self.setStyleSheet("background-color: white;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Title
        title_label = QLabel("<b>Add New Document</b>")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Form layout for document inputs
        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        # Assign Name Field
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter document name...")
        self.style_input(self.name_input)
        form_layout.addRow("Assign Name:", self.name_input)

        # Document Upload Field
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Select file...")
        self.file_input.setReadOnly(True)
        self.style_input(self.file_input)
        
        browse_button = QPushButton("Browse")
        self.style_button_primary(browse_button)
        browse_button.clicked.connect(self.browse_file)
        form_layout.addRow("Upload Document:", self.file_input)
        form_layout.addRow("", browse_button)

        # Category Dropdown
        self.category_dropdown = QComboBox()
        self.category_dropdown.addItems(["Personal", "Bills", "Receipts", "Government IDs", "Others"])
        self.style_combo(self.category_dropdown)
        form_layout.addRow("Select Category:", self.category_dropdown)

        # Status Label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("font-size: 14px; color: red;")
        form_layout.addRow("Status:", self.status_label)

        layout.addLayout(form_layout)

        # Upload and Cancel Buttons
        button_layout = QVBoxLayout()
        upload_button = QPushButton("Upload Document")
        cancel_button = QPushButton("Cancel")

        self.style_button_primary(upload_button)
        self.style_button_secondary(cancel_button)

        upload_button.clicked.connect(self.upload_document)
        cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(upload_button)
        button_layout.addWidget(cancel_button)
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

    def style_button_primary(self, button):
        button.setStyleSheet("""
            QPushButton {
                background-color: #27AE60;
                color: white;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)

    def style_button_secondary(self, button):
        button.setStyleSheet("""
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

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Document", "", "All Files (*.*)")
        if file_path:
            self.file_input.setText(file_path)

    def upload_document(self):
        file_name = self.name_input.text()
        file_path = self.file_input.text()
        category = self.category_dropdown.currentText()

        if not file_name:
            self.status_label.setText("Please enter a document name.")
            return

        if not file_path:
            self.status_label.setText("Please select a file to upload.")
            return

        # Simulate binary read and upload process
        binary_data = self.read_document_as_binary(file_path)
        if binary_data:
            self.status_label.setText(f"Document '{file_name}' uploaded successfully under category '{category}'.")
            self.status_label.setStyleSheet("font-size: 14px; color: green;")
        else:
            self.status_label.setText("Failed to read the document.")

    def read_document_as_binary(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return None


if __name__ == "__main__":
    app = QApplication([])
    dialog = AddDocumentPopup()
    dialog.exec_()
