import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
df = pd.read_csv('data/meus_centavos_contam.csv')

# Verificar se as colunas estão corretas
colunas_esperadas = ['Data', 'Tipo', 'Descrição', 'Categoria', 'Valor', 'Forma de Pagamento', 'Fixo?', 'Observações']
if not all(col in df.columns for col in colunas_esperadas):
    print("❌ Erro: CSV não está no formato esperado. Verifique os nomes das colunas.\n" \
    "Colunas esperadas: ['Data', 'Tipo', 'Descrição', 'Categoria', 'Valor', 'Forma de Pagamento', 'Fixo?', 'Observações']")
    exit()

# Visualizar as primeiras linhas
print("\n📋 Primeiras linhas do arquivo:")
print(df.head())

# Converter a coluna 'Data' para formato datetime
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

# Criar a coluna 'mes_ano'
df['mes_ano'] = df['Data'].dt.to_period('M')

# Somar os valores por categoria
print("\n📊 Total por categoria:")
soma_total = df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)
print(soma_total)

# Entradas vs saídas
print("\n💰 Entradas vs Saídas:")
entrada_saida = df.groupby('Tipo')['Valor'].sum()
print(entrada_saida)

# Total de gastos por mês
print("\n📆 Gastos por mês:")
gastos_por_mes = df[df['Tipo'] == 'Saída'].groupby('mes_ano')['Valor'].sum()
print(gastos_por_mes)

# Consulta por mês específico
ver_mes = input("\n📅 Deseja ver os gastos de um mês específico? (S/N): ").strip().upper()
if ver_mes == 'S':
    mes_escolhido = input("Digite o mês no formato AAAA-MM (ex: 2025-03): ")
    try:
        gastos_mes = df[(df['Tipo'] == 'Saída') & (df['mes_ano'] == mes_escolhido)]
        print(f"\n🔍 Gastos em {mes_escolhido}:")
        print(gastos_mes[['Data', 'Descrição', 'Categoria', 'Valor']])
        print(f"\n💸 Total: R$ {gastos_mes['Valor'].sum():.2f}")
    except:
        print("❌ Mês inválido ou sem dados.")

# Filtrar apenas os dados de Saída
gastos = df[df['Tipo'] == 'Saída']

# Somar os valores por categoria
gastos_por_categoria = gastos.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)

# Criar gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(gastos_por_categoria, labels=gastos_por_categoria.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Gastos por Categoria')
plt.axis('equal')
plt.tight_layout()
plt.savefig('graficos/grafico_pizza.png')

# Gráfico de barras: Gastos por mês
plt.figure(figsize=(10, 6))
gastos_por_mes.plot(kind='bar', color='tomato')
plt.title('Gastos por Mês')
plt.xlabel('Mês')
plt.ylabel('Valor (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('graficos/grafico_barra_mensais.png')

# Agrupar valores por mês e tipo (Entrada/Saída)
entrada_saida_mensal = df.groupby(['mes_ano', 'Tipo'])['Valor'].sum().unstack().fillna(0)

# Gráfico de barras lado a lado: Entradas vs Saídas por mês
plt.figure(figsize=(10, 6))
entrada_saida_mensal.plot(kind='bar', stacked=False, color=['mediumseagreen', 'tomato'])
plt.title('Entradas vs Saídas por Mês')
plt.xlabel('Mês')
plt.ylabel('Valor (R$)')
plt.xticks(rotation=45)
plt.legend(title='Tipo')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('graficos/grafico_entradaXsaida_mensais.png')

if __name__ == "__main__":
    print("\n✅ Análise concluída! Os gráficos foram salvos na pasta 'graficos'.")
