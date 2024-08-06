from playwright.sync_api import Page, expect


class AssertAppointmentPage:

    def __init__(self, page:Page):
        self.page=page

    def assertAppointment(self,facility:str, hospitalReadmission:str, healthcareProgram:str, visitDate:str, comment:str):
        expect(self.page.locator('#facility')).to_have_text(facility)
        if  hospitalReadmission==True:
            expect(self.page.locator('#hospital_readmission')).to_have_text("Yes")
        else:
            expect(self.page.locator('#hospital_readmission')).to_have_text("No")
        if  healthcareProgram=='Medicare' or healthcareProgram=='Medicaid':
            expect(self.page.locator('#program')).to_have_text(healthcareProgram)
        else:
            expect(self.page.locator('#program')).to_have_text('None')
        expect(self.page.locator('#visit_date')).to_have_text(visitDate)
        expect(self.page.locator('#comment')).to_have_text(comment)
        return self
    
