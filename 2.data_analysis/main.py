import pandas as pd

def converte_para_float(valor):
    return float(valor.replace("R$", "").replace(".", "").replace(",", ".").strip())

def converte_para_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formata_nome_produto(nome_produto):
    return str(nome_produto).capitalize()

dataframe = pd.read_csv('vendas.csv')
dataframe['total_vendas'] = dataframe['quantidade'] * dataframe['preco'].apply(converte_para_float)
print('\nDataFrame Base\n')
print(dataframe)

faturamento_df = dataframe.groupby('produto')['total_vendas'].sum()

# EXIBINDO PRODUTO MAIS VENDIDO
produto_mais_vendido = formata_nome_produto(faturamento_df.idxmax())
valor_produto_mais_vendido = converte_para_moeda(faturamento_df.max())
print(f'\nProduto com maior Faturamento: {produto_mais_vendido} - {valor_produto_mais_vendido}')

# EXIBINDO PRODUTO MENOS VENDIDO
produto_menos_vendido = formata_nome_produto(faturamento_df.idxmin())
valor_produto_menos_vendido = converte_para_moeda(faturamento_df.min())
print(f'Produto com menor Faturamento: {produto_menos_vendido} - {valor_produto_menos_vendido} \n')