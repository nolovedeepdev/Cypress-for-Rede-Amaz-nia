/*
Elements: possui o mesmo conceito do page objects, mas aqui colocamos os elementos da página. Tal organização permite que elementos sejam reutilizados e tenham fácil manutenção.
Ex.: HomeElements.js, PdpElements.js, CheckoutElements.js.
*/

/* global Given, Then, When */
import LoginPage from '../pageobjects/LoginPage'
const loginPage = new LoginPage

Given("acesso o site sarf", () => {
    loginPage.acessarSite();
})

When("acesso a pagina de login", () => {
    loginPage.clicarBotaoPaginaLogin();
})

Then("devo visualizar Usuário ou Senha Inválido(s)", () => {
    loginPage.visualizarBotaoRecuperarSenha();
})