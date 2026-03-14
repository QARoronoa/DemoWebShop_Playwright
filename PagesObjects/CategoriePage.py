from PagesObjects.BasePage import BasePage


class CategoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #locators

        self.titre_article = page.locator(".product-title")

    #methodes

    def ajouter_una_article_au_panier(self, nom_article):
        (self.page.locator(".item-box").filter(has_text=nom_article).locator('.button-2')).click()
