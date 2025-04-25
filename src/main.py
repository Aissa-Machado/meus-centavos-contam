import pandas as pd
import matplotlib.pyplot as plt


# Leitura do arquivo CSV
df = pd.read_csv('data/meus_centavos_contam.csv')

# Verificar se as colunas estão corretas
colunas_esperadas = ['Data', 'Tipo', 'Descrição', 'Categoria', 'Valor', 'Forma de Pagamento', 'Fixo?', 'Observações']
if not all(col in df.columns for col in colunas_esperadas):
    print("❌ Erro: CSV não está no formato esperado. Verifique os nomes das colunas.  " \
    "\n colunas_esperadas = ['Data', 'Tipo', 'Descrição', 'Categoria', 'Valor', 'Forma de Pagamento', 'Fixo?', 'Observações']")
    exit()

# Visualizar as primeiras linhas
print(df.head())

# Converter a coluna 'Data' para formato datetime
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

# Criar a coluna 'mes_ano'
df['mes_ano'] = df['Data'].dt.to_period('M')

# Somar os valores por categoria (opcional)
soma_total = df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)
print(soma_total)

# Entradas vs saídas
entrada_saida = df.groupby('Tipo')['Valor'].sum()
print(entrada_saida)

# Total de gastos por mês
gastos_por_mes = df[df['Tipo'] == 'Saída'].groupby('mes_ano')['Valor'].sum()
print(gastos_por_mes)


ver_mes = input("\n📅 Deseja ver os gastos de um mês específico? (S/N): ").strip().upper()
if ver_mes == 'S':
    mes_escolhido = input("Digite o mês no formato AAAA-MM (ex: 2025-03): ")
    try:
        gastos_mes = df[(df['Tipo'] == 'Saída') & (df['mes_ano'] == mes_escolhido)]
        print(f"\n🔍 Gastos em {mes_escolhido}:")
        print(gastos_mes[['Data', 'Descrição', 'Categoria', 'Valor']])
        print(f"\nTotal: R$ {gastos_mes['Valor'].sum():.2f}")
    except:
        print("❌ Mês inválido ou sem dados.")

