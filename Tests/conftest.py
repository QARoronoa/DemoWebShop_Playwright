import pytest
from playwright.sync_api import Playwright
from Data.Register_data import RegisterData

@pytest.fixture(scope="function")
def setup(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)

    page = context.new_page()
    page.goto("http://demowebshop.tricentis.com/")
    yield page


    page.close()
    context.close()
    browser.close()


@pytest.fixture
def formulaire_inscription():
    return RegisterData.formulaire_register()

@pytest.fixture
def formulaire_inscription_2():
    return RegisterData.formulaire_mail_existant()