import time

import allure
from PagesObjects.CartPage import CartPage
from PagesObjects.HomePage import HomePage
from PagesObjects.CategoriePage import CategoryPage



def test_verifier_panier_vide(setup):
    home_page = HomePage(setup)
    cart_page = CartPage(setup)

    with allure.step('clique sur shopping cart'):
        home_page.cliquer_sur_shopping_cart()
        home_page.verifier_le_tire('Demo Web Shop. Shopping Cart')

    with allure.step('verifier message panier vide'):
        cart_page.verifier_message_panier_vide_visible()

