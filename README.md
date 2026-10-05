# Tratamento de Pedidos com Pandas

Projeto desenvolvido em Python para praticar o tratamento, a validação e a classificação de dados utilizando a biblioteca Pandas.

A proposta é trabalhar com uma base de pedidos que apresenta valores ausentes, espaços desnecessários e registros que precisam ser classificados de acordo com regras de negócio.

## Objetivo

Realizar o tratamento de uma base de pedidos e separar os registros entre válidos e inválidos.

Um pedido é considerado válido quando:

- o valor está preenchido;
- o valor é maior que zero;
- o status do pedido é "Aprovado".

Além da validação, pedidos aprovados com valor acima de R$ 2.000 são classificados como prioritários.

## Tratamentos realizados

Durante o processamento da base, foram realizadas as seguintes etapas:

- remoção de espaços desnecessários nos nomes dos clientes e cidades;
- tratamento de cidades com valores ausentes;
- tratamento de cidades preenchidas apenas com espaços;
- validação dos pedidos de acordo com as regras definidas;
- separação entre pedidos válidos e inválidos;
- classificação de pedidos como "Normal" ou "Prioritário".

## Tecnologias utilizadas

- Python
- Pandas
- PyCharm

## Conceitos praticados

O projeto foi utilizado para praticar conceitos de manipulação e tratamento de dados com Pandas, incluindo:

- criação e manipulação de DataFrames;
- seleção de colunas;
- tratamento de valores ausentes com `fillna()` e `notna()`;
- tratamento de strings com `.str.strip()`;
- criação de máscaras booleanas;
- combinação de condições com `&`;
- inversão de condições com `~`;
- atualização condicional de dados com `.loc`;
- criação de novas colunas;
- aplicação de regras de negócio sobre uma base de dados.

## Como executar

1. Certifique-se de que o Python esteja instalado no computador.
2. Certifique-se de que a biblioteca Pandas esteja instalada. Caso necessário, execute `pip install pandas`.
3. Baixe o arquivo `tratamento_pedidos.py` do projeto.
4. Execute o arquivo pelo terminal ou por uma IDE de sua preferência, como:
   - PyCharm
   - Visual Studio Code
   - IDLE

## Exemplo de uso
Ao executar o programa, a base de pedidos é tratada e os registros são separados de acordo com as regras de validação.

**Saída:**

```text
PEDIDOS VÁLIDOS
   id       cliente          cidade   valor    status     categoria
0   1    João Silva       São Paulo  1200.0  Aprovado        Normal
1   2  Maria Souza   Não informado   850.0  Aprovado        Normal
5   6  Julia Santos  Não informado  1750.0  Aprovado        Normal
6   7  Marcos Lima          Cuiabá   2500.0  Aprovado   Prioritário

PEDIDOS INVÁLIDOS
   id        cliente          cidade   valor     status  categoria
2   3     Pedro Lima   Não informado     NaN   Aprovado     Normal
3   4      Ana Costa        Curitiba  -200.0   Aprovado     Normal
4   5  Carlos Alves        Salvador  2100.0  Cancelado     Normal
