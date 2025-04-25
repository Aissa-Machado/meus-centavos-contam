✅ TODO – Melhorias Futuras para `meus-centavos-contam`

🔧 Organização e Estrutura do Código
- [ ] Separar o código em funções reutilizáveis (ex: `carregar_dados()`, `gerar_graficos()`, `mostrar_resumo()`).
- [ ] Mover blocos de geração de gráfico para funções com parâmetros claros.
- [ ] Colocar a leitura do CSV em um bloco `try-except` para evitar falhas em caso de erro de caminho ou formatação.

💬 Experiência do Usuário
- [ ] Adicionar `print()` explicativos antes de cada bloco de análise (ex: "🧮 Somando os valores por categoria...", "📊 Gerando gráfico de barras...").
- [ ] Adicionar espaços (`\n`) entre as exibições de resultados para melhorar a legibilidade no terminal.
- [ ] Mostrar mensagens claras ao final da execução para iniciantes (ex: onde estão os gráficos salvos, como alterar os dados).

📁 Organização de Arquivos
- [ ] Criar uma pasta `scripts/` ou `src/` e mover o arquivo `.py` principal para dentro.
- [ ] Mover planilhas de exemplo para uma pasta `exemplos/` e deixar claro no README que ela pode ser duplicada.

📊 Visualização de Dados
- [ ] Adicionar rótulos aos gráficos para mostrar valores nos gráficos de barras (usar `plt.bar_label()`).
- [ ] Adicionar um gráfico de linha (opcional) para mostrar a evolução do saldo mês a mês.
- [ ] Exportar um resumo em `.txt` ou `.pdf` com os totais para quem não quer abrir gráficos.

📄 Documentação (README)
- [ ] Criar um README mais leve e direto para usuários básicos (foco só em como usar).
- [ ] Criar um README separado e criativo voltado a quem quer te contratar ou se inspirar (ex: `README_dev.md`).
- [ ] Adicionar imagens dos gráficos no README (dentro de uma pasta `img/`) para visualização direta.

🧪 Testes e Segurança
- [ ] Testar com CSVs que tenham colunas extras ou em ordem diferente, e adaptar o código para ser flexível.
- [ ] Garantir que campos numéricos e datas estejam sempre bem tratados com `try-except` ou validações.

🪄 Extras (se quiser brincar mais)
- [ ] Criar um notebook `.ipynb` com a versão visual e interativa do projeto.
- [ ] Tentar portar o projeto para o Streamlit quando quiser explorar interfaces web simples.
- [ ] Fazer um vídeo ou gif mostrando o projeto em uso.