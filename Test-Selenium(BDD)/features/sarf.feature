# language: pt

Funcionalidade: fazer login no SARF
  
  # Contexto são ações que serão executadas antes de cada cenário.
  
  Contexto: acessar página de teste
    Dado que acesso a página do SARF

  Cenário: acessar página de login do SARF
    Dado que preencho o campo de CPF e Senha com Python
    Quando clico no botão de Login
    Então devo visualizar Usuário ou Senha Inválido(s)