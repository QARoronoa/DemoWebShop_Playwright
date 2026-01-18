from PagesObjects.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    #locators
        self.link_register = page.get_by_role("link", name="Register")

    #methodes

    def cliquer_sur_register(self):
        self.cliquer_sur_un_element(self.link_register)