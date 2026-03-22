import time
import allure
from PagesObjects.HomePage import HomePage


def test_recherche_sans_resultat(setup):
    home_page = HomePage(setup)

    with allure.step('saisir un article dans recherche'):
        home_page.entrer_un_item_dans_barre_de_recherche("prout")

    with allure.step('clique sur bouton search'):
        home_page.cliquer_sur_bouton_search()

    with allure.step('message item inexistant est visible'):
        home_page.verifier_message_item_inexistant()