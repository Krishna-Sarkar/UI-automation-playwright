import pytest
from lib.utils.DataReader import read_xls, read_config
from lib.commons.fixtures import setup_teardown
from lib.commons.AppointmentApp import AppointmentApp
from playwright.sync_api import Page

@pytest.mark.parametrize("facility,hospitalReadmission,healthcareProgram,visitDate,Comment",
                         read_xls('appointmentData.xlsx', 'city'))
def test_appointment_details(page:Page, setup_teardown, facility, hospitalReadmission, healthcareProgram, visitDate, Comment):
    page=setup_teardown
    data = read_config()
    appointmentApp:AppointmentApp=AppointmentApp(page)
    appointmentApp.loginPage.navigateToLogin().performLogin(username=data['admin']['username'],password=data['admin']['password'])
    appointmentApp.appointmentPage.makeAppointment(facility,hospitalReadmission,healthcareProgram,visitDate,Comment)
    appointmentApp.assertAppointmentPage.assertAppointment(facility,hospitalReadmission,healthcareProgram,visitDate,Comment)