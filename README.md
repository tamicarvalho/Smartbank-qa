# Desafio SmartBank #1

## Pré requisitos
1. Instalar o Node JS (https://nodejs.org/en/)
2. Instalar NPM (https://www.npmjs.com/get-npm)
3. Instalar o Mocha globalmente através do comando `npm install -g mocha`

## Instruções
1. Após baixar o código do repositório rodar o comando `npm install` 
2. Após a instalação dos pacotes, executar o comando `mocha` que irá executar o arquivo dentro da pasta **test** e gerar os relatórios de execução no console

## Observações
Existem códigos comentados dentro do arquivo pois são problemas que acredito que estão relacionados a própria API. Não consegui invocar a API `/employee/{id}` corretamente pois, mesmo que o retorno seja um status code 200 (OK), o corpo da mensagem volta um texto que parece ser um arquivo HTML. Só consegui fazer funcionar no Postman.
Também enfrentei problemas na API `/delete/{id}` pois em todas as chamadas que executei apesar do retorno estar correto com a documentação da página o campo **status** sempre retorna com o valor **failed**.
Deste modo, deixei as validações que eu faria uma vez que as APIs estivessem retornando os valores esperados comentadas. Porém deixei comentado para que as iterações funcionassem sem erros no relatório. Pode executar sem os comentários para verificar os erros que as APIs estão retornando.
