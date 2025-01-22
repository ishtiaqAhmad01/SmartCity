from PyQt5.QtWidgets import QApplication
from user_complain import UserComplainManagmnet
from user_digitaldoc import DigitalDocumentStorage
from user_trasport import PublicTransportBooking
from user_appointment import AppointmentBooking
from user_bill import UtilityBillManagement
from dashboard import BaseDashboard

class UserDashboard(BaseDashboard):
    def __init__(self):
        super().__init__("User Dashboard")
        self.add_page("Complaint Management", UserComplainManagmnet())
        self.add_page("Digital Document Storage", DigitalDocumentStorage())
        self.add_page("Public Transport Booking", PublicTransportBooking())
        self.add_page("Appointment Booking", AppointmentBooking())
        self.add_page("Utility Bill Management", UtilityBillManagement())