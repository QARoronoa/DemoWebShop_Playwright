import allure
from playwright.sync_api import Locator, expect, Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Clique sur l element: {locator} ok ")
    def cliquer_sur_un_element(self, locator: Locator):
          expect(locator).to_be_visible()
          expect(locator).to_be_enabled()
          locator.click()


    @allure.step("saisir du text dans le champ: {text} ok ")
    def saisir_du_texte_dans_le_champ(self, locator: Locator, text):
        expect(locator).to_be_visible()
        expect(locator).to_be_enabled()
        locator.fill(text)

    @allure.step("L'élément est visible : {text}")
    def verifier_text_element(self, locator, text):
        expect(locator).to_be_visible()
        expect(locator).to_contain_text(text)

    @allure.step("le titre de la page est {titre}")
    def verifier_le_tire(self, titre):
        expect(self.page).to_have_title(titre)