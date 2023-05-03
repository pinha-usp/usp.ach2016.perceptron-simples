# USP - ACH2016 - Perceptron simples

> Implementação de um Perceptron simples

Essa implementação resolve o problema das portas lógicas. Ocorre um treinamento do Perceptron, que aprende como identificar a saída de uma porta lógica
com base em suas entradas.

Exemplos de portas lógicas e suas entradas e respectivas saídas se encontram dentro do diretório `/dados`. Para cada linha do arquivo CSV, os primeiros dois
números representam a entrada e o último a saída.

Abaixo está um exemplo para a porta lógica AND:

|Entrada|Saída|
|--|--|
|-1 `AND` -1|-1|
|-1 `AND` 1|-1|
|1 `AND` -1|-1|
|1 `AND` 1|1|

## Como executar?

No terminal, execute o seguinte comando:

```
python perceptron.py
```

> ⚠️ Aviso: A versão Python utiliza foi 3.10. Versões anteriores podem gerar erros
