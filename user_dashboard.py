import sys
from PyQt5.QtWidgets import QApplication
from page1 import Page1
from page2 import DigitalDocumentStorage
from page3 import PublicTransportBooking
from page4 import AppointmentBooking
from page5 import UtilityBillManagement
from dashboard import BaseDashboard


class UserDashboard(BaseDashboard):
    def __init__(self):
        super().__init__("User Dashboard")
        self.add_page("Complaint Management", Page1())
        self.add_page("Digital Document Storage", DigitalDocumentStorage())
        self.add_page("Public Transport Booking", PublicTransportBooking())
        self.add_page("Appointment Booking", AppointmentBooking())
        self.add_page("Utility Bill Management", UtilityBillManagement())



