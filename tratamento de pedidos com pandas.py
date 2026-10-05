##Realizar tratamento de uma base de pedidos, separado os clientes com pedidos válidos e inválidos. Um pedido só é válido quando o valor está preenchido, é maior que zero e o status é "aprovado". Crie uma priorização de pedidos com valor acima de 2000 reais.


import pandas as pd

pedidos = [
    {"id": 1, "cliente": "  João Silva  ", "cidade": "São Paulo", "valor": 1200, "status": "Aprovado"},
    {"id": 2, "cliente": "Maria Souza", "cidade": None, "valor": 850, "status": "Aprovado"},
    {"id": 3, "cliente": " Pedro Lima ", "cidade": "   ", "valor": None, "status": "Aprovado"},
    {"id": 4, "cliente": "Ana Costa", "cidade": "Curitiba", "valor": -200, "status": "Aprovado"},
    {"id": 5, "cliente": " Carlos Alves ", "cidade": " Salvador ", "valor": 2100, "status": "Cancelado"},
    {"id": 6, "cliente": "Julia Santos", "cidade": None, "valor": 1750, "status": "Aprovado"},
    {"id": 7, "cliente": " Marcos Lima ", "cidade": " Cuiabá ", "valor": 2500, "status": "Aprovado"}
]

df = pd.DataFrame(pedidos)

## tratamento dos dados para padronização
df["cidade"] = df["cidade"].fillna("Não informado")
df["cidade"] = df["cidade"].str.strip()
df["cliente"] = df["cliente"].str.strip()
df.loc[df["cidade"] == "", "cidade"] = "Não informado"

## etapa de criação da regra de negócio
condicao = (df["valor"].notna()) & (df["valor"] > 0) & (df["status"] == "Aprovado")

## etapa adicional para filtrar pedidos prioritários
df["Categoria"] = "Normal"
df.loc[(df["valor"] > 2000) & (df["status"] == "Aprovado"), "Categoria"] = "Prioritário"

pedidos_validos = df[condicao]
pedidos_invalidos = df[~condicao]

print("PEDIDOS VÁLIDOS")
print(pedidos_validos)
print()
print("PEDIDOS INVÁLIDOS")
print(pedidos_invalidos)