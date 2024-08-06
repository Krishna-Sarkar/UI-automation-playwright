from playwright.sync_api import Playwright

class BrowserActions:

    def __init__(self,playwright: Playwright):
        chromium = playwright.chromium
        browser=chromium.launch()
        self.page = browser.new_page()

    def returnPage(self):
        return self.page


    