from selenium import webdriver

driver = webdriver.Chrome()  # Acessar a URL especificada
driver.get('https://sarf.ufpa.br/sarf/')  # Acessar a URL especificada
driver.find_element_by_css_selector('#ui-inputfield ui-inputmask ui-widget ui-state-default ui-corner-all').send_keys("11111111111")  # Digita o cpf no input cpf
driver.find_element_by_css_selector('#ui-inputfield ui-password ui-widget ui-state-default ui-corner-all').send_keys("111111")  # Digita a senha no input senha
driver.find_element_by_css_selector('#ui-button-text ui-c').click()  # Clica no botão de Login
driver.quit()  # Encerra o browser