from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from functions import table_style, tab_style, offices
from database import insert_appointmnet, get_appointmnets
from globals import get_user_id
from datetime import datetime

class AppointmentBooking(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        
        header = QLabel("Appointment Booking System")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout.addWidget(header)

        
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet(tab_style())

        
        self.init_new_appointment_tab()
        self.init_appointment_history_tab()

        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def init_new_appointment_tab(self):
        new_appointment_tab = QWidget()
        layout = QVBoxLayout(new_appointment_tab)

        
        form_layout = QFormLayout()

        
        self.service_dropdown = QComboBox()
        self.service_dropdown.addItems(["Passport Renewal", "CNIC Issuance", "Driver's License"])
        self.service_dropdown.currentTextChanged.connect(self.update_locations)
        form_layout.addRow("Service:", self.service_dropdown)

        
        self.location_dropdown = QComboBox()
        self.location_dropdown.addItems(offices(self.service_dropdown.currentText()))
        form_layout.addRow("Location:", self.location_dropdown)

        
        self.date_picker = QDateEdit()
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setDate(QDate.currentDate())
        form_layout.addRow("Appointment Date:", self.date_picker)

        
        self.time_slot_dropdown = QComboBox()
        self.time_slot_dropdown.addItems(["10:00 AM", "12:00 PM", "2:00 PM", "4:00 PM"])
        form_layout.addRow("Time Slot:", self.time_slot_dropdown)

        
        self.notes_input = QTextEdit()
        self.notes_input.setPlaceholderText("Additional notes or reason for the appointment...")
        form_layout.addRow("Notes:", self.notes_input)

        layout.addLayout(form_layout)

        
        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton("Confirm Appointment")
        self.confirm_button.setStyleSheet("""
            QPushButton {
                background-color: #27AE60;
                color: white;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        self.confirm_button.clicked.connect(self.save_appointment)
        button_layout.addWidget(self.confirm_button)

        layout.addLayout(button_layout)

        
        self.tab_widget.addTab(new_appointment_tab, "New Appointment")

    def update_locations(self):
        self.location_dropdown.clear()
        self.location_dropdown.addItems(offices(self.service_dropdown.currentText()))

    def init_appointment_history_tab(self):
        history_tab = QWidget()
        layout = QVBoxLayout(history_tab)

        
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(6)
        self.history_table.setHorizontalHeaderLabels(
            ["Service", "Location", "Date", "Time", "Status", "Actions"]
        )
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.history_table.setStyleSheet(table_style())
        layout.addWidget(self.history_table)

        self.tab_widget.addTab(history_tab, "Appointment History")


        self.populate_appointment_table()

    def save_appointment(self):
        service = self.service_dropdown.currentText()
        location = self.location_dropdown.currentText()
        date = self.date_picker.date().toString("yyyy-MM-dd")
        time_slot = self.time_slot_dropdown.currentText()
        notes = self.notes_input.toPlainText()
        time_24hr = datetime.strptime(time_slot, "%I:%M %p").strftime("%H:%M:%S")
        try:
            insert_appointmnet(get_user_id(), service, location, 'Upcoming', date)
            QMessageBox.information(self, "Success", "Appointment is added to Sucessfully")
            self.populate_appointment_table()
        except ExceptionGroup as e:
            print(e)


    def populate_appointment_table(self):
        data = get_appointmnets(get_user_id())
        print(get_user_id())
        print(data)

        if not data:
            self.history_table.setRowCount(0)
            return
        
        # service,  location, date, time, status
        self.history_table.setRowCount(len(data))
        for row, appointment in enumerate(data):
            self.history_table.setItem(row, 0, QTableWidgetItem(appointment[0]))
            self.history_table.setItem(row, 1, QTableWidgetItem(appointment[1]))
            self.history_table.setItem(row, 2, QTableWidgetItem(str(appointment[2])))
            self.history_table.setItem(row, 3, QTableWidgetItem(str(appointment[3])))
            self.history_table.setItem(row, 4, QTableWidgetItem(appointment[4]))

            
            actions_widget = QWidget()
            actions_layout = QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(0, 0, 0, 0)

            if appointment[4] == "Upcoming":
                cancel_button = QPushButton("Cancel")
                cancel_button.clicked.connect(lambda _, r=row: self.cancel_appointment(r))
                actions_layout.addWidget(cancel_button)

                reschedule_button = QPushButton("Reschedule")
                reschedule_button.clicked.connect(lambda _, r=row: self.reschedule_appointment(r))
                actions_layout.addWidget(reschedule_button)
            elif appointment[4] == "Completed":
                feedback_button = QPushButton("Feedback")
                feedback_button.clicked.connect(lambda _, r=row: self.leave_feedback(r))
                actions_layout.addWidget(feedback_button)

            actions_widget.setLayout(actions_layout)
            self.history_table.setCellWidget(row, 5, actions_widget)

    def cancel_appointment(self, row):
        pass  

    def reschedule_appointment(self, row):
        pass

    def leave_feedback(self, row):
        pass 


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AppointmentBooking()
    window.setStyleSheet("background-color: #FFFFFF; color: #333;")
    window.show()
    sys.exit(app.exec_())
