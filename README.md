# Desafio Senior Labs - Data Science 

Este repositório tem por objetivo armazenar as implementações, resultados e gráficos gerados durante o desafio Data Science da Senior Labs.

## Informações gerais

A contextualização do desafio são mensagens SPAM (mensagens não solicitadas). Foi fornecido um arquivo contendo exemplos de mensagens comuns (4827 unidades) e mensagens spams (747 unidades). As mensagens foram previamente tratadas, sendo submetidas a uma etapa de mineração de texto, com o objetivo de identificar as palavras mais frequentes na base de dados.

O desafio é composto de duas etapas:

### Primeira etapa

Consiste nas seguintes ações:

1. Exibir um gráfico com as palavras mais frequentes em toda a base de dados
2. Exibir um gráfico com as quantidades de mensagens comuns e spams para cada mês
3. Calcular o máximo, o mínimo, a média, a mediana, o desvio padrão e a variância da quantidade total de palavras para cada mês
4. Exibir o dia de cada mês que possui a maior sequência de mensagens comuns (não spam).

### Segunda etapa

A segunda etapa consiste em aplicar um método capaz de classificar automaticamente as mensagens como “comum” e “spam”. Os resultados encontrados devem ser avaliados e justificados. 

## Guia de arquivos e diretórios

- /firstStep: diretório que contém os módulos referentes à primeira etapa do desafio
  - firstStep.py: módulo principal da primeira parte do desafio
  - generateCloud.py: módulo para função de criação de nuvem de palavras
  - lessSpam.py: módulo com função que imprime o dia do mês com maior sequência de mensagens comuns
  - readSenior.py: módulo com função de leitura de arquivo .csv
  - traceMonthGraph.py: módulo com funções de traçado gráfico
  - wordFreq.py: módulo com função que retorna um dicionário com frequências de palavras
  - wordStats.py: módulo com função que imprime estatísticas mensais
- /graphics: diretório que contém os arquivos de imagem com gráficos
- /secondStep: diretório que contém os módulos referentes à segunda etapa do desafio
  - readSenior.py: módulo com função de leitura de arquivo .csv
  - secondStep.py: módulo principal da segunda parte do desafio
- README.md: este arquivo
- artigo.pdf: artigo escrito durante o desafio
- mail.jpg: arquivo de imagem, máscara para a nuvem de palavras
- sms_senior.csv: base de dados fornecida para análise

## Guia de atributos da base de dados

- 1 coluna contendo a mensagem original ("Full_Text")
- 149 colunas com valores inteiros que indicam a frequência de uma determinada palavra na mensagem ("got"... "wan")
- 1 coluna contendo a quantidade de palavras frequentes na mensagem ("Common_Words_Count")
- 1 coluna contendo a quantidade total de palavras da mensagem ("Word_Count")
- 1 coluna contendo a data de recebimento da mensagem ("Date")
- 1 coluna que identifica se a mensagem é spam ou não ("IsSpam")

## Guia de pré-requisitos

Todas as implementações e experimentos foram executados no sistema operacional Ubuntu 20.04.4 LTS.

Para reprodução dos experimentos, é obrigatória a instalação de Python versão 3.8.10.

Além disso, são essenciais os seguintes pacotes:

- Numpy versão 1.20.2
- Matplotlib versão 3.5.1
- Scikit-learn versão 0.24.2
- Wordcloud versão 1.8.1
- Pandas versão 1.4.2

## Guia de execução

### Primeira etapa

Para rodar a primeira etapa do experimento, basta executar o arquivo firstStep.py, contido no diretório /firstStep:

```
python3 firstStep.py
```

**Saída esperada**:

Caso seja a primeira execução, é criado automaticamente o diretório /graphics, onde o programa irá salvar:
- "n".png (01 <= n <= 12): gráfico de setor para cada mês n
- bars.png: gráfico de barras agrupadas, comparando a quantia de spams mensalmente
- cloud.png: nuvem de palavras mais frequentes em toda a base de dados
  
No console será exibida a seguinte saída:

```
Mês 01:
Max = 190
Min = 2
Media = 16.336917562724015
Mediana = 13
Desvio = 12.529964086141668
Variancia = 157


Mês 02:
Max = 100
Min = 2
Media = 16.029043280182233
Mediana = 13.0
Desvio = 11.0
Variancia = 121


Mês 03:
Max = 115
Min = 2
Media = 16.28525469168901
Mediana = 12
Desvio = 11.532562594670797
Variancia = 134


Mês 01: dia 26

Mês 02: dia 04

Mês 03: dia 31
```

O primeiro grupo de informações corresponde aos dados estatísticos calculados para cada mês, enquanto o segundo exibe o dia do mês em que há maior sequência de mensagens comuns (não-spam).

### Segunda etapa

Para rodar a segunda etapa do experimento, basta executar o arquivo secondStep.py, contido no diretório /secondStep:

```
python3 secondStep.py
```

**Saída esperada**:

O programa irá automaticamente realizar os experimentos descritos no artigo, retornando a média da acurácia entre os testes:

```
0.9584698147041243
```

