from PagesObjects.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #locators
        self.nom_item = page.locator(".product-name")
        self.champ_quantite = page.locator('.qty-input')

    #methodes
    def verifier_que_item_visible_dans_panier(self, nom_article):
        self.verifier_text_element(self.nom_item, nom_article)

    def modifier_quantie_panier(self):
        ancienne_quantite = self.page.locator('.qty-input').input_value()
        self.page.locator('.qty-input').clear()
        self.page.locator('.qty-input').type('10')

        new_quantity = self.page.locator('.qty-input').input_value()
        assert ancienne_quantite != new_quantity