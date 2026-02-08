import time

from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage
import allure


def test_deconnexion(setup):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)


    with allure.step("cliquer sur le lien login"):
        home_page.cliquer_sur_login()
        login_page.verifier_le_tire("Demo Web Shop. Login")


    with allure.step("se connecter"):
        login_page.connexion_valide()
        login_page.cliquer_sur_bouton_login()

    with allure.step("L'utilisateur est connecté"):
        home_page.verifier_user_est_connecte()

    with allure.step("cliquer sur logout"):
        home_page.cliquer_sur_logout()
        home_page.verifier_que_le_lien_login_est_visible()
