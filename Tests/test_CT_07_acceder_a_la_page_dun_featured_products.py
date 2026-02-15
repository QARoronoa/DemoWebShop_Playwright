import time

import allure
from PagesObjects.HomePage import HomePage


def test_acceder_a_la_page_dun_poduit_featured_products(setup):
    home_page = HomePage(setup)

    with allure.step("cliquer sur un menu"):
        home_page.cliquer_sur_un_featured_products("$25 Virtual Gift Card")

    with allure.step("redirection vers la page du produit"):
        home_page.verifier_le_tire("Demo Web Shop. $25 Virtual Gift Card")
