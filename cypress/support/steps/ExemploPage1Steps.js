/*
Elements: possui o mesmo conceito do page objects, mas aqui colocamos os elementos da página. Tal organização permite que elementos sejam reutilizados e tenham fácil manutenção.
Ex.: HomeElements.js, PdpElements.js, CheckoutElements.js.
*/

/* global Given, Then, When */

import ExemploPage1 from '../pageobjects/ExemploPage1'
const ExemploPage1 = new ExemploPage1

Given("acesso o site CWI", () => {
    ExemploPage1.acessarSite();
})

When("acesso a pagina de login", () => {
    ExemploPage1.clicarBotaoPaginaLogin();
})

Then("devo visualizar botao de recuperar senha esquecida", () => {
    ExemploPage1.visualizarBotaoRecuperarSenha();
})