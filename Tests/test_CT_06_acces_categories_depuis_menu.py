import time

import allure

from PagesObjects.HomePage import HomePage


def test_acces_categorie_depuis_menu(setup):
    home_page = HomePage(setup)

    with allure.step("cliquer sur un menu"):
        home_page.cliquer_sur_une_categorie_du_menu("Jewelry")

    with allure.step("redirection vers le menu"):
        home_page.verifier_le_tire("Demo Web Shop. Jewelry")


