Feature: Login site Sarf

    Scenario: Visualizar Usuário ou Senha Inválido(s)
        Given acesso o site sarf
        When acesso a pagina de login
        Then devo visualizar Usuário ou Senha Inválido(s)