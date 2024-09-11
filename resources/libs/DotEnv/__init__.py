import os
from dotenv import load_dotenv, dotenv_values

class DotEnv:

    """
    Biblioteca para gerenciamento de variáveis de ambiente usando arquivos .env.

    Esta biblioteca realiza  o carregamento e limpeza de variáveis de ambiente usando a 
    biblioteca `dotenv`. Ele permite o carregamento de um arquivo `.env` específico, dependendo do 
    parâmetro fornecido, ou o uso do arquivo `.env` padrão.
    """


    def __init__(self, env=None):
        """
        Para realizar a importação da Biblioteca, basta fornecer o caminho para o módulo (pasta), exemplo:

        Library    resources/libs/DotEnv/

        Caso exista mais de um arquivo .env que represente ambientes diferentes será necessário:

        1 - Seguir a estrutra de pastas abaixo:

        /resources/env/<nome_do_ambiente>.env

        Cada arquivo `.env` deverá ficar dentro de uma pasta que representa o seu respectivo ambiente.

        2 - Na importação, será necessário informar o ambiente que deseja ser utilizado, exemplo:

        Library    resources/libs/DotEnv/   env=HML

        Dessa forma, será carregado o arquivo `.env` da pasta `/env/hml`.
        """

        self.env=env
        self.load_dotenv()

    def load_dotenv(self):
        """
        Carrega as variáveis de ambiente do arquivo .env especificado, removendo previamente 
        variáveis conflitantes já presentes em `os.environ`.
        """

        for key in dotenv_values().keys():
            if key in os.environ:
                del os.environ[key]

        if self.env:
            load_dotenv(f"resources/env/{self.env}/.env")
        else:
            load_dotenv()