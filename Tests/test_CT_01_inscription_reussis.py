from PagesObjects.HomePage import HomePage
from PagesObjects.RegisterPage import RegisterPage
import allure


def test_inscription_reussie(setup, formulaire_inscription):
    home_page = HomePage(setup)
    register_page = RegisterPage(setup)


    with allure.step("cliquer sur le lien register"):
        home_page.cliquer_sur_register()

    with allure.step("Formulaire d'inscription"):
        register_page.remplir_le_formulaire(**formulaire_inscription)

    with allure.step("clique sur register"):
        register_page.cliquer_sur_le_bouton_register()

    with allure.step("Message de confirmation inscription visible"):
        register_page.verifier_message_confirmation_inscription()
