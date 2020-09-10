from behave import *
from pages.login_sarf_page import sarfPage
from nose.tools import assert_equal

sarfPage = sarfPage()


@given('que acesso a página do SARF')
def step_impl(context):
    sarfPage.acess_page('https://sarf.ufpa.br/sarf/login.jsf')


@given('que preencho o campo de CPF e Senha com Python')
def step_impl(context):
    sarfPage.send_keys_input_cpf()
    sarfPage.send_keys_input_password()

@when('clico no botão de Login')
def step_impl(context):
    sarfPage.click_button_login()


@then('devo visualizar Usuário ou Senha Inválido(s)')
def step_impl(context):
    assert_equal(sarfPage.get_text_title_resultado(), 'Usuário ou Senha Inválido(s)')