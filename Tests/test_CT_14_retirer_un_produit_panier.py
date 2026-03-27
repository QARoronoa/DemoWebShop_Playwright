import time

import allure
from PagesObjects.CartPage import CartPage
from PagesObjects.HomePage import HomePage
from PagesObjects.CategoriePage import CategoryPage



def test_retirer_un_article_du_panier(setup):
    home_page = HomePage(setup)
    category_page = CategoryPage(setup)
    cart_page = CartPage(setup)


    with allure.step('clique categorie books'):
        home_page.cliquer_sur_une_categorie_du_menu('Books')

    with allure.step('redirection vers la page Books'):
        home_page.verifier_le_tire('Demo Web Shop. Books')

    with allure.step('clique sur add to cart'):
        category_page.ajouter_una_article_au_panier("Fiction")

    with allure.step('clique sur shopping cart'):
        home_page.cliquer_sur_shopping_cart()

    with allure.step("L'article est visible dans le panier"):
        cart_page.verifier_le_tire("Demo Web Shop. Shopping Cart")
        cart_page.verifier_que_item_visible_dans_panier("Fiction")

    with allure.step('suppresion article panier'):
        cart_page.supprimer_un_article()

    with allure.step('Message panier vide visible'):
        cart_page.verifier_message_panier_vide_visible()

