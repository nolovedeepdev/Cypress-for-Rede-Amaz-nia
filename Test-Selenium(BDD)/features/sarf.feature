# language: pt

Funcionalidade: realizar preenchimento de um cpf fake
  
  # Contexto são ações que serão executadas antes de cada cenário.
  Contexto: acessar página de teste
    Dado que acesso a página de login do SARF

  Cenário: acessar página de login do SARF e realizar preenchimento do campo cpf
    Dado que preencho o campo de cpf e senha com Python
    Quando clico no botão de login/entar
    Então devo visualizar Usuário ou Senha Inválido(s)