from browser import Browser
from behave import *
from nose.tools import assert_equal
from pages.login_sarf_page import sarfPage

# executa os comandos antes de todos os testes iniciarem
def before_all(context):
    context.browser = Browser()


# executa os comandos depois de todos os testes terminarem
def after_all(context):
    context.browser.browser_quit()


# executa os comandos entre cada cenário
def after_scenario(context, scenario):
    context.browser.browser_clear()

sarfPage = sarfPage()


@given('que acesso a página do Google')
def step_impl(context):
    sarfPage.acess_page('https://sarf.ufpa.br/sarf/')


@given('que preencho o campo de pesquisa com Python')
def step_impl(context):
    sarfPage.send_keys_input_pesquisa()


@when('clico no botão de pesquisar')
def step_impl(context):
    sarfPage.click_button_pesquisar()


@then('devo visualizar os resultados')
def step_impl(context):
    assert_equal(sarfPage.get_text_title_resultado(), 'Usuário ou Senha Inválido(s)')