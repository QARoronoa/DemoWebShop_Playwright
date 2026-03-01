import time
import allure
from PagesObjects.HomePage import HomePage


def test_retour_cateegorie_depuis_fiche_produit(setup):
    home_page = HomePage(setup)

    with allure.step('redirection vers une catégorie'):
        home_page.cliquer_sur_une_categorie_du_menu("Electronics")

    with allure.step("redirection vers le menu"):
        home_page.verifier_le_tire("Demo Web Shop. Electronics")

    with allure.step("redirection vers la sous categorie"):
        home_page.selectionner_sous_categorie("Cell phones")

    with allure.step("redirection vers la sous categorie"):
        home_page.verifier_le_tire("Demo Web Shop. Cell phones")

    with allure.step('redirection vers une catégorie'):
        home_page.cliquer_sur_une_categorie_du_menu("Electronics")

    with allure.step("redirection vers le menu"):
        home_page.verifier_le_tire("Demo Web Shop. Electronics")





        time.sleep(5)