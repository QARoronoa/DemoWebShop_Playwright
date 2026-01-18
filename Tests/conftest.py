import pytest
from playwright.sync_api import Playwright
from Data.Register_data import RegisterData

@pytest.fixture(scope="function")
def setup(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://demowebshop.tricentis.com/")
    yield page


    page.close()
    context.close()
    browser.close()


@pytest.fixture
def formulaire_inscription():
    return RegisterData.formulaire_register()