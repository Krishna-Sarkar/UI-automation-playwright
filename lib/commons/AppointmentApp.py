from lib.commons.LoginPage import LoginPage
from lib.pom.AppointmentPage import AppointmentPage
from lib.assertion.AssertAppintmentPage import AssertAppointmentPage



class AppointmentApp(LoginPage, AppointmentPage, AssertAppointmentPage):

    def __init__(self, page):
        self.loginPage = LoginPage(page)
        self.appointmentPage = AppointmentPage(page)
        self.assertAppointmentPage=AssertAppointmentPage(page)
