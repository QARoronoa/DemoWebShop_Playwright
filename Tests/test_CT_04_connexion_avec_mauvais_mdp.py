from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage
import allure


def test_connexion_avec_mauvais_mdp(setup):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)


    with allure.step("cliquer sur le lien login"):
        home_page.cliquer_sur_login()
        login_page.verifier_le_tire("Demo Web Shop. Login")


    with allure.step("se connecter"):
        login_page.connexion_invalide()
        login_page.cliquer_sur_bouton_login()

    with allure.step("Message d'erreur est visible"):
        login_page.visualiser_message_derreur()

