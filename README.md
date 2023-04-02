# web-scraping

### Passos:
1. Ao entrar no ambiente virtual criado, instala a biblioteca Scrapy no próprio ambiente virtual:
  ```
  pip install scrapy
  ```

2. inicia-se o projeto Scrapy com o comando:
  ```
  scrapy startproject nomeprojeto
  ```
3. Cria o arquivo 'sanguessuga', no qual será passado a URL do site a ser extraído os dados:
  ```
  scrapy genspider nomearq nome-url.com
  ```
4. Para rodar o projeto, utiliza-se o seguinte comando:
  ```
  scrapy crawl nomearq
  ```
  * OBS.: Para salvar os dados em um arquivo pode se utilizar as seguintes adições de comando:
  
  -o: continua a escrever no arquivo.
  ```
  scrapy crawl nomearq -o nomearquivo.extensao
  ```
  
   -O: Sobrepõe o que já foi escrito, iniciando do zero.
  ```
  scrapy crawl nomearq -O nomearquivo.extensao
  ```
