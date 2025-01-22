from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from functions import table_style, tab_style


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
        form_layout.addRow("Service:", self.service_dropdown)

        
        self.location_dropdown = QComboBox()
        self.location_dropdown.addItems(["City Hall", "Regional Office", "Downtown Office"])
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
        self.confirm_button.clicked.connect(self.confirm_appointment)
        button_layout.addWidget(self.confirm_button)

        layout.addLayout(button_layout)

        
        self.tab_widget.addTab(new_appointment_tab, "New Appointment")

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


        self.load_appointments()

    def confirm_appointment(self):
        """Confirm a new appointment and save to the database."""
        service = self.service_dropdown.currentText()
        location = self.location_dropdown.currentText()
        date = self.date_picker.date().toString("yyyy-MM-dd")
        time_slot = self.time_slot_dropdown.currentText()
        notes = self.notes_input.toPlainText()

        # Placeholder: Save appointment to the database
        self.save_appointment(service, location, date, time_slot, notes)

    def save_appointment(self, service, location, date, time_slot, notes):
        """Save the appointment to the database (Placeholder function)."""
        print(f"Saving appointment: {service}, {location}, {date}, {time_slot}, {notes}")
        pass  # Implement MySQL INSERT logic here

    def load_appointments(self):
        """Load appointments from the database (Placeholder function)."""
        print("Loading appointments from the database...")
        # Replace with MySQL SELECT logic
        example_data = [
            {"service": "Passport Renewal", "location": "City Hall", "date": "2025-01-15", "time": "10:00 AM", "status": "Upcoming"},
            {"service": "CNIC Issuance", "location": "Regional Office", "date": "2025-01-10", "time": "12:00 PM", "status": "Completed"},
        ]
        self.populate_appointment_table(example_data)

    def populate_appointment_table(self, data):
        """Populate the appointment history table with data."""
        self.history_table.setRowCount(len(data))
        for row, appointment in enumerate(data):
            self.history_table.setItem(row, 0, QTableWidgetItem(appointment["service"]))
            self.history_table.setItem(row, 1, QTableWidgetItem(appointment["location"]))
            self.history_table.setItem(row, 2, QTableWidgetItem(appointment["date"]))
            self.history_table.setItem(row, 3, QTableWidgetItem(appointment["time"]))
            self.history_table.setItem(row, 4, QTableWidgetItem(appointment["status"]))

            # Add action buttons
            actions_widget = QWidget()
            actions_layout = QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(0, 0, 0, 0)

            if appointment["status"] == "Upcoming":
                cancel_button = QPushButton("Cancel")
                cancel_button.clicked.connect(lambda _, r=row: self.cancel_appointment(r))
                actions_layout.addWidget(cancel_button)

                reschedule_button = QPushButton("Reschedule")
                reschedule_button.clicked.connect(lambda _, r=row: self.reschedule_appointment(r))
                actions_layout.addWidget(reschedule_button)
            elif appointment["status"] == "Completed":
                feedback_button = QPushButton("Feedback")
                feedback_button.clicked.connect(lambda _, r=row: self.leave_feedback(r))
                actions_layout.addWidget(feedback_button)

            actions_widget.setLayout(actions_layout)
            self.history_table.setCellWidget(row, 5, actions_widget)

    def cancel_appointment(self, row):
        """Cancel an appointment (Placeholder function)."""
        print(f"Cancelling appointment at row {row}")
        pass  # Implement MySQL UPDATE logic to mark as canceled

    def reschedule_appointment(self, row):
        """Reschedule an appointment (Placeholder function)."""
        print(f"Rescheduling appointment at row {row}")
        pass  # Implement MySQL UPDATE logic to reschedule

    def leave_feedback(self, row):
        """Leave feedback for an appointment (Placeholder function)."""
        print(f"Leaving feedback for appointment at row {row}")
        pass  # Implement MySQL INSERT/UPDATE logic for feedback


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AppointmentBooking()
    window.setStyleSheet("background-color: #FFFFFF; color: #333;")
    window.show()
    sys.exit(app.exec_())
