from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser


class sarfPageLocator(object):
    # Seletores dos elementos utilizados na página
    INPUT_CPF = '[name="j_username"]'
    BUTTON_CPF = 'ui-inputfield ui-inputmask ui-widget ui-state-default ui-corner-all'
    INPUT_PASSWORD = 'j_password'
    BUTTON_PASSWORD ='ui-inputfield ui-password ui-widget ui-state-default ui-corner-all'
    TITLE_RESULTADO = 'ui-messages-error-summary'


class sarfPage(Browser):
    def get_element(self, locator):
        # aguarda elemento estar visível na tela
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        # retorna elemento
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def acess_page(self, url):
        # acessa url passada
        self.driver.get(url)

    def send_keys_input_pesquisa(self):
        # envia para o elemento o texto 'Python'
        input_pesquisa = self.get_element(sarfPageLocator.INPUT_CPF)
        input_pesquisa.send_keys('Python')

    def click_button_pesquisar(self):
        # clica no botão de pesquisar
        button = self.get_element(sarfPageLocator.BUTTON_CPF)
        button.click()

    def send_keys_input_pesquisa(self):
        # envia para o elemento o texto 'Python'
        input_pesquisa = self.get_element(sarfPageLocator.INPUT_PASSWORD)
        input_pesquisa.send_keys('Python')

    def click_button_pesquisar(self):
        # clica no botão de pesquisar
        button = self.get_element(sarfPageLocator.BUTTON_PASSWORD)
        button.click()

    def get_text_title_resultado(self):
        # retorna o texto do elemento
        element = self.get_element(sarfPageLocator.TITLE_RESULTADO)
        return element.text