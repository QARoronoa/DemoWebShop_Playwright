from PagesObjects.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #locators
        self.nom_item = page.locator(".product-name")

    #methodes
    def verifier_que_item_visible_dans_panier(self, nom_article):
        self.verifier_text_element(self.nom_item, nom_article)