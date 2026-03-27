from playwright.sync_api import expect

from PagesObjects.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #locators
        self.nom_item = page.locator(".product-name")
        self.champ_quantite = page.locator('.qty-input')
        self.checkbox_remove = page.locator("input[name='removefromcart']")
        self.bouton_update_cart = page.locator('.update-cart-button')
        self.message_panier_vide = page.locator('.order-summary-content')

    #methodes
    def verifier_que_item_visible_dans_panier(self, nom_article):
        self.verifier_text_element(self.nom_item, nom_article)

    def modifier_quantie_panier(self):
        ancienne_quantite = self.page.locator('.qty-input').input_value()
        self.page.locator('.qty-input').clear()
        self.page.locator('.qty-input').type('10')

        new_quantity = self.page.locator('.qty-input').input_value()
        assert ancienne_quantite != new_quantity

    def supprimer_un_article(self):
        self.cliquer_sur_un_element(self.checkbox_remove)
        self.cliquer_sur_un_element(self.bouton_update_cart)

    def verifier_message_panier_vide_visible(self):
        expect(self.page.locator('.order-summary-content')).to_have_text('Your Shopping Cart is empty!')