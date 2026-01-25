from PagesObjects.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    # locators
        self.bouton_radio_gender_male = page.locator("#gender-male")
        self.champ_firstName = page.locator("#FirstName")
        self.champ_lastName = page.locator("#LastName")
        self.champ_email = page.locator("#Email")
        self.champ_password = page.locator("#Password")
        self.champ_confirmPassword = page.locator("#ConfirmPassword")
        self.bouton_register = page.locator("#register-button")
        self.message_success_registation = page.locator(".result")
        self.message_derreur_mail = page.locator(".validation-summary-errors")


    def remplir_le_formulaire(self, firstName, lastName, email, pwd, pwdConfirm):
        self.cliquer_sur_un_element(self.bouton_radio_gender_male)
        self.saisir_du_texte_dans_le_champ(self.champ_firstName, firstName)
        self.saisir_du_texte_dans_le_champ(self.champ_lastName, lastName)
        self.saisir_du_texte_dans_le_champ(self.champ_email, email)
        self.saisir_du_texte_dans_le_champ(self.champ_password, pwd)
        self.saisir_du_texte_dans_le_champ(self.champ_confirmPassword, pwdConfirm)

    def cliquer_sur_le_bouton_register(self):
        self.cliquer_sur_un_element(self.bouton_register)

    def verifier_message_confirmation_inscription(self):
        self.verifier_text_element(self.message_success_registation, "Your registration completed" )

    def verifier_la_presence_du_message_derreur(self):
        self.verifier_text_element(self.message_derreur_mail, "The specified email already exists")
