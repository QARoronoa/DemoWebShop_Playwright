from playwright.sync_api import expect

from PagesObjects.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    #locators
        self.link_register = page.get_by_role("link", name="Register")
        self.link_login = page.get_by_role("link", name="Log in")
        self.link_logout = page.get_by_role("link", name="Log out")

    #methodes

    def cliquer_sur_register(self):
        self.cliquer_sur_un_element(self.link_register)

    def cliquer_sur_login(self):
        self.cliquer_sur_un_element(self.link_login)

    def verifier_user_est_connecte(self):
        expect(self.page.locator('.account').nth(0)).to_have_text("sebastien19@example.net")

    def cliquer_sur_logout(self):
        self.cliquer_sur_un_element(self.link_logout)

    def verifier_que_le_lien_login_est_visible(self):
        self.verifier_text_element(self.link_login, "Log in" )

    def cliquer_sur_une_categorie_du_menu(self, categorie):
        self.page.get_by_role("link", name=categorie).nth(0).click()

    def cliquer_sur_un_featured_products(self, item):
        self.page.get_by_text(item).click()
