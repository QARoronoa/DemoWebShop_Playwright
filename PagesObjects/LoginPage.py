from playwright.sync_api import expect

from PagesObjects.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #locators
        self.champ_email = page.locator('#Email')
        self.champ_password = page.locator('#Password')
        self.bouton_login = page.locator('.login-button')
        self.message_erreur_connexion = page.locator('.validation-summary-errors')

    #methodes

    def connexion_valide(self):
        self.saisir_du_texte_dans_le_champ(self.champ_email, "sebastien19@example.net" )
        self.saisir_du_texte_dans_le_champ(self.champ_password, "password")

    def connexion_invalide(self):
        self.saisir_du_texte_dans_le_champ(self.champ_email, "sebaastien19@example.net" )
        self.saisir_du_texte_dans_le_champ(self.champ_password, "password")

    def cliquer_sur_bouton_login(self):
        self.cliquer_sur_un_element(self.bouton_login)

    def visualiser_message_derreur(self):
        message = 'Login was unsuccessful. Please correct the errors and try again.'
        self.verifier_text_element(self.message_erreur_connexion, message)

