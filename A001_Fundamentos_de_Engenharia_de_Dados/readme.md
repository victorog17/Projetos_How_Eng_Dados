# Módulo Fundamentos de Engenharia de Dados

- Criar ambiente virtual: Dentro da pasta de projeto criada, criar o ambiente virtual da seguinte forma:
-> “python3 -m venv nomeambiente” (se colocar um ponto na frente fica como pasta oculta)

- Ative o ambiente virtual: Para ativar o ambiente é necessário rodar o arquivo “activate”.
No powershell chame o caminho do arquivo como no exemplo “.\.venv\Scripts\activate.ps1”, a extensão ps1 é a própria do powershell, para o caso do cmd usar extensão .bat

- (opcional) É provavel que por padrão o powershell tenha restrição nativa para rodar um arquivo dessa extensão, para isso, deve-se abrir o powershell como administrador e incluir o seguinte comando:
-> “Set-ExecutionPolicy -scope CurrentUser -ExecutionPolicy RemoteSigned”
E na sequencia colocar S [Sim]

- Ativar o ambiente virtual novamente como no comando do exemplo “.\.venv\Scripts\activate.ps1” que ele já estará ativado.

- Com o ambiente virtual ativado, instalar as bibliotecas do requirements.txt. “py -m pip install -r requirements.txt”

- Para sair do ambiente virtual basta usar o comando “deactivate”
