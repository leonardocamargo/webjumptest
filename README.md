# project-Webjump
Projeto de automação de testes dos cenários da página https://webjump-user.github.io/testqa/

## Versão
A versão atual é a 1.0.0, sujeita a alteração devido as modificações.

### Instalação em ambiente Linux

- Projeto requer a versão do [Python3](https://www.python.org/downloads/) 
- Selenium WebDriver Latest Version
- Chrome versão 73.0.3683.75
- Behave Latest Version 
- ChromeDriver Latest Version [ChromeDriver](https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/)

```sh
$ sudo apt-get update
$ sudo apt-get install python3.6
$ sudo apt install python3-pip
$ pip3 install -U selenium
$ apt install python3-behave
$ wget https://chromedriver.storage.googleapis.com/75.0.3770.8/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
$ sudo mv chromedriver /usr/bin/chromedriver
$ sudo chown root:root /usr/bin/chromedriver
$ sudo chmod +x /ushw r/bin/chromedriver
```

### Headless Browser
O proprio chromedriver tem a função para rodar o browser em Headless (Abrir o navegador sem interface gráfica)
Caso queira utilizar o browser como Headless, basta apenas descomentar a linha
``` driver = webdriver.Chrome(chrome_options=chrome_options)```
e comentar a linha 
``` driver = webdriver.Chrome()```


### Run

Para executar os testes basta estar na pasta webjump-test e executar o comando:
```sh
$ behave
```

Caso queira executar um cenario especifico, basta executar o comando:
```sh
$ behave -n "NOME_DO_CENARIO"
```
