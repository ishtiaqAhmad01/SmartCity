from PyQt5.QtWidgets import *
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from page2_form import AddDocumentPopup
from functions import *
import globals
from user_database import add_doc_to_database, load_doc_from_database, get_file_from_database, get_fileinfo_from_database

class DigitalDocumentStorage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        
        header = QLabel("Digital Document Storage System")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        header.setFont(QFont("Arial", 20))
        layout.addWidget(header)

        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet(tab_style())
        layout.addWidget(self.tab_widget)

        self.view_documents_tab()
        self.settings_tab()

        self.setLayout(layout)

    def view_documents_tab(self):
        view_tab = QWidget()
        view_layout = QVBoxLayout()

        add_doc_button = QPushButton("Add Document")
        add_doc_button.setStyleSheet("""
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
        add_doc_button.clicked.connect(self.open_add_document_popup)
        view_layout.addWidget(add_doc_button, alignment=Qt.AlignRight) 

        filter_label = QLabel("Filter by Category")
        filter_label.setStyleSheet("font-size: 18px; font-weight: bold;color:white;")
        view_layout.addWidget(filter_label)

        self.filter_dropdown = QComboBox()
        self.filter_dropdown.addItems(["All", "Personal", "Bills", "Receipts", "Government IDs", "Others"])
        self.filter_dropdown.setStyleSheet("padding: 8px; border: 1px solid #BDC3C7; border-radius: 5px;")
        self.filter_dropdown.currentIndexChanged.connect(self.refresh_documents)
        view_layout.addWidget(self.filter_dropdown)

        self.document_table = QTableWidget()
        self.document_table.setColumnCount(3)
        self.document_table.setHorizontalHeaderLabels(["File Name", "Category", "Download/View"])
        self.document_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.document_table.setStyleSheet(table_style())
        self.document_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        view_layout.addWidget(self.document_table)

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

    def open_add_document_popup(self):
        popup = AddDocumentPopup(self)
        popup.move(self.geometry().right() - popup.width() - 20, self.geometry().top() + 50)  # Align popup to the right
        if popup.exec_() == QDialog.Accepted:
            file_name, file_path, category = popup.get_document_info()
            print(f"Document Name: {file_name}, File Path: {file_path}, Category: {category}")
            _ , ext = os.path.splitext(file_path)
            self.add_doc(file_name, file_path, category, ext)
        else:
            ... # do nothing
    
    def add_doc(self, file_name, file_path, category, ext):
        if add_doc_to_database(cnic=globals.get_user_id(), document_name=file_name, document_ext=ext, document_type=category, doc=file_path):
            QMessageBox.information(None, "Done", "Docment is uploaded Successfully.", QMessageBox.Ok)
            self.refresh_documents()
        else:
            QMessageBox.critical(None, "Error", "Docment is uploaded UnSuccessfull.", QMessageBox.Ok)

    def settings_tab(self):
        settings_tab = QWidget()
        settings_layout = QVBoxLayout()

        encryption_label = QLabel("Encryption Options")
        encryption_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        settings_layout.addWidget(encryption_label)

        encryption_checkbox = QCheckBox("Enable Encryption")
        encryption_checkbox.setStyleSheet("font-size: 14px;")
        settings_layout.addWidget(encryption_checkbox)

        quota_label = QLabel("Storage Quota: 2GB used of 10GB")
        quota_label.setStyleSheet("font-size: 14px; color: #7F8C8D;")
        settings_layout.addWidget(quota_label)

        settings_tab.setLayout(settings_layout)
        self.tab_widget.addTab(settings_tab, "Settings")

    def refresh_documents(self):
        data = []
        loaded_from_database = load_doc_from_database(globals.get_user_id())

        if not loaded_from_database:
            return
            

        for row in loaded_from_database:
            if row[2] == self.filter_dropdown.currentText() or self.filter_dropdown.currentText() == 'All':
                data.append({"File Name": row[0]+row[1], "Category": row[2]})


        self.document_table.setColumnCount(3)
        self.document_table.setRowCount(len(data))

        for row, data in enumerate(data):
            print(self.filter_dropdown.currentText(),"===",data["Category"] )
            self.document_table.setItem(row, 0, QTableWidgetItem(data["File Name"]))
            self.document_table.setItem(row, 1, QTableWidgetItem(data["Category"]))

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

            self.document_table.setCellWidget(row, 2, actions_widget)

    def view_document(self, file_name):
        document_id, upload_date, cnic, document_name, document_ext, document_type = get_fileinfo_from_database(globals.get_user_id(), file_name)
        QMessageBox.information(self, "View Document", f" File Id : {document_id} \n File Name :  {document_name} \n File Extention : {document_ext} \n Upload date : {upload_date} \n Category : {document_type}")

    def download_document(self, file_name):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Document", file_name)
        if file_path:
            try:
                doc = get_file_from_database(globals.get_user_id(), file_name)
                print("path = ",file_name)
                print("user = ",globals.get_user_id())
                if len(doc)!=0:
                    binary_as_doc(doc[0], file_path) #bcz it return tuple 
                    QMessageBox.information(self, "Download Document", f"Saved {file_name} to {file_path}")
                else:
                    print("return none file from database")
            except Exception as e:
                print(e)
        else:
            QMessageBox.critical(self, "Error", "Please Select a Valid location/Path")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = DigitalDocumentStorage()
    window.setStyleSheet("background-color: #2C3E50; color: white;")
    window.show()
    sys.exit(app.exec_())
