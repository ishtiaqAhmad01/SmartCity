from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from functions import doc_as_binary, binary_as_doc

class DigitalDocumentStorage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Header section
        header = QLabel("Digital Document Storage System")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        header.setFont(QFont("Arial", 20))
        layout.addWidget(header)

        # Tab Widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #C0C0C0;
                background: #F0F0F0;
                border-radius: 10px;
            }
            QTabBar::tab {
                background: #3498DB;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
                margin: 2px;
                width: 200px;
            }
            QTabBar::tab:selected {
                background: #2980B9;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.tab_widget)

        # Add Tabs
        self.add_document_tab()
        self.view_documents_tab()
        self.settings_tab()

        self.setLayout(layout)

    def add_document_tab(self):
        """Tab for adding new documents"""
        add_tab = QWidget()
        add_layout = QVBoxLayout()
        
        # Document upload section
        file_label = QLabel("Upload Document")
        file_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        add_layout.addWidget(file_label)
        
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Select file...")
        self.file_input.setReadOnly(True)
        self.file_input.setStyleSheet("padding: 8px; border: 1px solid #BDC3C7; border-radius: 5px;")
        add_layout.addWidget(self.file_input)
        
        browse_button = QPushButton("Browse")
        browse_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                padding: 8px 15px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        browse_button.clicked.connect(self.browse_file)
        add_layout.addWidget(browse_button)

        # Category selection
        category_label = QLabel("Select Category")
        category_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        add_layout.addWidget(category_label)

        self.category_dropdown = QComboBox()
        self.category_dropdown.addItems(["Personal", "Bills", "Receipts", "Government IDs", "Others"])
        self.category_dropdown.setStyleSheet("padding: 8px; border: 1px solid #BDC3C7; border-radius: 5px;")
        add_layout.addWidget(self.category_dropdown)

        # Upload button
        upload_button = QPushButton("Upload Document")
        upload_button.setStyleSheet("""
            QPushButton {
                background-color: #27AE60;
                color: white;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        upload_button.clicked.connect(self.upload_document)
        add_layout.addWidget(upload_button)

        # Status label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("font-size: 14px; color: red;")
        add_layout.addWidget(self.status_label)

        add_tab.setLayout(add_layout)
        self.tab_widget.addTab(add_tab, "Add Document")

    def view_documents_tab(self):
        """Tab for viewing stored documents"""
        view_tab = QWidget()
        view_layout = QVBoxLayout()

        # Filter dropdown
        filter_label = QLabel("Filter by Category")
        filter_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        view_layout.addWidget(filter_label)

        self.filter_dropdown = QComboBox()
        self.filter_dropdown.addItems(["All", "Personal", "Bills", "Receipts", "Government IDs", "Others"])
        self.filter_dropdown.setStyleSheet("padding: 8px; border: 1px solid #BDC3C7; border-radius: 5px;")
        self.filter_dropdown.currentIndexChanged.connect(self.filter_documents)
        view_layout.addWidget(self.filter_dropdown)

        # Documents table
        self.document_table = QTableWidget()
        self.document_table.setColumnCount(3)
        self.document_table.setHorizontalHeaderLabels(["File Name", "Category", "Download/View"])
        self.document_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.document_table.setStyleSheet("""
            QTableWidget {
                background-color: #ECF0F1;
                border: 1px solid #BDC3C7;
                border-radius: 10px;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: #3498DB;
                color: white;
                font-weight: bold;
                padding: 5px;
            }
        """)
        self.document_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        view_layout.addWidget(self.document_table)

        # Refresh button
        refresh_button = QPushButton("Refresh")
        refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        refresh_button.clicked.connect(self.refresh_documents)
        view_layout.addWidget(refresh_button)
        self.refresh_documents()

        view_tab.setLayout(view_layout)
        self.tab_widget.addTab(view_tab, "View Documents")

    def settings_tab(self):
        """Tab for application settings"""
        settings_tab = QWidget()
        settings_layout = QVBoxLayout()

        # Encryption settings
        encryption_label = QLabel("Encryption Options")
        encryption_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        settings_layout.addWidget(encryption_label)

        encryption_checkbox = QCheckBox("Enable Encryption")
        encryption_checkbox.setStyleSheet("font-size: 14px;")
        settings_layout.addWidget(encryption_checkbox)

        # Storage quota
        quota_label = QLabel("Storage Quota: 2GB used of 10GB")
        quota_label.setStyleSheet("font-size: 14px; color: #7F8C8D;")
        settings_layout.addWidget(quota_label)

        settings_tab.setLayout(settings_layout)
        self.tab_widget.addTab(settings_tab, "Settings")

    def browse_file(self):
        """Open file dialog to select a document"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Document", "", "All Files (*.*)")
        if file_path:
            self.file_input.setText(file_path)

    def upload_document(self):
        """Handle document upload"""
        file_path = self.file_input.text()
        category = self.category_dropdown.currentText()

        if not file_path:
            self.status_label.setText("Please select a file to upload.")
            return

        # Convert file to binary and simulate database storage
        binary_data = doc_as_binary(file_path)
        if binary_data:
            # Simulate storing binary in database (replace with real DB logic)
            print(f"Storing document in category '{category}': {len(binary_data)} bytes")
            self.status_label.setText(f"Document uploaded successfully under category '{category}'.")
            self.status_label.setStyleSheet("color: green;")
        else:
            self.status_label.setText("Failed to read the document.")

    def filter_documents(self):
        """Filter documents based on category"""
        pass

    def refresh_documents(self):
        """Refresh document table"""
        self.document_table.setRowCount(3)  # Example row count, replace with dynamic fetch logic
        example_data = [
            {"File Name": "Document1.pdf", "Category": "Bills"},
            {"File Name": "ID_Card.jpg", "Category": "Government IDs"},
            {"File Name": "Receipt.png", "Category": "Receipts"}
        ]

        self.document_table.setColumnCount(3)  # Set the table to have 3 columns

        for row, data in enumerate(example_data):
            self.document_table.setItem(row, 0, QTableWidgetItem(data["File Name"]))
            self.document_table.setItem(row, 1, QTableWidgetItem(data["Category"]))

            # Add action buttons (View + Download) in a single cell under the 3rd column
            actions_widget = QWidget()
            actions_widget.setStyleSheet("background-color: white;")

            actions_layout = QHBoxLayout()
            actions_layout.setContentsMargins(0, 0, 0, 0)

            view_button = QPushButton("View")
            view_button.setStyleSheet("""
                QPushButton {
                    background-color: #3498DB;
                    color: white;
                    padding: 10px;
                    font-size: 12px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #2980B9;
                }
            """)
            view_button.clicked.connect(lambda _, doc=data["File Name"]: self.view_document(doc))

            download_button = QPushButton("Download")
            download_button.setStyleSheet("""
                QPushButton {
                    background-color: #27AE60;
                    color: white;
                    padding: 10px;
                    font-size: 12px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #229954;
                }
            """)
            download_button.clicked.connect(lambda _, doc=data["File Name"]: self.download_document(doc))

            actions_layout.addWidget(view_button)
            actions_layout.addWidget(download_button)
            actions_widget.setLayout(actions_layout)

            self.document_table.setCellWidget(row, 2, actions_widget)  # Place both buttons in the 3rd column

    def view_document(self, file_name):
        """Simulate viewing a document"""
        QMessageBox.information(self, "View Document", f"Viewing {file_name}")

    def download_document(self, file_name):
        """Simulate downloading a document"""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Document", file_name)
        if file_path:
            QMessageBox.information(self, "Download Document", f"Saved {file_name} to {file_path}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = DigitalDocumentStorage()
    window.setStyleSheet("background-color: #2C3E50; color: white;")
    window.show()
    sys.exit(app.exec_())
