from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser


class sarfPageLocator(object):
    # Seletores dos elementos utilizados na página
    INPUT_CPF = '[name="j_username"]'
    INPUT_PASSWORD = '[name="j_password"]'
    BUTTON_LOGIN = '[name="j_idt17"]'
    TITLE_RESULTADO = '[id="j_idt18"]'


class sarfPage(Browser):
    def get_element(self, locator):
        # aguarda elemento estar visível na tela
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        # retorna elemento
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def acess_page(self, url):
        # acessa url passada
        self.driver.get(url)

    def send_keys_input_cpf(self):
        # envia para o elemento o texto o cpf falso
        input_cpf = self.get_element(sarfPageLocator.INPUT_CPF)
        input_cpf.send_keys('11111111111')

    def send_keys_input_password(self):
        # envia para o elemento o texto o cpf falso
        input_password = self.get_element(sarfPageLocator.INPUT_PASSWORD)
        input_password.send_keys('1111111')

    def click_button_login(self):
        # clica no botão de Login
        button = self.get_element(sarfPageLocator.BUTTON_LOGIN)
        button.click()

    def get_text_title_resultado(self):
        # retorna o texto do elemento
        element = self.get_element(sarfPageLocator.TITLE_RESULTADO)
        return element.text