import time
import allure
from PagesObjects.HomePage import HomePage


def test_recherche_avec_resultat(setup):
    home_page = HomePage(setup)

    with allure.step('saisir un article dans recherche'):
        home_page.entrer_un_item_dans_barre_de_recherche("phone")

    with allure.step('clique sur bouton search'):
        home_page.cliquer_sur_bouton_search()

    with allure.step('element rechercher est visible'):
        home_page.verifier_element_chercher_est_visible("phone")

