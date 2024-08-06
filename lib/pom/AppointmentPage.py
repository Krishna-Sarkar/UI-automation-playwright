from playwright.sync_api import Page, Locator

class AppointmentPage:

    def __init__(self, page:Page):
        self.page=page

    def makeAppointment(self, facility:str, hospitalReadmission:str, healthcareProgram:str, visitDate:str, comment:str):
        self.page.select_option('#combo_facility',value=facility)
        if  hospitalReadmission==True:
            self.page.click('#chk_hospotal_readmission')
        match   healthcareProgram:
            case    'Medicare':
                self.page.click('#radio_program_medicare')
            case    'Medicaid':
                self.page.click('#radio_program_medicaid')
            case    'None':
                self.page.click('#radio_program_none')
            case    _:
                self.page.click('#radio_program_none')
        self.page.evaluate(f'''$('#txt_visit_date').val('{visitDate}')''')
        self.page.fill('#txt_comment',comment)
        self.page.click('#btn-book-appointment')        
        return self

    