TESTE PYTHON MICROSERVICES - INTRODUÇÃO

	1. O projeto foi desenvolvido no Windows 10, 64 bits
	2. A API Flask foi usada para capturar as informações de entrada (cidade e sigla do país) e 
	apresentar os dados da previsão do tempo que são retornados pelo Microservice 1
	3. Os microservices foram desenvolvidos utilizando o Framework Nameko 
		Microservice 1 (name="consult"): 
			Recebe a cidade/país, "fala" com o Microservice 2 (reponsável por buscar o clima) e insere
			as informações no banco de dados
		Microservice 2 (name="weather"):
			Responsável por buscar o clima através da API OpenWeather e retornar as informações para o microservice 1.
			Esse microservice usa a biblioteca Python PyOWM que permite interagir com a API OpenWeatherMap
	4. O Broker escolhido foi o RabbitMQ pois o Nameko usa vários recursos desse servidor
	5. O banco de dados SQLite foi usado para armazenar as informações do clima
	
REQUISITOS

	python 3.7
	pip 19.3.1
    virtualenv 16.7.9
	flask 1.1.1
	nameko 2.12.0
	pyowm 2.10.0
	RabbitMQ

INSTALANDO O PYTHON
	
	Guias de instalação:
		Windows: https://python.org.br/instalacao-windows/
		Linux: https://python.org.br/instalacao-linux/
		MAC OS: https://python.org.br/instalacao-mac/

INSTALANDO O RabbitMQ

	Guia de instalação: https://www.rabbitmq.com/install-windows.html

	O RabbitMQ é um servidor de mensageria feito para suportar AMQP. Foi escrito em Erlang e segundo seu site, 
	é robusto, fácil de usar, roda nos principais sistemas operacionais, suporta enorme número de plataformas 
	de desenvolvimento e é Open Source.

DOWNLOAD DO CÓDIGO

     git clone https://github.com/caroline-salvador/nameko_sqlite.git

AMBIENTE VIRTUAL

	1. No terminal, navege até a pasta do projeto
	2. Crie um ambiente virtual na pasta raiz do projeto executando o comando:
		virtualenv venv
	3. Ative o ambiente virtual usando o comando:
		souce venv/bin/activate (Linux ou macOS)
		venv/Scripts/activate (Windows)
	4. Instale as dependências:
		pip install -r requirements.txt

EXECUTANDO O PROJETO

	1. Com a venv ativada, execute o Nameko service:
		nameko run service
	1. Abra um novo terminal, inicie a venv e execute o projeto usando o seguinte comando: 
		python app.py
	2. O servidor estará disponível no endereço abaixo. Os argumentos cidade e sigla do país devem ser informados: 
		http://127.0.0.1:8000/blumenau/br
	3. Se a porta 8000 não estiver disponível, altere no arquivo app.py
		linha 31 => app_service.run(port=8000)

