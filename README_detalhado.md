📄 README.md
# 💸 Meus Centavos Contam
Um projeto simples e didático para organizar suas finanças pessoais usando **Python** e **planilhas**. Aqui, você vai aprender como transformar uma tabela em gráficos de análise de gastos, entradas, categorias e muito mais.
Feito com carinho pensando em quem tá começando! 🌱

---

## 📂 Estrutura do Projeto
meus-centavos-contam/ │ ├── data/ │ ├── meus_centavos_contam.csv ← Exemplo de preenchimento │ └── modelo_planilha_meus_centavos.xlsx ← Planilha modelo para baixar e preencher │ ├── graficos/ │ ├── grafico_entradaXsaida_mensais.png │ ├── grafico_pizza_categorias.png │ └── grafico_gastos_mensais.png │ ├── src/ │ └── main.py ← Script principal │ ├── requirements.txt └── README.md

---
## 🚀 Como usar
### 1. Clone este repositório
no terminal:
git clone https://github.com/seu-usuario/meus-centavos-contam.git
cd meus-centavos-contam
2. Instale os requisitos
Você precisa ter o Python instalado (recomendo o Python 3.10+).

Depois disso, instale as bibliotecas:
pip install -r requirements.txt

3. Preencha sua planilha
Você pode:
Abrir o arquivo data/modelo_planilha_meus_centavos.xlsx
Preencher com seus dados pessoais
Salvar como .csv (no Excel: Salvar Como > CSV UTF-8)
Substituir o arquivo meus_centavos_contam.csv pelo seu próprio CSV

⚠️ Atenção: os nomes das colunas devem ser mantidos iguais:
Data, Tipo, Descrição, Categoria, Valor, Forma de Pagamento, Fixo?, Observações

4. Execute o programa
python src/main.py
python3.9 scr/main.py

O programa vai:
Analisar seus dados
Mostrar resumos no terminal
Gerar gráficos na pasta graficos/ automaticamente

📊 Gráficos gerados
Entrada vs Saída mensal (grafico_entradaXsaida_mensais.png)
Gastos por categoria (grafico_pizza_categorias.png)
Gastos totais por mês (grafico_gastos_mensais.png)
Você pode abrir os arquivos .png normalmente no seu computador ou compartilhar com outras pessoas.

✨ Futuras ideias (se quiser ir além)
Interface com Streamlit
Exportar relatório em PDF
Adicionar metas financeiras
Automatizar via Google Sheets

🙋‍♀️ Feito por
Esse projeto foi criado como parte do meu processo de aprendizado em Python e dados.
Se quiser trocar ideias ou dar sugestões, fique à vontade pra abrir uma issue ou me chamar.

Porque sim: Meus centavos contam! ✨
---

### 📄 `requirements.txt`
```txt
pandas
matplotlib
