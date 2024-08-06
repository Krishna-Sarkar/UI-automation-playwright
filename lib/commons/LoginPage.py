from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page:Page):
        self.page=page

    def navigateToLogin(self, url=None):
        self.page.goto('https://katalon-demo-cura.herokuapp.com/')
        self.page.click('#menu-toggle')
        self.page.click('''//a[normalize-space()='Login']''')
        return self

    def performLogin(self,username:str, password:str):
        self.page.fill("#txt-username",username)
        self.page.fill("#txt-password",password)
        self.page.click("#btn-login")
        return self
    
