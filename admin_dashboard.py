import sys
from PyQt5.QtWidgets import QApplication
from dashboard import BaseDashboard
from admin_bill import BillManagement
from admin_traspost import Admin_transport
from admin_appointment import AdminAppointmentManagement
from admin_complain import AdminPage



class AdminDashboard(BaseDashboard):
    def __init__(self):
        super().__init__("User Dashboard")
        self.add_page("Bill Management", BillManagement())
        self.add_page("Public Transport Management", Admin_transport())
        self.add_page("Appointment Booking", AdminAppointmentManagement())
        self.add_page("Complain", AdminPage())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = AdminDashboard()
    dashboard.show()
    sys.exit(app.exec_())